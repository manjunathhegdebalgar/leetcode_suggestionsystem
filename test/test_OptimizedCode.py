import random
from Code.OptimizedCode import *

""" The following method tests  the correctness of the logic"""
products_list = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
output = suggested_products(products_list, searchWord)

""" Following method tests the logic of the code"""


def test_suggested_products_method():
    products_list = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    global output
    test_list = list()
    products_list.sort()
    for i in range(len(searchWord)):
        word = searchWord[: i + 1]
        products_list = [
            product for product in products_list if product.startswith(word)
        ]
        test_list.append(products_list)
    assert test_list == output


"""" Tests for the correctness of display method in the class SizedDisplay"""


def test_sized_display():
    SizedDisplay_obj = SizedDisplay()
    global output
    result_size = random.randint(1, 4)
    test_list = SizedDisplay_obj.display(output, result_size)
    # if the length of any list is greater than the result_size then the code isn't working fine
    for i in test_list:
        if len(i) > result_size:
            assert False
        else:
            assert True


def test_alternate_display():
    global output
    AlternateDisplay_obj = AlternateDisplay()
    test_list = AlternateDisplay_obj.display(output)
    # Printing alternate elements will leave us with the number of elements equal to half or 1 more than half
    if len(test_list) > (len(output) + 1) / 2:
        assert False
    else:
        assert True


""" Following code tests the correctness of display method of MaxDisplay class"""


def test_max_display():
    global output
    MaxDisplay_obj = MaxDisplay()
    test_list = MaxDisplay_obj.display(output)
    # The returned list contains only one element
    max_element_length = len(test_list[0])
    max_count = 0
    for i in range(len(output)):
        temp_ct = len(output[i])
        if temp_ct > max_count:
            final_op = list()
            final_op.append(output[i])
            max_count = temp_ct
    if max_count == max_element_length:
        assert True
    else:
        assert False
