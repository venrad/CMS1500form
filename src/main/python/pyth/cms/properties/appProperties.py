'''
Created on Dec 1, 2016

@author: Venkatesh
'''
providerfilename='../resources/providerlist.txt'
providerhdr=True
billproviderfilename='../resources/billproviderlist.txt'
billproviderhdr=True
claimantfilename='../resources/claimantlist.txt'
claimanthdr=True
cptcodesfilename='../resources/cptcodes.txt'
cpthdr=True
CLAIM_PREFIX='4302'
BILL_PREFIX='743'
MAX_CLAIMANT_COUNT = 3
MAX_CLAIM_COUNT = 60
MAX_BILLS_COUNT=70
MAX_LINES_PER_BILL=10
target_sink='file database'
target_sink_file_name='cms1500.txt'
db_config = {'user':'mysql', 'password': 'mysql', 'host':'localhost', 'database':'bigdata'}
solrCollection='providerbilling'
solrUrl='http://localhost:8983/solr/'