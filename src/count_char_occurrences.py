"""
Problem 2: Count Occurrences of a Character
Problem Statement: Write a function count_char_occurrences(s, char) that takes a string s and a character char as input and returns how many times char appears in s.

Input: A string s and a character char.
Output: The number of occurrences of char in s.

Example:
assert count_char_occurrences("hello world", "l") == 3
assert count_char_occurrences("python", "o") == 1
"""
# count_char_occurrences.py
def count_char_occurrences(s, char):
    """
    This function takes a string and a character and returns how many times the character appears in the string.
    """
    # Your code here
    
    length=len(s)
    count=0

    for i in range(0,length):
        if s[i] == char:
            count+=1

    return count
