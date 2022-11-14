gene_code = {'Phe': ['UUU', 'UUC'],
             'Leu': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
             'Ile': ['AAU', 'AUC', 'AUA'],
             'Met': ['AUG'],
             'Val': ['GUU', 'GUC', 'GUA', 'GUG'],
             'Ser': ['UCU', 'UCC', 'UCA', 'UCG'],
             'Pro': ['CCU', 'CCC', 'CCA', 'CCG'],
             'Thr': ['ACU', 'ACC', 'ACA', 'ACG'],
             'Ala': ['GCU', 'GCC', 'GCA', 'GCG'],
             'Tyr': ['UAU', 'UAC'],
             'His': ['CAU', 'CAC'],
             'Gln': ['CAA', 'CAG'],
             'Asn': ['AAU', 'AAC'],
             'Lys': ['AAA', 'AAG'],
             'Asp': ['GAU', 'GAC'],
             'Glu': ['GAA', 'GAG'],
             'Cys': ['UGU', 'UGC'],
             'Trp': ['UGG'],
             'Arg': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
             'Ser': ['AGU', 'AGC'],
             'Gly': ['GGU', 'GGC', 'GGA', 'GGG'],
             'Stop': ['UAA', 'UAG', 'UGA']}

gene_code_list = []
for k, v in gene_code.items():
    for c in v:
        gene_code_list.append(c)
print(gene_code_list)