import argparse
import subprocess
from utils import list_fastq_files, read_sequence_file, reverse_compl

parser = argparse.ArgumentParser(description = 'RNA Sequence Search')
parser.add_argument('--dataset', help = 'Your dataset')
parser.add_argument('--sequence-file', help = 'Your sequence file')
parser.add_argument('--with-reverse-compl', help = 'Whether include reverse complement as part of the search', action = argparse.BooleanOptionalAction)
args = parser.parse_args()

def search_sequence(sequence, fastq_file, output_file, max_errors = 1):
    command = "seqkit grep -s -p {sequence} -m {max_errors} -i -j 8 {fastq_file} -o {output_file}".format(sequence = sequence, max_errors = max_errors, fastq_file = fastq_file, output_file = output_file)
    subprocess.run(command, shell = True)

"""
First pass: search for a common sequence in the datasets.
"""
for fastq_file in list_fastq_files(args.dataset, first_pass = True):
    sequence, _ = read_sequence_file(args.sequence_file)
    output = fastq_file.parent / "matches" / "common" / "common_matches.fastq"

    print("Searching for " + sequence + " in " + str(fastq_file))
    search_sequence(sequence, fastq_file, output)

    if args.with_reverse_compl:
        sequence = reverse_compl(sequence)
        output = fastq_file.parent / "matches" / "common" / "common_reverse_compl_matches.fastq"
        print("Searching for " + sequence + " in " + str(fastq_file))
        search_sequence(sequence, fastq_file, output)

"""
Second pass: search for specific sequences in the first pass results.
"""
for fastq_file in list_fastq_files(args.dataset, first_pass = False):
    _, specific_sequences = read_sequence_file(args.sequence_file)
    
    for sequence in specific_sequences:
        output = fastq_file.parent.parent / "specific" / (sequence + "_matches.fastq")
        print("Searching for " + sequence + " in " + str(fastq_file))
        search_sequence(sequence, fastq_file, output, max_errors = 2)