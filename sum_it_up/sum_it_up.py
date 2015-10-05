__author__ = 'marc'

import operator
import functools

input() # we dont care much for this one
seq = map(int, input().split())
num_of_operations = int(input())
print(functools.reduce(operator.add, seq) * 2 ** num_of_operations % (10**9 + 7))