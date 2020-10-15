def common_chars(s1, s2):
    res = ""

    if ch in s2:
        for ch in s1:
            res = res + ch
    return res
