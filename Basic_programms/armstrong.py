# An Armstrong number (or narcissistic number) is an n-digit number that is equal to the sum of the $n$-th powers of its digits. 
# For a 3-digit number, this is: $abc = a^3 + b^3 + c^3.

def is_armstrong_number(n):
    # determine num of digit n
    num_str = str(n)
    num_digits = len(num_str)
    sum = 0
    temp = n  #extract the digits of the number without changing the original value of $n$

    while temp > 0:
        digit = temp % 10 #get last digit (3, then 5, then 1 for 153)
        sum += digit ** num_digits
        temp //= 10 #remove last digit

    return n == sum

print(is_armstrong_number(153))        