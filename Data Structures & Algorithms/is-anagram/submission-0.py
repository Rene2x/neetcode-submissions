class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # compare length of both strings since they must match to be an anagram
        if len(s) != len(t):
            # if they dont match, return false since can't be anagram
            return False
        # If same length strings, sort and compare strings. Will provide same output if anagram.
        return sorted(s) == sorted(t)