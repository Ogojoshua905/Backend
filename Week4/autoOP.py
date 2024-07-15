class Automobile():
    store = []
    net_worth = 0
    def __init__(self, name, founded, ceo): #Constructor
        self.name = name
        self.founded = founded
        self.ceo = ceo

    def add_a_car(self, car_name, model, color, price=0):
        self.store.append({"car_name": car_name, "model":model, "color":color, "price":price}) #Members Function
     
    def update_net_worth(self, price):
        self.net_worth += int(price)

    def view_cars(self):
        if len(self.store) == 0:
            print("No Net Worth")
        else:
            for car in self.store:
                print(
                    "==" * 8,
                    f"name: {car['car_name']}"
                    f"model: {car['model']}",
                    f"color: {car['color']}",
                    f'price: {car['price']}',
                    "==" * 8,
                    sep="\n"
                )

    def run_company(self): # methods or member functions
        while True:
            command = input("Enter 'add' to add a car, 'view' to see cars , 'quit', to exit: ")
            if command == "add":
                car_name = input("What is Your Taste Of Cars: ")
                model = input("What is The Model of the Car you looking for: ")
                color = input("What Color do you want, Lemme see if I'll be able to arrange The Car: ")
                price = input("What is your Budget: ")
                print(car_name, model, color, price)

                self.add_a_car(car_name, model, color, price)
                self.update_net_worth(price)
                print(f"Car Added, {car_name} {model} Will be Ready for Shipment in the Next 24hrs. Your Net Worth is ${self.net_worth}")
            
            elif command == "view":
                self.view_cars()
            elif command == "quit":
                print(f"Keep Pushing, as for Now your Aza is {self.net_worth}. Go and Hustle")
                break
            else:
                print("Invalid Command")
    
           
uni_Global = Automobile("Uni Global", "2005", "Mr Kayode")

print(uni_Global.run_company())

print(f'From the CEO "Nice Businessing" You || {uni_Global.ceo}')