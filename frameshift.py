def is_frameshift(ref, alt):
    return abs(len(ref)-len(alt)) % 3 != 0