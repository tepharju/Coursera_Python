def contains(value, lst):
    """ (object, list of list) -> bool
  
   Return whether value is an element of one of the nested        lists in lst.

   >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
   True
   """

    found = False
   
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            found = (lst[i][j] == value)

    return found
