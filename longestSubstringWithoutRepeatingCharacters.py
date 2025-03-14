class Solution(object):
    def lengthOfLongestSubstring(s):
        index = 0
        unique = 0
        maxUnique = 0
        list = []
        length = len(s)

        while index < length:
            if s[index] not in list: # if there are no duplicates
                list.append(s[index])
                unique += 1
                if unique > maxUnique:
                    maxUnique = unique
            else:
                list.clear()
                index = index - unique
                unique = 0
            index +=1
        
        return maxUnique

Solution.lengthOfLongestSubstring("pwwkew")
        