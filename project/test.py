from generate_gene import *
from searching_intron import *

"""
genes: dict("index")
 = [
        0. bool: mis_spliced || whether mis-spliced(True) or not(False)
        1. tuple: ((0, mis_spliced_pos_f), (mis_spliced_pos_b, 48)) || intron (reads 0 to 48), mis_spliced positions
        2. tuple: (
            (pre_exon_size * 3, pre_exon_size * 3 + mis_spliced_pos_f),
            (pre_exon_size * 3 + mis_spliced_pos_b, len(origin_string) - 1),
        ) || in origin gene, intron locations
        3. origin_string,
        4. spliced_string,
        5. len(origin_string),
        6. len(origin_string) - len(intron_string),
        7. len(intron_string),
    ]

"""

gene_cnt = 100000
genes = make_gene(gene_cnt)

# print(genes["0"])
# print(determination(genes["0"][3], genes["0"][4]))
# print(type(genes["0"][0]))

whole_cnt = gene_cnt
correct_cnt = 0
for k, v in genes.items():
    if genes[k][0] == False:
        whole_cnt -= 1
        continue

    if genes[k][0] == determination(genes[k][3], genes[k][4]):
        correct_cnt += 1

print(correct_cnt / whole_cnt)
