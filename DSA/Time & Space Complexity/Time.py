# Time Complexity = number of operations

i = 1
while i <= 5:
   print("Code and Debug")
i += 1

# Step-by-Step Analysis
# In terms of Big O notation, time complexity reflects the number of steps relative to the input size. 

# Initialization: The variable i is assigned an initial value of 1
# Comparison: The condition i <= 5 is checked
# Execution: The statement print(“Code and Debug”) is executed
# Increment: The value of i is increased by 1 using i += 1
# This flow repeats, and the condition i <= 5 is re-checked after each increment. The process continues until the condition becomes false, i.e., when i exceeds 5.

# Let’s analyze the steps further:

# The loop runs 5 times since i starts at 1 and increments by 1 until it reaches 6.
# For each iteration, three core steps are executed:
# Checking the condition
# Executing the print statement
# Incrementing i
# Thus, the total number of steps can be calculated as 5 × 3 = 15. In terms of Big O notation, this is O(15).

# If we replace the constant 5 with a variable N, the loop will run N times. The number of steps would then become:

# N×3=3N

# When expressed in terms of Big O, we ignore constant factors. So the time complexity becomes O(N).