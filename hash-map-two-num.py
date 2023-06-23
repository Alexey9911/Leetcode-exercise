def two_sum(nums, target):
    
	
    prevMap = dict()
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i