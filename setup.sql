DROP DATABASE IF EXISTS bankproject;
CREATE DATABASE bankproject;
USE bankproject;

CREATE TABLE customer (
    acno INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL,
    aadhar_no VARCHAR(20) NOT NULL,
    acc_type VARCHAR(20) NOT NULL,
    balance DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL
) AUTO_INCREMENT = 1001;

CREATE TABLE transaction (
    tid INTEGER PRIMARY KEY AUTO_INCREMENT,
    acno INTEGER NOT NULL,
    dot DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    type VARCHAR(20) NOT NULL,
    FOREIGN KEY (acno) REFERENCES customer(acno)
);