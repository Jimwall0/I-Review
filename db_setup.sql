CREATE DATABASE IF NOT EXISTS media_catalog;
CREATE USER IF NOT EXISTS 'Andy'@'localhost' IDENTIFIED BY '@ver@g3V#1w3r';
GRANT ALL PRIVILEGES ON media_catalog.* TO 'Andy'@'localhost';
FLUSH PRIVILEGES;
USE media_catalog;

DROP TABLE IF EXISTS media;
CREATE TABLE IF NOT EXISTS media (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  watched ENUM('not watched', 'watched'),
  media_type ENUM('movie', 'show') NOT NULL,
  recommendation ENUM('Cracked', 'Wack') NOT NULL,
  review text
);

INSERT INTO media (title, watched, media_type, recommendation, review)
VALUES (
  'How to Train Your Dragon (Live Action)',
  'watched',
  'movie',
  'Cracked',
  "It's alright for a live action. It's good for the kids"
);
