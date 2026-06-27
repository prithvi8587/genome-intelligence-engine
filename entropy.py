from collections import Counter
import math
def entropy(seq):
    c=Counter(seq)
    n=len(seq)
    return -sum((v/n)*math.log2(v/n) for v in c.values())