#   ******* Task-1: Data Management using Arrays ******  #
import time
class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f"Product(ID: {self.id}, Name: {self.name}, Price: {self.price}, Category: {self.category})"

class ProductManager:
    def __init__(self):
        self.products = []

    def load_products(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                id, name, price, category = line.strip().split(', ')
                self.products.append(Product(id, name, float(price), category))


#   ******* Task-2: Data Manipulation Operations ******  #
    def insert_product(self, product):
        self.products.append(product)

    def update_product(self, id, new_name=None, new_price=None, new_category=None):
        for product in self.products:
            if product.id == id:
                if new_name is not None:
                    product.name = new_name
                if new_price is not None:
                    product.price = new_price
                if new_category is not None:
                    product.category = new_category
                break

    def delete_product(self, id):
        self.products = [product for product in self.products if product.id != id]

    def display_products(self):
        for product in self.products:
            print(product)

    def search_by_id(self, id):
        for product in self.products:
            if product.id == id:
                return product
        return None

    def search_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def sort_measure_time(self):
        start_time = time.time()
        self.quick_sort(0, len(self.products) - 1)
        end_time = time.time()
        return end_time - start_time


#   ******* Task-3: Sorting Algorithm (Quick Sort) *********  #
    def quick_sort(self, start, end):
        if start >= end:
            return

        pivot_index = self.partition(start, end)
        self.quick_sort(start, pivot_index - 1)
        self.quick_sort(pivot_index + 1, end)

    def partition(self, start, end):
        pivot = self.products[end].price
        partition_index = start

        for i in range(start, end):
            if self.products[i].price < pivot:
                self.products[i], self.products[partition_index] = self.products[partition_index], self.products[i]
                partition_index += 1

        self.products[partition_index], self.products[end] = self.products[end], self.products[partition_index]
        return partition_index


#************ Below code be used by taking off # from each line ********************

manager = ProductManager()
manager.load_products('product_data.txt')
#print("Data imported from the product_data.txt")
#manager.display_products()

search_result = manager.search_by_id("57353")
print("Product searched:", search_result)

#manager.update_product("57353", new_name="Test", new_price=90.90, new_category="Assignment#1")
#print("After Update:")
#manager.display_products()

#Deleting the very first product from the list
#manager.delete_product("57353")
#print("After Deletion:")
#manager.display_products()

#manager.quick_sort(0, len(manager.products) - 1)
#print("After Sorting:")
#manager.display_products()

#new_product = Product("00001", "NewProduct for Testing", 15.99, "Assignment#1")
#manager.insert_product(new_product)
#print("After Insertion:")
#manager.display_products()

# Measure time for sorting already sorted data
#manager.quick_sort(0, len(manager.products) - 1)
#time_sorted = manager.sort_measure_time()
#print("Time taken to already sorted data:", time_sorted)

# Measure time for sorting reverse sorted data
# Reverse the list
#manager.products.reverse()
#time_reverse_sorted = manager.sort_measure_time()
#print("Time take to sort data in reverse order:", time_reverse_sorted)




