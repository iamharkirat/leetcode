haystack = "aaaa"
needle = "aaa"

def strStr(haystack, needle):
    len_hay = len(haystack)
    len_needle = len(needle)

    for i in range(0, len_hay-len_needle+1):
        if needle == haystack[i:(i+len_needle)]:  
            return i
    return -1



pos = strStr(haystack=haystack, needle=needle)
print(pos)

     