"""
reference:
https://carshen.github.io/data-structures/algorithms/2014/04/07/aho-corasick-implementation-in-python.html
"""

from collections import deque

adj_list = []


def init_trie(keywords):
    create_empty_trie()
    add_keywords(keywords)
    set_fail_transitions()
    pass


def create_empty_trie():
    adj_list.append({"value": "", "next_states": [], "fail_state": 0, "output": []})


def add_keywords(keywords):
    for keyword in keywords:
        add_keyword(keyword)


def set_fail_transitions():
    pass


def find_next_state(current_state, value):
    for node in adj_list[current_state]["next_states"]:
        if adj_list[node]["value"] == value:
            return node
    return None


def add_keyword(keyword):
    current_state = 0
    j = 0
    keyword = keyword.lower()
    child = find_next_state(current_state, keyword[j])
    while child != None:
        current_state = child
        j = j + 1
        if j < len(keyword):
            child = find_next_state(current_state, keyword[j])
        else:
            break
    for i in range(j, len(keyword)):
        node = {"value": keyword[j], "next_states": [], "fail_state": 0, "output": []}
        adj_list.append(node)
        adj_list[current_state]["next_states"].append(len(adj_list) - 1)
        current_state = len(adj_list) - 1
    adj_list[current_state]["output"].append(keyword)


def set_fail_transitions():
    q = deque()
    child = 0
    for node in adj_list[0]["next_states"]:
        q.append(node)
        adj_list[node]["fail_state"] = 0

    while q:
        r = q.popleft()
        for child in adj_list[r]["next_states"]:
            q.append(child)
            state = adj_list[r]["fail_state"]
            while (
                find_next_state(state, adj_list[child]["value"]) == None and state != 0
            ):
                state = adj_list[state]["fail_state"]
            adj_list[child]["fail_state"] = find_next_state(
                state, adj_list[child]["value"]
            )
            if adj_list[child]["fail_state"] is None:
                adj_list[child]["fail_state"] = 0
            adj_list[child]["output"] = (
                adj_list[child]["output"]
                + adj_list[adj_list[child]["fail_state"]]["output"]
            )


def get_keywords_found(line):
    line = line.lower()
    current_state = 0
    keywords_found = []

    for i in range(len(line)):
        while find_next_state(current_state, line[i]) is None and current_state != 0:
            current_state = adj_list[current_state]["fail_state"]
        current_state = find_next_state(current_state, line[i])
        if current_state is None:
            current_state = 0
        else:
            for j in adj_list[current_state]["output"]:
                keywords_found.append({"index": i - len(j) + 1, "word": j})
    return keywords_found


init_trie(["cash", "shew", "ew"])
print(get_keywords_found("cashew"))
