from heapq import heappush, heappop
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        if len(intervals) == 0:
            return 0
        roomsInUse = []
        intervals.sort(key = lambda i: i.start)
        heappush(roomsInUse, intervals[0].end)
        for i in intervals[1:]:
            if roomsInUse[0] <= i.start:
                heappop(roomsInUse)
            heappush(roomsInUse, i.end)
        return len(roomsInUse)
i1 = Interval(7, 10)
i2 = Interval(2, 4)
#i3 = Interval(15, 20)
intervals = [i1, i2]
s1 = Solution()
print(s1.minMeetingRooms(intervals))
