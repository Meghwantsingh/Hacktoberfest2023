def fib(n):  
                                  #creating function fib and assigning variables to it
    a, b = 0, 1                   #assinging values to variables 
    i=0 
    while i<n:                    #using while loop till n
        b=a+b                     #updating the value
        a, b=b, a                 #returning the value
        i+=1                      #incrementing it by 1
    return a

print(fib(10))
