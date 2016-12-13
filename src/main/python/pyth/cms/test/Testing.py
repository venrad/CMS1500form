'''
Created on Dec 13, 2016

@author: Venkatesh
'''
from pyth.cms.dao.EntityDAO import BillingProviderDAO
import random
import pyth.cms.properties.appProperties as appProp

def test1():
        
    pdao = BillingProviderDAO()
    spl = pdao.getBillProviders()
    for x in spl:
        print x

def test2():
    const = 20
    rat = [89,10]
    s = int(20* rat[0]/100)
    print s

def test3():
    NO_OF_CLAIMS=6
    clm_ctr=1
    status=[]
    for x in range(1,NO_OF_CLAIMS):
        print NO_OF_CLAIMS * appProp.CLAIM_STATUS_RATIO[0]/100
        clm_status = 'Accepted' if(clm_ctr < (NO_OF_CLAIMS * appProp.CLAIM_STATUS_RATIO[0]/100)) else 'Rejected'
        status.append(clm_status)
        clm_ctr+=1
    print status


test3()