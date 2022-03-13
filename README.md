# RetrieveGene
python script to retrieve a sequence from a genome or tyranscriptome  feasts file.

Usage: RetrieveGene.py -g [name of gene] -f [name og f genome or transcriptome] [options]

Script that retrieves a sequence (or part of) from a genome or transcriptome
fasta file. Requires python 3.6 or higher

Options:
  -h, --help            show this help message and exit
  -g GENE, --gene=GENE  name of thetranscript, gene or fragment that needs to
                        be retrieved
  -f GENOME_FASTA, --genome_fasta=GENOME_FASTA
                        path and name of genome or transcriptome fasta file, a
                        file containing the the sequence that needs to be
                        retrieved.
  -o OUTPUT_FILE, --output_file=OUTPUT_FILE
                        path and name of the output file the sequence needs to
                        be writen to. If filename is not specified the
                        sequence will be printen in the console. Default =
                        NULL
  -d DIRECTION, --direction=DIRECTION
                        This option offers the posibility to chose the
                        orientation of the sequence. Forward for forward, and
                        reverse or rv for reverse and complement of the
                        desired sequence.
  -s START_POSITION, --start_position=START_POSITION
                        position of the first base of the sequence to be
                        retrieved. If -1, the full transcript, gene, scaffold
                        or chromosome will be retrieved. Default = -1
  -e END_POSITION, --end_position=END_POSITION
                        position of the last base of the sequence to be
                        retrieved. If -1, the full transcript, gene, scaffold
                        or chromosome will be retrieved. Default = -1
