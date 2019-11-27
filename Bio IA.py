from Bio import ExPASy
from Bio import SwissProt
from Bio import Phylo
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
import matplotlib
from Bio import Align
from Bio import AlignIO
from Bio.Alphabet import generic_dna, generic_protein

handle = open("uniprot_sprot.dat")


t_rex_seq = SeqIO.read("t-rex.fasta", "fasta")
canine_seq = SeqIO.read("t-rex.fasta", "fasta")
lizard_seq = SeqIO.readd("lizard.fasta", "fasta")
feline_seq = SeqIO.readd("feline.fasta", "fasta")


def get_score(seq1, seq2):
    alignments = pairwise2.align.globalxx(seq1, seq2, score_only=True)
    print(alignments)
a

def get_ancestors_list():
    i = 0
    handle = open("uniprot_sprot.dat")
    for record in SwissProt.parse(handle):
        descriptions.append(record.sequence)
          print(descriptions)
        i += 1
        if i == 1:
            break


