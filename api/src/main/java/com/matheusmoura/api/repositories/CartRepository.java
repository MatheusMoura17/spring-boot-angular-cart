package com.matheusmoura.api.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.matheusmoura.api.entities.Cart;

@Repository
public interface CartRepository extends JpaRepository<Cart, Long> {

}
