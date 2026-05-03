class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        
        longest_seq_len = 0
        for curr in numset:
            prev_num = curr-1
            if prev_num in numset:
                continue
            
            seq_len = 1
            next_num = curr+1
            while next_num in numset:
                seq_len += 1
                next_num += 1

            if seq_len > longest_seq_len:
                longest_seq_len = seq_len
        return longest_seq_len