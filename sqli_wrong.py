#!/usr/bin/env python3
"""
Author: Jakob Schaffarczyk
Date: 24. April 2021
Contact: Jakob.Schaffarczyk@leibniz-fh.de
Description: correct implementation of parsed SQL input
"""
import sqlite3 as sqlite
DB = "tutorial.db"

con = sqlite.connect(DB)
cur = con.cursor()
mail = input("Mail: ")
sql = f"SELECT * FROM test WHERE mail=\"{mail}\""
print("Command:", sql)
cur.execute(sql)
print("Output: ", cur.fetchall())
con.close()
