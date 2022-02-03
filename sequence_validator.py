from Bio import SeqIO
from argparse import ArgumentParser


def nctd(seq):
    """
    Function that checks if a sequence of nctd is valid.
    :param seq: Sequence to be analyzed
    :return: Return if the sequence is valid or not
    """
    # Defining valid nucleotides
    valid_nuc = 'ATCG'
    for n in seq.upper():
        # Checking if each letter of seq is contained in the valid nctds
        if n not in valid_nuc:
            return False
    return True


def ptn(seq):
    """
    Function that checks if a sequence of ptn is valid.
    :param seq: Sequence to be analyzed
    :return: Return if the sequence is valid or not
    """
    # Defining valid aminoacids
    valid_ptn = 'ABCDEFGHIKLMNPQRSTVWYZ'
    # Control to avoid consider protein sequences with a '*' at end as invalid
    seq = seq.rstrip('*')
    for a in seq.upper():
        # Checking if each letter of ptn is contained in valid aas
        if a not in valid_ptn:
            return False
    return True


if __name__ == '__main__':
    # Describing the program
    parser = ArgumentParser(description='Checks if the characters in a '
                                        'sequence within a fasta are valid and'
                                        ' generates a fasta with only valid '
                                        'sequences.')
    parser.add_argument('-fi', required=True, help='Fasta input')
    parser.add_argument('-fo', required=True, help='Fasta output')
    parser.add_argument('-m', required=True, choices=['n', 'p'],
                        help='Validation mode: nucleotide or protein')
    args = parser.parse_args()  # Parsing arguments with the args variable

    c_s_total = 0
    c_s_final = 0
    # Running the script
    try:
        with open(args.fi, 'r') as fasta_in:
            for record in SeqIO.parse(fasta_in, 'fasta'):
                # Checking the mode
                if args.m == 'p':
                    valid = ptn(record.seq)
                    # Counting the total of sequences
                    c_s_total += 1
                    if valid:
                        with open(args.fo, 'a') as fasta_out:
                            SeqIO.write(record, fasta_out, 'fasta')
                            # Counting the total of valid sequences
                            c_s_final += 1
                # Checking the mode
                elif args.m == 'n':
                    valid = nctd(record.seq)
                    # Counting the total of sequences
                    c_s_total += 1
                    if valid:
                        with open(args.fo, 'a') as fasta_out:
                            SeqIO.write(record, fasta_out, 'fasta')
                            # Counting the total of valid sequences
                            c_s_final += 1
                else:
                    raise Exception("Invalid mode! There's only modes n or p "
                                    "in parameter -m.")
    except Exception as err:
        print(f'Probably your fasta file is not valid.\nError: {err}')

    if c_s_total == 0:
        raise Exception('Total sequences is equal to 0, then your fasta is not'
                        ' adequately formatted.')
    else:
        print(f'Total sequences: {c_s_total}')
        print(f'Total valid sequences: {c_s_final}')
