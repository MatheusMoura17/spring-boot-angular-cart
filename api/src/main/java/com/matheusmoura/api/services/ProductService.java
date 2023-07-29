package com.matheusmoura.api.services;

import java.io.File;
import java.util.List;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.matheusmoura.api.entities.Product;
import com.matheusmoura.api.exceptions.ProductNotFoundException;
import com.matheusmoura.api.exceptions.ProductSeedException;
import com.matheusmoura.api.repositories.ProductRepository;

import lombok.AllArgsConstructor;

@Service
@AllArgsConstructor
public class ProductService {
  private ProductRepository productRepository;

  public Product get(Long id) {
    if (!productRepository.existsById(id)) {
      throw new ProductNotFoundException(id);
    }
    return productRepository.findById(id).get();
  }

  public Page<Product> getAll(Integer page, Integer size) {
    var pageRequest = PageRequest.of(page, size);
    return productRepository.findAll(pageRequest);
  }

  public Product update(Long id, Product product) {
    product.setId(id);
    if (!productRepository.existsById(id)) {
      throw new ProductNotFoundException(id);
    }

    return productRepository.save(product);
  }

  public Product create(Product product) {
    var saved = productRepository.save(product);
    return saved;
  }

  public void delete(Long id) {
    if (!productRepository.existsById(id)) {
      throw new ProductNotFoundException(id);
    }
    productRepository.deleteById(id);
  }

  public List<Product> seed() {
    try {
      var mapper = new ObjectMapper();
      var products = mapper.readValue(new File("products.json"), Product[].class);
      var saved = productRepository.saveAll(List.of(products));
      return saved;
    } catch (Exception e) {
      System.out.println("Falha ao efetuar seed: " + e.getMessage());
      throw new ProductSeedException("Falha ao efetuar seed: " + e.getMessage());
    }
  }
}
