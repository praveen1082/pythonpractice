annual_requirement = input("please insert annual requirement / consumption / usage: ")
order_cost = input("please insert order cost per unit: ")
cost_per_unit = input("please insert cost per unit: ")
percent_of_order_cost = input("please insert percentage of order cost per unit(like 10,20): ")

if annual_requirement is None:
    global user_press
    user_press == input("press 1 for EOQ and 2 for Total cost at EOQ: ")
    if user_press == 1:
        global eoq
        eoq = input("Insert EOQ: ")
    elif user_press == 2:
        global total_cost_eoq
        total_cost_eoq = input("Insert Total cost at EOQ: ")
    else:
        print("*******Either annual requirement / EOQ / Total cost at EOQ should be provided********")
        quit()
else:
    print("----------Calculating Carrying cost per order---------------")
    global carry_cost
    carry_cost = (float(cost_per_unit)/100)*float(percent_of_order_cost)
    print("Carrying cost: "+str(carry_cost))
    print("-----------Calculating EOQ---------------")
    eoq =





