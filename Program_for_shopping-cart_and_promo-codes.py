"""
This is the program for shopping cart and promo codes
Author: Gurleen Kaur
Date: 25-07-2021
"""
menu={
    "Pasta": {
        "price": 350,
        "delivery": 15
    },
    "Burger": {
        "price": 150,
        "delivery": 12
    },
    "Noodles": {
        "price": 200,
        "delivery": 10
    },
    "Pizza": {
        "price": 500,
        "delivery":13
    },
    "Paneer": {
        "price": 200,
        "delivery": 25
    }
}
print("*"*10,"MENU","*"*10)
print()

for keys in menu:
    print("~" * 20)
    print("{}\n\u20b9{} | {}".format(keys,menu[keys]["price"],menu[keys]["delivery"]))
    print("~" * 20)
    print()

shopping_cart=[]
amount=0
total_time=0

while(True):
    food_item_choice=input("Enter the food item you want or enter No to exit ")
    food_item=food_item_choice.capitalize()

    if food_item=="No":
        break

    if food_item in menu:
        shopping_cart.append(food_item)
        amount+=menu[food_item]["price"]
        total_time+=menu[food_item]["delivery"]

    else:
        print("Sorry! We don't have",food_item,"at this time")

print("Shopping Cart [{}]".format(len(shopping_cart)))
print("Ordered Dishes:")
print("-" * 20)
for items in shopping_cart:
    print("{}\n\u20b9{} | {}".format(items,menu[items]["price"],menu[items]["delivery"]))
    print()
print("-" * 20)

print("The total amount is \u20b9",amount)
print("The total delivery time is",total_time)

print()

promo_codes={
    "WELCOME60": {
        "min":159,
        "discount": 0.60,
        "upto": 100
    },
    "NOCOOKING": {
        "min": 149,
        "discount": 0.50,
        "upto": 100
    },
    "WELCOMEPTM": {
        "min": 159,
        "flat": 75
    },
    "WELCOME": {
        "min": 149,
        "discount": 0.60,
        "upto": 150
    },
    "WELCOME100": {
        "min": 130,
        "flat": 100,
    }
}

print("*"*70)
for promo in promo_codes:
    print("|",promo,"|",end="")

print()
print("*" * 70)

while(1):
    promo_choice= input("Enter the promocode ")

    if promo_choice in promo_codes:
        print("Valid promo code")
        if "discount" in promo_codes[promo_choice]:
            print("We will offer a discount of",(promo_codes[promo_choice]["discount"])*100,"%")
            if amount>=promo_codes[promo_choice]["min"]:
                discount= promo_codes[promo_choice]["discount"]*amount
                if discount>promo_codes[promo_choice]["upto"]:
                    amount-=promo_codes[promo_choice]["upto"]
                else:
                    amount-=discount
                print("Hence, the amount you need to pay is \u20b9", amount)
            else:
                print("Amount is less. You need to pay \u20b9",promo_codes[promo_choice]["min"]-amount,"more for promo code:",promo_choice)

        else:
            print("We will offer flat discount of \u20b9", promo_codes[promo_choice]["flat"])
            if amount>=promo_codes[promo_choice]["min"]:
                amount-=promo_codes[promo_choice]["flat"]
                print("Hence, the amount you need to pay is \u20b9", amount)
            else:
                print("Amount is less. You need to pay \u20b9",promo_codes[promo_choice]["min"]-amount,"more for promo code:",promo_choice)
        break

    else:
        print("Invalid promo code")
        my_choice=input("Do you want to enter the promo code again (Enter Yes) or exit (Enter No) ")
        if my_choice=="No" or my_choice=="no":
            break
