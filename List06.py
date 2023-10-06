def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    a=0
    while a<5:
        if list1[a]==1:
            list1[a]=True
        a+=1
    return list1
print(main([1,0,0,0,0]))
print(main(list1=[1, 0, 1, 1, 0]))