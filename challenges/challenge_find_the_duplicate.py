def validate_param(nums):
    has_param = nums
    is_list = isinstance(nums, list)
    if not has_param or not is_list or len(nums) <= 1:
        return True

    for num in nums:
        if not isinstance(num, int) or num < 0:
            return True


def find_duplicate(nums):
    nums.sort()
    index = 0
    if validate_param(nums):
        return False

    while index < len(nums) - 1:
        if nums[index] == nums[index + 1]:
            return nums[index]
        index += 1

    return False
