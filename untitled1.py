.-., [02.12.23 22:18]
print("Hello, World!")

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = 5
y = "John"
print(type(x))
print(type(y))

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

Try it Yourself »

x = 200
print(isinstance(x, int))

Try it Yourself »

print(bool("Hello"))
print(bool(15))

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello, World!"
print(a.split(","))

a = " Hello, World! "
print(a.strip())

a = "Hello, World!"
print(a.lower())

b = "Hello, World!"
print(b[-5:-2])

x = 5
y = "John"
print(x, y)

x = 5
y = 10
print(x + y)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = "Python is awesome"
print(x)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

b = "Hello, World!"
print(b[2:])

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("free" in txt)

a = "Hello, World!"
print(len(a))

Try it Yourself »

for x in "banana":
  print(x)

a = "Hello, World!"
print(a[1])

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

Try it Yourself »

import random

print(random.randrange(1, 10))

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

Try it Yourself »

x = 1    # int
y = 2.8  # float
z = 1j   # complex

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

Try it Yourself »

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
