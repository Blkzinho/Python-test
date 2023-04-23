
"""     for i in range(10):
        print(i,'for in range 10')
        
    for element in range(2,10,3): # numero de debut , Numero max , De combien de pas je saute
        print(element,'For in range starting at 2 at jump by 3')


    for element in range(10,-10,-1):
        print(element,'For in range from 10 to -10 backwards')
        
    x = 0
    while x<=10:
        print(x , 'While')
        x += 1 """
        
    
def fibonacci(n):
    #Declare base variables
   if n in {0,1}:
       return
   return fibonacci(n -1) + fibonacci(n - 2)
      
print(fibonacci(21))