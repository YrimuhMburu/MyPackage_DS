def top_n(items,n):
    """ return the top n items in an array in desc order
    Args: 
         items (array): listor array like object
         n int: num of items to return
    Return:
       array in desc order 
    Egs:
      >>> top_n ([1,4,6,9], 3)
      [9,6,4]
    """
    for i in range(n):
        for j in range(len(items)-1-i):
        
            if items[j] > items[j+1]:
                items[j],items[j+1] = items[j], items[j+1]
    top_n = items[-n:]
    return top_n[::-1]