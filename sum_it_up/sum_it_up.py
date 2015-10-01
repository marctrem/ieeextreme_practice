__author__ = 'marc'

import operator
import functools

def backcycler(seq, back_index):
    seq_len = len(seq)
    idx = seq_len - (back_index % seq_len)

    while True:
        idx %= seq_len
        yield seq[idx]
        idx += 1


input() # we dont care much for this one

seq = [int(x) for x in input().split()]

num_of_operations = int(input())

for i in range(num_of_operations):
    new_seq = seq[:]

    backcycle = backcycler(seq, int(input()))

    for j in range(len(seq)):
        new_seq[j] += next(backcycle)

    seq = new_seq

print(functools.reduce(operator.add, seq) % (10**9 + 7))