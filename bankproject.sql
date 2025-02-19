SET SQL_NODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT=0;
START TRANSACTION;
SET time_zone="+00:00";

CREATE DATABASE bankproject;

USE bankproject;

CREATE TABLE customer (
    acno INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(255),
    phone VARCHAR(15),
    email VARCHAR(100),
    aadhar_no VARCHAR(20),
    acc_type VARCHAR(20),
    balance DECIMAL(10, 2),
    status VARCHAR(20)
);

CREATE TABLE transaction (
    tid INT AUTO_INCREMENT PRIMARY KEY,
    acno INT,
    dot DATE,
    amount DECIMAL(10, 2),
    type VARCHAR(20),
    FOREIGN KEY (acno) REFERENCES customer(acno)
);
