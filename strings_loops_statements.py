# -*- coding: utf-8 -*-
"""strings_loops_statements.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11WbIRe0ZmQ7_fqA4JqCFPTYIWjpxt4pw

**if,else, else if**
"""

name= "Rudra"

if name!= "Shloka":
  print("Okay")
elif name == "Rudra":
    print("Hi"+ name)
else:
  print("name not equal to Shloka")

if name!= "Shloka"and name!= "Rudra":
  print("Okay")
elif name == "Rudra":
    print("Hi "+ name)
else:
  print("name not equal to Shloka")

n = -2

if n>0:
  print("positive")
elif n<0:
  print("negative")
else:
  print("zero")

names= ["Shloka","Ria"]

len(names)

for items in names:
  print(items)

for items in names:
  if items == "Shloka":
    print(items+ " is present")
  elif items =="Ria":
      print(items+ " is present")
  else:
        print("do it yourself")
        break

for items in names:
  if items == "Riya":
    print(items+ " is present")
  elif items =="Rudy":
      print(items+ " is present")
  else:
        print("do it yourself")
        break

for items in names:
  if items == "Ria":
    print(items+ " is present")
    continue
  elif items =="Shloka":
      print(items+ " is present")
      continue
  else:
        print("do it yourself")
        break

numbers= [1,2,3,4,5,6]

sum=0

for number in numbers:
  sum=sum+number

sum

"""**While**"""

age = 0

while age<=18:
  if age==18:
   print("go and vote")
  else:
   print("you are not eligible at the age"+str(age))
  age=age+1

while age<=18:
  if age==18:
   print("go and vote your age is " +str(age))


  age=age+1

age

"go and vote your age is " +str(age)

salutation = f"go and vote your age is {age}"

salutation.format(age=19)

message=f"Hi {name} how are you doing"

message.format(name=name)

message="Hi {} how are you doing"

for item in names:
  print(message.format(item))