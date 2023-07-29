package com.matheusmoura.api.controllers;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.matheusmoura.api.services.CartService;
import com.matheusmoura.api.services.ProductService;

import lombok.AllArgsConstructor;

@RestController
@RequestMapping("seed")
@AllArgsConstructor
public class SeedController {
  private CartService cartService;
  private ProductService productService;

  @PostMapping
  public String index() {
    var cart = cartService.create(1L);
    var products = productService.seed();

    var result = cart.toString() + products.toString();

    return result;
  }
}
