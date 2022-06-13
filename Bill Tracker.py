#income and bill tracker
#bills
billOne = 90
billTwo = 200
billThree = 100
billFour = 100
billFive = 100
billSix = 100
billSeven = 100
billEight = 100
billNine = 100
billTen = 100

#income
incomeOne = 180
incomeTwo = 1250


#expenses
houseHold = 100
groceries = 200
gas = 100
random = 100

#variables for calculations
myIncome = incomeOne + incomeTwo
myExpenses = houseHold + groceries + gas + random
myBills = billOne + billTwo + billThree + billFour + billFive + billSix + billSeven + billEight + billNine + billTen


moneyLeaving = myExpenses + myBills

#calculation
if moneyLeaving > myIncome:
    print("Bitch, get your shit together because you are failing at adulting.")
elif moneyLeaving == myIncome:
    print("Bitch, you're getting better but are you even an adult?")
else:
    print("Bitch!!! You're killing it! You are forsure an adult!")
