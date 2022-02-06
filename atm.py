
class Atm:
     def __init__(self,cardNumber,pin):
          self.cardNumber = cardNumber
          self.pin = pin
     
     def balanceEnquiry(self):
          print("Your balance is: $100")
     
     def cashWidthDrawal(self,amount):
          new_amount = 100-amount
          print("You Widthdrawled: "+ str(amount)+ "your remaining balance is: "+ str(new_amount))
     
def main():
          name = input("Enter your name: ")
          print("Hi, " + name)
          cardNumber = input("Enter your CardNumber: ")
          pin = input("Enter your Pin: ")
          new_user = Atm(cardNumber, pin)

          print("Choose your acivity")
          print("1. Balance Enquiry")
          print("2. cash widthdrawal ")
          activity = int(input("Enter the choice"))

          if (activity == 1):
               new_user.balanceEnquiry()
          elif(activity ==2 ):
               amount = int(input("enter amount: "))
               new_user.cashWidthDrawal(amount)
          else:
               print("Enter valid number")

if __name__ == "__main__":
     main()



