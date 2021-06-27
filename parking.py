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
            print('Ticket Left: ' + str(self.ticket))

    def Exit(self):
        if self.ticket >= 10:
            print('Garage Is Empty')


    def Quit(self):
        print('Spaces Left: ' + str(self.ticket))
        print('Ticket Left: ' + str(self.ticket))
        print('EXITING..')

    def Pay(self):
        ticketnum = input 
        if self.ticket == 0:
            print("You haven't purchased a ticket yet!")
            
        ask = input("What's your ticket number?\n")
        payment = input("You're stay has cost you $10 please pay now. ")
        if payment == '$10':
            self.ticket = self.ticket+1
            print('Spaces Left: ' + str(self.ticket))
            print('\nPlease have a nice day and drive safe.')
        else:
        
            print('That was not the correct amount')
    def run():
        garage_tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        garage_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        garage = Garage(garage_tickets, garage_spaces)

    


#Easier way to call to the class.
park = Garage()


#The one class makes things simple to code
#Below is the driver code. each if/elif calls to each method above.
#Learned from rewatching week_2 day 5 around 20mins in. 

while (x == 1):
    try:
        input("\nWelcome to Parking Lot, press 'Enter' to continue")
    except:
        pass
    choice = input("Would you like to do? Enter/Exit/Pay or Quit: ")

    if choice == 'enter':
        park.Enter()

    elif choice == 'exit':
        park.Exit()
    
    elif choice=='pay':
        park.Pay()

    elif choice == 'quit':
        park.Quit()
        break

    else:
        print("Wrong input, select Enter/Exit or Quit: ")
