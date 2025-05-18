#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_most_likely_ancestor_consensus(dna_string1, dna_string2):

    positions = []
    
    for i in range(len(dna_string1) - len(dna_string2) + 1):
        if dna_string1[i:i + len(dna_string2)] == dna_string2:
            positions.append(i + 1)
        
    if not positions:
        return None
    else:
        return tuple(positions)
