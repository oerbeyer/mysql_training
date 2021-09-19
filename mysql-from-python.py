import os
import pymysql


# print(os.environ)

# Get usernames fro Cloud9 workspace???
# Connect to the database
connection = pymysql.connect(host='localhost', user='', password='', db='Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection regardless of whether the above was successful or not
    connection.close()