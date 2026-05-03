class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        idx_map = {}
        for i in range(len(nums)):
            idx_map[nums[i]] = i
        
        longest_seq = []
        for i in range(len(nums)):
            curr = nums[i]
            
            prev_num = curr-1
            if prev_num in idx_map:
                continue
            
            curr_seq = [curr]
            next_num = curr+1
            while next_num in idx_map:
                curr_seq.append(next_num)
                next_num += 1

            if len(curr_seq) > len(longest_seq):
                longest_seq = curr_seq
        return len(longest_seq)