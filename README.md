# Bioinformatic utils

> This repository contains some scripts that could be useful for bioinformatics analysis.

## Dependencies

- Python3.8 or superior;
- Libraries present in the requirements file.

## Installation

After install the external programs, download the repository:
```
git clone https://github.com/Nickolaz47/bioinfo_utils.git 
```
Enter the Conciliation folder and install the python libraries:
```
pip install -r requirements.txt
```

## Scripts

### **Sequence validator**

This script aims to remove nucleotide/aminoacid sequences that have some invalid character.

#### Usage

```
python3 sequence_validator.py -fi fasta input -fo fasta output -m (n or p)
```

#### Parameters

- **fi:** Fasta file input.
- **fo:** Fasta file output.
- **m:** Mode to run the script, n for nucleotide sequences and p for protein sequences.

### **Transcript filter**

This script aims to generate a fasta file with only the longest transcript of each gene.

#### Usage

```
python3 transcript_filter.py -fi fasta input -fo fasta output -tp pattern
```

#### Parameters

- **fi:** Fasta file input.
- **fo:** Fasta file output.
- **tp:** Transcript pattern used to identify a transcript from a gene. Example: gene1-transc1, transcript pattern = "-".