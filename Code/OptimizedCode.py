from abc import ABC, abstractmethod

output = list()

""" The solution class is an abstract class """


class Solution(ABC):
    global output
    """ The following method populates the output - list with the result"""

    def suggested_products(self, products, searchWord):
        products.sort()
        for i in range(len(searchWord)):
            word = searchWord[:i + 1]
            products = [product for product in products if product.startswith(word)]
            output.append(products)
        return output

    """ The following is an abstract method which can be used by implementing methods with the logic of 
    displaying the output list"""

    @abstractmethod
    def display(self, op_list):
        pass


class SizedDisplay(Solution):
    """ The display method below displays the lists having the count of elements less than or equal to
    resultSize"""

    def display(self, op_list, resultSize):
        for i in output:
            print(i[:resultSize])


class AlternateDisplay(Solution):
    "The display method below displays the alternate elements in the output list starting from the first element"

    def display(self, op_list):
        for i in range(len(op_list)):
            if i % 2 == 0:
                print(op_list[i])


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
        print(final_op)


# Initializing products and searchWord variables
product_list = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
search_string = "mouse"
size = int(input("Enter the atmost size that you want in the result"))

print("Displaying the lists with specified atmost size", size)
SizedDisplay_obj = SizedDisplay()
resultant_list = SizedDisplay_obj.suggested_products(product_list, search_string)
SizedDisplay_obj.display(resultant_list, size)
print("--------------")
print("Displaying alternate elements in the list")
AlternateDisplay_obj = AlternateDisplay()
resultant_list = AlternateDisplay_obj.suggested_products(product_list, search_string)
AlternateDisplay_obj.display(resultant_list)
print("------------------------------------")
print("Displaying the result with maximum number of elements")
MaxDisplay_obj = MaxDisplay()
resultant_list = MaxDisplay_obj.suggested_products(product_list, search_string)
MaxDisplay_obj.display(resultant_list)
print("-----------------------------")
