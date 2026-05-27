class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {} # num : times seen 

        for num in nums:
            if num not in seen: 
                seen[num] = 1
            else: 
                count = seen[num]
                seen.update({num : count + 1})

        arr = []
        for num, count in seen.items():
            arr.append([count,num])
        print(arr)
        arr.sort()
        print(arr)

        res=[]
        while len(res) < k:
            res.append(arr.pop()[1])

        return res