def intro ():
    print('WELCOME TO MY ATM PROGRAM')
    print("YOU HAVE VARIETIES OF OPTIONS TO PICK FROM")
    print('FOR A CUSTOMER, ')
    print('TO WITHDRAW, ENTER A')
    print("TO DEPOSIT, ENTER B")
    print()
    print()
    print("FOR AN AGENT")
    print("TO TRACK WITHDRAW HISTORY, ENTER C")
    print("TO TRACK DEPOSIT HISTORY,  ENTER D")
    print()
    print()


import time
def withdraw():

    drawal_file = open('out.txt', 'a')

    print("\tWelcome to the withdrawal program..")
    name = input("\tYour name: ")
    c_type = input("\tEnter your card type: ")
    c_amt = (input("\tEnter amount: "))
    c_pin = str(input("\tEnter your card pin: "))
    c_len = len(c_pin)
    time.sleep(5)
    if c_len == 4:
        # print()
        # c_pin = str(input("\nEnter a valid a pin: "))

        print()
        print("Your request is being processed")
        time.sleep(5)
        print("Request sent")
        time.sleep(3)
        print("Transaction was successful.")
        time.sleep(3)
    else:
        if c_len != 4:
            print("Invalid pin")
            time.sleep(1)
            print("Transaction unsuccessful ")

        drawal_file.write(name + '\n')
        drawal_file.write(c_type + '\n')
        drawal_file.write(c_amt + "\n")

        print("Thank you for patronizing this program...")

    drawal_file.close()



#withdraw()


def deposit():
    deposit_file = open("depos.txt", 'a')

    bank = input("What bank are you transferring to: ")
    acc = str(input("Enter the recipient account: "))
    a_name = input("Enter recipient name: ")
    amt = input("Enter amount to be transferred: ")
    time.sleep(5)
    print("\tTransaction processed")
    time.sleep(3)
    print("\tRequest sent")
    time.sleep(2)
    print("\tTransaction was successful")
    print("The sum of ", amt, " naira was sent to ", a_name)

    deposit_file.write(bank + "\n")
    deposit_file.write(acc + '\n')
    deposit_file.write(amt + "\n")
    deposit_file.write(a_name + '\n')

    deposit_file.close()

#deposit()



def store_draw():
    drawal_file = open('out.txt', 'r')

    name = drawal_file.readline()
    while name != '':
        c_type = drawal_file.readline()
        c_amt = drawal_file.readline()


        name = name.rstrip("\n")
        c_type = c_type.rstrip("\n")
        c_amt = c_amt.rstrip('\n')


        print('Name: ' , name)
        print("Card type: ", c_type)
        print("Amount: ", c_amt)
        print()
        print()

        name = drawal_file.readline()

    drawal_file.close()





def store_depo():
    deposit_file = open("depos.txt", "r")
    bank = deposit_file.readline()
    while bank != '':
        acc = deposit_file.readline()
        amt = deposit_file.readline()
        a_name = deposit_file.readline()

        bank = bank.rstrip('\n')
        acc = acc.rstrip('\n')
        amt = amt.rstrip('\n')
        a_name = a_name.rstrip("\n")

        #print("Name: ", a_name)
        print("Bank: ", bank)
        print("Account number: ", acc)
        print("Amount: ", amt)
        print("Name : ", a_name)
        print()
        print()

        bank = deposit_file.readline()

    deposit_file.close()


def main ():
    repeat = 'Yes'
    intro()
    while repeat == 'Yes' or repeat == "yes":
        user = input("Enter your option: ")
        if user == "A":
            withdraw()
        elif user == "B":
            deposit()
        elif user == "C":
            store_draw()
        elif user == "D":
            store_depo()

        repeat = input("\nLike to perform more actions, Enter Yes to perform, Anything else stops all operation: ")

main()