from operator import imod
from queue import Queue

class Node(dict):
    def __init__(self):
        super().__init__()
        self.final = False
        self.out = set()
        self.fail = None;

    def add_out(self, out):
        if type(out) is set:
            self.out = self.out.union(out)
        else:
            self.out.add(out)
    
    def add_child(self, alphabet, node = None):
        self[alphabet] = Node()if node is None else node

class AC():
    def __init__(self, patterns):
        self.patterns = patterns
        self.head = Node()
        self.maketrie()
        self.constructfail()

    def search(self, sentence):
        cur = self.head
        ret = []
        for c in sentence:
            while cur is not self.head and c not in cur:
                cur = cur.fail
            if c in cur:
                cur = cur[c]
            if cur.final:
                ret.extend(list(cur.out))
        return ret

    def make_trie(self):
        for pattern in self.patterns:
            cur = self.head
            for c in pattern :
                if c not in cur:
                    cur.addchild(c)
                cur = cur[c]
            cur.final = True
            cur.addout(pattern)

    def constuct_fail(self):
        queue = Queue()
        self.head.fail = self.head
        queue.put(self.head)
        while not queue.empty():
            cur = queue.get()
            for nextc in cur:
                child = cur[nextc]
                
                if cur is self.head:
                    child.fail = self.head
                else :
                    f = cur.fail
                    while f is not self.head and nextc not in f:
                        f = f.fail
                    if nextc in f:
                        f = f[nextc]
                    child.fail = f
                
                child.addout(child.fail.out)
                child.final |= child.fail.final
                
                queue.put(child)