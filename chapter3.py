## List and Tuples

# marks1 = 90.0
# marks2 = 84.5
# marks3 = 60.3
# marks4 = 99.5
# marks5 = 97.5

marks = [90.0, 84.5, 60.3, 99.5, 97.5]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[3])

student = [
    "name:" "Akshay",
    "Sem:" "7th sem",
    "CGPA:" "7.0"
]
print(student)

# List -> Mutable
student = ["Karan", 7.0 , 21, "Mangaluru"]
print(student[0])
student[0] = "Akshay"
print(student)


#list slicing
marks = [87,90,64,86,88]
print(marks[1:5])
print(marks[-3:])

#list Method -> Mutable -> Can change

# list = [2,1,3]
list = ["banana", "apple", "mango", "litchi"]
#append
# list.append(4)
# print(list)

#sorting
list.sort()
print(list)

list.sort(reverse = True)
print(list)

list.reverse()
print(list)

list.insert(1,"jackfruit")
print(list)

list.remove("jackfruit")
print(list)

list.pop(2)
print(list)

#tuple - Immutable -> Cannot Change

tuple = ("banana", "apple", "mango", "litchi")
print(tuple[0])
print(tuple[1])

tup = ()
print(tup)
print(type(tup))

print(tuple.index("apple"))
print(tuple.count("mango"))


#WAP to ask the user to enter names of their favorite movies & store them in a list
movies = []
movie1 = input("Enter a 1st Movie: ")
movie2 = input("Enter a 2nd Movie: ")
movie3 = input("Enter a 3rd Movie: ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

#WAP to check a list contains a palindrome of elements
list1 = [1, 2, 3, 2, 1]

if list1 == list1[::-1]:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")