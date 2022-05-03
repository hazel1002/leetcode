from unittest import result


def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        check_table = dict()
        for i in range(len(nums)):
            included_number = target - nums[i]
            if included_number in check_table :
                return(check_table[included_number],i)
            else:
                check_table[nums[i]] = i
    

nums = [2,7,11,15]
target = 9
f = twoSum(nums,target)
print(f)
