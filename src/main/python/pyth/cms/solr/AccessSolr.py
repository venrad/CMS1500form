'''
Created on Dec 2, 2016

@author: Venkatesh
'''

import pysolr


class CMSSolr(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.solrUrl = 'http://localhost:8983/solr/'
        self.solrCollection='providerbilling'
    
    def querySolrCollection(self):

        #SolrConnection(self.solrUrl+self.solrCollection)
        
        r = s.query() 
        print r

c = CMSSolr()
c.querySolrCollection()
           