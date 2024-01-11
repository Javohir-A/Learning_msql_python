import mysql.connector

try:
    with open('Password.txt', 'r') as get_file_info:
        passwd = get_file_info.read().strip()
except FileNotFoundError as file_err:
    print('Error occurred while opening file!: ', file_err)

mydb_dic = {
    "host": "localhost",
    "passwd": passwd,
    "user": "root",
    "database": "user_info"
}

try:
    with mysql.connector.connect(**mydb_dic) as get_access:
        my_cursor = get_access.cursor()

        # Create database if not exists
        my_cursor.execute('CREATE DATABASE IF NOT EXISTS user_info')

        # Switch to the user_info database
        my_cursor.execute("USE user_info")
        
        # Create table if not exists
        my_cursor.execute("""CREATE TABLE IF NOT EXISTS Customers (
                            CusomerId INT(10),
                            CustomerName VARCHAR(25),
                            PurchasedDetails VARCHAR(25))""")

        CustomerInfo = set()

        for i in range(2):
            id = i + 1
            name = input("Insert customer name: ")
            detail = input("Insert items detail: ")
            info = (id, name, detail)
            CustomerInfo.add(info)
            print(CustomerInfo)

        sqlFormula = "INSERT INTO Customers (CusomerId, CustomerName, PurchasedDetails) VALUES (%s, %s, %s)"

        my_cursor.executemany(sqlFormula, CustomerInfo)
        get_access.commit()

        my_cursor.execute("SELECT CustomerName FROM Customers")
        
        for x in my_cursor.fetchall():
            print(x)

except mysql.connector.Error as err:
    print(f"MySQL Connector error: {err}")
