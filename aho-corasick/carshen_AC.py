"""
reference:
https://carshen.github.io/data-structures/algorithms/2014/04/07/aho-corasick-implementation-in-python.html
"""

from collections import deque

adj_list = []


def init_trie(keywords):
    """
    aho-corasick은 trie 구조를 사용한다.
    찾고자 하는 pattern(이하 keyword)들로 trie 구조를 생성하고,
    이들의 다음 state가 없을 때 (fail), 다음 state를 정의하기 위한 fail state를 만든다.
    """
    create_empty_trie()
    add_keywords(keywords)
    set_fail_transitions()


def create_empty_trie():
    """
    trie의 첫 root를 생성한다.
    """
    adj_list.append({"value": "", "next_states": [], "fail_state": 0, "output": []})


def add_keywords(keywords):
    """
    찾고자 하는 keyword들로, add_keyword 함수를 이용하여 trie를 생성한다.
    """
    for keyword in keywords:
        add_keyword(keyword)


def find_next_state(current_state, value):
    """
    하나의 state(alphabet)에서 다음 state로 가기 위하여 다음 state가 어떤 것인지 찾아야 한다.
    이는 현재 state에 연결되어 있는 다음 state들 중에 value(다음 글자)가 같은 state를 찾는 것이다.
    만약 없다면 None을 반환한다.
    """
    for node in adj_list[current_state]["next_states"]:
        if adj_list[node]["value"] == value:
            return node
    return None


def add_keyword(keyword):
    """
    keyword를 trie에 추가 하는 함수
    이를 위해서 root에서 시작하는 trie에, keyword의 가장 긴 prefix를 탐색
    ------------------------------
    마지막 node(state)를 output에 표시
    """
    # 처음 state를 0으로
    current_state = 0
    # keyword의 처음부터 탐색
    j = 0
    keyword = keyword.lower()
    # 다음 state를 모두 찾음
    child = find_next_state(current_state, keyword[j])
    # 만약 child state가 존재한다면
    while child != None:
        current_state = child
        j = j + 1
        # j는 keyword의 index를 나타내므로 총 길이보다 작을 때까지 다음 state를 계속 탐색
        # 이를 통하여 가장 긴 prefix까지 탐색하게 된다.
        if j < len(keyword):
            child = find_next_state(current_state, keyword[j])
        else:
            break
    # keyword의 남은 부분에 대해서 각 alphabet을 adjlist에 추가
    for i in range(j, len(keyword)):
        node = {"value": keyword[i], "next_states": [], "fail_state": 0, "output": []}
        adj_list.append(node)
        adj_list[current_state]["next_states"].append(len(adj_list) - 1)
        current_state = len(adj_list) - 1
    # trie에 keyword를 추가한 이후, 마지막으로 가리키고 있는 state까지가 output이므로
    # 이를 adjlist의 현재 state output에 추가하여 표시
    adj_list[current_state]["output"].append(keyword)


def set_fail_transitions():
    """
    각 state의 다음 state가 없을 때, 그 state의 fail transition을 설정
    """
    q = deque()
    child = 0
    # init, root state부터 시작
    for node in adj_list[0]["next_states"]:
        q.append(node)
        # root state의 fail state는 root이므로 0으로 설정
        adj_list[node]["fail_state"] = 0

    # root부터 fail transition을 설정
    while q:
        r = q.popleft()
        for child in adj_list[r]["next_states"]:
            q.append(child)
            state = adj_list[r]["fail_state"]
            # 지금보고 있는 state의 child의 마지막 state를 찾음
            while (
                find_next_state(state, adj_list[child]["value"]) == None and state != 0
            ):
                state = adj_list[state]["fail_state"]
            # 가장 긴 prefix를 가지는 state를 찾았으므로 이를 child의 fail state로 설정
            adj_list[child]["fail_state"] = find_next_state(
                state, adj_list[child]["value"]
            )
            # 만약 fail state가 없다면 root state를 가리키게 설정
            if adj_list[child]["fail_state"] is None:
                adj_list[child]["fail_state"] = 0
            # child의 output은 child와 fail state에 존재하는 output의 합
            adj_list[child]["output"] = (
                adj_list[child]["output"]
                + adj_list[adj_list[child]["fail_state"]]["output"]
            )


def get_keywords_found(line):
    """
    aho-corasick을 호출하는 함수, 즉 get_keywords_found가 aho-corasick으로 pattern들의 index와 정보들을 dictionary의 list로 반환
    """
    # keyword들이 trie에 존재한다면, 해당 정보를 return
    # line이 주어진 input string을 의미
    line = line.lower()
    current_state = 0
    keywords_found = []

    for i in range(len(line)):
        # 주어진 input string의 각 alphabet을 비교하면서 탐색
        while find_next_state(current_state, line[i]) is None and current_state != 0:
            current_state = adj_list[current_state]["fail_state"]
        current_state = find_next_state(current_state, line[i])
        if current_state is None:
            current_state = 0
        else:
            # fail state가 root가 아니고 어떠한 state를 나타내고 있으면 pattern을 찾았음을 의미
            # 이를 return list에 추가
            for j in adj_list[current_state]["output"]:
                keywords_found.append({"index": i - len(j) + 1, "word": j})
    return keywords_found


# init_trie(["cash", "shew", "ew"])
# print(get_keywords_found("cashew"))

contents = []
cnt = 0
with open(r"C:\Users\gnaro\Desktop\SDP_Project\iread\data\mouse_test.txt", "r") as f:
    for row in f:
        contents.append(row.replace("\t", "^").split("^")[9])
        cnt += 1
    if cnt == 1:
        raise


# init_trie(["gu", "ag"])
init_trie(["gu"])
for input_string in contents:
    temp_indices = get_keywords_found(input_string)
    if len(temp_indices) != 0:
        print(temp_indices)
# print(len(contents))
# print(get_keywords_found(contents[0]))
