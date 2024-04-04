def longestCommonPrefix(strs):

    a = 0
    string = ""
    length = len(strs)

    if len(strs)==0:
        return string
    
    if len(strs)==1:
        return strs[0]

    for i in strs:
        if len(i)==0:
            return string

    length -= 1

    while length >= 1:
        if (strs[length][a] == strs[length-1][a]) and (length == 1):
            string = string + str(strs[length][a])
            length = len(strs)-1
            if len(min(strs, key=len)) > a+1:
                a+=1 
            else: 
                return(string)
        elif (strs[length][a] == strs[length-1][a]) and (length != 1): 
            length = length-1
        else:
           return string

strs = ["aa","aa"]
longestCommonPrefix(strs)
strs = ["flower","flow","flight"]
longestCommonPrefix(strs)
