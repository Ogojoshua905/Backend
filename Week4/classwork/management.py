from file import File

class Management(File):
    def __init__(self, name, founded, ceo):
        super().__init__()
        self.store = self.load_from_file("store/manage.json")
        self.net_worth = {}
        self.name = name
        self.founded = founded
        self.ceo = ceo
        self.capital = 100000000  

    def add_a_car(self, car_name, model, color, price=0):
        self.store[car_name] = {"model": model, "color": color, "price": int(price)}

    def update_net_worth(self, price):
        self.net_worth += int(price)

    
    def view_cars(self):
        if len(self.store) == 0:
            print("No Cars in Store")
        else:
            for car in self.store:
                print(
                    "==" * 8,
                    f"name: {car['car_name']}",
                    f"model: {car['model']}",
                    f"color: {car['color']}",
                    f"price: {car['price']}",
                    "==" * 8,
                    sep="\n"
                )

    def purchase_car(self, car_name, model, color, price):
        if self.capital >= price:
            self.capital -= price
            self.add_a_car(car_name, model, color, price)
            self.update_net_worth(price)
            self.save_to_file(self.store, 'store/mobiles.json')
            print(f"Purchase Successful! {car_name} {model} added to inventory. Remaining capital: ${self.capital}")
        else:
            print("Not enough capital to pu rchase this car")
