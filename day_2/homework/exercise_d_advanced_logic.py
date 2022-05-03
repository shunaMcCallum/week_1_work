# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
# for num in numbers:
#     if num % 2 == 0:
#         print(num)

# 2. Print the difference between the largest and smallest value:
# max_num = max(numbers)
# min_num = min(numbers)
# print(max_num - min_num)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
# for i in range(len(numbers) - 1):
#     if numbers[i] == 2 and numbers[i+1] == 2:
#         print("True")

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

total = 0
num = iter(numbers)

for x in num:
    if x == 6:
        7 in num
    else:
        total = total + x
print(total)


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 
numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

total = 0
num = iter(numbers)

for x in num:
    if x == 13:
        range(len(numbers)) in num
    else:
        total = total + x
print(total)



