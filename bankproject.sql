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

INSERT INTO customer (acno, name, address, phone, email, aadhar_no, acc_type, status, balance) VALUES
(1, 'riya singhal', 'cf-4 surya nagar', '987181818', 'support@gmail.com', '1234-1243-4545', 'saving', 'active', 12200.00),
(2, 'mansi goyal', 'A-75-B Brij Vihar', '9673434318', 'raju@gmail.com', '4545-1243-4545', 'current', 'active', 10000.00),
(3, 'archana', 'cf04', '4545456', 'archana@gmail.com', '1234-5656-4545', 'saving', 'active', 10000.00),
(7, 'Veronica', 'J-50', '112233', 'a@gmail.com', '123456', 'saving', 'active', 19500.00);

CREATE TABLE transaction (
    tid INT AUTO_INCREMENT PRIMARY KEY,
    acno INT,
    dot DATE,
    amount DECIMAL(10, 2),
    type VARCHAR(20),
    FOREIGN KEY (acno) REFERENCES customer(acno)
);

INSERT INTO transaction (tid, dot, amount, type, acno) VALUES
(1, '2022-10-16', 2000, 'deposit', 1),
(2, '2022-10-15', 2000, 'deposit', 2),
(3, '2022-10-16', 1200, 'withdraw', 7),
(4, '2022-09-26', 10000, 'deposit', 7),
(5, '2022-09-26', 5000, 'withdraw', 7);
