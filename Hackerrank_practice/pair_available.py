#identiy no of pair available in given list
ar=[10, 20, 20, 10, 10, 30, 50, 10, 20]
from collections import Counter

a=Counter(ar)
count=0
for v in a.values():
    if v>2:
        count+=int(v/2)
print(count)