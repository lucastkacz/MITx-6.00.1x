"""
Assume s is a string of lower case characters.
rite a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print:
    >>> Number of times bob occurs is: 2
"""
s = 'azcbobobegghakl'

count = 0
for i in range(len(s)):
    if 'bob' in s[i:i+3]:
        count += 1
print('Number of times bob occurs is: ' + str(count))
