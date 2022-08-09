from fastapi import FastAPI
import psycopg2
from psycopg2 import Error


app=FastAPI()

# establishing the connection
connection_to_database = psycopg2.connect(
    database="electronics_devices_db",
    user="postgres",
    password="pokemon123",
    host="localhost"
)

connection_to_database.autocommit = True

# creating cursor object
cursor = connection_to_database.cursor()

# create database
def create_database():
    '''This function is to create a database'''
    cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'electronics_devices_db'")
    exists = cursor.fetchone()
    if not exists:
       cursor.execute('CREATE DATABASE electronics_devices_db')


def create_table():
    '''This function creates a table'''
    cursor.execute('DROP TABLE IF EXISTS electronics_devices_details')
    create_table_for_database = (''' CREATE TABLE IF NOT EXISTS electronics_devices_details(electronic_device_name CHAR(255) PRIMARY KEY,transistor_used CHAR(255),
    ic_used CHAR(255),diode_used CHAR(255),cmos_semi_used CHAR(255),number_required INT)''')
    cursor.execute(create_table_for_database)
    connection_to_database.commit()
    print("Table created successfully........")
    return 


cursor.execute('''SELECT * from electronics_devices_details''')
#Fetching 1st row from the table
result = cursor.fetchall()
print(result)

try:
    x=create_table()
except (Exception, Error) as error:
    print(f"Error occurred",error)
finally:
    if connection_to_database:
        # closing the connection
        connection_to_database.close()

@app.post('/add_data_into_table')
def add_data_into_table():
    cursor.execute(f"INSERT INTO {x}(electronic_device_name,transistor_used,ic_used,diode_used,cmos_semi_used,number_required) VALUES(%s, %s, %s, %s, %s)")
    connection_to_database.commit()
    return ("Data ENTERED Successfully")


@app.put('/update_electronic_devices_data')
def update_electronic_devices_data():
    '''This is to do the UPDATE operation '''
    cursor.execute(f"UPDATE {x} SET electronic_device_name = %s, transistor_used = %s, ic_used = %s, diode_used = %s")
    connection_to_database.commit()
    connection_to_database.close()
    return ("Table Updated Successfully")


@app.get('/get_all_details')
def get_all_details(electronic_device_name:str,number_required:int):
    '''This is to do the UPDATE operation'''
    cursor.execute("UPDATE names SET electronics name? and number? ",[electronic_device_name,number_required])
    connection_to_database.commit()
    connection_to_database.close()
    return ("Table Updated Successfully")
   

@app.delete('/delete_electronic_device_name/{id}')
def delete_employee(electronic_device_name:str):
    '''This is to do the DELETE operation'''
    cursor.execute(f"DELETE FROM {x} WHERE electronic_device_name = %s",[electronic_device_name])
    connection_to_database.commit()
    connection_to_database.close()
    return ("Table Deleted Successfully")
