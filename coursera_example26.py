def gather_every_nth(L, n):
    '''(list, int) -> list

    Return a new list containing every n'th element in L, starting at index 0.

    Precondition: n >= 1

    >>> gather_every_nth([0, 1, 2, 3, 4, 5], 3)

    [0, 3]
    >>> gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2)
   ['a', 'c', 'e', 'g', 'i']
   '''

    result = []
    i = 0

    while i < len(L):
        result.append(L[i])
        i = i + n# CODE MISSING HERE
   
    return result
