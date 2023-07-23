package com.matheusmoura.api.controllers;

import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.matheusmoura.api.entities.Product;
import com.matheusmoura.api.services.ProductService;

import lombok.AllArgsConstructor;

@RestController
@RequestMapping("products")
@AllArgsConstructor
public class ProductController {

  ProductService productService;

  @GetMapping("/{id}")
  public Product get(@PathVariable Long id) {
    return productService.get(id);
  }

  @GetMapping
  public List<Product> list() {
    return productService.getAll();
  }

  @PutMapping("/{id}")
  public Product update(@PathVariable Long id, @RequestBody Product product) {
    return productService.update(id, product);
  }

  @PostMapping
  public Product create(@RequestBody Product product) {
    return productService.create(product);
  }

  @DeleteMapping("/{id}")
  public String delete(@PathVariable Long id) {
    productService.delete(id);
    return "Produto " + id + " removido com sucesso!";
  }
}
