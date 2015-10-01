__author__ = 'marc'

import collections
import functools
import itertools
import sys, os

bag_of_chars = collections.defaultdict(int)

done_reading = False
while not done_reading:
    inp = sys.stdin.read(1)

    if len(inp) == 0 or ord(inp) == 10:
        done_reading = True
        break

    bag_of_chars[inp] += 1

cnt = 0
for _ in filter(lambda x: x[1] % 2 != 0, bag_of_chars.items()):
    cnt += 1

print("YES" if cnt < 2 else "NO")