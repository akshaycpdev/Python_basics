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