class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = sorted([("".join(sorted(string)), idx) for idx, string in enumerate(strs)])
        prev_str = sorted_strs[0][0]
        res = []
        curr_group = [strs[sorted_strs[0][1]]]
        for i in range(1, len(sorted_strs)):
            curr_str = sorted_strs[i][0]
            og_idx = sorted_strs[i][1]
            if prev_str == curr_str:
                curr_group.append(strs[og_idx])
            else:
                prev_str = curr_str
                res.append(curr_group)
                curr_group = [strs[og_idx]]
        if curr_group:
            res.append(curr_group)
        return res