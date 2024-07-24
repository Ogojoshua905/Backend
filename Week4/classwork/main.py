from management import Management


class Automobile(Management):
    net_worth = 0
    def __init__(self): #Constructor
        super().__init__("Uni Global", "2005", "Mr Kayode") # brings in the Properties from The File Class
        self.store = self.load_from_file("store/mobiles.json")

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

    def delete_cars(self, car_name, model):
        for car in self.store:
            if car['car_name'] == car_name and car['model'] == model:
                self.store.remove(car)
                print(f"{car_name} {model} has been Removed Successfully, U too dey Price.....")
                break
        else:
            print("Car Not In Shipment")

    def run_company(self): # methods or member functions
        while True:
            print("1. Add a Car")
            print("2. View a Car")
            print("3. Remove a Car")
            print("4. Purchase a Car")
            print("5. Quit")
            command = input("Choose Options 1/2/3/4: ")
            if command == "1":
                car_name = input("What is Your Taste Of Cars: ") #PS: \n means New Line in Python like <br /> in html 
                model = input("What is The Model of the Car you looking for: ")
                color = input("What Color do you want, Lemme see if I'll be able to arrange The Car: ")
                price = input("What is your Budget: ")
                print(car_name, model, color, price)

                self.add_a_car(car_name, model, color, price)
                self.update_net_worth(price)
                self.save_to_file(self.store, 'store/mobiles.json') # or ./store/mobiles.json both will work
                self.purchase_car(car_name, model, color, price)
                print(f"Car Added, {car_name} {model} Will be Ready for Shipment in the Next 24hrs. Your Net Worth is ${self.net_worth}")
            
            elif command == "2":
                self.view_cars()
            elif command == "3":
                car_name = input("Enter Car Name: ")
                model = input("Enter Car Model: ")
                self.delete_cars(car_name, model)
                self.save_to_file(self.store, 'store/mobiles.json')
            elif command == "5":
                print(f"Keep Pushing, as for Now your Aza is {self.net_worth}. Go and Hustle")
                break
            else:
                print("Invalid Command")
    
           
uni_Global = Management("Uni Global", "2005", "Mr Kayode")

uni_Global = Automobile()

print(uni_Global.run_company())

print(f'From the CEO "Nice Businessing" You || {uni_Global.ceo}')   