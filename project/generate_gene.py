import pandas as pd
import random as rd
from carshen_AC import *

reads = ["U", "C", "A", "G"]
gene_code = {
    "Phe": ["UUU", "UUC"],
    "Leu": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
    "Ile": ["AAU", "AUC", "AUA"],
    "Met": ["AUG"],
    "Val": ["GUU", "GUC", "GUA", "GUG"],
    "Ser": ["UCU", "UCC", "UCA", "UCG"],
    "Pro": ["CCU", "CCC", "CCA", "CCG"],
    "Thr": ["ACU", "ACC", "ACA", "ACG"],
    "Ala": ["GCU", "GCC", "GCA", "GCG"],
    "Tyr": ["UAU", "UAC"],
    "His": ["CAU", "CAC"],
    "Gln": ["CAA", "CAG"],
    "Asn": ["AAU", "AAC"],
    "Lys": ["AAA", "AAG"],
    "Asp": ["GAU", "GAC"],
    "Glu": ["GAA", "GAG"],
    "Cys": ["UGU", "UGC"],
    "Trp": ["UGG"],
    "Arg": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "Ser": ["AGU", "AGC"],
    "Gly": ["GGU", "GGC", "GGA", "GGG"],
    "Stop": ["UAA", "UAG", "UGA"],
}


def make_gene(gene_cnt=5):
    gene_code_list = []
    for k, v in gene_code.items():
        for c in v:
            gene_code_list.append(c)
    # print(gene_code_list)

    # exon - 18*3 reads
    # intron - 48 reads
    genes = dict()
    gene_idx = 0

    for _ in range(gene_cnt):
        temp_string = ""
        temp_string_spliced = ""
        mis_spliced = False
        pre_exon_size = rd.randint(2, 18)
        post_exon_size = 18 - pre_exon_size

        # 가정, pre-mRNA, mRNA
        in_intron = "GU" + "".join(rd.choices(reads, k=44)) + "AG"
        in_intron_spliced = in_intron
        pre_exon = "".join(rd.choices(gene_code_list, k=pre_exon_size))
        post_exon = "".join(rd.choices(gene_code_list, k=post_exon_size))

        # origin_string = pre_exon + "||" + in_intron + "||" + post_exon
        origin_string = pre_exon + in_intron + post_exon
        splicing_p = rd.randint(0, 100)
        if splicing_p >= 50:
            mis_spliced = True

        if mis_spliced == True:
            mis_spliced_pos_f = rd.randint(0, 24)
            mis_spliced_pos_b = rd.randint(24, 48)
            in_intron_spliced = rd.choice(
                [
                    in_intron_spliced[0:mis_spliced_pos_f],
                    in_intron_spliced[mis_spliced_pos_b:],
                ]
            )
            # in_intron_spliced[
            #     mis_spliced_pos_f : 48 - mis_spliced_pos_b
            # ]
            # temp_string = pre_exon + "||" + in_intron_spliced + "||" + post_exon
            temp_string = pre_exon + in_intron_spliced + post_exon
        else:
            mis_spliced_pos_f = 0
            mis_spliced_pos_b = 0
            # temp_string = pre_exon + "||" + post_exon
            temp_string = pre_exon + post_exon

        genes[str(gene_idx)] = [
            mis_spliced,
            ((0, mis_spliced_pos_f), (mis_spliced_pos_b, 48)),
            (
                (pre_exon_size * 3, pre_exon_size * 3 + mis_spliced_pos_f),
                (pre_exon_size * 3 + mis_spliced_pos_b, len(origin_string) - 1),
            ),
            origin_string,
            temp_string,
            len(origin_string),
            len(origin_string) - len(temp_string),
            len(temp_string),
        ]
        gene_idx += 1
    return genes

    # print(genes)
    # print(temp_string)


def make_csv(genes):
    df = pd.DataFrame.from_dict(genes, orient="index").rename(
        columns={
            0: "mis_spliced",
            1: "spliced_intron_pos",
            2: "spliced_pos",
            3: "origin",
            4: "spliced",
            5: "origin_len",
            6: "intron_len",
            7: "spliced_len",
        }
    )
    df.to_csv("project/genes.csv", index=False, encoding="utf8")


# def main():
#     origin_genes = []
#     spliced_genes = []
#     origin_ss_idxs = []
#     spliced_ss_idxs = []
#     for i in range(gene_cnt):
#         origin_genes.append(genes[str(i)][3])
#         spliced_genes.append(genes[str(i)][4])

#     for i in range(gene_cnt):
#         origin_ss_idxs.append(get_keywords_found(origin_genes[i]))
#         spliced_ss_idxs.append(get_keywords_found(spliced_genes[i]))

#     print(origin_ss_idxs[0])
#     print(spliced_ss_idxs[0])
#     make_csv()

# if __name__ == "__main__":
#     init_trie(["GU", "AG"])
#     main()
