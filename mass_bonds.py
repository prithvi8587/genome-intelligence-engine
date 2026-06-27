weights={"A":313.2,"T":304.2,"G":329.2,"C":289.2}
def mass(seq): return sum(weights[b] for b in seq)
def bonds(seq): return sum(3 if b in "GC" else 2 for b in seq)