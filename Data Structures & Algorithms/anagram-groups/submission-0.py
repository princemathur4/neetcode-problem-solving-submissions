class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        already_grouped = set()

        for i in range(len(strs)):
            if i in already_grouped:
                continue
            str1 = strs[i]

            # group = [strs[i]]
            for j in range(len(strs)):
                if i == j:
                    continue
                
                str2 = strs[j]

                if self.isAnagram(str1, str2):
                    groups
                    already_grouped.add(j)
                    if groups.get(str1):
                        groups[str1] = groups.get(str1, []) + [str2]
                    else:
                        groups[str1] = groups.get(str1, []) + [str1, str2]
            
            if not groups.get(str1) and i not in already_grouped:
                groups[str1] = [str1]
        return list(groups.values())

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        
        return count_s == count_t