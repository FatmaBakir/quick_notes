# Coding Challenge 003 : Find the Largest Number
# Purpose of the this coding challenge is to solve a simple sorting problem in Python.

# get a basic understanding of sorting algorithms.
# demonstrate their knowledge of lists in python
# implement loops to solve the problems in python
# get a better understanding of computational thinking concepts
# Problem Statement
# Write a python code that finds the largest number among the 5 numbers given by the user as input.

# It is forbidden to use max() function.

# Indicate which computational thinking concepts have you used.

# Example for user inputs and respective outputs

# Input            Output
# ------------     ------
# 1 2 3 4 5         5
# 67 85 19 39       85






count=0
array=[]
while count < 5:
  number= int(input('Please enter the number: '))
  array.append(number)
  count = count +1
def findLargestNum(nums):
  largest = nums[0]
  for i in nums:
    if i > largest:
      largest = i
  return largest
print(findLargestNum(array))