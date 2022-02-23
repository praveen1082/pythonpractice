numbers = input("Insert Phone Numbers: ")
customer_dictionary = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six"}
output = ""
for ch in numbers:
    output +=customer_dictionary.get(ch, "!") + " "
print(output)