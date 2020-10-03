class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bitmap = [False]*128
        window_start = 0
        window_end = 0
        current_length = 0
        max_length = 0
        if len(s) == 0:
            return 0
        else:
            for window_end in range(0, len(s)):
                index = ord(s[window_end])
                if bitmap[index]:
                    old_window_start = window_start
                    window_start += (s[window_start:window_end].index(s[window_end]) + 1)
                    for c in s[old_window_start:window_start]:
                        bitmap[ord(c)] = False
                else:
                    bitmap[index] = True
                bitmap[index] = True
                max_length = max(max_length, window_end - window_start + 1)
            return max_length
