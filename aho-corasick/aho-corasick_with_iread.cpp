#include <bits/stdc++.h>

using namespace std;

struct Trie { // 노드 객체 클래스
public:
	bool isEnd; // 이 노드가 한 검색어의 끝인지 아닌지를 알려줌 
	string p;   // 이 노드까지의 접두사 (아호 코라식의 필요한 부분은 아니다.)
	map<char, Trie*> child; // 자식 노드 링크
	Trie* fail; // 실패 링크 ⭐

	Trie() : isEnd(false), fail(nullptr) {}

	void Insert(string pattern) {
		Trie* now = this;
		int m = pattern.length();
		for (int i = 0; i < m; ++i) {
			if (now->child.find(pattern[i]) == now->child.end())
				now->child[pattern[i]] = new Trie;
			now = now->child[pattern[i]];

			if (i == m - 1) {
				now->p = pattern;
				now->isEnd = true;
			}
		}
	}

	void Fail() {  // BFS + KMP
		Trie* root = this;
		queue<Trie*> q;

		q.push(root);

		while (!q.empty()) {
			Trie* now = q.front();
			q.pop();

			for (auto& ch : now->child) {

				Trie* next = ch.second;
				if (now == root)
					next->fail = root;
				else {
					Trie* prev = now->fail;
					while (prev != root && prev->child.find(ch.first) == prev->child.end())
						prev = prev->fail;
					if (prev->child.find(ch.first) != prev->child.end())
						prev = prev->child[ch.first];
					next->fail = prev;
				}

				if (next->fail->isEnd)
					next->isEnd = true;

				q.push(next);
			}
		}
	}
};

vector<pair<string, int>> KMP(string text, Trie* root) {
	Trie* now = root;
	int n = text.length();
	vector<pair<string, int>> answer;
	for (int i = 0; i < n; ++i) {
		while (now != root && now->child.find(text[i]) == now->child.end())
			now = now->fail;
		if (now->child.find(text[i]) != now->child.end())
			now = now->child[text[i]];
		if (now->isEnd) {
			answer.push_back({ now->p, i });
		}
	}
	return answer;
}

int main() {
	freopen("input.txt", "r", stdin);

	int N;
	cin >> N;
	vector<string> patterns(N);
	for (int i = 0; i < N; ++i)
		cin >> patterns[i];
	Trie* root = new Trie;
	for (int i = 0; i < N; ++i)
		root->Insert(patterns[i]);
	root->Fail();

	string text;
	cin >> text;

	vector<pair<string, int>> answer = KMP(text, root);
  cout << text << "에서 검색하기" << '\n';
	for (int i = 0; i < answer.size(); ++i) 
		cout << "확인된 검색어 : " << answer[i].first << ", 위치 : " << answer[i].second << '\n';
}