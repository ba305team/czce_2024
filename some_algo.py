#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 11:11:52 2024

@author: zichengli
"""

import timeit
import math

def pageCount(n, p):
    last_page = n if n % 2 else n+1
    if p in (1, last_page, n):
        return 0
    left = p // 2
    right = (last_page-p) // 2
    return min(left, right)

# 'n' = number of pages, 'p' = the page we're looking to find
n, p = 6, 2
output01 = pageCount(n, p)
print(f'Question 01 output: {output01}\n')


def countingValleys(n, steps):
	altitude = valleys = 0
	
	for step in steps:
		altitude += 1 if step == 'U' else -1
		if altitude == 0 and step == 'U':
			valleys += 1

	return valleys

n = 12
steps = 'DDUUDDUDUUUD'
output02 = countingValleys(n, steps)
print(f'Question 02 output: {output02}\n')
