class Solution(object):
    def lengthOfLongestSubstring(self, s):
        length = len(s)
        longest = 0
        cur = 0
        if length == 0 or length == 1:
            return length
        elif length > 1:
            ss = ""
            for ch in s:
                if ch not in ss:
                    ss = ss + ch
                    cur = len(ss)
                else:
                    ss = ss[ss.rfind(ch)+1:] + ch
                longest = max(cur, longest)
        return longest