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
        add_keywords(keyword)


def set_fail_transitions():
    pass


def find_next_state(current_state, value):
    for node in adj_list[current_state]["next_states"]:
        if adj_list[node]["value"] == value:
            return node
    return node
