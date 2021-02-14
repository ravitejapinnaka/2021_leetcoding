from heapq import heappop, heapify, heappush

"""
https://leetcode.com/discuss/interview-question/854052/Roblox-Intern-OA-2020
https://leetcode.com/problems/non-overlapping-intervals/
https://leetcode.com/problems/meeting-rooms-ii/
"""

arrival = [1,3,3,5,7]
duration = [2,2,1,2,1]

def careerFair(arrival, duration):

    maxEvents = []
    heapify(maxEvents)
    intervals = sorted([[start, start+time] for start, time in zip(arrival, duration)], key = lambda x:x[0])

    for interval in intervals:
        if maxEvents and -maxEvents[0] > interval[0]:
            heappop(maxEvents)
        heappush(maxEvents, -interval[1])
    return len(maxEvents)

print(careerFair(arrival, duration))