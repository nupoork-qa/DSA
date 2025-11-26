# The Fibonacci sequence is a series where the next number is the sum of the previous two, 
# starting with 0 and 1. (0, 1, 1, 2, 3, 5, 8, 13, ...)

# The sequence starts with 0 and 1. 
# Every subsequent number is the sum of the two preceding numbers:

#step 1 : define function and initail state

def fibonacci_num(n):
    #1.1 initalize the first two term
    a = 0 #first term
    b = 1 #second term

    #initalize an empty list to store te sequence
    fib_list = []
    #step 2 : handle the edge cases (0,1,2)
    #handle 0 term , return empty list
    if n < 0 :
       return fib_list
    
    #handle 1 term , only includes 0
    fib_list.append(a) #fib_list is now 0

    #handle 2 terms 0 & 1

    if n == 1:
        return fib_list
    
    fib_list.append(b) #fib_ist is now [0,1]

   # step 3 : the main loop
   #loops runs for remaining terms starting from3rd term
    for _ in range(2, n): 
          c = a + b

          #add new term to list
          fib_list.append(c)

        # 3c. SHIFT the variables for the next iteration
        # 'a' becomes the old 'b'
        # 'b' becomes the new 'c' 

          a = b
          b = c
    return fib_list        

print(fibonacci_num(10))