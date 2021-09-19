import os
import datetime
import pymysql

# print(os.environ)

# Get usernames fro Cloud9 workspace???
# Connect to the database
connection = pymysql.connect(host='localhost', user='', password='', db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        
        row = ("Bob",)
        sql = "DELETE FROM Friends WHERE name = %s;"
        cursor.execute(sql, row)
        
        # sql = "DELETE FROM Friends WHERE name = 'Bob';"
        # cursor.execute(sql)

        # rows = [(24, "Bob"),(56,"Jim")]
        # sql = "UPDATE Friends SET age = %s WHERE name = %s;"
        # cursor.executemany(sql, rows)

        # row = (23, "Bob")
        # sql = "UPDATE Friends SET age = %s WHERE name = %s;"
        # cursor.execute(sql, row)

        # cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'Bob';")
        
        # rows = [("Bob", 21, "1990-02-06 23:04:56"),("Jim", 56, "1955-05-09 13:12:45"),("Fred", 100, "1911-09-12 01:01:01")]
        # sql = "INSERT INTO Friends VALUES (%s, %s, %s);"
        # cursor.executemany(sql, rows)

        connection.commit()
finally:
    # Close the connection regardless of whether the above was successful or not.
    connection.close()
