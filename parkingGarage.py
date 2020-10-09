class Garage():

    def __init__(self, sizeOf):
        self.spots = sizeOf[:]
        self.tickets = sizeOf[:]
        self.currentTicket = dict()
        for spot in self.spots:
            self.currentTicket[spot] = False
    
    def showSpots(self):
        return "Current available spots: " + str(len(self.spots))

    def takeTicket(self):
        if self.spots and self.tickets:
            user_spot = self.spots.pop()
            user_tickets = self.tickets.pop()
            print(f"Your parking spot is {user_spot}.\n"

                    + f"Your ticket number is {user_tickets}.")
        else:
            print("Sorry the parking lot is full.")

    def payForParking(self):
        ticket_number = int(input("Scan your ticket: "))
        if ticket_number in self.currentTicket:
            print("Valid Ticket")
            if self.currentTicket[ticket_number] == False:
                input("Press any key to pay for your parking stop. ")
                self.currentTicket[ticket_number] = True
                print("Okay now you have paid")
            else:
                print("Ticket has been paid, Thank you")
            return ticket_number
        else:
            print("Invalid Ticket")

    def leaveGarage(self):
        ticket_number = self.payForParking()
        input("You have 15 minutes to leave ")
        print("Thank you, have a nice day!")
        self.spots.append(ticket_number)
        self.tickets.append(ticket_number)

    def run(self):
        while True:
            print("\n" + self.showSpots())
            response = input("What do you want to do? You can: park, pay, leave, or quit. Type only one! ")
        
            if response.lower() == 'park':
                self.takeTicket()
            
            if response.lower() == 'pay':
                self.payForParking()

            if response.lower() == 'leave':
                self.leaveGarage()
                
            if response.lower() == 'quit':
                print("Thanks for using our Parking Garage!")
                break


garage = Garage([1, 2, 3, 4,5, 6, 7, 8 , 9, 10])
print("Welcome to our garage")
garage.run()

