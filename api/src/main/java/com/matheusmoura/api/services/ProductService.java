package com.matheusmoura.api.services;

import java.util.List;

import org.springframework.stereotype.Service;

import com.matheusmoura.api.entities.Product;
import com.matheusmoura.api.exceptions.ProductNotFoundException;
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

  public List<Product> getAll() {
    return productRepository.findAll();
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
}
