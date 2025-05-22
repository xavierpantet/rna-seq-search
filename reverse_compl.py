import argparse

COMPLEMENTARY_BASES = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C',
    ' ': '',
}

def reverse_compl(seq):
    compl = list(map(lambda char: COMPLEMENTARY_BASES[char], seq))
    reversed = compl[::-1]
    return ''.join(reversed)

parser = argparse.ArgumentParser(description = 'Inverse complement calculator.')
parser.add_argument('sequence', help = 'Your sequence')
args = parser.parse_args()

print(reverse_compl(args.sequence.upper()))