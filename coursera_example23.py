def both_start_with(s1, s2, prefix):
    '''(str, str, str) -> bool

    Return True if and only if s1 and s2 both start with the letters in prefix.
    '''
    if s1.startswith(prefix) and s2.startswith(prefix):
        return True
    else:
        return False
