from Code.OptimizedCode import suggestedProducts
import random


def test_suggestedProducts():
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    resultSize = 3
    # Considering a test case and asserting for its correctness
    output = suggestedProducts(products, searchWord, resultSize)
    assert output == [['mobile', 'moneypot', 'monitor'], ['mobile', 'moneypot', 'monitor'],
                      ['mouse', 'mousepad'], ['mouse', 'mousepad'], ['mouse', 'mousepad']]
    # Testing the size
    k = list()  # this list contains the length of the lists in the output list
    for i in range(len(output)):
        k.append(len(output[i]))
    # Check whether the result contains at least one element with the length = resultSize
    assert max(k) == resultSize
    # Checking the datatype of the output
    assert type(output) is list
