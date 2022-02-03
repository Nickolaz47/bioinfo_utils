from Bio import SeqIO
from argparse import ArgumentParser


def filter_transcript(fasta_inp, transcript_pattern) -> dict:
    """
    This function gets only the longest transcript of each gene from the input.
    :param fasta_inp: Fasta input.
    :param transcript_pattern: transcript pattern, pattern used to identify a
    transcript from a gene. Example: gene1-transc1.
    :return: Returns a dict with the transcripts
    """
    transcripts = {}
    with open(fasta_inp, 'r') as inp:
        for record in SeqIO.parse(inp, 'fasta'):
            if 'Sequence' not in record.seq:
                dict_key = record.id.split(transcript_pattern)[0]
                length = len(record.seq)
                record.seq = record.seq.rstrip('*')
                if dict_key not in transcripts:
                    transcripts[dict_key] = [record, length]
                else:
                    if transcripts[dict_key][-1] < length:
                        transcripts[dict_key] = [record, length]
    return transcripts


def write_fasta(transc_dict, fasta_out):
    """
    This function writes the filtered fasta output.
    :param transc_dict: Dict with the transcripts.
    :param fasta_out: Fasta output.
    :return:
    """
    with open(fasta_out, 'w') as out:
        for k, v in transc_dict.items():
            SeqIO.write(v[0], out, 'fasta')
    return


if __name__ == '__main__':
    parser = ArgumentParser(description='The main objective of this script is '
                            'generate a fasta file with only the longest '
                            'transcript of each gene from the input.')
    parser.add_argument('-fi', required=True, help='Fasta input')
    parser.add_argument('-fo', required=True, help='Fasta output')
    parser.add_argument('-tp', required=True, help='Transcript pattern used to'
                        ' identify a transcript from a gene. Example: '
                        'gene1-transc1, transcript pattern = "-".')
    args = parser.parse_args()
    transcripts_dict = filter_transcript(args.fi, args.tp)
    write_fasta(transcripts_dict, args.fo)
