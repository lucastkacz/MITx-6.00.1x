"""
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print:
    >>> Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print:
    >>> Longest substring in alphabetical order is: abc
"""
s = 'azcbobobegghakl'

n = ''
for i in range(len(s)):
    if i < len(s)-1 and s[i] <= s[i+1]:
        n += s[i]
    else:
        n += s[i]
        if len(s) > i+1:
            n += ' '

ans, temp_ans = '', ''
for i in n:
    temp_ans += i
    if i == ' ':
        temp_ans = ''
    if len(temp_ans) > len(ans):
        ans = temp_ans

print('Longest substring in alphabetical order is: ' + str(ans))
