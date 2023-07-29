package com.matheusmoura.api.controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.matheusmoura.api.entities.Cart;
import com.matheusmoura.api.services.CartService;

import lombok.AllArgsConstructor;

@RestController
@RequestMapping("carts")
@AllArgsConstructor
public class CartController {
  CartService cartService;

  @GetMapping("/{id}")
  public Cart get(@PathVariable Long id) {
    return cartService.get(id);
  }

  @PostMapping("/add-product")
  public Cart addProduct(@RequestParam Long cartId, @RequestParam Long productId, @RequestParam Integer amount) {
    return cartService.addProduct(cartId, productId, amount);
  }

  @PostMapping("/remove-product")
  public Cart removeProduct(@RequestParam Long cartId, @RequestParam Long productId, @RequestParam Integer amount) {
    return cartService.removeProduct(cartId, productId, amount);
  }
}
