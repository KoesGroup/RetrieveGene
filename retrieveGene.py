import sys
from optparse import OptionParser 
import glob

# get the command line arguments
parser = OptionParser(description="Script that retrieves a sequence (or part of) from a genome or transcriptome fasta file. Requires python 3.6 or higher")
parser.add_option('-g', '--gene', 
                    type=str,
                    default="empty",
                    metavar="",
                    help = "name (or comma separated list of multiple) of the transcript, gene or fragment that needs to be retrieved")
parser.add_option('-f', '--genome_fasta', 
                    type=str,
                    default="empty",
                    metavar="",
                    help = "path and name of genome or transcriptome fasta file, a file containing the the sequence that needs to be retrieved.")
parser.add_option('-o', '--output_file', 
                    type=str,
                    default="empty",
                    metavar="",
                    help = "path and name of the output file the sequence needs to be writen to. If filename is not specified the sequence will be printen in the console. Default = NULL")
parser.add_option('-d', '--direction', 
                    type=str,
                    default="forward",
                    metavar="",
                    help = "This option offers the posibility to chose the orientation of the sequence. Forward for forward, and reverse or rv for reverse and complement of the desired sequence.")
parser.add_option('-s', '--start_position', 
                    type=int,
                    default=-1,
                    metavar="",
                    help = "position of the first base of the sequence to be retrieved. If nan, the full transcript, gene, scaffold or chromosome will be retrieved. Default = nan")
parser.add_option('-e', '--end_position', 
                    type=int,
                    default=-1,
                    metavar="",
                    help = "position of the last base of the sequence to be retrieved. If nan, the full transcript, gene, scaffold or chromosome will be retrieved. Default = nan")

## Set arguments.
(options, args) = parser.parse_args()
go = True
seq = ""

## Function to get reverse and complement if requested.
def revComp(seq):
    seq = seq.upper()
    revSeq = ""
    base = ""
    for step in range(len(seq)-1,-1,-1):
        if seq[step] == 'A': base = 'T'
        if seq[step] == 'C': base = 'G'
        if seq[step] == 'G': base = 'C'
        if seq[step] == 'T': base = 'A'
        if seq[step] == 'N': base = 'N'
        revSeq = revSeq + base
    return(revSeq)

## check if the arguments are sane.
if options.gene == "empty":
    print("error: Name of the transcript, scaffold or chromosome is not specified. Specify using: -g [name1,name2,..]")
    go = False
if options.genome_fasta == "empty":
    print("error: Name of the genome or transcript fasta file is not specified. Specify using: -f [filename]")
    go = False   
if len(glob.glob(options.genome_fasta)) != 1:
    print("error: Cannot find genome or transcriptome fasta")
    go = False
if go == False:
    sys.exit("Script terminated, see error message above.\n Usage:\npython3 RetrieveGene.py -f [name of genome or transcriptome] -g [name of sequence to retrieve] [options]\n For more info run:\npython3 RetrieveGene.py -h\
        \n\n\t#=========================#\n\t|       tijs bliek        |\n\t| University of Amsterdam |\n\t#=========================#\n")

## get the sequence.
fasta = open(options.genome_fasta)
name = ""
retrieve = False
no = 0
for l in fasta:
    if l.startswith(">"):
        retrieve = False
        if options.gene in l:
            name = l
            retrieve = True
            no += 1
    elif retrieve:
        seq += l.rstrip()
    if no > 1:
        print("error: multiple sequences found that match the name.")
        sys.exit("Script terminated, see error message above.\n Usage:\npython3 RetrieveGene.py -f [name of genome or transcriptome] -g [name of sequence to retrieve] [options]\n For more info run:\npython3 RetrieveGene.py -h\
            \n\n\t#=========================#\n\t|       tijs bliek        |\n\t| University of Amsterdam |\n\t#=========================#\n")

fasta.close()

## check if any sequence has been found.
if len(seq) == 0:
    print(f"error: Gene {options.gene} not found")
    sys.exit("Script terminated, see error message above.\n Usage:\npython3 RetrieveGene.py -f [name of genome or transcriptome] -g [name of sequence to retrieve] [options]\n For more info run:\npython3 RetrieveGene.py -h\
        \n\n\t#=========================#\n\t|       tijs bliek        |\n\t| University of Amsterdam |\n\t#=========================#\n")

## Cut sequence to desired length.
if options.start_position == -1 and options.end_position == -1:
    first = 0
    last = len(seq)
elif options.start_position == -1:
    first = 0
    last = int(options.end_position)
elif options.end_position == -1:
    first = int(options.start_position)
    last = len(seq)
else:
    first = int(options.start_position)
    last = int(options.end_position)
seq = seq[first:last]

if options.direction.lower() == "reverse" or options.direction.lower() == "rv" or options.direction.lower() == "rev":
    seq = revComp(seq)

## print sequence to console or write to file.
if options.output_file == "empty":
    print(seq)
else:
    outFile = open(options.output_file, "w")
    outFile.write(name + seq + "\n")
    outFile.close()
    print(f"Sequences written to file: {options.output_file}.")
print("\n\t#=========================#\n\t|       tijs bliek        |\n\t| University of Amsterdam |\n\t#=========================#\n")
