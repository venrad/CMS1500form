'''
Created on Dec 5, 2016

@author: Venkatesh
'''

from pyth.cms.model.Entities import BillingProvider, FacilityProvider, RenderingProvider, ReferringProvider, BilledCpt, PaidCpt
from pyth.cms.properties import appProperties as appProp
import csv

import logging

module_logger = logging.getLogger('pyth.cms.dao.EntityDAO')

class ProviderDAO(object):
    pass

class BillingProviderDAO(ProviderDAO):
    def __init__(self):
        self.logger = logging.getLogger('pyth.cms.dao.EntityDAO.BillingProviderDAO')
        pass
    
        # function to get provider array to be used during the file file building
    def getBillProviders(self):
        billproviders=[]
        i=0
        with open(appProp.billproviderfilename, 'rU') as csvfile:
            csvread = csv.reader(csvfile, delimiter='|')
            for line in csvread:
                if appProp.billproviderhdr:
                    if i==0:
                        i+=1
                        continue
                billproviders.append(self.parseProviderInfo(line))        
            return billproviders
    
    #function to parse the line to get a provider object
    def parseProviderInfo(self, line):
        return BillingProvider(line[0], line[1], line[2], line[3], line[4],line[5], line[6])

    
class FacilityProviderDAO(ProviderDAO):
    '''
    classdocs
    '''
    def __init__(self):
        pass
    def getProviders(self):
        providers=[]
        i=0
        with open(appProp.providerfilename, 'rU') as csvfile:
            csvread = csv.reader(csvfile, delimiter='|')
            for line in csvread:
                if appProp.providerhdr:
                    if i==0:
                        i+=1
                        continue
                providers.append(self.parseProviderInfo(line))        
            return providers
    
    #function to parse the line to get a provider object
    def parseProviderInfo(self, line):
        return FacilityProvider(line[0], line[1], line[2], line[3], line[4],line[5])

class RenderingProviderDAO(ProviderDAO):
 
    def __init__(self):
        pass
        
    def getProviders(self):
        providers=[]
        i=0
        with open(appProp.providerfilename, 'rU') as csvfile:
            csvread = csv.reader(csvfile, delimiter='|')
            for line in csvread:
                if appProp.providerhdr:
                    if i==0:
                        i+=1
                        continue
                providers.append(self.parseProviderInfo(line))        
            return providers
    
    #function to parse the line to get a provider object
    def parseProviderInfo(self, line):
        return RenderingProvider(line[0], line[1], line[2], line[3], line[4],line[5])

class ReferringProviderDAO(ProviderDAO):

    def __init__(self):
        pass
            
    def getProviders(self):
        providers=[]
        i=0
        with open(appProp.providerfilename, 'rU') as csvfile:
            csvread = csv.reader(csvfile, delimiter='|')
            for line in csvread:
                if appProp.providerhdr:
                    if i==0:
                        i+=1
                        continue
                providers.append(self.parseProviderInfo(line))        
            return providers
    
    #function to parse the line to get a provider object
    def parseProviderInfo(self, line):
        return ReferringProvider(line[0], line[1], line[2], line[3], line[4],line[5])


class CptCodeDAO(object):
    pass

class BilledCptCodeDAO(CptCodeDAO):
    def getCodes(self):
        cptcodes=[]
        i=0
        with open(appProp.cptcodesfilename, 'rU') as csvfile:
            csvread = csv.reader(csvfile, delimiter='|')
            for line in csvread:
                if appProp.cpthdr:
                    if i==0:
                        i+=1
                        continue
                cptcodes.append(self.parsecptFileInfo(line))        
            return cptcodes
    
    def parsecptFileInfo(self, line,hdr=True):
        return BilledCpt(line[0], float(line[1]))
    
class PaidCptCodeDAO(CptCodeDAO):
    def getCodes(self):
        cptcodes=[]
        i=0
        with open(appProp.cptcodesfilename, 'rU') as csvfile:
            csvread = csv.reader(csvfile, delimiter='|')
            for line in csvread:
                if appProp.cpthdr:
                    if i==0:
                        i+=1
                        continue
                cptcodes.append(self.parsecptFileInfo(line))        
            return cptcodes
    
    def parsecptFileInfo(self, line,hdr=True):
        return PaidCpt(line[0], float(line[1]))
