# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 01:04:01 2021

@author: user
"""
#s = 'aaaaaaazaaaaaaaaaaaaabccccc'
count_o = 0
word = ""
count_c = 0
challenger = ""

for char in s:
    if len(word) == 0:
        count_o += 1
        word += char
        continue
    
    if char >= word[-1] and count_c == 0:
        count_o += 1
        word += char
        
    else:
        if len(challenger) == 0:
            count_c += 1
            challenger += char
            continue
        
        if char >= challenger[-1]:
            count_c += 1
            challenger += char
            if count_c > count_o:
                count_o = count_c
                word = challenger
        
        else:
            count_c = 1
            challenger = char
        
print("Longest substring in alphabetical order is : " + word)