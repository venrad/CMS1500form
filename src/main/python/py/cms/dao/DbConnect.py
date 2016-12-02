'''
Created on Dec 2, 2016

@author: Venkatesh
'''

from __future__ import print_function
import mysql.connector
from mysql.connector import cursor

class DbConnector(object):
    '''
    classdocs
    '''


    def __init__(self, appProp):
        '''
        Constructor
        '''
        self.appProp = appProp
        self.mysqlConnect=''
    
    def connect(self):  
        self.mysqlConnect = mysql.connector.connect(**self.appProp.db_config)
        
    def insertRecord(self, billLine):
        insert_stmt = 'INSERT INTO BillLines VALUES (' + billLine.dbOutputFormat() + ')'
        self.connect()
        cur = self.mysqlConnect.cursor()
        cur.execute(insert_stmt)  