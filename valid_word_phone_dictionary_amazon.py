"""
Ref: https://leetcode.com/discuss/interview-question/1012161/amazon-phone-interview-valid-dictionary-word-from-phone-number/818651
"""

word_dict = ['a','and','also', 'qnbpt', 'qnbut', 'qnbps', 'roast', 'smart', 'snast', 'zebra']
phone_pad = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}

def load_dict():
    return word_dict

def build_options(number):
    trie = Trie(load_dict())
    trie.build_trie()
    return trie.search_word_with_number(number)


class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWordEnd = False

class Trie():
    def __init__(self, word_dict):
        self.word_dict = word_dict
        self.root = TrieNode()

    def addWord(self, word):
        root = self.root
        for letter in word:
            if letter not in root.children:
                root.children[letter] = TrieNode()
            root = root.children[letter]
        root.isWordEnd = True

    def build_trie(self):
        for word in self.word_dict:
            self.addWord(word)

    def search_word_with_number(self, number):
        root = self.root
        self.res = []
        def dfs(path, root, start):
            if len(path) == len(number):
                if root.isWordEnd:
                    self.res.append(path)
                return

            digit = int(number[start])
            for letter in phone_pad[digit]:
                if letter not in root.children:
                    continue
                tmp = root
                root = root.children[letter]
                dfs(path + letter, root, start+1)
                root = tmp

        dfs('', root, 0)
        return self.res


assert(build_options('76278')) == ['qnbpt', 'roast', 'smart', 'snast']