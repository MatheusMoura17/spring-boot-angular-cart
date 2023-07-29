package com.matheusmoura.api.services;

import org.springframework.stereotype.Service;

import com.matheusmoura.api.entities.Cart;
import com.matheusmoura.api.exceptions.CartException;
import com.matheusmoura.api.exceptions.CartNotExistsException;
import com.matheusmoura.api.exceptions.ProductNotFoundException;
import com.matheusmoura.api.repositories.CartRepository;
import com.matheusmoura.api.repositories.ProductRepository;

import lombok.AllArgsConstructor;

@Service
@AllArgsConstructor
public class CartService {
  private CartRepository cartRepository;
  private ProductRepository productRepository;

  public Cart addProduct(Long cartId, Long productId, Integer amount) {
    if (!cartRepository.existsById(cartId)) {
      throw new CartNotExistsException(cartId);
    }

    if (!productRepository.existsById(productId)) {
      throw new ProductNotFoundException(productId);
    }

    if (amount <= 0) {
      throw new CartException("A quantidade deve ser maior que 0");
    }

    var cart = cartRepository.findById(cartId).get();
    var product = productRepository.findById(productId).get();

    if (product.getQuantity() < amount) {
      throw new CartException("Quantidade de produto indisponível no estoque");
    }

    if (cart.hasProduct(product)) {
      cart.incrementProductAmount(product, amount);
    } else {
      cart.addProduct(product, amount);
    }

    return cartRepository.saveAndFlush(cart);
  }

  public Cart removeProduct(Long cartId, Long productId, Integer amount) {
    if (!cartRepository.existsById(cartId)) {
      throw new CartNotExistsException(cartId);
    }

    if (!productRepository.existsById(productId)) {
      throw new ProductNotFoundException(productId);
    }

    if (amount <= 0) {
      throw new CartException("A quantidade deve ser maior que 0");
    }

    var cart = cartRepository.findById(cartId).get();
    var product = productRepository.findById(productId).get();

    if (!cart.hasProduct(product)) {
      throw new CartException("Produto não existe no carrinho");
    }

    cart.decrementProductAmount(product, amount);

    if (cart.getProductAmount(product) <= 0) {
      cart.removeProduct(product);
    }

    return cartRepository.saveAndFlush(cart);
  }

  public Cart get(Long id) {
    if (!cartRepository.existsById(id)) {
      throw new CartNotExistsException(id);
    }

    return cartRepository.findById(id).get();
  }

  public Cart create(Long id) {
    var cart = Cart.builder()
        .id(id)
        .build();
    return cartRepository.save(cart);
  }

  public Cart clear(Long cartId) {
    if (!cartRepository.existsById(cartId)) {
      throw new CartNotExistsException(cartId);
    }

    var cart = cartRepository.findById(cartId).get();
    cart.getCartItems().clear();

    return cartRepository.save(cart);
  }
}
