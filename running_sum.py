def runningSum(self, nums: List[int]) -> List[int]:
        list = []
        sum = 0
        for x in nums:
            sum += x
            list.append(sum)
        return list