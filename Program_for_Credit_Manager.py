"""
This is the program for credit card manager.
Author: Gurleen Kaur
Date: 01-08-2021
"""

transactions = []
months = {
    0: "January",
    1: "February",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "December"
}


def welcome():
    welcome_msg = {
        1: "Enter the fixed amount(to be paid every month)",
        2: "Enter the transaction amount",
        3: "Make a payment",
        4: "Transaction History",
        5: "QUIT"
    }
    print("\nWelcome to CredManager")
    print("~" * 30)
    print("Enter your choice")
    for key in welcome_msg.keys():
        print("[{}]:{}".format(key, welcome_msg[key]))
    print("~" * 30)


def fixed_amount(amount):
    print(f"We have set a fixed amount of \u20b9{amount}")


def transaction_amount(expense):
    print(f"Made a transaction of \u20b9{expense}")
    transactions.append(expense)


def make_payment(fixed_amt):
    payment = 0
    for transaction in transactions:
        payment = payment + transaction
    print(f"Total amount transacted:\u20b9{payment}")
    pay = 0.10 * payment + payment
    print(f"You have to pay \u20b9{pay}")
    amt = pay
    # By default=> start from JAN
    month = 0  # start from next month
    while amt > 0:
        amt = amt - fixed_amt
        month += 1

    print("The amount would be paid till", months.get(month % 12))
    print("Total months:", month)


def transaction_history():
    idx = 0
    print("-" * 20)
    for transaction in transactions:
        idx += 1
        print(f"[{idx}]:\u20b9{transaction}")
    print("-" * 20)


def enter_choice():
    while True:
        choice = int(input("\nEnter your choice:"))
        if choice == 1:
            amount = int(input("Enter the fixed amount(to be paid every month):"))
            fixed_amount(amount)
        elif choice == 2:
            expense = int(input("Enter the transaction amount:"))
            transaction_amount(expense)
        elif choice == 3:
            make_payment(amount)
        elif choice == 4:
            print("Transaction History")
            transaction_history()
        elif choice == 5:
            break
        else:
            print("Enter a valid choice!")


def main():
    welcome()
    enter_choice()


if __name__ == '__main__':
    main()
