
def list_divide(num, divide=2):
    divisibleNumbers = []
    for i in num:
        if(i % divide == 0):
            divisibleNumbers.append(i)

    return len(divisibleNumbers)
    """
    The function returns the number of elements in the numbers list that are divisible by 2
    """

class listDivideException:

    def __init__(self):
        raise Exception("Division Error")



def list_divide(num, divide=2):
    divisibleNumbers = []
    for i in num:
        if(i % divide == 0):
            divisibleNumbers.append(i)

    return len(divisibleNumbers)      


def test_list_divide():

    try:
        assert list_divide([1,2,3,4,5]) == 2
        assert list_divide([2,4,6,8,10]) == 5
        assert list_divide([30,54,63,98,100], 10) == 2
        assert list_divide([]) == 0
        assert list_divide([1,2,3,4,5], 1) == 5

    except:
        listDivideException()
    
    test_list_divide()