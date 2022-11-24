from carshen_AC import *


def determination(input_origin_string, input_spliced_string):
    init_adj_list()
    init_trie(["GU", "AG"])

    # origin_string = "AAACAACCGAGCGGAGUUGUCCCUCAGAAAGCCCAGGGCGGUAAAAGACUGAAUGGCCUGCCACAGGGGAAGCUCAUAAGAACGUGGUAUGUCGACACUCGG"
    # spliced_string = (
    #     "AAACAACCGAGCGGAGUUACUGAAUGGCCUGCCACAGGGGAAGCUCAUAAGAACGUGGUAUGUCGACACUCGG"
    # )
    origin_string = input_origin_string
    spliced_string = input_spliced_string

    r_origin_string = origin_string[::-1]
    r_spliced_string = spliced_string[::-1]

    origin_ss_idxs = []
    spliced_ss_idxs = []

    origin_ss_idxs = get_keywords_found(origin_string)
    spliced_ss_idxs = get_keywords_found(spliced_string)
    # print("ori ss: {}".format(len(origin_ss_idxs)))
    # print("spl ss: {}".format(len(spliced_ss_idxs)))

    alpha_iter = 0
    alpha_idx = 0

    # alpha searching
    # is_alpha_found = False
    while True:
        if len(spliced_ss_idxs) == 0:
            break
        flag = False
        # print(alpha_iter)
        if origin_ss_idxs[alpha_iter]["word"] == spliced_ss_idxs[alpha_iter]["word"]:
            # if origin_ss_idxs[alpha_iter]["index"] == spliced_ss_idxs[alpha_iter]["index"]:
            temp_o_a = origin_ss_idxs[alpha_idx]["index"]
            try:
                if origin_string[temp_o_a - 1] == spliced_string[temp_o_a - 1]:
                    alpha_idx = alpha_iter
                else:
                    alpha_idx = alpha_iter - 1
                    flag = True
            except:
                pass
            try:
                if origin_string[temp_o_a + 2] == spliced_string[temp_o_a + 2]:
                    alpha_idx = alpha_iter
                else:
                    alpha_idx = alpha_iter - 1
                    flag = True
            except:
                pass
        else:
            flag = True
        alpha_iter += 1
        if (
            flag == True
            or alpha_iter > len(spliced_ss_idxs) - 1
            or alpha_iter > len(origin_ss_idxs) - 1
            or alpha_idx < 0
        ):
            break
    if alpha_idx == len(origin_ss_idxs) - 1:
        alpha_idx -= 1
    if alpha_idx < 0:
        alpha_idx = 0
    # print(alpha_idx)

    # beta searching
    init_adj_list()
    init_trie(["GA", "UG"])
    r_origin_ss_idxs = get_keywords_found(r_origin_string)
    r_spliced_ss_idxs = get_keywords_found(r_spliced_string)

    beta_iter = 0
    beta_idx = 0

    # is_alpha_found = False
    while True:
        if len(r_spliced_ss_idxs) == 0:
            break
        # print("loc: {}".format(beta_iter))
        flag = False
        if r_origin_ss_idxs[beta_iter]["word"] == r_spliced_ss_idxs[beta_iter]["word"]:
            # if (
            #     r_origin_ss_idxs[beta_iter]["index"]
            #     == r_spliced_ss_idxs[beta_iter]["index"]
            # ):
            temp_o_b = r_origin_ss_idxs[beta_idx]["index"]
            try:
                if r_origin_string[temp_o_b - 1] == r_spliced_string[temp_o_b - 1]:
                    beta_idx = beta_iter
                else:
                    beta_idx = beta_iter - 1
                    flag = True
            except:
                pass
            try:
                if r_origin_string[temp_o_b + 2] == r_spliced_string[temp_o_b + 2]:
                    beta_idx = beta_iter
                else:
                    beta_idx = beta_iter - 1
                    flag = True
            except:
                pass
        else:
            flag = True
        beta_iter += 1
        if (
            flag == True
            or beta_iter > len(r_spliced_ss_idxs) - 1
            or beta_iter > len(r_origin_ss_idxs) - 1
            or beta_idx < 0
        ):
            break

    if beta_idx < 0:

        beta_idx = 0

    # print(beta_idx)

    # looking up a, g
    # origin_ag = ""
    # for i in origin_ss_idxs:
    #     if i["word"] == "ag":
    #         origin_ag += "A"
    #     else:
    #         origin_ag += "G"
    # spliced_ag = ""
    # for i in spliced_ss_idxs:
    #     if i["word"] == "gu":
    #         spliced_ag += "G"
    #     else:
    #         spliced_ag += "A"

    # print(origin_ag)
    # print(spliced_ag)
    # r_origin_ag = ""
    # for i in r_origin_ss_idxs:
    #     if i["word"] == "ga":
    #         r_origin_ag += "A"
    #     else:
    #         r_origin_ag += "G"
    # r_spliced_ag = ""
    # for i in r_spliced_ss_idxs:
    #     if i["word"] == "ug":
    #         r_spliced_ag += "G"
    #     else:
    #         r_spliced_ag += "A"

    # print("-" * 40)
    # print(r_origin_ag)
    # print(r_spliced_ag)

    """
    AAACAACCGAGCGGAGUU||GUCCCUCAGAAAGCCCAGGGCGGUAAAAGACUGAAUGGCCUGCCACAG||GGGAAGCUCAUAAGAACGUGGUAUGUCGACACUCGG
    AAACAACCGAGCGGAGUU||ACUGAAUGGCCUGCCACAG||GGGAAGCUCAUAAGAACGUGGUAUGUCGACACUCGG
    """

    # print("alpha: {}".format(alpha_idx))
    # print("beta: {}".format(beta_idx))

    a_next_GU_idx = 0
    b_prev_AG_idx = 0
    if alpha_idx != 0:
        a_next_GU_idx = alpha_idx
    if beta_idx != 0:
        b_prev_AG_idx = beta_idx
    front_exon = origin_string[: origin_ss_idxs[alpha_idx]["index"]]
    back_exon = origin_string[
        origin_ss_idxs[len(origin_ss_idxs) - beta_idx - 1]["index"] :
    ]
    try:
        intron = origin_string[
            origin_ss_idxs[alpha_idx + 1]["index"] : origin_ss_idxs[
                len(origin_ss_idxs) - beta_idx - 1
            ]["index"]
            + 2
        ]
    except Exception as e:
        print(e)
        print(origin_string)
        print(origin_ss_idxs)
        print(spliced_string)
        print(spliced_ss_idxs)
        print("alpha: {}".format(alpha_idx))
        print("beta: {}".format(beta_idx))
        print(origin_ss_idxs)
        print(spliced_ss_idxs)
        assert e

    # print(front_exon + "||" + back_exon)
    # print(intron)

    # print("origin len:{}".format(len(origin_string)))
    # print("spliced len:{}".format(len(spliced_string)))
    # print(
    #     "front_exon len: {}, back_exon len: {}, intron len: {}".format(
    #         len(front_exon), len(back_exon), len(intron)
    #     )
    # )
    ans = False
    if len(origin_string) - len(intron) != len(spliced_string):
        ans = True

    return ans


# i = 'GUUUCACAAUUCAAAAUCACAUCAUGUCGUCUGAAGUAAGCCCAAAAG'
# m = 'GUCUGAAGUAAGCCCAAAAG'
# o = "CGGACUGACCUUAAUCAUUUCCUAGGGCGUACCAUCGGGCGAUGGGCUUAAACAGUUUCACAAUUCAAAAUCACAUCAUGUCGUCUGAAGUAAGCCCAAAAG"
# s = "CGGACUGACCUUAAUCAUUUCCUAGGGCGUACCAUCGGGCGAUGGGCUUAAACAGUUUC"
# # o = "GAACUGACUGUGGCCACUGUCAAUAAGGUCGACAAUUAGGUUUAGACUAAAGCAGCUAUGUCCGGUACAAUAAAGUAACCAACUCCGAAUUUCGAUACAGGG"
# # s = "GAACUGACUGUGGCCACUGUCAAUAAGUAACCAACUCCGAAUUUCGAUACAGGG"
# determination(o, s)
