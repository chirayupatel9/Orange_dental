import mysql.connector
from mysql.connector import Error, connection
import webbrowser
import datetime

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='orangedental',
                                         user='root',
                                         password='')
    cursor = connection.cursor()
    print("connected")

except mysql.connector.Error as error:
    print("Failed to insert into MySQL table {}".format(error))


def insertVariblesIntoTable(name, number, proced, insurance):
    x = datetime.datetime.now()
    mySql_insert_query = """INSERT INTO myoffice (name,number,proced,insurance,rdate) 
                                VALUES (%s, %s, %s, %s, %s) """
    recordTuple = (name, number, proced, insurance, x)
    cursor.execute(mySql_insert_query, recordTuple)
    connection.commit()
    # print("Record inserted successfully into Laptop table")
    return print("Thank you")

# insertVariblesIntoTable("sha", 9081985540, "cleaning", "yes")


def printvaluesfrommyoffice():
    mycursor = connection.cursor()

    mycursor.execute("SELECT * FROM myoffice")

    myresult = mycursor.fetchall()

    return myresult


# DELETE FROM myoffice;
# def checkin(boo):
#     mycursor = connection.cursor()
#     mySql_insert_query = """INSERT INTO myoffice (check_in) VALUES (%s)"""
#     recordTuple = (boo)
#     cursor.execute(mySql_insert_query, recordTuple)
#     connection.commit()
#     return print("DOne")

# checkin(1)

def tryregister(username, password, email):
    mycursor = connection.cursor()
    # mycursor.execute("SELECT * FROM frontdesk", username, password,email)
    # rs = mycursor.fetchall()
    mySql_insert_query = """INSERT INTO frontdesk (username,password,email) 
                                   VALUES (%s, %s, %s) """
    recordTuple = (username, password, email)
    cursor.execute(mySql_insert_query, recordTuple)
    connection.commit()
    return print("done")
# print(tryregister("chirayu","abc@123","abc@abc.com"))

# def fetcher(username,password):
