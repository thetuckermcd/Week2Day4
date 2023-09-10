class Parking_Garage:



    def __init__(self):
        self.name = ""
        self.spaces = [1,2,3,4,5,6,7,8,9,10]
        self.tickets =[1,2,3,4,5,6,7,8,9,10]
        self.current_ticket = {}
        self.start_prompt = "\Please Take Ticket"
        self.pay_prompt = "\Please insert money"
        self.paid_prompt = "\Your Ticket has been paid, (You now have 15 minutes to leave)"
        self.success_prompt = "\Thank you have a nice day"

    #Parking Ticket System
    def enter_garage(self): 
        self.name = input("What is your first name?").strip().capitalize()
        my_space = self.spaces.pop()
        my_ticket = self.tickets.pop()
        self.current_ticket = {
            "name": self.name, 
            "space" : my_space,
            "ticket" : my_ticket,
            "paid" : False

        }

        return self.current_ticket


    #Take Ticket
    #Ask for users name(self.name= What's )
    #Using assigned number in dictionary, we set value to be their name
    #Here is your ticket number  Thank you for parking with us


    def pay_for_parking(self):
        self.name = input("What is your first name?").strip().capitalize()
        if self.name in self.current_ticket.values():
          amount= int(input(self.pay_prompt)) 
          if amount < 15 
        

    #Ask for users name and compare against dictionary (Use input function) 
    #If user is still in dictionary ask for payment
    #Verify payment amount
    #Reassign dictionary key to have user value in empty string

    print(success_prompt)

#Empty Dictionary to store info later
current_ticket = {}

#List of spaces available




print("Welcome to the Parking Garage")

start = input(start_prompt)
    #Runs until a ticket is taken
    while True:
        #empty list to store the space the user has selected
        spaces = []

        #Pay for the ticket
        Ticket_selection = input(pay_prompt)
        ticket_selection = int(pay_prompt)
