# Importing math library for mathematical functions
import math
# Importing time library for time functions
import time

# Getting the first number as input
num1 = int(input("Input the first number:"))

# Getting the second number as input
num2 = int(input("Input the second number:"))

# Getting the starting time
start_time = time.time()

# Initializing variables
count = 0
specialNumbers = []
length1 = math.log10(num1) + 1
length2 = math.log10(num2) + 1
five_hard_coded_values = [2, 3, 5, 7, 11]
maximum = False
found = False

# Checking conditions for num1
if num1 <= 2:
    length1 = 3
    specialNumbers = five_hard_coded_values
    count = 5
elif 0 < num1 <= 11:
    length1 = 3
    for y in five_hard_coded_values:
        if num1 <= y <= num2:
            specialNumbers.append(y)
            count += 1

        # Loop for finding special numbers until current number is greater than num2
while not maximum:
    branch = length1 // 2
    if length1 <= length2:
        # Loop for generating palindromes that have an odd length
        for x in range(int((10 ** branch)), int(10 ** (branch + 1))):
            temp = int(str(x) + str(x)[-2::-1])
            # If the palindrome is odd, loop to check if it is a prime number
            if temp % 2 == 1:
                for z in range(3, int(round(math.sqrt(temp) + 1)), 2):
                    if temp % z == 0:
                        found = False
                        break
                    else:
                        found = True
                        # If palindromic prime is found, check if it is in the range
                if found:
                    if num1 <= temp <= num2:
                        # If the length of the list is greater than or equal to 6, remove the 4th element so that the list is in the correct format
                        if len(specialNumbers) >= 6:
                            specialNumbers.pop(3)
                        specialNumbers.append(temp)
                        count += 1
                        # Check if the current number exceedes the range
                    elif temp > num2:
                        maximum = True
                        break
                        # Check if the current number exceedes the range
    else:
        maximum = True
    length1 += 2

# Printing the count and special numbers
print(count, ":", specialNumbers)
# Printing the time taken to execute
print("--- %s seconds ---" % (time.time() - start_time)) 