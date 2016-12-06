'''
Created on Dec 5, 2016

@author: Venkatesh
'''

from pyth.cms.model.Entities import BillingProvider, FacilityProvider, RenderingProvider, ReferringProvider, BilledCpt, PaidCpt
from pyth.cms.properties import appProperties as appProp
import csv

class ProviderDAO(object):
    pass
    
class FacilityProviderDAO(ProviderDAO):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
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
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
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
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
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
