def detect(ref, alt):
    if len(ref) > len(alt): return "Deletion"
    if len(ref) < len(alt): return "Insertion"
    return "Substitution"
