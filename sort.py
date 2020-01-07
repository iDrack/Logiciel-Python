#!/usr/bin/python3


def basicSort(toSort,dsc):
    """

    """
    n = len(toSort)
    #Sorting in dsc order
    if dsc >= 1:
        for i in range(n-1):
            max = i
            for j in range(i+1, n):
                if toSort[j] > toSort[max]:
                    max = j
            if max != i:
                tmp = toSort[i]
                toSort[i] = toSort[max]
                toSort[max] = tmp
                
    #Sorting in asc order    
    else:
        for i in range(n-1):
            min = i
            for j in range(i+1, n):
                if toSort[j] < toSort[min]:
                    min = j
            if min != i:
                tmp = toSort[i]
                toSort[i] = toSort[min]
                toSort[min] = tmp