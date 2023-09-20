def linear_search_product(product_list, target_product):
    indices = []
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    return indices
products = ["Jackfruit", "Rambootan", "Cherry", "Papaya", "Grapes"]
target = "Cherry"
result = linear_search_product(products, target)
print('The Result is',result)
#print(result)  # Output: [0, 2, 4]