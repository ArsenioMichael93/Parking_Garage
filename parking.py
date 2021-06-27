# Some reason the x = 1 only works here -\_(^-^)_/-
x = 1


class Garage:
    def __init__(self):

        self.ticket = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.Spaces = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.current = {}

    # Was unsure if anything else needed to come in here but everything
    # functions as it should thus far.

    def Enter(self):

        if self.ticket == []:
            print("Garage is full.")
            return Garage()
        print("Here are the available tickets: ", self.ticket)
        ticketnum = (input('Choose a ticket number: '))
        while ticketnum not in self.ticket:
            print("\nTicket not available.")
            print("Here are the available tickets: ", self.ticket)
            ticketnum = (input('Please enter valid ticket number: '))

        self.ticket.remove(ticketnum)
        self.Spaces.remove(ticketnum)
        self.current[ticketnum] = ""
        print("Success")

    def Quit(self):
        self.show()
        print('EXITING..')

# Condensed the rest of exit into pay to make Pay and Exit.

    def Pay(self):
        ticketnum = input

        if self.ticket == []:
            print('Garage Is Empty')
            return Garage

        elif ticketnum == 0:
            print("You haven't purchased a ticket yet!")

        ticketnum = input("What's your ticket number?\nOr would you like to quit?\n")

        while ticketnum not in self.current:
            if ticketnum == 'quit':
                exit()
            print("\nTicket not available.")
            ticketnum = (input('Please enter valid ticket number '))
        self.ticket.extend(ticketnum)
        self.Spaces.extend(ticketnum)
        self.current[ticketnum] = ""
        payment = input("You're stay has cost you $10 please pay now.")
        if payment == '$10' or 10:

            self.show()
            print('\nPlease have a nice day and drive safe.')

        else:
            print('That was not the correct amount')


# added self.show to all areas that had the below print statements just to clean things up a smidge.

    def show(self):
        self.ticket.sort
        self.Spaces.sort
        print('Spaces Left: ' + str(sorted(self.Spaces)))
        print('Ticket Left: ' + str(sorted(self.ticket)))


# Easier way to call to the class.

park = Garage()


# The one class makes things simple to code
# Below is the driver code. each if/elif calls to each method above.
# Learned from rewatching week_2 day 5 around 20mins in.

while (x == 1):
    start = input("\nWelcome to Parking Lot, press 'Enter' to continue")
    if start == "":

        choice = input(
            "Would you like to do? Enter/Pay and Exit/Show or Quit: ")

        if choice == 'enter':
            park.Enter()

    # Condensed the rest of exit into pay to make Pay and Exit.

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
