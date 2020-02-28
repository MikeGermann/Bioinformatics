seq = "AAAACCCGGT"

def BaseCount(Sequence) :
    #for a given DNA sequence, count the number of each base (A, C, G, T) present
    A_count = Sequence.count("A")
    C_count = Sequence.count("C")
    G_count = Sequence.count("G")
    T_count = Sequence.count("T")
    return(A_count, C_count, G_count, T_count)
    
print(BaseCount(seq))
