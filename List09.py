def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    c=0
    a=0
    while a<len(list1)-1:
        if list1[a]==list1[a-1]:
            c+=1
        a+=1   
    if len(list1)-1==c:
        return True
    else:return False
print(main(list1=[0, 0, 0, 0, 0]))
print(main(list1=['x', 'x', 'y', 'y', 'z']))