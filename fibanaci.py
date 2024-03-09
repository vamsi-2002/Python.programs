n = int(input ("Enter the number you want to print: "))     
a = 0    
b = 1    
for i in range(0,n):  
    print(a, end = " ")   
    c = a+b    
    a = b 
    b = c 
    print(c)    

#def fibanaci(n):
 #   fib_series=[0,1]
  #  for i in range(2,n):
   #     fib_series.append(fib_series[-1]+fib_series[-2])
    #return fib_series[:n]
#n=10
#print(fibanaci(n))
