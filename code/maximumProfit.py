class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def profit_calc(start, end, profit, max_overlap, opt):
            for i in range(1, len(profit)):
                opt[i] = max(profit[i]+ opt[max_overlap[i]], opt[i-1])
            return max(opt)

        def aux_func(start, end):
            max_overlap = [0] * (len(profit))
            for i in range(2, len(start)):
                j = bisect_right(endTime, startTime[i]) - 1
                max_overlap[i] = j
                
            return max_overlap

        startTime = [0] + startTime
        endTime = [0] + endTime
        profit = [0] + profit
        pairs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        startTime, endTime, profit = zip(*pairs)

        max_overlap = aux_func(startTime, endTime)
        opt = [0] * (len(profit))


        return profit_calc(startTime, endTime, profit, max_overlap, opt)