"""
https://leetcode.com/discuss/interview-question/406086/Roblox-or-OA-2020

Generate all unique substrings from given string, then return last string in (asc.) sorted string array.

"""




def generateAllSubstrings(s):
    for i in range(len(s)):
        for j in range(i, len(s)):
            print(s[i:j+1])

generateAllSubstrings('abc')
# print(res)