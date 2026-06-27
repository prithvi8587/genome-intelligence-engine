def validate(seq):
    return all(x in "ATCG" for x in seq.upper())