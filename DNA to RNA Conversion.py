def dna_to_rna(dna):
    RNA = [s.replace('T','U') for s in dna]
    RNA = ''.join(RNA)
    return RNA