'''
Created on Nov 30, 2016

@author: Venkatesh
'''

from pyth.cms.dao.DbConnect import DbConnector
from pyth.cms.model.Entities import Provider, Claimant, CptCode, BillLine, BillingProvider
from pyth.cms.properties import appProperties as appProp


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
    provider = Provider()
    providerlist = provider.getProviders()
    providerslen = len(providerlist)
    
    billprovider = BillingProvider()
    billingproviderlist = billprovider.getBillProviders()
    billproviderslen =len(billingproviderlist)
    
        
    claimant = Claimant()
    cllist = claimant.getClaimants()
    claimantslen = len(cllist)
    
    cptcodes = CptCode()
    cpts = cptcodes.getCodes()
    cptslen = len(cpts)   
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
                        BillLine(cllist[clmt],   #Claimant 
                                 appProp.CLAIM_PREFIX + str(claim).ljust(3,'0'), # claim number
                                 appProp.BILL_PREFIX+appProp.CLAIM_PREFIX+str(bills).ljust(6,'0'), # Bill Number
                                 billingproviderlist[bills  % billproviderslen], # Billing Provider
                                 providerlist[(bills) % providerslen], # Rendering Provider
                                 providerlist[(bills - 2)% providerslen], #facility provider
                                 lineno, 
                                 cpts[lineno % cptslen], # Billed copt
                                 cpts[(lineno -1) % cptslen], # paid cpt
                        ))
 
    return billlines                
            
if __name__ == '__main__':
    billlines = prepareData(appProp)
    if appProp.target_sink == 'file':
        print billlines[0].printHeaderLabels()
        for bill_file in billlines:
            d={}
            bill_file.printdict(d)
            print d
    elif appProp.target_sink=='database':
        db = DbConnector(appProp)
        for bill in billlines:
            db.insertRecord(bill) 
    #for bill in billlines:
    #    print bill
             
                
                
                
                
                
                
                