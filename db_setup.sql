CREATE DATABASE IF NOT EXISTS media_catalog;
CREATE USER IF NOT EXISTS 'Andy'@'localhost' IDENTIFIED BY '@ver@g3V#1w3r';
GRANT ALL PRIVILEGES ON media_catalog.* TO 'Andy'@'localhost';
FLUSH PRIVILEGES;
USE media_catalog;

CREATE TABLE IF NOT EXISTS media (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  watched BOOLEAN DEFAULT FALSE,
  media_type ENUM('movie', 'show') NOT NULL,
  recommendation ENUM('Cracked', 'Wack') NOT NULL,
  review text
);