import math
annual_requirement = float(input("please insert annual requirement / consumption / usage: "))
order_cost = float(input("please insert order cost per unit: "))
cost_per_unit = float(input("please insert cost per unit: "))
percent_of_order_cost = float(input("please insert percentage of order cost per unit(like 10,20): "))

if annual_requirement is None:
    global user_press
    user_press == int(input("press 1 for EOQ and 2 for Total cost at EOQ: "))
    if user_press == 1:
        global eoq
        eoq = float(input("Insert EOQ: "))
    elif user_press == 2:
        global total_cost_eoq
        total_cost_eoq = float(input("Insert Total cost at EOQ: "))
    else:
        print("*******Either annual requirement / EOQ / Total cost at EOQ should be provided********")
        print("______________________________________________EXITING________________________")
        quit()
else:
    print("----------Calculating Carrying cost per order---------------")
    global carry_cost
    costperunit = 1.0
    if order_cost is None:
        print("setting order cost default to Rs. 100")
        ordercost = float(100)
    else:
        ordercost = float(order_cost)
    if cost_per_unit is not None:
        costperunit = float(cost_per_unit)

    carry_cost = float((float(costperunit)/100.0)*float(percent_of_order_cost))
    print("Carrying cost: "+str(carry_cost))
    print("-----------Calculating EOQ---------------")
    eoq = math.sqrt((2*int(annual_requirement)*int(order_cost))/carry_cost)
    print("value of EOQ is : "+str(eoq)+" units")






