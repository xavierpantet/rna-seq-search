from pathlib import Path

COMPLEMENTARY_BASES = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C',
    ' ': '',
}

"""
List all FASTQ files in a directory and filter them based on the first_pass flag.

Example:
    list_fastq_files("data/") -> [Path("data/file1.fastq"), Path("data/file2.fastq")]
"""
def list_fastq_files(path, first_pass = True):
    path = Path("./data/" + path)
    fastq_files = list(path.rglob("*.fastq"))
    filter = lambda f: f.stem.endswith("_matches")
    select = lambda f: not filter(f) if first_pass else filter(f)
    return [f for f in fastq_files if select(f)]

"""
Read the common and specific sequences from a file.
By convention, the first line is the common sequence.

Example:
    read_sequence_file("data/sequences.txt") -> ("ATCG", ["ATCGA", "ATCGT"])
"""
def read_sequence_file(path):
    with open(path, "r") as file:
        seqs = [l.strip() for l in file.readlines() if l.strip() != '']
        return seqs[0], seqs[1:]

"""
Calculate the reverse complement of a sequence using COMPLEMENTARY_BASES.

Example:
    reverse_compl("ATCG") -> "CGAT"
"""
def reverse_compl(seq):
    compl = list(map(lambda char: COMPLEMENTARY_BASES[char], seq))
    reversed = compl[::-1]
    return ''.join(reversed)