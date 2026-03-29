class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(
            map(
                lambda x: x[0], 
                    sorted(
                        list(Counter(nums).items()), 
                        key=lambda x: x[1], 
                        reverse=True
                    )[:k]
            )
        )