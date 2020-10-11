class Garage():

    def __init__(self, sizeOf):
        values = list(range(1, sizeOf + 1))
        self.parkingSpaces = values
        self.tickets = values[:]
        self.currentTicket = dict()
        for spot in self.parkingSpaces:
            self.currentTicket[spot] = ''
    
    def showSpots(self):
        return "Current available spots: " + str(len(self.parkingSpaces))

    def takeTicket(self):
        if self.parkingSpaces and self.tickets:

            user_spot = self.parkingSpaces.pop()
            self.currentTicket[user_spot] = False
            user_tickets = self.tickets.pop()
            print(f"Your parking spot is {user_spot}.\n"
                  + f"Your ticket number is {user_tickets}.")
        else:
            print("Sorry the parking lot is full.")

    def payForParking(self):
        ticket_number = int(input("Scan your ticket: "))
        paid = self.currentTicket[ticket_number]
        if ticket_number in self.currentTicket:
            if paid != '':
                print("Valid Ticket")
                if not paid:
                    input("Press 'Enter' to pay for your parking stop: ")
                    self.currentTicket[ticket_number] = True
                    print("Your payment has been completed.")
                else:
                    print("Your ticket has been paid for. Thank you!")
                return ticket_number
            else:
                print("Sorry, that ticket hasn't been distributed today.")
                return -1
        else:
            print("Invalid Ticket.")
            return -1

    def leaveGarage(self):
        ticket_number = self.payForParking()
        if ticket_number == -1:
            print('Please retry with an appropriate ticket.')
            return -1
        input("You have 15 minutes to leave. Press 'Enter' button to confirm: ")
        print("Thank you, have a nice day!")
        self.parkingSpaces.append(ticket_number)
        self.tickets.append(ticket_number)

    def run(self):
        while True:
            print("\n" + self.showSpots())
            response = input("What do you want to do? You can: park, pay, leave, or quit. Type only one! ")
            response = response.strip().lower()

            if response == 'park':
                self.takeTicket()
            elif response == 'pay':
                self.payForParking()
            elif response == 'leave':
                self.leaveGarage()    
            elif response == 'quit':
                print("Thanks for using our Parking Garage!")
                break
            else:
                print("Invalid command.")


garage = Garage(10)
print("Welcome to our garage")
garage.run()