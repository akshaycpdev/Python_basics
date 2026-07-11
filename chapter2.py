## Strings and Conditions


str1 = 'This is a string'
str2 = "Akshay"
str3 = '''Learning Day 2 of Python'''

#escape sequence character
str1 = "Akshay : \t4th year B.E \nAlva's Institute of Engineering and Technology"
print(str1)

#concatenation: adding both the string
str1 = "hello"
str2 = "world"
final = str1+" "+str2
print(final)

#length of string
str1 = 'This is a string'
str2 = "Akshay"
str3 = '''Learning Day 2 of Python'''

print(len(str1))
print(len(str2))
print(len(str3))

#indexing: Hrlps to access character
index = "Learning Day 2 of Python"
ch = index[4]
print(ch)

#slicing:accessing parts of string
index = "Learning Day 2 of Python"
print(index[:3])
print(index[:8])
print(index[0:3])
print(index[1:])
print(index[2:6])
print(index[:-3])
print(index[-5:])
print(index[-1:3])
print(index[4:-3])


#string function
str = '''Learning Day 2 of Python'''
print(str.endswith("er"))
print(str.endswith("on"))
print(str.endswith("of"))
print(str.startswith("of"))
print(str.startswith("Le"))

#capitalization, replace, find, count
str = "i am a coder"
print(str.capitalize())
print(str.replace("i","we").replace("am","are"))
print(str.find("am"))
print(str.count("a"))

#WAP to input user's first name and print its length
name = "Akshay"
print(len(name))

#WAP to find the occurences of $ in a String
str = " I am $$Akshay , $f$rom $ma$ngalor$e"
print(str.count("$"))

#conditional statement
#if
#elif
#else

age = 10
if (age > 18):
    print("Can Vote")
else:
    print("cannot vote")


marks = -33
if (marks<=625 and marks>=525):
    print("Destintion")
elif (marks<=524 and marks>=400):
    print("First class")
elif (marks<=280 and marks>=300):
    print("Second class")
elif (marks<=0 and marks >=199):
    print("Fail")
else:
    print("Error")
print(marks)


#even numbers
num = int(input("Enter a number: "))
if num % 2 ==0:
    print("even")
else:
    print("odd")
    
#greatest of 3 numbers entered by users
a = float(input("Enter first: "))
b = float(input("Enter second: "))
c = float(input("Enter third: "))
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
