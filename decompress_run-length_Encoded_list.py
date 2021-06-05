def decompressRLElist(nums):
        list = []
        first = 0
        second = 1 
        while first < len(nums):
            el = [x*0+nums[second] for x in range(nums[first])]
            for x in el:
                list.append(x)
            first += 2
            second += 2
        
        return list
list = [1,2,3,4]
print(decompressRLElist(list))