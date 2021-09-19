import os
import datetime
import pymysql

# print(os.environ)

# Get usernames fro Cloud9 workspace???
# Connect to the database
connection = pymysql.connect(host='localhost', user='', password='', db='Chinook')

try:
    # Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = """CREATE TABLE IF NOT EXISTS Friends(name char(20), age int, DOB datetime);"""
        cursor.execute(sql)
        # Note that the above will still display a warning (no error) if the table already exists
        for row in cursor:
            print(row)
finally:
    # Close the connection regardless of whether the above was successful or not.
    connection.close()