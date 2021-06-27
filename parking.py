# Some reason the x = 1 only works here -\_(^-^)_/-
x = 1


class Garage:
    def __init__(self):
        self.ticket = 10

    # Was unsure if anything else needed to come in here but everything
    # functions as it should thus far.

    def Enter(self):
        if self.ticket <= 0:
            print('Garage is full try again later')
        else:
            self.ticket = self.ticket-1
            self.show()

    def Quit(self):
        self.show()
        print('EXITING..')

#Condensed the rest of exit into pay to make Pay and Exit. 

    def Pay(self):
        ticketnum = input
        if self.ticket >= 10:
            print('Garage Is Empty')
        if self.ticket == 0:
            print("You haven't purchased a ticket yet!")

        ask = input("What's your ticket number?\n")
        payment = input("You're stay has cost you $10 please pay now. ")
        if payment == '$10' or 10:
            self.ticket = self.ticket+1
            self.show()
            print('\nPlease have a nice day and drive safe.')
        else:

            print('That was not the correct amount')
        self.show()

#idea append and pop to add and remove numbers. need to make pay method confinded to 1-10
    def run():
        garage_tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        garage_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        garage = Garage(garage_tickets, garage_spaces)

#added self.show to all areas that had the below print statements just to clean things up a smidge.

    def show(self):
        print('Spaces Left: ' + str(self.ticket))
        print('Ticket Left: ' + str(self.ticket))


# Easier way to call to the class.

park = Garage()


# The one class makes things simple to code
# Below is the driver code. each if/elif calls to each method above.
# Learned from rewatching week_2 day 5 around 20mins in.

while (x == 1):
    start = input("\nWelcome to Parking Lot, press 'Enter' to continue")
    if start == "":

        choice = input("Would you like to do? Enter/Pay and Exit/Show or Quit: ")

        if choice == 'enter':
            park.Enter()

    #Condensed the rest of exit into pay to make Pay and Exit. 

        elif choice == 'exit':
            park.Pay()

        elif choice == 'pay':
            park.Pay()

        elif choice == 'quit':
            park.Quit()
            break

        elif choice == 'show':
            park.show()

        else:
            print("Wrong input, select Enter/Pay and Exit/Show or Quit: ")
