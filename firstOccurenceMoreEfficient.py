class Solution(object):
    def strStr(haystack, needle):
        index = 0
        match = 0
        while index < len(haystack):
            if len(needle) > len(haystack):
                return -1
        
            if haystack[index] == needle[match]:
                match += 1
                if match == len(needle):
                    print(index-len(needle) + 1)
                    return index-len(needle) + 1
            elif haystack[index] != needle[match] and match != 0:
                index = index-match
                match = 0
            else:
                match = 0
            index +=1

        print(-1)
        return -1


haystack = "mississippi"
# if it doesn't match, go back len(needle -1 places) and try again
# use a while loop
needle = "pi"

Solution.strStr(haystack, needle)