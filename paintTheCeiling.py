"""
https://leetcode.com/discuss/interview-question/892579/paint-the-ceiling-swe-hackerrank-test

https://www.chegg.com/homework-help/questions-and-answers/5-paint-ceiling-want-build-house-building-company-hired-build-houses-sides-specific-set-s--q43901799

"""



n,k,b,m,a = 10,3,3,2,15

s = [0] * n
s[0] = 2
for i in range(1,n):
    s[i] = ((k* s[i-1] + b) % m)+ 1+ s[i-1]

print(s)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# [2,4,6]

# choose two sides such that s1 * s2 <= a

# let a = 115
# 14*8=112

nums = [2, 4, 6]
a = 15

def get_combs(nums, a):
    low, high = 0, len(nums)-1
    combs = []
    while low <= high:
        if nums[low] * nums[high] <= a:
            combs += 
        
