from typing import List


def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    out_l = list()
    chars = len(searchWord)
    products = sorted(products)
    for i in range(1,chars+1):
        temp_l = list()
        for j in range(len(products)):
            if products[j].startswith(searchWord[:i]):
                if len(temp_l)>=3:
                    continue
                else:
                    temp_l.append(products[j])
        out_l.append(temp_l)
    return out_l
""" driver code """
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
print(suggestedProducts(products, searchWord))