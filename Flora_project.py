name = str(input("Enter your name: "))
try:
    age = int(input("Enter your age: "))
except:
    print("Just do it!")
fav_number = int(input("Enter your favorite number: "))
print("My name is",name,",", "I am",age, "years old and my favorite number is",fav_number,".")