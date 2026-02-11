#Task 1: The Product Catalog (Series Creation & Indexing)
import pandas as pd
products = pd.Series([700, 150, 300], index=['Laptop', 'Mouse', 'Keyboard'])
print(products)
print("The Laptop Prize is:", products['Laptop'])
print(products[0:3])