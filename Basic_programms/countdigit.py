def countdigit(n):
    # Initialize the local count
    count = 0
    num = n # Work with a local copy of the input
    
    # Use integer division (//) to correctly remove the last digit
    while num > 0 :
        count +=1
        num = num // 10
        
    return count

n = 5438
digit_count  = countdigit(n)
print("The number of digits in", n, "is", countdigit(n))    
