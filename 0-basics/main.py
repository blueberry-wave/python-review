# python basics

# Hello world
print("Hello World!")

# cli input
prompt = "\n   > "
name = input(f"What is your name?{prompt}")

print(f"Well, hello there handsome.")

# mathetmatical operations and casting
x1 = 5
x2 = 7
x3 = x1 + x2

x4 = input(f"Enter an integer value for x4:{prompt}")
x5 = input(f"Enter an integer value for x5:{prompt}")

print(f"The sum of x4 and x5 is {x4 + x5}")
print(f"Remember, all cli inputs are strings in Python!")
print(f"Let's try casting these inputs to integers.")

x6 = int(input(f"Enter an integer value for x6:{prompt}"))
x7 = int(input(f"Enter an integer value for x7:{prompt}"))

print(f"The sum of x6 and x7 is {x6 + x7}. That looks about right!")
