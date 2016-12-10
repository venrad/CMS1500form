'''

This module would host class definitions for the entities 
1. Providers
2. Claimants
3. CPT codes
4. BillLine

Created on Nov 30, 2016

@author: Venkatesh
'''

import csv

from pyth.cms.properties import appProperties


class Provider:             
    def __init__(self,  npi='', name='', addr1='', city='', state='', zipcode=''):
        self.npi = npi
        self.name = name
        self.addr1 = addr1
        self.city = city
        self.state = state
        self.zipcode = zipcode
            
    def __str__(self):
        return '%s | %s| %s| %s| %s| %s' %(self.npi, self.name, self.addr1, self.city, self.state, self.zipcode)
    
    def printHeaderLabels(self,type=''):
       prefix=type+self.__class__.__name__
       return '%s | %s| %s| %s| %s| %s' %(prefix+'NPI', 
                                          prefix+'Name',
                                          prefix +'Address',
                                          prefix + 'City',
                                          prefix + 'State',
                                          prefix + 'Zip')    
    def dbOutputFormat(self):      
        return '%s, %s, %s, %s, %s, %s' %('NULL' if self.npi =='' else "'" + self.npi +"'",
                                          'NULL' if self.name == '' else "'" +self.name+"'",
                                          'NULL' if self.addr1 == '' else "'" +self.addr1+"'", 
                                          'NULL' if self.city == '' else "'" +self.city+"'", 
                                          'NULL' if self.state == '' else "'" +self.state+"'", 
                                          'NULL' if self.zipcode == '' else "'" +self.zipcode+"'")


class FacilityProvider(Provider):
    pass

class RenderingProvider(Provider):
    pass

class ReferringProvider(Provider):
    pass
           
'''

'''
class BillingProvider:             
    def __init__(self,  taxid='', npi='', name='', addr1='', city='', state='', zipcode=''):
        self.taxid= taxid
        self.npi = npi
        self.name = name
        self.addr1 = addr1
        self.city = city
        self.state = state
        self.zipcode = zipcode
            
    def __str__(self):
        return '%s |%s | %s| %s| %s| %s| %s' %(self.taxid, self.npi, self.name, self.addr1, self.city, self.state, self.zipcode)
    
    def printHeaderLabels(self,type=''):
       prefix=type+self.__class__.__name__
       return '%s |%s | %s| %s| %s| %s| %s' %('Taxid', 
                                              prefix+'NPI', 
                                              prefix+'Name',
                                              prefix +'Address',
                                              prefix + 'City',
                                              prefix + 'State',
                                              prefix + 'Zipcode')
    
    def dbOutputFormat(self):      
        return '%s, %s, %s, %s, %s, %s, %s' %("'" + self.taxid + "'", 
                                          'NULL' if self.npi =='' else "'" + self.npi +"'",
                                          'NULL' if self.name == '' else "'" +self.name+"'",
                                          'NULL' if self.addr1 == '' else "'" +self.addr1+"'", 
                                          'NULL' if self.city == '' else "'" +self.city+"'", 
                                          'NULL' if self.state == '' else "'" +self.state+"'", 
                                          'NULL' if self.zipcode == '' else "'" +self.zipcode+"'")
           



class Claimant :
    def __init__(self, id='', name='', gender='', addr1='', city='', state='', zipcode=''):
        self.id=id
        self.name = name
        self.gender=gender
        self.addr1 = addr1
        self.city = city
        self.state = state
        self.zipcode = zipcode        
    def __str__(self):
        return '%s | %s| %s| %s| %s| %s| %s' %(self.id, self.name, self.gender, self.addr1, self.city, self.state, self.zipcode)
 
    def dbOutputFormat(self):      
        return '%s, %s, %s, %s, %s, %s, %s' %('NULL' if self.id =='' else "'" + self.id+"'",
                                          'NULL' if self.name == '' else "'" + self.name+"'",
                                          'NULL' if self.gender == '' else "'" + self.gender+"'",
                                          'NULL' if self.addr1 == '' else "'" + self.addr1+"'", 
                                          'NULL' if self.city == '' else "'" + self.city+"'", 
                                          'NULL' if self.state == '' else "'" + self.state+"'", 
                                          'NULL' if self.zipcode == '' else "'" + self.zipcode+"'")
   
    def printHeaderLabels(self):
        return 'ClaimantId|Claimant Name|Gender|Claimant Address|Claimant City|Claimant State|Claimant Zipcode'
    
    # function to get provider array to be used during the file file building
    def getClaimants(self):
        claimants=[]
        i=0
        with open(appProperties.claimantfilename, 'rU') as csvfile:
            csvread = csv.reader(csvfile, delimiter='|')
            for line in csvread:
                if appProperties.claimanthdr:
                    if i==0:
                        i+=1
                        continue    
                claimants.append(self.parseClaimantInfo(line))        
        return claimants
    
    #function to parse the line to get a provider object
    def parseClaimantInfo(self, line):
        return Claimant(line[0], line[1], line[2], line[3], line[4],line[5],line[6])

