def fun(*, mydict=None, outkey=None, inkey=None, f=None):
    """
    Processes a dictionary (1D or 2D) and optionally filters its elements.

    Parameters:
    - mydict (dict): The dictionary to process.
    - outkey (str): Outer key in the dictionary. Default is None.
    - inkey (str, optional): Inner key for 2D dictionaries. Default is None.
    - f (callable, optional): Function to filter elements. Default is None.

    Returns:
    - list or float: The filtered list or its average (depending on implementation).
      Returns None if outkey is None or resulting list is empty.
    """
    if outkey is None:
        print("gare gasaghebi aris None")
        return
    
    lis = mydict[outkey]
    if inkey is not None:
        lis = lis[inkey]
    if f is not None:
        lis = [elem for elem in lis if f(elem)]
        
    if len(lis) == 0:
        print("listsi sigrdze aris 0")
        return
    
    return sum(lis) / len(lis)

def f1(num):
    if num % 10 == 3:
        return True
    return False

test1 = {
    "a": [13, 23, 33, 42, 52],
    "b": [3, 63, 33, 12, 15]
}

test2 = {
    "a": {"b": [1, 2, 3], "c": [4, 5, 6]},
    "d": {"e": [7, 8, 9], "f": [3, 33, 63]}
}

print(f"Average of numbers ending with 3 for key 'a': {fun(mydict=test1, outkey='a', inkey=None, f=f1)}")    

print(f"Average of numbers ending with 3 for outer key 'd' and inner key 'f': {fun(mydict=test2, outkey='d', inkey='f', f=None)}")