package com.matheusmoura.api.entities;

import jakarta.persistence.GeneratedValue;

import java.util.Set;

import com.fasterxml.jackson.annotation.JsonIdentityInfo;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonManagedReference;
import com.fasterxml.jackson.annotation.ObjectIdGenerators;
import com.matheusmoura.api.exceptions.CartException;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Entity
@JsonIdentityInfo(generator = ObjectIdGenerators.PropertyGenerator.class, property = "id")
public class Cart {
  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  @OneToMany(mappedBy = "cart", cascade = CascadeType.ALL, orphanRemoval = true)
  private Set<CartItem> cartItems;

  public double getTotalPrice() {
    return cartItems.stream().mapToDouble(item -> item.getProduct().getPrice() * item.getAmount()).sum();
  }

  public void addProduct(Product product, Integer amount) {
    var cartItem = CartItem.builder()
        .cart(this)
        .product(product)
        .amount(amount)
        .build();

    cartItems.add(cartItem);
  }

  public boolean hasProduct(Product product) {
    return cartItems.stream().anyMatch(cartItem -> cartItem.getProduct().equals(product));
  }

  public void removeProduct(Product product) {
    cartItems.removeIf(cartItem -> cartItem.getProduct().equals(product));
  }

  public Integer getProductAmount(Product product) {
    var cartItem = cartItems.stream()
        .filter(item -> item.getProduct().equals(product))
        .findFirst()
        .get();

    return cartItem.getAmount();
  }

  public void incrementProductAmount(Product product, Integer amount) {
    var cartItem = cartItems.stream()
        .filter(item -> item.getProduct().equals(product))
        .findFirst()
        .get();

    if (cartItem.getAmount() + amount > product.getQuantity()) {
      throw new CartException("Quantidade de produto indisponível no estoque");
    }

    cartItem.setAmount((cartItem.getAmount() + amount));
  }

  public void decrementProductAmount(Product product, Integer amount) {
    var cartItem = cartItems.stream()
        .filter(item -> item.getProduct().equals(product))
        .findFirst()
        .get();

    var normalizedAmount = Math.max(cartItem.getAmount() - amount, 0);

    cartItem.setAmount(normalizedAmount);
  }
}
