class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = dict()

        for idx, val in enumerate(nums):

            # we will not return the value in the same index
            # because we store the value in the dictionary after we check the dictionary

            # idx will be the second index

            if target - val in values:
                return [values[target - val], idx]

            values[val] = idx

        # return an empty list if the result is not found
        return []
