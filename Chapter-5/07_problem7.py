d = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})


print(d)

# The values entered later will be updated
# OUTPUT
# Enter friends name: A
# Enter Language name: B
# Enter friends name: C
# Enter Language name: D
# Enter friends name: E
# Enter Language name: F
# Enter friends name: E
# Enter Language name: G
# {'A': 'B', 'C': 'D', 'E': 'G'}