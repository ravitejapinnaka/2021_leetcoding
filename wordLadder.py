"""
https://leetcode.com/problems/word-ladder/

"""

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        q = [(beginWord, 1)]

        while q:
            root, level = q.pop(0)
            if root == endWord:
                return level

            for neighbor in self.get_all_neighbors(root, wordList):
                q.append((neighbor, level + 1))

        return 0

    def get_all_neighbors(self, word, wordList):
        neighbors = []
        for i in range(len(word)):
            for char in range(26):
                letter = chr(char + ord('a'))
                if letter != word[i]:
                    tmp = word[:i] + letter + word[i+1:]
                    if tmp in wordList:
                        neighbors.append(tmp)
                        wordList.remove(tmp)
        return neighbors

print(Solution().ladderLength(beginWord, endWord, wordList))

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(Solution().ladderLength(beginWord, endWord, wordList))
# print(Solution().get_all_neighbors(beginWord, wordList))
