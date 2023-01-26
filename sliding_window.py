def largest_sum(x, k):
    if k > len(x):
        return "Invalid value of K"

    max_sum = 0
    for i in range(len(x) - k + 1):
        current_sum = 0

        for j in range(i, i + k):
            current_sum += x[j]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

def window(x, k):
    start = 0
    max_sum = 0

    for i in range(len(x) - k + 1):
        start = i
        window = sum(x[start:start + k])
        max_sum = max(max_sum, window)

    return max_sum

def longestSubstring(x):
    dic = {}
    max_length = start = 0

    for i, v in enumerate(x):
        if v in dic and start <= dic[v]:
            start = dic[v] + 1
        else:
            max_length = max(max_length, i - start + 1)
                
            dic[v] = i
            
    return max_length

def twoSum(nums, target):
    dic = {}
    for i, v in enumerate(nums):
        optimal = target - v
        if optimal in dic:
            return [dic[optimal], i]
        dic[v] = i

    return "No matches found"

def subarraySum(nums, target):
        subarrays = []
        dic = {}
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                storage = []
                subarrays.append(storage)
                for k in range(i, j + 1):
                    storage.append(nums[k])

        for i, v in enumerate(subarrays):
            if sum(v) in dic:
                dic[sum(v)].append(v)
            else:
                dic[sum(v)] = []
                dic[sum(v)].append(v)

        return len(dic[target])

def maxProfit(prices):
    max_prof = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_prof:
                max_prof = profit
                profit = 0
    return max_prof



if __name__ == '__main__':
    x = [7,5,3,6,4]
    k = 2
    print(maxProfit(x))
