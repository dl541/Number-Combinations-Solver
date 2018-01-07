from math import factorial
import time
import random

class Solution:
    def __init__(self,question):
        self.question = question
        self.sol = []
        self.operation_dict = {0:'+',1:'-',2:'*',3:'/',4:'^'}
        self.seen = set([])
        self.time = 0
        
        
    def solver(self):
        start = time.time()
        self.dfs(self.question)
        end = time.time()
        
        self.time = end-start
        return list(reversed(self.sol))
    
    def combine(self,question): #combining numbers

        for ind in range(len(question)-1):
            for fac in range(4): #4 cases for factorial, none, 1 is factorial or both factorial
                if fac==3 and question[ind]<100 and question[ind+1]<100:
                    #print('hi3')
                    try:
                        num1 = factorial(question[ind])
                        num2 = factorial(question[ind+1])
                    except:
                        continue
                if fac==2 and question[ind+1]<100:
                    #print('hi2')
                    try:
                        num1 = question[ind]
                        num2 = factorial(question[ind+1])
                    except:
                        continue
                if fac==1 and question[ind]<100:
                    #print('hi')
                    try:
                        num1 = factorial(question[ind])
                        num2 = question[ind+1]
                    except:
                        continue
                if fac==0:
                    num1 = question[ind]
                    num2 = question[ind+1]
                    
                operations = []
                operations.append(num1+num2) #plus
                operations.append(num1-num2) #minus    
                operations.append(num1*num2) #mul
                try:
                    operations.append(num1/num2) #div
                except:
                    operations.append(None)
                
                for operation,element in enumerate(operations):
                    if element==None:
                        continue
                    result = self.dfs(question[:ind]+[element]+question[ind+2:])
                    
                    if result==True:
                        #print(question)
                        #print(operations)
                        self.sol.append((self.operation_dict[operation],ind,fac))
                        return True
                
        return False
                
            
        
    
    def dfs(self,question):
        #print(question)
        if tuple(question) in self.seen:
            return False
        else:
            self.seen.add(tuple(question))
        
        if len(question)<=1:
            #print('end reached')
            if question[0]==8:
                #print(question)
                return True
            else:
                return False
        
        else:
            #case 1: no factorials needed
            ans = self.combine(question)
            if ans!=False:
                return True
            
#            for ind in range(len(question)): #factorial each number
#                if question[ind]<0 or question[ind]>=100 or int(question[ind])!=question[ind]: #prevent overflow
#                    continue
#                
#                else:
#                    ans = self.combine(question[:ind]+[factorial(question[ind])]+question[ind+1:])
#                    
#                    if ans!=False:
#                        #print('factorial',question[:ind]+[factorial(question[ind])]+question[ind+1:])
#                        #print(question)
#                        self.sol.append(ind)
#                        return True
##    
            return False

def SolToExpression(res,var):
   
    for element in res:
        if element[2]==0: fac1,fac2 = '',''
        if element[2]==1: fac1,fac2 = '!',''
        if element[2]==2: fac1,fac2 = '','!'
        if element[2]==3: fac1,fac2 = '!','!'
        new = '({}{}{}{}{})'.format(var[element[1]],fac1, element[0], var[element[1]+1],fac2)
        var = var[:element[1]]+[new]+var[element[1]+2:]
            
            
    return var[0]

while True:
    print('Input the question,e.g.1234,or press enter to exit')
    var = input()
    if var=='':
        break
    question = [int(char) for char in list(var)]
    
    sol = Solution(question)
    res = sol.solver()
    print (SolToExpression(res,list(var)))
    
    if res==[]:
        print('No solution found')
        continue
    #print(res)
    
#digits = 6
#time_used = []
#for num in range(1000):
#    if num%100==0: print('{} completed'.format(num))
#    question = int(random.random()*(10**digits))
#    question = list(str(question))
#    #print (question)
#    if len(question)<digits:
#        zeros = ['0' for count in range(digits-len(question))]
#        var = zeros+question
#    
#    question = [int(char) for char in list(var)]
#    
#    sol = Solution(question)
#    res = sol.solver()
#    
#    if res!=[]:
#        time_used.append((sol.time,question))
        


