def FirstReverse(str):
    strlist = list(str)
    strlist.reverse()
    return ''.join(strlist)
print FirstReverse(raw_input())