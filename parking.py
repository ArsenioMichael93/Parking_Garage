#Some reason the x = 1 only works here -\_(^-^)_/-
x = 1

class Garage:
    def __init__(self):
        self.ticket = 10
    #Was unsure if anything else needed to come in here but everything
    #functions as it should thus far.

    def Enter(self):
        if self.ticket <= 0:
            print('Garage is full try again later')

        else:
            self.ticket = self.ticket-1
            print('Spaces Left: ' + str(self.ticket))

    def Exit(self):
        if self.ticket >= 10:
            print('Garage Is Empty')

        else:
            payment = input("You're stay has cost you $10 please pay now. ")
            if payment == '$10':
                self.ticket = self.ticket+1
                print('Spaces Left: ' + str(self.ticket))
                print('\nPlease have a nice day and drive safe.')
            else:
                print('That was not the correct amount')

    def Quit(self):
        print('Spaces Left: ' + str(self.ticket))
        print('EXITING..')



#Easier way to call to the class.
park = Garage()


#The one class makes things simple to code
#Below is the driver code. each if/elif calls to each method above.
#Learned from rewatching week_2 day 5 around 20mins in. 

while (x == 1):
    choice = input("Would you like to do? Enter/Exit or Quit: ")

    if choice == 'enter':
        park.Enter()

    elif choice == 'exit':
        park.Exit()

    elif choice == 'quit':
        park.Quit()
        break

    else:
        print("Wrong input, select Enter/Exit or Quit: ")
