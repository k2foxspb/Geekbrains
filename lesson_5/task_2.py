n = 15
nums_gen = (nums for nums in range(1, n+1, 2))
print(next(nums_gen), next(nums_gen), next(nums_gen), next(nums_gen))