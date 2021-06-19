import sys
import re
from Bio import SeqIO
from matplotlib.backends.backend_pdf import PdfPages
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
plt.style.use('ggplot')

infile = sys.argv[1]

with PdfPages(infile.split('.')[0] + '.pdf') as pdf:
    for sequence in SeqIO.parse(infile, 'fasta'):
        print('Processing: ', sequence.name)
        counted_dict = dict(Counter(sequence.seq))
        s = pd.Series(counted_dict)
        sorted_s = s.sort_values(ascending=False)
        ax = sorted_s.plot.bar(color='green')
        org_match = re.search('\[.*\]', sequence.description)
        org = org_match.group(0)[1:-1]
        ax.set_title(f'{org}  {sequence.name}')
        ax.set_xticklabels(sorted_s.index, rotation='horizontal')
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        pdf.savefig()
        plt.close()