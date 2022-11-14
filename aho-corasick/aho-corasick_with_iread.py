"""
input: strings(gene)
output: 5' & 3' splice sites' indices (AG, GU)
"""


"""
다음 state를 go 함수로 정의
go(state, alphabet) = next state
output node에 도달했다면 그 문자열들이 S에 등장
output함수는 output node들을 지날 때 내뱉는 단어의 목록
fail함수는 다음 state가 없을 때 다음 state를 찾는 함수
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
        self.output = []
        
        
    def insert(self, k):
        if 
    
    
