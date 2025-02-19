from db_config import get_db_config
import mysql.connector
from datetime import date

def get_connection():
    return mysql.connector.connect(**get_db_config())

def clear():
    for _ in range(65):
        print()



def account_status(acno):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT status, balance FROM customer WHERE acno=%s"
    cursor.execute(sql, (acno,))
    result = cursor.fetchone()
    conn.close()
    return result

def deposite_amount():
    conn = get_connection()
    cursor = conn.cursor()
    clear()
    acno = input('Enter account No :')
    amount = input('Enter amount :')
    today = date.today()
    result = account_status(acno)
    if result and result[0] == 'active':
        sql1 = "UPDATE customer SET balance = balance + %s WHERE acno = %s AND status='active'"
        sql2 = "INSERT INTO transaction (amount, type, acno, dot) VALUES (%s, 'deposit', %s, %s)"
        cursor.execute(sql1, (amount, acno))
        cursor.execute(sql2, (amount, acno, today))
        conn.commit()
        print('\n\nAmount deposited')
    else:
        print('\n\nClosed or Suspended Account...')
    input('\n\n\n Press any key to continue...')
    conn.close()

def withdraw_amount():
    conn = get_connection()
    cursor = conn.cursor()
    clear()
    acno = input('Enter account No :')
    amount = input('Enter amount :')
    today = date.today()
    result = account_status(acno)
    if result and result[0] == 'active':
        sql1 = "UPDATE customer SET balance = balance - %s WHERE acno = %s AND status='active'"
        sql2 = "INSERT INTO transaction (amount, type, acno, dot) VALUES (%s, 'withdraw', %s, %s)"
        cursor.execute(sql1, (amount, acno))
        cursor.execute(sql2, (amount, acno, today))
        conn.commit()
        print('\n\nAmount Withdrawn')
    else:
        print('\n\nClosed or Suspended Account or Insufficient amount.')
    input('\n\n\n Press any key to continue...')
    conn.close()

def transaction_menu():
    while True:
        clear()
        print(' Transaction Menu')
        print('\n1. Deposit Amount')
        print('\n2. Withdraw Amount')
        print('\n3. Back to Main Menu')
        print('\n\n')
        choice = int(input('Enter your choice...: '))
        if choice == 1:
            deposite_amount()
        elif choice == 2:
            withdraw_amount()
        elif choice == 3:
            break

def search_menu():
    conn = get_connection()
    cursor = conn.cursor()
    while True:
        clear()
        print(' Search Menu')
        print('\n1. Account No')
        print('\n2. Aadhar Card')
        print('\n3. Phone No')
        print('\n4. Email')
        print('\n5. Names')
        print('\n6. Back to Main Menu')
        print('\n\n')
        choice = int(input('Enter your choice...: '))
        field_name = ''
        
        if choice == 1:
            field_name = 'acno'
        elif choice == 2:
            field_name = 'aadhar_no'
        elif choice == 3:
            field_name = 'phone'
        elif choice == 4:
            field_name = 'email'
        elif choice == 5:
            field_name = 'name'
        elif choice == 6:
            break
        msg = 'Enter ' + field_name + ': '
        value = input(msg)
        if field_name == 'acno':
            sql = 'SELECT * FROM customer WHERE ' + field_name + ' = %s'
            cursor.execute(sql, (value,))
        else:
            sql = 'SELECT * FROM customer WHERE ' + field_name + ' LIKE %s'
            cursor.execute(sql, ('%' + value + '%',))
        records = cursor.fetchall()
        n = len(records)
        clear()
        print('Search Result for ', field_name, ' ', value)
        print('-' * 80)
        for record in records:
            print(record)
        if n <= 0:
            print(field_name, ' ', value, ' does not exist')
        input('\n\n\n Press any key to continue...')
    conn.close()

