import pymysql
import pymysql.cursors

from mysql.connector import connect, Error

def get_connection():
    connection = pymysql.connect(host="localhost",
                                 user="admin",
                                 password="zxc123",
                                 db="no_db",
                                 charset="utf8",
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


def f_connection():
    f_conn = connect(
        host="localhost",
        user="admin",
        password="zxc123",
    )
    return f_conn


def make_db():
    f_conn = f_connection()
    try:
        with f_conn.cursor() as cursor:
            sql = 'CREATE DATABASE IF NOT EXISTS no_db'
            cursor.execute(sql)
    finally:
        f_conn.close()


def make_table():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'CREATE TABLE IF NOT EXISTS users (\nid INT NOT NULL AUTO_INCREMENT,\n user_id varchar(256),\ntext varchar(256),\nsrc varchar(256)б\ncnt INT\nsent INT;'
            cursor.execute(sql)
    finally:
        connection.close()


def add_user(user_id, source, text):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql1 = 'SELECT * FROM no_db WHERE user_id = %s'
            check = cursor.execute(sql1, (user_id))
            connection.commit()

            if check == 0:
                sql2 = 'INSERT INTO no_db (user_id, src, text) VALUES (%s, %s, %s)'
                cursor.execute(sql2, (user_id, source, text))
                connection.commit()
    finally:
        connection.close()
    return


def get_user():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM no_db WHERE sent = 0'
            cursor.execute(sql)
            user = cursor.fetchone()
    finally:
        connection.close()
    return user
