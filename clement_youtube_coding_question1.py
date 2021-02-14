Source = "https://www.youtube.com/watch?v=rw4s4M3hFfs&t=1566s"

"""
Question 1
Find the block which minimizes the distance to all three of
reqs = ['gym', 'school', 'store]

In this example, answer is blocks[3]
"""
blocks = [
    {
        'gym': False,
        'school': True,
        'store': False
    },
    {
        'gym': True,
        'school': False,
        'store': False
    },
    {
        'gym': True,
        'school': True,
        'store': False
    },
    {
        'gym': False,
        'school': True,
        'store': False
    },
    {
        'gym': False,
        'school': True,
        'store': True
    },
]

reqs = ['gym', 'school', 'store']

dp = [[float('inf') for _ in range(len(reqs))] for j in range(len(blocks))]


for i, block in enumerate(blocks):
    for j, req in enumerate(reqs):
        if i == 0:
            dp[i][j] = 0 if blocks[i][req] else dp[i][j]

        elif i>0:

            if blocks[i][req]:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j])

for ll in dp:
    print(ll)
print('***************')

for i in range(len(blocks)-2,-1,-1):
    for j, req in enumerate(reqs):
        if blocks[i][req]:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i+1][j] + 1, dp[i][j])

for ll in dp:
    print(ll)

# Question 2

"""
Sort the lists in decreasing order of True %
"""

builds = [
    [True, True, True, False, False], # True % = 60
    [True, True, True, True, False], # True % = 80
    [True, True, True, True, True, True, False, False, False],
    [True, False, False, False, False, False],
    [True, True, True, True, True, True, True, True, True, True, True, True, False],
    [True, False],
    [True, True, True, True, False, False],
]

def binary_search(build):
    n = len(build)
    start, end = 0, n-1
    while start < end:
        mid = (start + end) // 2

        if build[mid]:
            start = mid+1
        else:
            end=mid
    return start


true_perc = []
for i, build in enumerate(builds):
    index = binary_search(build)
    print(index)
    true_perc.append([( index / len(build) ) * 100, i])

print(sorted(true_perc, key=lambda x:x[0], reverse= True))