class CptCode(object):
    '''
    classdocs
    '''
    def __init__(self, code='', amount=0.0):
        '''
        Constructor
        '''
        self.code = code
        self.amount=amount
    
    def __str__(self):
        return '%s | %f' %(self.code, self.amount)
    
    def dbOutputFormat(self):      
        return '%s, %f' %('NULL' if self.code =='' else "'" + self.code+"'", self.amount)
    
    def printHeaderLabels(self,prefix=''):
        #prefix = type
        return '%s | %s' %(prefix+'CPT code', prefix + 'Amount')
    def getCodes(self):
        cptcodes=[]
        i=0
        with open(appProperties.cptcodesfilename, 'rU') as csvfile:
            csvread = csv.reader(csvfile, delimiter='|')
            for line in csvread:
                if appProperties.cpthdr:
                    if i==0:
                        i+=1
                        continue
                cptcodes.append(self.parsecptFileInfo(line))        
            return cptcodes
    
    def getdict(self):
        d={}
        d['code'] = self.code
        d['amount'] = self.amount
        return d
    #function to parse the line to get a provider object
    def parsecptFileInfo(self, line,hdr=True):
        return CptCode(line[0], float(line[1]))

class BilledCpt(CptCode):
    pass

class PaidCpt(CptCode):
    pass    
    
class BillLine(object):
    def __init__(self, claimant=None,claim=None, bills=None, billprovider=None, renderingprovider=None,
                 facilityprovider=None, linenumber=None, billedcptcodes=None, paidcptcodes=None, receiveddate=None, servicedate=None):
        self.claimant = claimant
        self.claimnumber=claim
        self.billnumber = bills
        self.billprovider= billprovider
        self.renderingprovider = renderingprovider
        self.facilityprovider = facilityprovider
        self.linenumber=linenumber
        self.billedcptcodes = billedcptcodes
        self.paidcptcodes = paidcptcodes
        self.receiveddate = receiveddate
        self.servicedate=servicedate
    
    def printHeaderLabels(self):
       return '%s |%s |%s |%s |%s |%s |%s |%s |%s |%s |%s' %(self.claimant.printHeaderLabels(), 'Claim Number', 'Bill Number', 
                                                         self.billprovider.printHeaderLabels('Billing'),
                                              self.renderingprovider.printHeaderLabels('Rendering'), 
                                              self.facilityprovider.printHeaderLabels('Facility'),
                                              'Line Number',
                                              self.billedcptcodes.printHeaderLabels('Billed'), 
                                              self.paidcptcodes.printHeaderLabels('Paid'),
                                              'Received Date',
                                              'Service Date')
    def __str__(self):
        return '%s |%s |%s |%s |%s |%s |%s |%s |%s |%s |%s' %(self.claimant, self.claimnumber, self.billnumber, self.billprovider,
                                              self.renderingprovider, self.facilityprovider, self.linenumber,
                                              self.billedcptcodes, self.paidcptcodes,
                                              self.receiveddate, self.servicedate)
    def dbOutputFormat(self):
        return '%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s, %s, %s' %(self.claimant.dbOutputFormat(),
                                                      'NULL' if self.claimnumber == None else "'" + self.claimnumber+"'",
                                                      'NULL' if self.billnumber == None else "'" + self.billnumber+"'",
                                                      self.billprovider.dbOutputFormat(),
                                                      self.renderingprovider.dbOutputFormat(),
                                                      self.facilityprovider.dbOutputFormat(),
                                                      'NULL' if self.linenumber == None else self.linenumber,
                                                      self.billedcptcodes.dbOutputFormat(),
                                                      self.paidcptcodes.dbOutputFormat(),
                                                      'NULL' if self.receiveddate == None else "'" + str(self.receiveddate) + "'",
                                                      'NULL' if self.servicedate==None else "'" + str(self.servicedate) + "'")
    def solrFormat(self):
        output={}
        self.printdict(self.__dict__, output)
        return output
        
    def printdict(self,home_d={},output={},objtype=None):
        keys = home_d.keys()
        for key in keys:
            if isinstance(home_d[key], dict):
                self.printdict(home_d[key],output)
            elif (isinstance(home_d[key],CptCode) or 
                            isinstance(home_d[key],BillingProvider) or 
                            isinstance(home_d[key],FacilityProvider) or 
                            isinstance(home_d[key],RenderingProvider) or
                            isinstance(home_d[key],ReferringProvider) or
                            isinstance(home_d[key],Claimant) or
                            isinstance(home_d[key],BilledCpt) or
                            isinstance(home_d[key],PaidCpt)):
                self.printdict(home_d[key].__dict__,output, home_d[key].__class__.__name__)
            else:
                if objtype != None:
                    output[(objtype+key).lower()] = home_d[key]
                else: 
                    output[key.lower()]=home_d[key]

