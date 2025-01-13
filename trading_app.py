'''This is trading apps'''
import time
class vendor:
    '''vendor enrollment'''
    def __init__(self,vName,vID,vGST,vAddress):
        self.vName = vName
        self.vID = vID
        self.vGST = vGST
        self.vAddress = vAddress
        print(f'Vendor {vName} Enrollment is done')
    def product_billing(self,pName,pCost=0.0,pQty=0):
        self.pName = pName
        self.pCost = pCost
        self.pQty = pQty
        self.total = self.pCost * self.pQty
        self.tax = self.total * 0.18
        self.gs = self.tax + self.total
        self.report()
    def report(self):
        '''update product details to log file'''
        with open("product_info.log","a") as wobj:
            s1=f'Vendor Name{self.vName}\tProduct Name:{self.pName}\tCost:{self.pCost}\t'
            s2=f'Total Amount(including Tax):{self.gs}\t Purchase date:{time.ctime()}\n'
            wobj.write(s1+s2)
