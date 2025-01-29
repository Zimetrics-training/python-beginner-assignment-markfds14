"""
Problem 1: Sum of Even Numbers
Problem Statement: Write a function sum_of_even_numbers(lst) that takes a list of integers as input and returns the sum of all even numbers in the list.

Input: A list of integers.
Output: The sum of the even numbers in the list.

Example:
assert sum_of_even_numbers([1, 2, 3, 4, 5, 6]) == 12
assert sum_of_even_numbers([10, 15, 20]) == 30
"""
# sum_of_even_numbers.py
def sum_of_even_numbers(lst):
    """
    This function takes a list of integers and returns the sum of all even numbers.
    """
    # Your code here

    sum=0
    for num in lst:
        
        if num%2==0:
            sum+=num

    return sum
