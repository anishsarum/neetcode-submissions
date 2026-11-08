class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        results = []
        index = 0
        added = False

        if not intervals:
            return [newInterval]

        while index < len(intervals):
            if newInterval[0] <= intervals[index][1]:
                if newInterval[1] < intervals[index][0]:
                    if not added:
                        results.append(newInterval)
                        added = True
                    results.append(intervals[index])
                    index += 1
                
                elif not added:
                    left = min(newInterval[0], intervals[index][0])
                    right = max(newInterval[1], intervals[index][1])

                    while index < len(intervals) and newInterval[1] >= intervals[index][0]:
                        right = max(newInterval[1], intervals[index][1]) 
                        index += 1
                    
                    added = True
                    results.append([left, right])
                
                else:
                    results.append(intervals[index])
                    index += 1


            else:
                results.append(intervals[index])
                index += 1
        
        if not added:
            results.append(newInterval)
        
        return results


