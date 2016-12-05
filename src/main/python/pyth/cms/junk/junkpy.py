'''
Created on Nov 30, 2016

@author: Venkatesh
'''
from pyth.cms.model.Entities import CptCode

def printdict(dictitem,d2):
    keys = dictitem.keys()
    for key in keys:
        if isinstance(dictitem[key], dict):
            printdict(dictitem[key],d2)
        elif isinstance(dictitem[key],CptCode):
            d2[key]=dictitem[key].__dict__
        else:
            d2[key]=dictitem[key]



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
printdict(d,d2)
print d2

        
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