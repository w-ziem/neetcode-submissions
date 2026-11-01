class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}

        for char in s :
            seen_s[char] = seen_s.get(char, 0) + 1

        for char in t :
            seen_t[char] = seen_t.get(char, 0) + 1
        
        return seen_s == seen_t