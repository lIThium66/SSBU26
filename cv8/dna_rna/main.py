from Bio import SeqIO
from Bio.Seq import Seq
from random import randint, choice

# Task 1: Load sequence from a file in the inputs directory
def load_sequence(filepath):
    """
    Pseudocode:
    - Use SeqIO to read the file in GenBank format.
    - Print the sequence ID.
    - Check if the sequence is defined or non-empty:
        - If valid, print the sequence.
        - Otherwise, print a message and assign an empty sequence.
    - Return the sequence record.
    """
    record = SeqIO.read(filepath, "genbank")
    if record.id:
        print(record.id)
    elif record.seq:
        print(record.seq)
        return record.seq
    else:
        print(f"No sequence ID in {filepath}")
# Task 2: Create complementary strand
def create_complementary_strand(dna_sequence):
    """
    Pseudocode:
    - Create a translation table for DNA base complements (A <-> T, G <-> C).
    - Translate the input DNA sequence using the complement table.
    - Print the complementary strand.
    - Return the complementary strand.
    """
    translations = str.maketrans("ATGC", "TACG")
    complementary_strand = dna_sequence.translate(translations)
    complementary= Seq(complementary_strand).reverse_complement()
    print(complementary)
    return complementary

# Task 3: Create gene mutation
def mutate(dna):
    """
    Pseudocode:
    - Convert the DNA sequence into a list of characters.
    - Perform 1000 random mutations:
        - Select a random index in the DNA sequence.
        - Replace the base at the selected index with a random different base.
    - Join the mutated list back into a string.
    - Print the mutated DNA sequence.
    - Return the mutated DNA sequence.
    """
    for i in range(1000):
        index = randint(0, len(dna) - 1)
        index2 = randint(0, len(dna) - 1)
        dna.replace(dna[index], dna[index2])
    list_dna = list(dna)
    dna_str = "".join(list_dna)
    print(dna_str)
    return dna_str

# Task 4: Calculate GC content
def calculate_gc_content(dna_sequence):
    """
    Pseudocode:
    - Count the occurrences of 'G' and 'C' in the DNA sequence.
    - Calculate the GC content as a percentage of the total sequence length.
    - Print the GC content percentage.
    - Return the GC content percentage.
    """
    count_g = dna_sequence.count('G')
    count_c = dna_sequence.count('C')
    sum_gc = count_g + count_c
    gc_perc = round((sum_gc/ len(dna_sequence)) * 100, 2)
    print(gc_perc)
    return gc_perc

# Example usage
if __name__ == "__main__":
    # Task 1: Load sequence from the inputs directory
    sequence_record = load_sequence("inputs/NC_005816.gb")

    # Task 2: Create complementary strand
    create_complementary_strand("TACCGGAT")

    # Task 3: Mutate a sequence loaded from the inputs directory
    fasta_sequence = SeqIO.read("inputs/AE017046.1.fasta", "fasta").seq
    mutated_sequence = mutate(str(fasta_sequence))

    # Task 4: Calculate GC content
    calculate_gc_content(str(fasta_sequence))