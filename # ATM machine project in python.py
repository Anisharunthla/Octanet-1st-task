# ATM machine project in python 

print("Welcome to ABC bank \n\n Please insert your card")

password=2345
balance=12000

choice=0

pin=int(input("Enter your 4 digit pin number: 2345"))
if(password==pin):
    while(choice != 4):
     print("1==balance")
     print("2==withdrawal")
     print("3==deposite")
     print("4==cancel\n")
     print("Correct pin number")

     choice=int(input("\n Enter your option: "))
     if(choice==1):
          print(" Balance is: Rs",balance)

     elif(choice==3):
          deposite=int(input("Enter your deposite: Rs"))
          balance += deposite
          print("\n Deposited amount = Rs",deposite)
          print(" Total amount = Rs",balance)


     elif(choice==2):
          withdrawal = int(input("Enter the amount to withdraw: Rs", withdrawal))
          balance -= withdrawal
          print("\n Withdraw amount = Rs",withdrawal)
          print("Total amount = Rs", balance)

     elif(choice==4):
          print("\nSession ended")
else:
    print("Incorrect pin number!! Please try again.....")

