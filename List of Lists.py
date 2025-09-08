import pandas as pd

my_list = []

# List of Lists 
fruits = ["apple", "banana", "cherry", "watermelon", "dragonfruit", "grape"]
cars = ["BMW", "Mazda", "Peugeot", "Yamaha", "Honda", "Lamborghini"]
numbers = ["3", "6", "9", "12", "15", "18"]
books = ["The Great Gatsby", "1984", "To Kill a Mockingbird", "Pride and Prejudice", "The Catcher in the Rye", "Game of Thrones"]

choosen_book = (books [3], books[1])
print (choosen_book)

choosen_fruits = (fruits[1], fruits[3], fruits[5])
print (choosen_fruits)

choosen_cars = (cars[1], cars [2])
print(choosen_cars)
# ======= 3 ==========
df1 = pd.DataFrame({
    'Cars' : cars, 
    'Numbers' : numbers,
})

df2 = pd.DataFrame({
    'Fruits' : fruits, 
    'Books' : books
})

df3 = pd.DataFrame({
    'Fruits' : fruits, 
    'Cars' : cars,
    'Numbers' : numbers,
    'Books' : books
})

print(df3.iloc[0,3])

groceries = ["Apples", "Bread", "Carrots", "Detergent", "Eggs", "Fish", "Grapes", "Honey"]
groceries.append("Mayonnaise")
groceries.remove("Fish")
groceries.insert(2, "Ice Cream")

print (groceries)
# ======= 4 ==========
groceries2 = ["Apples", "Bread", "Carrots", "Detergent", "Eggs", "Fish", "Grapes", "Honey", "Cauliflower", "Ice Cream"]
groceries2.sort()

print(groceries2)   

groceries2.reverse()

print(groceries2)

def split_into_bags(items, bag_size=4):
    bags = []
    for i in range(0, len(items), bag_size):
        bags.append(items[i:i+bag_size])
    return bags

bags = split_into_bags(groceries2)

print("Each Bags:", bags)
print (bags)
print (f"Number of bags: {len(bags)}")
