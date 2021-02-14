"""
https://leetcode.com/problems/word-ladder-ii/
"""


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        self.wordList = set(wordList)
        self.graph = {}
        depth = float('inf')
        self.paths = []
        q = [(beginWord, 1)]
        visited = set()

        all_combo_dict = self.build_dict(beginWord)
        while q:
            root, level = q.pop(0)
            # visited.add(root)

            if root == endWord:
                # depth = min(level, depth)
                depth = level
                # break

            for neighbor in self.get_neighbors(root):
                if neighbor not in visited:
                    q.append((neighbor, level+1))
                    visited.add(neighbor)

        print(depth)
        self.backtrack(beginWord, endWord, depth, [beginWord], set())
        return self.paths

    def backtrack(self, word, endWord, depth, path, visited):
        if word == endWord:
            if len(path) == depth:
                self.paths.append(path)
            return
        visited.add(word)
        for child in self.graph.get(word, []):
            if child not in visited:
                self.backtrack(child, endWord, depth, path + [child], visited)

        visited.remove(word)



    # def process_paths(self, endWord, prev):
    #     for word, level in set(prev.get(endWord, [])):
    #         self.paths


    def get_neighbors(self, word):
        neighbors = []
        for j in range(len(word)):
            for i in range(26):
                letter = chr(i + ord('a'))
                if letter != word[j]:
                    tmp = word[:j] + letter + word[j+1:]
                    if tmp in self.wordList:
                        if word not in self.graph:
                            self.graph[word] = {tmp}
                        else:
                            self.graph[word].add(tmp)
                        # self.graph[word] = self.graph.get(word, []) + [tmp]
                        neighbors.append(tmp)
                        # self.wordList.remove(tmp)
        return neighbors

    def build_dict(self, word):
        import collections
        all_combo_dict = collections.defaultdict(list)
        for word in self.wordList:
            for i in range(len(word)):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        return all_combo_dict


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution().findLadders(beginWord, endWord, wordList))
# print(Solution().get_neighbors(beginWord, wordList))


beginWord = "qa"
endWord = "sq"
wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
print(Solution().findLadders(beginWord, endWord, wordList))