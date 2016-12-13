'''
Created on Dec 2, 2016

@author: Venkatesh
'''

from __future__ import print_function

from mysql.connector import cursor
from pyth.cms.properties import appProperties as appProp
import mysql.connector, pysolr, json
import csv


class DbConnector(object):
    def __init__(self, appProp):
        self.appProp = appProp
        self.mysqlConnect=''
    
    def connect(self):  
        self.mysqlConnect = mysql.connector.connect(**self.appProp.db_config)
        
    def insertRecord(self, billLine):
        hdr='(ClaimantId, ClaimantName, Gender, ClaimantAddress, ClaimantCity, ClaimantState, ClaimantZipcode, ClaimNumber, BillNumber, TaxId, BillingProviderNPI, BillingProviderName, BillingProviderAddress, BillingProviderCity, BillingProviderState, BillingProviderZip, BillingProviderSpeciality, RenderingProviderNPI, RenderingProviderName, RenderingProviderAddress, RenderingProviderCity, RenderingProviderState, RenderingProviderZip, FacilityProviderNPI, FacilityProviderName, FacilityProviderAddress, FacilityProviderCity, FacilityProviderState, FacilityProviderZip, LineNumber, BilledCPTcode, BilledAmount, PaidCPTcode, PaidAmount, ReceivedDate, ServiceDate, ClaimStatus)'
        insert_stmt = 'INSERT INTO BillLines '+ hdr + ' VALUES (' + billLine.dbOutputFormat() + ')'
        #print(insert_stmt)
        self.connect()
        cur = self.mysqlConnect.cursor()
        cur.execute(insert_stmt) 
        self.mysqlConnect.commit()
        cur.close()
        self.mysqlConnect.close() 



class SolrConnector(object):
    def __init__(self,appProp):
        self.solrUrl = appProp.solrUrl
        self.solrCollection=appProp.solrCollection
        self.conn = pysolr.Solr(self.solrUrl+self.solrCollection)
            
    def insertDocument(self,bill_dict):
        #arr=[]
        #arr.append(bill_dict.solrFormat())
        #print(arr)
        self.conn.add(bill_dict)
        
class FileConnector(object):
    def __init__(self,appProp):
        self.appProp = appProp
        self.csvwriter = open(appProp.target_sink_file_name, 'wb')
        self.csvwriter.seek(0)
        
    def close(self):
        self.csvwriter.close()
        
    def writelines(self,line):
            self.csvwriter.write(line + '\n');
            
    def writehdr(self, fileheader):
            self.csvwriter.write(fileheader + '\n')
