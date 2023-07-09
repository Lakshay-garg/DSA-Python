# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word 
# or phrase, typically using all the original letters exactly once.

# For example 
# Input: s = "anagram", t = "nagaram"
# Output: true

def isAnagram(s,t):
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for i in t:
            if i in d and d[i] > 0:
                d[i] -= 1
            else:
                return False
        
        return False if any(d.values()) else True

s = "anagram"
t = "nagaram"
print(isAnagram(s,t))

# Output 
# True

