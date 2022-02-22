weight = input("Weight: ")
which = input("k for kilogram and l for pound: ")
if which == 'K' or which == 'k':
    data = float(weight) * 0.45
    print("weight in pounds: "+str(data))
elif which == 'l' or which == "L":
    data = float(weight)/0.45
    print("weight in kilos: " + str(data))
