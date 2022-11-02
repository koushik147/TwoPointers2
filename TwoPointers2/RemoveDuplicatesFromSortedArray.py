#Time_Complexity: O(n) 
#Space_Complexity : O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1    # create slow pointer to 1
        fast = 1    # create fast pointer to 1
        count =1    
        k = 2 
        n = len(nums)  # n is the length of nums
        for fast in range(1, n): # run fast until the lenght of nums

            if nums[fast] == nums[fast-1]:  # if nums[fast] is equal to nums[fast-1] 
                count+= 1   # increment count by 1
            else:    
                count = 1   # count will remain 1
                
            if count <=k:   # if the count is equal to k
                nums[slow] = nums[fast] # change nums[slow] to nums[fast]
                slow+=1 # increment slow with 1
        return slow # return slow
