# Banking Project
A comprehensive banking management system built with Python and MySQL that allows for account management, transaction, and customer data handling.
## Features:
### Account Management 
•	Create new bank accounts
•	Modify existing account details
•	Close/Activate accounts
•	View account details
### Transaction Management 
•	Deposit funds
•	Withdraw funds
•	View transaction history
### earch Functionality 
•	Search by Account Number
•	Search by Aadhar Card
•	Search by Phone Number
•	Search by Email
•	Search by Customer Name

## Prerequisites
•	Python 3.x
•	MySQL 8.0 or higher
•	mysql-connector-python

## Installation
1.	Clone the repository:
3.	Install required Python packages:
    ![image](https://github.com/user-attachments/assets/54352a3d-068d-4f53-a645-bc4147a692c2)
  	![image](https://github.com/user-attachments/assets/aede7e9f-fe8f-4de2-8b1b-3ab926ffa07e)
3.	Set up the MySQL database:
   ![image](https://github.com/user-attachments/assets/a4e9746b-5e08-43a1-a164-ea61c22d9e76)

## Database Configuration
1.	Open Banking.py
2.	Update the MySQL connection details with your credentials:
   ![image](https://github.com/user-attachments/assets/15b5049a-56d0-4c19-90fa-c43eee228b78)

## Database Schema
### Customer Table
•	acno - Account Number (Primary Key, Auto Increment)
•	name - Customer Name
•	address - Customer Address
•	phone - Phone Number
•	email - Email Address
•	aadhar_no - Aadhar Card Number
•	acc_type - Account Type (savings/current)
•	balance - Current Balance
•	status - Account Status (active/closed)

### Transaction Table
•	tid - Transaction ID (Primary Key, Auto Increment)
•	acno - Account Number (Foreign Key)
•	dot - Date of Transaction
•	amount - Transaction Amount
•	type - Transaction Type (deposit/withdraw)

## Usage
### 1.	Run the application:
![image](https://github.com/user-attachments/assets/9ea17346-5ae1-4bed-a83a-efb2726c079c)
### 2.	Main Menu Options: 
•	Add Account
•	Modify Account
•	Close Account
•	Activate Account
•	Transaction Menu
•	Search Menu
•	Close Application
### 3.	Transaction Menu Options: 
•	Deposit Amount
•	Withdraw Amount
•	Back to Main Menu
### 4.	Search Menu Options: 
•	Search by Account Number
•	Search by Aadhar Card
•	Search by Phone Number
•	Search by Email
•	Search by Names
•	Back to Main Menu

## Security Features
•	Account status verification before transactions
•	Transaction logging
•	Balance validation for withdrawals
•	Data integrity through MySQL foreign key constraints

## Error Handling
The system includes comprehensive error handling for:
•	Database connection issues
•	Invalid input data
•	Insufficient funds
•	Closed/Suspended accounts
•	Transaction failures

## Author: Suman Ghosh
