#!/usr/bin/python3
#coding=utf-8

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","root","zwdtest")

# 使用游标
cursor = db.cursor()

cursor.execute("select version()")

sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)
cursor.close()