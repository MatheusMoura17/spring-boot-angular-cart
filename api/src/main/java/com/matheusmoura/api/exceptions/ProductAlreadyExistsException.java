package com.matheusmoura.api.exceptions;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(HttpStatus.BAD_REQUEST)
public class ProductAlreadyExistsException extends RuntimeException {
  public ProductAlreadyExistsException(Long id) {
    super("Produto " + id + " já existe!");
  }
}
