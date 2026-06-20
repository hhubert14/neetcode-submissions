"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
[(0,40),(5,10),(15,20)]

"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0: return 0
        if len(intervals) == 1: return 1
        ans = 0
        allocated = set()
        intervals.sort(key=lambda x: x.start)
        while len(allocated) < len(intervals):
            ans += 1
            prev = None
            for i in range(len(intervals)):
                if i in allocated:
                    continue
                if not prev:
                    prev = intervals[i]
                    allocated.add(i)
                    continue
                if prev.end <= intervals[i].start:
                    prev = intervals[i]
                    allocated.add(i)

        return ans