def account_details():
    clear()
    acno = input('Enter account no :')
    conn = get_connection()
    cursor = conn.cursor()
    sql = 'SELECT * FROM customer WHERE acno = %s'
    sql1 = 'SELECT tid, dot, amount, type FROM transaction WHERE acno = %s'
    cursor.execute(sql, (acno,))
    result = cursor.fetchone()
    clear()
    print('Account Details')
    print('-' * 120)
    print('Account No :', result[0])
    print('Customer Name :', result[1])
    print('Address :', result[2])
    print('Phone No :', result[3])
    print('Email ID :', result[4])
    print('Aadhar No :', result[5])
    print('Account Type :', result[6])
    print('Account Status :', result[7])
    print('Current Balance :', result[8])
    print('-' * 120)
    cursor.execute(sql1, (acno,))
    results = cursor.fetchall()
    for result in results:
        print(result[0], result[1], result[2], result[3])
    conn.close()
    input('\n\n\n Press any key to continue...')


def add_account():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Get user input
        name = input('Enter Name :')
        addr = input('Enter address :')
        phone = input('Enter Phone no :')
        email = input('Enter Email :')
        aadhar = input('Enter Aadhar no :')
        acc_type = input('Account Type (saving/current) :')
        balance = float(input('Enter opening balance :'))  # Convert to float
        
        # SQL query with explicit column names
        sql = """
            INSERT INTO customer 
            (name, address, phone, email, aadhar_no, acc_type, balance, status) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, 'active')
        """
        
        # Execute the query with parameters
        cursor.execute(sql, (name, addr, phone, email, aadhar, acc_type, balance))
        
        # Get the new account number
        acno = cursor.lastrowid
        
        conn.commit()
        print(f'\n\nNew customer added successfully with Account Number: {acno}')
        
    except mysql.connector.Error as err:
        print(f"\n\nDatabase Error: {err}")
        conn.rollback()
        
    except Exception as err:
        print(f"\n\nError: {err}")
        conn.rollback()
        
    finally:
        input('\n\n\nPress any key to continue...')
        if conn.is_connected():
            cursor.close()
            conn.close()

def modify_account():
    conn = get_connection()
    cursor = conn.cursor()
    acno = input('Enter customer Account No :')
    print('Modify screen ')
    print('\n 1. Customer Name')
    print('\n 2. Customer Address')
    print('\n 3. Customer Phone No')
    print('\n 4. Customer Email ID')
    choice = int(input('What do you want to change ? '))
    new_data = input('Enter New value :')
    field_name = ''
    if choice == 1:
        field_name = 'name'
    elif choice == 2:
        field_name = 'address'
    elif choice == 3:
        field_name = 'phone'
    elif choice == 4:
        field_name = 'email'
    sql = 'UPDATE customer SET ' + field_name + ' = %s WHERE acno = %s'
    cursor.execute(sql, (new_data, acno))
    conn.commit()
    print('\n\nCustomer Information modified..')
    input('\n\n\n Press any key to continue...')
    conn.close()

def close_account():
    conn = get_connection()
    cursor = conn.cursor()
    clear()
    acno = input('Enter customer Account No :')
    sql = 'UPDATE customer SET status="close" WHERE acno=%s'
    cursor.execute(sql, (acno,))
    conn.commit()
    print('\n\nAccount closed')
    input('\n\n\n Press any key to continue...')
    conn.close()

def active_account():
    conn = get_connection()
    cursor = conn.cursor()
    clear()
    acno = input('Enter customer Account No :')
    sql = 'UPDATE customer SET status="active" WHERE acno=%s'
    cursor.execute(sql, (acno,))
    conn.commit()
    print('\n\nAccount Activated')
    input('\n\n\n Press any key to continue...')
    conn.close()

def main_menu():
    while True:
        clear()
        print(' Main Menu')
        print('\n1. Add Account')
        print('\n2. Modify Account')
        print('\n3. Close Account')
        print('\n4. Activate Account')
        print('\n5. Transaction Menu')
        print('\n6. Search Menu')
        print('\n7. Close application')
        print('\n\n')
        choice = int(input('Enter your choice.. :'))
        if choice == 1:
            add_account()
        elif choice == 2:
            modify_account()
        elif choice == 3:
            close_account()
        elif choice == 4:
            active_account()
        elif choice == 5:
            transaction_menu()
        elif choice == 6:
            search_menu()
        elif choice == 7:
            break

if __name__ == "__main__":
    main_menu()