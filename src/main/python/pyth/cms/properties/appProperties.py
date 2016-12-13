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
datesfilename='../resources/dates.txt'
dateshdr=True
specialityfilename='../resources/providerspeciality.txt'
splhdr=True
CLAIM_PREFIX='4302'
BILL_PREFIX='743'
MAX_CLAIMANT_COUNT = 3
MAX_CLAIM_COUNT = 20
MAX_BILLS_COUNT=7
MAX_LINES_PER_BILL=10
CLAIM_STATUS_RATIO=[90,10] # accept to reject ratio for example: '90 10' is 90% accepted and 10% rejected
target_sink='solr' # to specify more than one sink just list with a space in between 
target_sink_file_name='/tmp/cms1500.txt'
db_config = {'user':'mysql', 'password': 'mysql', 'host':'localhost', 'database':'bigdata'}
solrCollection='providerbilling'
solrUrl='http://localhost:8983/solr/'