
# A string or number is a palindrome if it reads the same forwards and backward (e.g., "madam" or 121).
def check_palindrome_number(n):
    num = n
    result = 0

    while num > 0:
      ld = num % 10
      result = result * 10 + ld
      num = num // 10
    
    return n == result     

is_palindrome = check_palindrome_number(121)
print("Is the number a palindrome?", 121, is_palindrome)