"""
Given two integer arrays A and B,
return the maximum length of an subarray that appears in both arrays.

Ref: https://leetcode.com/problems/maximum-length-of-repeated-subarray/
https://leetcode.com/discuss/interview-question/963852/Wayfair(karat)-or-OA-or-Find-longest-matching-url-visits

list1 = [1,5,9,3,16] ; list2 = [4,9,3,16,1,5]
output = 3 -> [9, 3, 16]
"""


class Solution:
    # def findLength(self, A: List[int], B: List[int]) -> int:
    def findLength_brute(self, A, B):
        # brute force solution
        A, B = ''.join(A), ''.join(B)
        result = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                sub_str = A[i:j]
                # print(sub_str)
                if sub_str in B:
                    result = max(result, len(sub_str))
        return result

    def findLength(self, A, B):
        output = 0; maxIndex = -1;
        dp = [[0 for j in range(len(B))] for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1] + 1 if i>0 and j>0 else 1
                    if dp[i][j] > output:
                        output = dp[i][j]
                        maxIndex = j
                    # output = max(output, dp[i][j])
        # return output, maxIndex
        return B[maxIndex - output+1: maxIndex+1]

list1 = ['1','5','9','3','16'] ; list2 = ['4','9','3','16','1','5']
print(Solution().findLength_brute(list1, list2))

# maxlength, indexB = Solution().findLength(list1, list2)
# print(list2[indexB - maxlength+1: indexB+1])


# list1 = ['1','5','9','3','16'] ; list2 = ['16','3']

# maxlength, indexB = Solution().findLength(list1, list2)
# print(list2[indexB - maxlength+1: indexB+1])


user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]


print(Solution().findLength(user0, user1)) # ["/pink", "/register", "/orange"]
print(Solution().findLength(user0, user2)) # [] (empty)
print(Solution().findLength(user2, user1)) # ["a"] 
print(Solution().findLength(user5, user2)) # ["a"]
print(Solution().findLength(user3, user4)) # ["/plum", "/blue", "/tan", "/red"]
print(Solution().findLength(user4, user3)) # ["/plum", "/blue", "/tan", "/red"]
print(Solution().findLength(user3, user6)) # ["/tan", "/red", "/amber"]