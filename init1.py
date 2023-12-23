class Railway():
    def __init__(self,traine_number,traine_name,traine_arrival,traine_destination,traine_nextstop):
        self.num = traine_number
        self.name = traine_name
        self.arrival = traine_arrival
        self.dest = traine_destination
        self.stop = traine_nextstop
    

    



    def platform1(self):
        print("Welcome to the platform-1 details:")
        print("Traine Number is:",self.num)
        print("Traine name is:",self.name)
        print("Traine Arrival Station Name:",self.arrival)
        print("Traine Destination station name:",self.dest)
        print("Traine NextStop:",self.stop)


    def platform2(self):
        print("Welcome to the platform-2 details:")
        print("Traine Number is:",self.num)
        print("Traine name is:",self.name)
        print("Traine Arrival Station Name:",self.arrival)
        print("Traine Destination station name:",self.dest)
        print("Traine NextStop:",self.stop) 

    def Booking(self):
        self.num1 = int(input("Enter Traine Numer:"))
        self.name1 = input("Enter Traine Name:")
        print("Traine Arrival Station Name:",self.arrival)
        print("Traine Destination station name:",self.dest)
        self.price = int(input("Enter the Price:"))
        sub = input("If you want to ticket confirm(yes/no):")
        if sub == "yes":
            print("Succesfull Confirmation Your Ticket")
            print("Thankyou for choosing us, /nVisit Again!")

        else:
            print("Your Ticket was not confirmed")

    def search(self):
        ser = int(input("Enter the Traine Number:"))
        if ser == 16227:
            print("Traine Number is:",self.num)
            print("Traine name is:",self.name)
            print("Traine Arrival Station Name:",self.arrival)
            print("Traine Destination station name:",self.dest)
            print("Traine NextStop:",self.stop)
        else:
            print("Incorrect Trainee Number")
            
            
ral = Railway(16227,"Tirupati Expresss","Tirupati","Chennai","Reniguta Junction")

rak = Railway(16337,"Hyderabad Express","Tirupati","Hyderabad","Vijayawada")
while True:
    print("*************************************************")
    print("         Welcome to railway Booking System       ")
    print("*************************************************")
    print("     1.Platform-1 Details")
    print("     2.Platform-2 Details")
    print("     3.Booking Ticket Details")
    print("     4.Search Traine Details")
    print("     5.Exit")
    print()
    print("Choose anyone option from above menu")
    opt = int(input("Enter the option:"))
     
    if opt == 1:
        print(ral.platform1())
    elif opt == 2:
        print(rak.platform2())
    elif opt == 3:
        print(rak.Booking())
    elif opt == 4:
        print(ral.search())
    elif opt == 5:
        break
    else:
        print("Try Again")




        


