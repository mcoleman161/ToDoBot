##This file serves as a method to interact with an SQLite Database'
import sqlite3
import os
import datetime
import time
import json
import sys
import logging
import traceback
import re

class DatabaseWrapper:
    def __init__(self):
        self.db = 'database.db'
        self.conn = sqlite3.connect(self.db)
        self.c = self.conn.cursor()
        self.createTable()
        self.createUsersTable()
        self.createList
    
    def createTable(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, user TEXT, date TEXT, completed INTEGER)')
        self.conn.commit()
    
    ##we need to query 