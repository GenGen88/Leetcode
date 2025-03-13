class Solution(object):
    def strStr(haystack, needle):
        innerCounter = 0
        innerIndex = 0
        outerIndex = 0
        for h in haystack:
            if len(haystack) - outerIndex == len(needle) -1:
                #print(-1)
                return -1
            for n in needle:
                if n == haystack[innerIndex + outerIndex]:
                    innerCounter +=1
                if innerCounter == len(needle):
                    #print(outerIndex)
                    return outerIndex
                innerIndex += 1
            outerIndex +=1
            innerCounter = 0
            innerIndex = 0

        #print(-1)
        return -1


haystack = "leetcode"
needle = "h"

Solution.strStr(haystack, needle)