package com.matheusmoura.api.exceptions;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(HttpStatus.NOT_FOUND)
public class CartNotExistsException extends RuntimeException {
  public CartNotExistsException(Long id) {
    super("Carrinho " + id + " não encontrado!");
  }
}
