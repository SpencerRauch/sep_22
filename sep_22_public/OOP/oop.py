#OOP
#OBJECTS - things, items, they can do things, they have properties / attributes that describe
# emphasizes grouping data and functionality together in entities known as Objects


cat1_data = {
    'name': 'Scar',
    'color': 'dark brown',
    'age': 3,
    'breed': 'lion'
}

cat2_data = {
    'name': 'Garfield',
    'color': 'orange/striped',
    'age': 30,
    'breed': 'lasagna'
}

class Cat():
    all_cats = []
    def __init__(self, cat_data):
        self.name = cat_data['name']
        self.color = cat_data['color']
        self.age = cat_data['age']
        self.breed = cat_data['breed']
        Cat.all_cats.append(self)

    def __repr__(self):
        return f"Name: {self.name} color: {self.color} age: {self.age} breed: {self.breed}"

    def print_info(self):
        print(f"Name: {self.name} color: {self.color} age: {self.age} breed: {self.breed}")
        return self

    def meow(self):
        print(f"{self.name} lets out a cry: MEOOWWW")
        return self


cat1 = Cat(cat1_data)
cat2 = Cat(cat2_data)
print(cat1)
# print(cat1.name)
# print(cat1.color)

# cat1.meow().meow().meow()

# print(Cat.all_cats)

# cat1.meow()
# cat1.meow()
# cat1.meow()
# cat1.meow()
# cat1.meow()
# cat1.meow()
# for anything in Cat.all_cats:
#     anything.print_info()
