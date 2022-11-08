"""
input: strings(gene)
output: 5' & 3' splice sites' indices (AG, GU)
"""


class Trie(dict):
    def __init__(self):
        super().__init__()
        self.final = False
        self.out = set()
        self.fail = None


class Node:
    def __init__(self):
        self.child = []
        self.fail = None
        self.isEnd = None
        self.isRoot = False
