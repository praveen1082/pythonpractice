import math
annual_requirement = input("please insert annual requirement / consumption / usage: ")
order_cost = input("please insert order cost per unit: ")
cost_per_unit = input("please insert cost per unit: ")
percent_of_carry_cost = input("please insert percentage of order cost per unit(like 10,20): ")
def carrycostcalc(costperunit,percent):
    return (costperunit/100)*percent
def eoqcalculator(annualrequirement,ordercost,costperunit,percentofcarrycost):
    print("---------------------------Calculating the value of carrying cost-------------------------------")
    carrycost = carrycostcalc(costperunit,percentofcarrycost)
    print("---------------------------Carrying cost (c) = Rs."+str(carrycost)+"------------------------------")
    print("---------------------------Calculating the value of EOQ-------------------------------")
    eoq = math.sqrt((2*annualrequirement*ordercost)/carrycost)
    print("---------------------------Economic Order Quantity (EOQ) = " + str(round(eoq)) + "------------------------------")
def annual_requirement_calculator_from_eoq(eoq,ordercost,costperunit,percentofcarrycost):
    carrycost = carrycostcalc(costperunit,percentofcarrycost)
    leftsidevalue = ((eoq ** 2)/carrycost)
    rightsidevalue = (2*ordercost)
    annualrequirement = leftsidevalue / rightsidevalue
    print(">>>>>>>>>------------------Annual requirement: "+str(round(annualrequirement))+"---------------------------------<<<<<<<<<<<<<<<<")

def annual_requirement_calc_from_total_cost_at_eoq(totalcost,ordercost,costperunit,percent):
    carrycost = carrycostcalc(costperunit,percent)
    leftsidevalue = totalcost ** 2
    rightsidevalue = 2*ordercost*carrycost
    annualrequirement = leftsidevalue / rightsidevalue
    print("_______________________Annual Requirement: "+str(round(annualrequirement))+"_______________________")
    pass
if not annual_requirement and not order_cost and not cost_per_unit and not percent_of_carry_cost:
    print("**********************************************************************************************************************")
    print("*****************-----------------------------Assigning default value to all-----------------------------*************")
    print("***********************************************************************************************************************")
    print("---------------------------Annual Requirements: 100000 units------------------------------")
    print("---------------------------Order cost (o): Rs. 100-------------------------------------------------")
    print("---------------------------Cost per unit: Rs. 1")
    print("----------------------------percent of carry cost: 10%-------------------------------------------")
    eoqcalculator(100000,100,1,10)
elif annual_requirement and order_cost and cost_per_unit and percent_of_carry_cost:
    eoqcalculator(float(annual_requirement),float(order_cost),float(cost_per_unit),float(percent_of_carry_cost))
elif not annual_requirement and order_cost and cost_per_unit and percent_of_carry_cost:
    choice = int(input("press 1 for EOQ and press 2 for Total cost at EOQ: "))
    if choice == 1:
        eoq = float(input("Insert EOQ: "))
        if not eoq:
            print("_______________________Assigning default value to EOQ 5000 units________________________________________")
            eoq: 5000
        annual_requirement_calculator_from_eoq(eoq,float(order_cost),float(cost_per_unit),float(percent_of_carry_cost))
    else:
        totalcostateoq = float(input("Insert Total cost at EOQ:"))
        annual_requirement_calc_from_total_cost_at_eoq(totalcostateoq,float(order_cost),float(cost_per_unit),float(percent_of_carry_cost))
