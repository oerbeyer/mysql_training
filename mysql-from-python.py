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
        row = ("Nic", 21, "1990-02-06 23:04:56")
        sql = "INSERT INTO Friends VALUES (%s, %s, %s);"
        # sql = "DELETE FROM Friends WHERE name = 'Nic';"
        cursor.execute(sql, row)
        # cursor.execute(sql)
        connection.commit()
finally:
    # Close the connection regardless of whether the above was successful or not.
    connection.close()
