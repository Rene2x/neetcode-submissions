class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # determine if the length of strings match
        if len(s) != len(t):
            # if strings dont match, cant be an anagram
            return False
        
        # create new array for strings s and t
        arrayS, arrayT = {}, {}

        # iterate through s and add values to our array
        for i in range(len(s)):
            arrayS[s[i]] = 1 + arrayS.get(s[i], 0) 
            arrayT[t[i]] = 1 + arrayT.get(t[i], 0)
        # arrayS should match arrayT, reveals anagram
        return arrayS == arrayT  
 







        # compare length of both strings since they must match to be an anagram
    #    if len(s) != len(t):
            # if they dont match, return false since can't be anagram
    #        return False
        # If same length strings, sort and compare strings. Will provide same output if anagram.
    #    return sorted(s) == sorted(t)