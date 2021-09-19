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
        rows = [("Bob", 21, "1990-02-06 23:04:56"),("Jim", 56, "1955-05-09 13:12:45"),("Fred", 100, "1911-09-12 01:01:01")]
        sql = "INSERT INTO Friends VALUES (%s, %s, %s);"
        cursor.executemany(sql, rows)
        # sql = "DELETE FROM Friends WHERE name = 'Nic';"
        # cursor.execute(sql)
        connection.commit()
finally:
    # Close the connection regardless of whether the above was successful or not.
    connection.close()
