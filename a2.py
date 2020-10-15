#coursera Learn to program: The fundamentals
# Teppo Harju 2020

def get_length(dna):
    return len(dna)
    
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """


def is_longer(dna1, dna2):
    if (len(dna1) > len(dna2)):
        return True
    else:
        return False
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """


def count_nucleotides(dna, nucleotide):
    result = 0

    for nucleotide in dna:
        result +=1
    return result
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """


def contains_sequence(dna1, dna2):
    if dna2 in dna1:
        return True
    else:
        return False
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

def is_valid_sequence(dna):


    valid = True

    for char in dna:
        if char in "BDEFHIJKLMNOPQRSUVWXYZabcdefghijklmnopqrstuvwxyz":
            valid = False

    return valid
    
    #n = 0
    #for i in range(0,len(dna)):
    #    if dna[i] == "A" or "T" or "C" or "G":
    #        n += 1
    #if len(dna) == n:
    #    return True
    #else:
    #    return False

def insert_sequence(dna1, dna2, index):
    result = dna1[:index] + dna2 + dna1[index:]
    print (result)
    return result

def get_complement(dna):
    if dna == "A":
        return "T"
    elif dna == "T":
        return "A"
    elif dna == "G":
        return "C"
    elif dna == "C":
        return "G"
    else:
        print("Not a Valid DNA.")
        
    


def get_complementary_sequence(dna):
    comp = ""

    for char in dna:
        if char in "ATCG":
            comp = comp + get_complement(char)
    return comp
