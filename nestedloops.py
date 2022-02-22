for x in range(4):
    for y in range(3):
        print(f"({x},{y})")
#exercise : using nested loops print the following
"""
XXXXX
XX
XXXXX
XX
XX

"""
numbers = [1, 1, 1, 1, 5]
for x in numbers:
    output = ''
    for count in range(x):
        output += 'x'
    print(output)
