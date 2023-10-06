def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    a=0
    while a<len(list1):
        if list1[a]==1:
            list1[a]=True
        if list1[a]==0:
            list1[a]=False
        a+=1
    return list1
print(main(list1=[1, 0, 1, 1, 0]))