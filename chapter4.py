## Dictionary and Sets

dict = {
    "name": "Akshay",
    "Subjects": ["C Program", "Python", "Java", "ADA", "DSA"],
    "Marks": [90, 98, 85, 94, 75],
    "CGPA": 9.32,
}

print(dict)
print(dict["name"])
print(dict["Marks"])
print(dict["CGPA"])


null_dict = {}
null_dict['name'] = "Xyz"
print(null_dict)
print(type(null_dict))


## Nested Dictionary

student = {
    "name": "Akshay",
    "score" : {
        "Maths": 93,
        "Physics": 90,
        "Chemistry": 96
    }
}
print(student)
print(student["score"]["Physics"])



## Dictionary Methods
# .keys(): Returns all keys
# .values(): Returns all values
# .items(): Returns key-value pairs
# .get("key"): Returns value for that key
# .update(newDict): Adds new key-value pairs


print(student.keys())
print(list(student.keys()))
print(student.values())
print(student.items())
print(student.get("score"))

print(student.update({"city":"Mangaluru"})) 
# new_dict = {"city": "delhi"} 
# student.update(new_dict)
 
print(student)




## Sets

collection = {1,2,3,4, "Hello", "Hello", "world"}
print(collection)
print(type(collection))
print(len(collection))

#empty set

null_set = set() # empty set; syntax
print(type(null_set))

null_set.add(1)
null_set.add(2)
null_set.add(2)
print(null_set)
null_set.remove(2)
print(null_set)
null_set.add("Akshay")
print(null_set)
null_set.clear()
print(null_set)
print(collection.pop())
print(collection.pop())

# Set Methods

# set.add(el): Inserts a new element into the set.
# set.remove(el): Deletes a specific element; raises a KeyError if the element does not exist.
# set.clear(): Removes all elements, leaving the set completely empty.
# set.pop(): Removes and returns an arbitrary (random) element from the set.

# Sets is Muttable but 
# Sets in a Element is Immutable


#Key Concepts

# Set 1: Contains elements {1, 2, 3}.
# Set 2: Contains elements {3, 4, 5}.

# Overlap: Element 3 is shared between both.
# Python Set Methods 

# set.union(set2)Combines all unique values from both sets.Removes duplicate entries automatically.
# Code output: {1, 2, 3, 4, 5}.

# set.intersection(set2)
# Finds only the shared, common values.
# Ignores elements unique to one set.
# Code output: {3}.

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}

print(set_1.union(set_2))
print(set_1.intersection(set_2))



# Practice

dictionary = {
    "cat" : "a small animal",
    "table" : [
        "a piece of furniture", 
        "list of facts and furniture"
    ]
}
print(dictionary)


#

set = {"Python","Java","C++","Python","Javascript","Java","Python","Java","C++","C"}
print(set)
print(len(set))


#

marks = {}

x = int(input("Enter Physics: "))
marks.update({"physics": x})

y = int(input("Enter Chemistry: "))
marks.update({"Chemistry": y})

z = int(input("Enter Mathematics: "))
marks.update({"Mathematics": z})

print(marks)
