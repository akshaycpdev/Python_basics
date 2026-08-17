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