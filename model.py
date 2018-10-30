import sqlite3 
from sqlite3 import Error
import os
import libs.nucrypt as nc

def create_connection(db_file):
    """ Create a Database connection to sqllite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        # print('connected to database :'+ db_file)
        return conn
    except Error as e:
        pass
        # print(e)
    return None

def create_table(conn):
    """ Create a table in sqlite Database file """
    try:
        c = conn.cursor()
        # print('table creation started.')
        sql = """create table credential( 
                    id integer primary key autoincrement, 
                    name char(50) not null,
                    type char(50) not null,
                    user char(50) not null,
                    password  not null,
                    url char(100) not null
                    );"""

        c.execute(sql)
        # print('table created.')
    except Error as e:
        pass
        # print(e)

def insert_data(conn, data):
    """ Add data to created table """
    # print('data adding started')

    cp = nc.NuCrypt()
    try:
        c = conn.cursor()
        sql2 = """
                insert into credential values(
                  null, '{name}', '{type}', '{user}', "{password}",'{url}');
             """.format(name=data['name'].get().lower(), type=data['type'].get().lower(), user=data['user'].get(), password=cp.encrypt(data['password'].get()), url=data['url'].get())
        c.execute(sql2)
        conn.commit() #commit is mandatory
    except Error as e:
        pass
        # print(e)
        # print("DONE:", sql2)
    finally:
        c.close()

def select_from(conn, query):
    """ Get data from the database """
    try:
        c = conn.cursor()
        sql = """ select * from credential where name='{name}';""".format(name=query.lower())
        # print(sql)
        c.execute(sql)
        rows = c.fetchall()

        return rows
        
    except Error as e:
        pass
        # print(e)
    finally:
        c.close()
def execute_query(conn, query):
    """ Execute Given query on given database connection"""
    try:
        c = conn.cursor()
        # print(query)
        c.execute(query)
        rows = c.fetchall()

        return rows
    except Error as e:
        pass
        # print(e)

if __name__ == '__main__':
    create_connection('default.db')