'''
Created on Nov 30, 2016

@author: Venkatesh
'''
from pyth.cms.model.Entities import CptCode, BillingProvider, FacilityProvider, Provider, Claimant

        
def printdict(home_d={},output={}):
    keys = home_d.keys()
    for key in keys:
        if isinstance(home_d[key], dict):
            printdict(home_d[key],output)
        elif isinstance(home_d[key],CptCode) or isinstance(home_d[key],BillingProvider) or isinstance(home_d[key],Provider) or isinstance(home_d[key],Claimant):
            printdict(home_d[key].__dict__,output)
        else:
            output[key]=home_d[key]

def solrFormat(self):
     output={}
     self.printdict(self.__dict__, output)
     return output


import urllib2, json

req = urllib2.Request('http://localhost:8983/solr/providerbilling/select?q=*%3A*&wt=json&indent=true&facet=true&facet.field=billingprovidertaxid')
response = urllib2.urlopen(req)
this_page = json.loads(response.read())

for keys in this_page.keys():
    print(keys)
    if keys == 'response':
        print(this_page[keys])
    elif keys == 'facet_counts':
        print(this_page[keys]['facet_fields'])    

'''

def printdict(dictitem,d2):
    keys = dictitem.keys()
    for key in keys:
        if isinstance(dictitem[key], dict):
            printdict(dictitem[key],d2)
        elif isinstance(dictitem[key],CptCode):
            d2[key]=dictitem[key].__dict__
        else:
            d2[key]=dictitem[key]

'''

d={
    "a": 1,
    "b": {
        "v": 22,
        "w": CptCode("99898",12.11),
        "x": {
            "x1": 2,
            "x2": 3
            }
          }
   }

d2={}
#printdict(d,d2)
#print d2

#from pyth.cms.solr.AccessSolr import CMSSolr

#c = CMSSolr()
#d = c.conn.add([{'claimnumber': '4302100', 'billingproviderzipcode': '10110', 'facilityproviderzipcode': '20557', 'claimantname': 'Andrea Wood', 'billingprovidernpi': '1324040', 'billingproviderstate': 'NY', 'billedcptamount': 17867.0, 'renderingprovidercity': 'Washington', 'billingprovideraddr1': '70389 Fairfield Center', 'facilityprovideraddr1': '831 Dayton Alley', 'billedcptcode': '99082', 'renderingprovidername': 'McKesson Packaging Services Business unit of McKesson Corporation', 'paidcptamount': 17867.0, 'facilityprovidername': 'McKesson Packaging Services Business unit of McKesson Corporation', 'claimantcity': 'Kansas City', 'renderingproviderzipcode': '20557', 'billingprovidercity': 'New York City', 'linenumber': 1, 'renderingprovidernpi': '1324069', 'paidcptcode': '99082', 'claimantgender': 'Female', 'claimantzipcode': '64136', 'renderingproviderstate': 'DC', 'billingprovidername': 'Akorn, Inc.', 'claimantid': '4232142', 'claimantaddr1': '4066 David Point', 'facilityproviderstate': 'DC', 'facilityprovidercity': 'Washington', 'billingprovidertaxid': '9432424', 'facilityprovidernpi': '1324069', 'claimantstate': 'Missouri', 'bills': '7434302100000', 'renderingprovideraddr1': '831 Dayton Alley'}]
#)

# def time_this(original_function):      
#     def new_function(*args,**kwargs):
#         import datetime                 
#         before = datetime.datetime.now()                     
#         x = original_function(*args,**kwargs)                
#         after = datetime.datetime.now()                      
#         print "Elapsed Time = {0}".format(after-before)      
#         return x                                             
#     return new_function                                   
# 
# @time_this
# def func_a(stuff):
#     import time
#     time.sleep(3)
# 
# if __name__ == '__main__':
#     func_a(1)