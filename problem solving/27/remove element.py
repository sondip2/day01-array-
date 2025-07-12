class Solution:
    def removeElement(self, nums, val):
        # Initialize pointer for next non-val element position
        k = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If current element is not val, place it at k
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k
