from Bio.Seq import Seq
def translate(seq): return str(Seq(seq).translate())