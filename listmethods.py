numbers = [5, 2, 3, 7, 4]
numbers.append(20)
print(numbers)
#numbers.clear()
print(numbers)
numbers.insert(0, 29)
print(numbers)
numbers.remove(7)
numbers.pop()
print(numbers.index(5))
print(numbers)
print(50 in numbers)
numbers.sort()
numbers.reverse()
numbers2 = numbers.copy()
numbers2.append(50)
print(numbers)
print(numbers2)

#write a program to remove the duplicates in a list

numbers3 = [1, 2, 3, 4, 5, 6, 7, 2, 4, 7]
uniques = []
for number in numbers3:
    if number not in uniques:
        uniques.append(number)
print(uniques)