class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chain = ""
        max_length = 0
        for l in s:
            pos = chain.find(l)
            if pos == -1:
                chain+=l
                if len(chain) > max_length:
                    max_length = len(chain)
            else:
                chain = chain.split(l)
                chain = chain[1]
                chain+=l
                if len(chain) > max_length:
                    max_length = len(chain)
        return max_length
        
print(Solution().lengthOfLongestSubstring('abcabcbb'))
print(Solution().lengthOfLongestSubstring('abcazxw'))
print(Solution().lengthOfLongestSubstring('bbbbb'))
print(Solution().lengthOfLongestSubstring('pwwkew'))
