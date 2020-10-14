from Bio import SeqIO
import sys

def usage():
    print("""
    python extract_seqs_by_ID.py <input_fasta> <gene_of_interest> <output_fasta>
    """)

input_file = sys.argv[1]
gene_of_interest = sys.argv[2]
output_file = sys.argv[3]

inhandle = SeqIO.parse(input_file, 'fasta')
outhandle = open(output_file, 'w')

for s in inhandle:
    if gene_of_interest in s.description:
        outhandle.write(">{id}\n{seq}\n".format(id=s.description, seq=str(s.seq)))

outhandle.close() 
