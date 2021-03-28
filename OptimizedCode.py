def suggestedProducts( products, searchWord, resultSize):
    output = list()
    products.sort()
    for i in range(len(searchWord)):
        word = searchWord[:i + 1]
        products = [product for product in products if product.startswith(word)]
        output.append(products[:resultSize])
    return output

resultSize = int(input("Enter the number of results that you want"))
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
print(suggestedProducts(products, searchWord, resultSize))