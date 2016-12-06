'''
Created on Dec 2, 2016

@author: Venkatesh
'''

from __future__ import print_function

import pysolr, json
from pyth.cms.properties import appProperties

class CMSSolr(object):
    def __init__(self):
        self.solrUrl = appProperties.solrUrl
        self.solrCollection=appProperties.solrCollection
        self.conn = pysolr.Solr(self.solrUrl+self.solrCollection)
            
    def insertDocument(self,bill_dict):
        arr=[]
        arr.append(bill_dict.solrFormat())
        print(arr)
        self.conn.add(arr)