import random
members = ["khusbu", "prawin", "khagendra", "Mosh"]
leader = random.choice(members)
print(leader)
for i in range(3):
    print(random.randint(10, 20))

#mosh exercise
#generate a random values for a dice like (1,2),(1,3),(3.5)

x = random.randint(1, 6)
y = random.randint(1, 6)
data = (x, y)
print(data)