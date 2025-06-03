
def want_continue():
    while True:
        answer = input("Do you want to try a different calculation? (yes/no)").lower()
        if answer == "yes" or answer == "y":
            return True
        if answer == "no" or answer == "n":
            return False
        else:
            print("Answer with yes or no only.")





def intrest():
    while True:
        start = int(input("What is your starting balance"))
        increase = int(input("What % increase will u have"))
        time = int(input("For how long will u invest?"))

        total = start * (increase / 100 + 1) ** time
        print(
            f"If you invest ${start}, you will have ${int(total)} after {time} years with a yearly interest rate of {increase}%.")

        if not want_continue():
            print("Goodbye")
            break


intrest()