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
con.set_trace_callback(print)
cur = con.cursor()
mail = input("Mail: ")
print("Command:", end=' ')
SQL = "SELECT * FROM test WHERE mail=?"
cur.execute(SQL, (mail, ))
print("Output: ", cur.fetchall())
con.commit()
con.close()
