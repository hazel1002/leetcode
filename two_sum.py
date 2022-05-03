from unittest import result


def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 先設置一個字典，來去裝我們取過的數字
        check_table = dict()
        for i in range(len(nums)):
            included_number = target - nums[i]
            # 用in去找included_number這個key有沒有在check_table的key
            if included_number in check_table :
                return(check_table[included_number],i)
            else:
                # check_table[key]=value
                check_table[nums[i]] = i
    

nums = [2,7,11,15]
target = 9
f = twoSum(nums,target)
print(f)
