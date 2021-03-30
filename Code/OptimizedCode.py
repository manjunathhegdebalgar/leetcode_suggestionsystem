from abc import ABC, abstractmethod


def suggested_products(products, searchWord):
    output = list()
    products.sort()
    for i in range(len(searchWord)):
        word = searchWord[: i + 1]
        products = [product for product in products if product.startswith(word)]
        output.append(products)
    return output


class Solution(ABC):
    """The following is an abstract method which can be used by implementing methods with the logic of
    displaying the output list"""

    @abstractmethod
    def display(self, op_list):
        pass


class SizedDisplay(Solution):
    """The display method below displays the lists having the count of elements less than or equal to
    resultSize"""

    def display(self, op_list, resultSize):
        final_list = list()
        for i in op_list:
            final_list.append(i[:resultSize])
        return final_list


class AlternateDisplay(Solution):
    """The display method below displays the alternate elements in the output list starting from the first element
    as of now it is considered as the elements with even indices"""

    def display(self, op_list):
        list_with_alternate = list()
        for i in range(len(op_list)):
            if i % 2 == 0:
                list_with_alternate.append(op_list[i])
        return list_with_alternate


class MaxDisplay(Solution):
    """ The display method below displays the list in the output list having maximum number of elements"""

    def display(self, op_list):
        max_count = 0
        for i in range(len(op_list)):
            temp_ct = len(op_list[i])
            if temp_ct > max_count:
                final_op = list()
                final_op.append(op_list[i])
                max_count = temp_ct
        return final_op


# Initializing products and searchWord variables
product_list = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
search_string = "mouse"
size = 3

print("Displaying the lists with specified atmost size", size)
SizedDisplay_obj = SizedDisplay()
resultant_list = suggested_products(product_list, search_string)
print(SizedDisplay_obj.display(resultant_list, size))

print("--------------")

print("Displaying alternate elements in the list")
AlternateDisplay_obj = AlternateDisplay()
resultant_list = suggested_products(product_list, search_string)
print(AlternateDisplay_obj.display(resultant_list))

print("------------------------------------")

print("Displaying the result with maximum number of elements")
MaxDisplay_obj = MaxDisplay()
resultant_list = suggested_products(product_list, search_string)
print(MaxDisplay_obj.display(resultant_list))
print("-----------------------------")
