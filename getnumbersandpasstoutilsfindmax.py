import utils

try:
    numbers = input("Please insert numbers ---> I will find the greatest among them: ")
    string_array_of_numbers = numbers.split(' ')
    int_array_of_numbers =[]
    print(string_array_of_numbers)
    for numbers in string_array_of_numbers:
        int_array_of_numbers.append(int(numbers))
    print(int_array_of_numbers)
    print("------------calling a method from another file and finding the greatest one---------------------------------")
    greatest = utils.find_max(int_array_of_numbers)
    print(f"The greatest number among the numbers you have inserted is: {greatest}")
except ValueError:
    print("please insert numbers only")



