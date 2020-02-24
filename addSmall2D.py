def big_diff(nums):
    total_small = 0
    for x in range(len(nums)):
        smallest = nums[x][0] 
        for i in range(len(nums[x])):
            if nums[x][i] < smallest:
                smallest = nums[x][i]
        total_small = smallest + total_small    
    print(total_small)        

big_diff([[10, 3, 5], [20,50,6]])