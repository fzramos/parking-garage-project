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
        pass

    def leaveGarage(self):
        pass



garage = Garage([1, 2, 3, 4,5, 6, 7, 8 , 9, 10], [1, 2, 3, 4,5, 6, 7, 8 , 9, 10])

garage.takeTicket()
