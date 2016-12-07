'''
Created on Nov 30, 2016

@author: Venkatesh
'''

from pyth.cms.dao.DbConnect import DbConnector
from pyth.cms.model.Entities import Provider, Claimant, CptCode, BillLine, BillingProvider,\
    FacilityProvider, RenderingProvider, ReferringProvider, PaidCpt
from pyth.cms.properties import appProperties as appProp
from pyth.cms.solr.AccessSolr import CMSSolr
from pyth.cms.dao.EntityDAO import FacilityProviderDAO, RenderingProviderDAO,\
    ReferringProviderDAO, BilledCptCodeDAO, PaidCptCodeDAO, BillingProviderDAO


def printdict(dictitem,d2):
    keys = dictitem.keys()
    for key in keys:
        if isinstance(dictitem[key], dict):
            printdict(dictitem[key],d2)
        elif isinstance(dictitem[key],CptCode):
            d2[key]=dictitem[key].__dict__
        else:
            d2[key]=dictitem[key]


def prepareData(appProp):
    
    billprovider = BillingProviderDAO()
    billingproviderlist = billprovider.getBillProviders()
    billproviderslen =len(billingproviderlist)
    
    facilityprovider = FacilityProviderDAO()
    facilitylist = facilityprovider.getProviders()
    facilitylen = len(facilitylist)
    
    renderingprovider = RenderingProviderDAO()
    renderinglist = renderingprovider.getProviders()
    renderinglen = len(renderinglist)
    
    referringprovider = ReferringProviderDAO()
    referringlist = referringprovider.getProviders()
    referringlen = len(referringlist)
    
    claimant = Claimant()
    cllist = claimant.getClaimants()
    claimantslen = len(cllist)
        
    billedCptcodes = BilledCptCodeDAO()
    billedcpts = billedCptcodes.getCodes()
    billedcptlen = len(billedcpts) 
    
    paidCptcodes = PaidCptCodeDAO()
    paidcpts = paidCptcodes.getCodes()
    paidcptlen = len(paidcpts) 
      
    '''
    Generate a billline and then use this array to build bills which in turn will generate the cclaims
    '''
    import random
    billlines=[]
    
    for clmt in range(1, random.randint(2,appProp.MAX_CLAIMANT_COUNT)):
        for claim in range(1, random.randint(1,appProp.MAX_CLAIM_COUNT)):
            for bills in range(1, random.randint(2,appProp.MAX_BILLS_COUNT)):
                
                for lineno in range(1, random.randint(1,appProp.MAX_LINES_PER_BILL)):
                    billlines.append(
                        BillLine(cllist[clmt % claimantslen],   #Claimant 
                                 appProp.CLAIM_PREFIX + str(claim).ljust(3,'0'), # claim number
                                 appProp.BILL_PREFIX+appProp.CLAIM_PREFIX+str(bills).ljust(6,'0'), # Bill Number
                                 billingproviderlist[bills  % billproviderslen], # Billing Provider
                                 renderinglist[(bills) % renderinglen], # Rendering Provider
                                 facilitylist[(bills)% facilitylen], #facility provider
                                 lineno, 
                                 billedcpts[lineno % billedcptlen], # Billed copt
                                 paidcpts[lineno % paidcptlen], # paid cpt
                        ))
 
    return billlines                
            
if __name__ == '__main__':
    
    billlines = prepareData(appProp)
#    c = CMSSolr()
#   for 
#    c.insertDocument()
    for sink in appProp.target_sink.split(" "):
        if sink == 'file':
            print billlines[0].printHeaderLabels()
            for bill_file in billlines:
                print(bill_file)   
        
        elif sink=='solr':
            c = CMSSolr()
            for bill_file in billlines:
                #dictArr.append(bill_file)
                c.insertDocument(bill_file)    
                
        elif sink=='database':
            db = DbConnector(appProp)
            for bill in billlines:
                db.insertRecord(bill) 
        #for bill in billlines:
    #    print bill  