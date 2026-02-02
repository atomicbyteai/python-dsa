# Banking program

def show_balance(balance):
    print(f"Your balance is ${balance: .2f}")


def deposit():
    amount = float(input("Enter the amount you want to deposit: "))

    if amount < 0:
        print("Enter a valid amount")
    else:
        return amount


def withdraw(balance):
    amount = float(input("Enter the amount you want to withdraw: "))

    if amount > balance:
        print("Insufficient Balance!")
        return 0
    elif amount < 0:
        print("Amount should be greater than 0")
        return 0
    else:
        return amount


def main():
    balance = float(0)
    is_running = True

    while is_running:
        print("*************************")
        print("-----Banking Program-----")
        print("*************************")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*************************")

        choice = int(input("Enter what you want to do (1-4):"))

        match choice:
            case 1:
                show_balance(balance)
            case 2:
                balance = balance + deposit()
            case 3:
                balance = balance - withdraw(balance)
            case 4:
                is_running = False
            case _:
                print("This is not a valid choice")

    print("Thank you! Have a nice day")


if __name__ == '__main__':
    main()
