import sys

from Bio import SeqIO

file_name = sys.argv[1]

print('File name: ' + file_name)
for record in SeqIO.parse(file_name, 'fasta'):
    print(record.name)

print('-' * 20)