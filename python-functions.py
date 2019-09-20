# Practice: Activities for Kids
def run(name):
    print(f"{name} ran like the wind!")

run("Jay")

def swing(name):
    print(f"{name} swings like a failing marriage!")

swing("Holmes")

def slide(name):
    print(f"{name} slides like a senior!")

slide("Mary")

def hide_seek(name):
    print(f"{name} hides like a cat!")

hide_seek("Lucy")



# Practice: Chicken Monkey
def chicken():
    for i in range(1, 101):
        if i%5 == 0 and i%7 ==0:
            print("ChickenMonkey")
        elif i%5 == 0:
            print("Chicken")
        elif i%7 == 0:
            print("Monkey")
        else:
            print(i)

chicken()

for i in range(1,101):
    output = ""
    if (i % 5 == 0):
        output = f'{output} Chicken'
    if (i % 7 == 0):
        output = f'{output} Monkey'

    print(output if output != "" else i)

# Challenge: Coin to Cash
def calc_cash():

    total_dollars = 0

    piggy_bank = {
        "quarters": 21,
        "dimes": 67,
        "nickels": 46,
        "pennies": 623
    }

    for key, value in piggy_bank.items():
        if key == "quarters":
            total_dollars += (value * .25)
        if key == "dimes":
            total_dollars += (value * .1)
        if key == "nickels":
            total_dollars += (value * .05)
        if key == "pennies":
            total_dollars += (value)

    print("$$$:", total_dollars)

calc_cash()

# Challenge: Cash to Coins

dollar_amount = 24.23

piggy_bank = {
    "quarters": 0,
    "dimes": 0,
    "nickels": 0,
    "pennies": 0
    }

def calc_coins(amount):

    quarters = amount // .25
    piggy_bank["quarters"] = quarters
    diff = amount - (quarters * .25)

    dimes = diff // .1
    piggy_bank["dimes"] = dimes
    diff = diff - (dimes * .1)

    nickels = diff // .05
    piggy_bank["nickels"] = nickels
    diff = diff - (nickels * .05)

    pennies = diff // .01
    piggy_bank["pennies"] = pennies
    diff = diff - (pennies * .01)

    print(piggy_bank)

calc_coins(dollar_amount)











