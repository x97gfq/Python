
CREATE DATABASE `barcodescanner`;

CREATE TABLE `barcode_master` (
  `id` int NOT NULL AUTO_INCREMENT,
  `barcode` varchar(50) NOT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `barcode_scanned` (
  `id` int NOT NULL AUTO_INCREMENT,
  `barcode` varchar(100) NOT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  `datetimestamp` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);