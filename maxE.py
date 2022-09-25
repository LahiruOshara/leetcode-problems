from itertools import count


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    maxE = 0
    maxCount = 0 
    for key, val in dict.items():
        if val > maxCount:
            maxE = key
            maxCount = count
    return maxE

if __name__ == "__main__":
    arr = [3, 3, 4]
    print(majorityElement(arr))