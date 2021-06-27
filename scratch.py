def New_Ticket():
    ticket = 10
    x = 1
    while (x == 1):

        myInput = input("Would you like to do? enter/exit or quit: ")

        if (myInput == 'exit'):
            if ticket >=10:
               print('garage is empty')
               break    
            else:
                ticket = ticket+1
                print('spaces left: ' + str(ticket))


        elif (myInput == 'enter'):
            if ticket <= 0:
                print('garage is full try again later')
                break
            else:
                ticket = ticket-1
                print ('spaces left: ' + str(ticket))

        elif (myInput == 'quit'):
            print (ticket)
            print ('exiting..')
            break

        else:
            print ("wrong input, select enter/exit or cancel: ")

New_Ticket()