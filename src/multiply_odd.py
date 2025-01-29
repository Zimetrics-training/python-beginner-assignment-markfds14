"""
This module provides functions to filter and process odd numbers in a list of integers:

1. filter_odd_numbers(numbers: List[int]) -> List[int]: 
   This function takes a list of integers and returns a new list that only contains the odd numbers 
   from the input list.

2. multiply_odd_numbers(numbers: List[int]) -> int:
   This function first filters out the odd numbers from the input list and then multiplies them 
   together. If no odd numbers are found, it returns 1.

The module's purpose is to separate the odd numbers from a given list and then 
compute the product of those odd numbers, providing a final result.
"""

from typing import List

def filter_odd_numbers(numbers: List[int]) -> List[int]:
    """
    Filters the odd numbers from a given list of integers.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of odd integers from the input list.
    """
    odd=[]
    for num in  numbers:
        if num % 2 != 0:
            odd.append(num)
    return odd

def multiply_odd_numbers(numbers: List[int]) -> int:
    """
    Multiplies all odd numbers in the given list. If there are no odd numbers, return 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        int: The product of the odd numbers in the list. If no odd numbers are found, return 1.
    """
    
    count_odd=0
    odd_product=1

    for num in numbers:

        if num % 2 != 0:
            count_odd+=1
            if count_odd > 0:
                odd_product*=num
            else:
                return 1
    return odd_product
        


