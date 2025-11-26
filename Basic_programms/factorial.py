# The factorial of a non-negative integer $n$, denoted by $n!$, is the product of all positive integers less than or equal to n.
#  5! = 5 \times 4 \times 3 \times 2 \times 1 = 120 .

def fact_num(n):  # Define a function
    if n < 0:  # Handle the special case for negative numbers
        return "Factorial is not defined for negative numbers"

    # Handle the base cases for 0 and 1
    if n == 0 or n == 1:
       
        return 1

    # Initialize the result variable
    result = 1

    # Loop from 1 up to (and including) n
    for i in range(1, n + 1):
        result *= i  # Multiply the current result by loop counter

    
    return result

print(fact_num(5))