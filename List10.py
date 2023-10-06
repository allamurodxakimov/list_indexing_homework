def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    a=0
    ma = list_num[0]
    while a<len(list_num):
        if ma<list_num[a]:
            ma=list_num[a]
        a+=1
    return ma
print(main(list_num=[5, 32, 1, 4, 3]))