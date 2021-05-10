# prime numbers, they are only divisable by them self except for one which is named a unit,
# other numbers are called composite and psudoprimes also exist, they are not primes but they pass
# prime tests like the one below. 11 * 31 = 341, 19 * 73 = 1387, these are two, but there is
# infinteley many.
 

def primetest():
    '''take an input check if it is a prime or composite number''' 
    num = int(input("Enter a number: "))  
      
    if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               print(num,"is not a prime number")  
               print(i,"times",num//i,"is",num)  
               break  
       else:  
           print(num,"is a prime number")
           
             
    else:  
       print(num,"is not a prime number")
       
primetest()