#3.1 write a function called linear_search_product that takes the list of products and a target products name as input.the function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found.
def linear_Search_Product(product_list, target_product):
  indices =[]
  for i, product in enumerate(product_list):
    if product ==target_product:
      indices.append(i)
      return indices

# Example usage:
products=[ "apple" , "banana" , "apple" , "orange" , "apple" ]
target ="banana"
result =linear_Search_Product(products, target)
if result:
  print(f"the product '{target}' was found at indices:{result}")
else:
  print(f"the product '{target}' was not found in the list.")
  