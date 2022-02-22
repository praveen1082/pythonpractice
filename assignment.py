weight = input("Weight: ")
which = input("k for kilogram and l for pound: ")
if which.upper() == 'K':
    data = float(weight) / 0.45
    print("weight in pounds: "+str(data))
elif which.upper() == "L":
    data = float(weight) * 0.45
    print("weight in kilos: " + str(data))
else:
    print("No data provided by user to what to perform")
