package com.matheusmoura.api.services;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

import org.springframework.stereotype.Service;

import com.matheusmoura.api.entities.Product;
import com.matheusmoura.api.exceptions.ProductNotFoundException;
import com.matheusmoura.api.exceptions.ProductAlreadyExistsException;

import lombok.AllArgsConstructor;

@Service
@AllArgsConstructor
public class ProductService {

  private static Map<Long, Product> products = new HashMap<>();

  public Product get(Long id) {
    var product = products.get(id);
    if (product == null) {
      throw new ProductNotFoundException(id);
    }
    return product;
  }

  public List<Product> getAll() {
    return new ArrayList<>(products.values());
  }

  public Product update(Long id, Product product) {
    var exists = products.get(id) != null;
    if (!exists) {
      throw new ProductNotFoundException(id);
    }
    products.put(id, product);
    return product;
  }

  public Product create(Product product) {
    var id = product.getId();
    var exists = products.get(id) != null;
    if (exists) {
      throw new ProductAlreadyExistsException(id);
    }
    products.put(id, product);
    return product;
  }

  public void delete(Long id) {
    var exists = products.get(id) != null;
    if (!exists) {
      throw new ProductNotFoundException(id);
    }
    products.remove(id);
  }
}
