package com.matheusmoura.api.controllers;

import org.springframework.core.io.Resource;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import com.matheusmoura.api.services.FileService;

import jakarta.servlet.http.HttpServletRequest;

import com.matheusmoura.api.entities.File;

import lombok.AllArgsConstructor;

@RestController
@RequestMapping("files")
@AllArgsConstructor
public class FileController {
  private FileService fileService;

  @PostMapping("/upload")
  public File upload(@RequestParam("file") MultipartFile file) {
    var fileName = fileService.upload(file);
    var downloadUrl = ServletUriComponentsBuilder.fromCurrentContextPath()
        .path("/files/download/")
        .path(fileName)
        .toUriString();

    return new File(fileName, downloadUrl, file.getContentType(), file.getSize());
  }

  @GetMapping("/download/{fileName}")
  public ResponseEntity<Resource> download(@PathVariable String fileName, HttpServletRequest request) {
    var resource = fileService.download(fileName);
    var contentType = fileService.getContentType(request, resource);
    return ResponseEntity.ok()
        .contentType(MediaType.parseMediaType(contentType))
        .header("Content-Disposition", "attachment; filename=\"" + resource.getFilename() + "\"")
        .body(resource);
  }
}
