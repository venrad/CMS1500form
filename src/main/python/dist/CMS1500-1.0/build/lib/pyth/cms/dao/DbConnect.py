'''
Created on Dec 2, 2016

@author: Venkatesh
'''

from __future__ import print_function

from mysql.connector import cursor
import mysql.connector


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
        hdr='(ClaimantId, ClaimantName, Gender, ClaimantAddress, ClaimantCity, ClaimantState, ClaimantZipcode, ClaimNumber, BillNumber, BillingProviderNPI, BillingProviderName, BillingProviderAddress, BillingProviderCity, BillingProviderState, BillingProviderZip, RenderingProviderNPI, RenderingProviderName, RenderingProviderAddress, RenderingProviderCity, RenderingProviderState, RenderingProviderZip, FacilityProviderNPI, FacilityProviderName, FacilityProviderAddress, FacilityProviderCity, FacilityProviderState, FacilityProviderZip, LineNumber, BilledCPTcode, BilledAmount, PaidCPTcode, PaidAmount)'
        insert_stmt = 'INSERT INTO BillLines '+ hdr + ' VALUES (' + billLine.dbOutputFormat() + ')'
        print(insert_stmt)
        self.connect()
        cur = self.mysqlConnect.cursor()
        cur.execute(insert_stmt) 
        self.mysqlConnect.commit()
        cur.close()
        self.mysqlConnect.close() 