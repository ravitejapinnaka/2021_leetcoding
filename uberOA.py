"""
https://leetcode.com/discuss/interview-question/418351/Uber-Internship-(No-Offer)

Question:
Uber used to call Ubercab, and they have a lot of "ubercab" stickers and assuming you can
cut them into individual characters. You are now given a word in string, and
return how many stickers you need to make the word.

Example 1:

Input: "abc"
Output: 1
Explanation: because you only need a 'ubercab' sticker to make 'abc'

Example 2:

Input: "abcd:
Output: -1
Explanation: you do not have 'd'

"""

import collections

def uberStickers(word):
    original = "ubercab"
    original_counter = collections.Counter(original)

    word_counter = collections.Counter(word)
    res = 0
    for key,val in word_counter.items():
        if key not in original_counter:
            return -1
        orig_val = original_counter[key]
        res = max(res, round(val/orig_val))
    return res

word = 'bb'
print(uberStickers(word))

word = 'aabbc'
print(uberStickers(word))

word = 'bbb'
print(uberStickers(word))

word = 'bbbd'
print(uberStickers(word))

