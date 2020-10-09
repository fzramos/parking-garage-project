class Garage():

    def __init__(self, spots, tickets):
        self.spots = spots
        self.tickets = tickets
        self.currentTicket = {
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
            6: False,
            7: False,
            8: False,
            9: False,
            10: False
        }

    # def showSpots(self):
    #     pass

    def takeTicket(self):
        if self.spots and self.tickets:
            user_spot = self.spots.pop()
            user_tickets = self.tickets.pop()
            print(f"Your parking spot is {user_spot}\n"
                    + f"Your ticket number is {user_tickets}.")
        else:
            print("Sorry the parking lot is full.")

    def payForParking(self):
        ticket_number = int(input("Scan your ticket: "))
        if ticket_number in self.currentTicket:
            print("Valid Ticket")
            if self.currentTicket[ticket_number] == False:
                input("Press any key to pay for your ticket")
                self.currentTicket[ticket_number] = True
                print("Okay new you have paid")
            else:
                print("Ticket has been paid, Thank you")
            return ticket_number
        else:
            print("Invalid Ticket")

    def leaveGarage(self):
        ticket_number = self.payForParking()
        # ticket_number = int(input("Scan your ticket: "))
        # if ticket_number in self.currentTicket:
        #     print("Valid Ticket")
        #     if self.currentTicket[ticket_number] == False:
        #         print("Okay pay for your ticket")
        #         self.currentTicket[ticket_number] = True
        #         print("Okay new you have paid")
        #     else:
        #         print("Ticket has been paid, Thank you")
        # else:
        #     print("Invalid Ticket")
        input("You have 15 minutes to leave ")
        print("Thank you, have a nice day!")
        self.spots.append(ticket_number)
        self.tickets.append(ticket_number)

    def run():
        while True:
           response = input("What do you want to do? You can: pay or quit. Type only one!")
        
        if response.lower() == 'park':
            self.takeTicket()
        
        if response.lower() == 'pay':
            self.payForParking()

        if response.lower() == 'leave':
            self.leaveGarage()
            
        if response.lower() == 'quit':
            self.payForParking()
            print("Thanks for using our Parking Garage!")

#Added comment for test            

garage = Garage([1, 2, 3, 4,5, 6, 7, 8 , 9, 10], [1, 2, 3, 4,5, 6, 7, 8 , 9, 10])

garage.takeTicket()
#garage.payForParking() 
garage.leaveGarage()

