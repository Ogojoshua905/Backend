class SEO():
    EM = {}
    welcome = "Welcome! This is A Beta Version Of The Social Event Planner, Your Participation and Review could be the Catalyst on whether to be Reduced Globally or Not"
    
    def __init__(self, event):
        self.event = event
    
    def update_em(self, e_name, o_name, o_age, o_sex, e_date, e_time, e_location, e_description):
        self.EM[e_name] = {
            "Organizer_Name": o_name,
            "Organizer_Age": o_age,
            "Organizer_Sex": o_sex,
            "Date": e_date,
            "Time": e_time,
            "Location": e_location,
            "Description": e_description,
        }
    
    def cancel_event(self, e_name):
        if e_name in self.EM:
            del self.EM[e_name]
        else:
            print("Event doesn't exist on this timeline")
    
    def search_event(self, e_name):
        if e_name in self.EM:
            details = self.EM[e_name]
            print("=" * 10)
            print(f"Event Name: {e_name}")
            print(f"Organizer's Name: {details['Organizer_Name']}")
            print(f"Organizer's Age: {details['Organizer_Age']}")
            print(f"Organizer's Sex: {details['Organizer_Sex']}")
            print(f"Date: {details['Date']}")
            print(f"Time: {details['Time']}")
            print(f"Location: {details['Location']}")
            print(f"Description: {details['Description']}")
            print("=" * 10)
        else:
            print("Event not found")
    
    def view_all_event(self):
        if self.EM:
            for e_name, details in self.EM.items():
                print("=" * 10)
                print(f"Event Name: {e_name}")
                print(f"Organizer's Name: {details['Organizer_Name']}")
                print(f"Organizer's Age: {details['Organizer_Age']}")
                print(f"Organizer's Sex: {details['Organizer_Sex']}")
                print(f"Date: {details['Date']}")
                print(f"Time: {details['Time']}")
                print(f"Location: {details['Location']}")
                print(f"Description: {details['Description']}")
                print("=" * 10)
        else:
            print("No events available")                                                          
    
    def run_events(self):
        print(self.welcome)
        while True:
            print("Options")
            print("1. Create an Event")
            print("2. View all Events")
            print("3. Search an Event")
            print("4. Cancel an Event")
            print("5. Exit")
            eM = input("Choose from Option 1/2/3/4/5: ")
            if eM == "1":
                e_name = input("Enter Event Name: ")
                o_name = input("Organizer's Name: ")
                o_age = input("Organizer's Age: ")
                o_sex = input("Organizer's Gender: ")
                e_date = input("Enter Event Date: ")
                e_time = input("Enter Event Time: ")
                e_location = input("Enter Event Location: ")
                event_description = input("Enter Event Description: ")
                self.update_em(e_name, o_name, o_age, o_sex, e_date, e_time, e_location, event_description)
                print("Event created successfully")
            elif eM == "2":
                self.view_all_event()
                input("Press Enter to continue...")
            elif eM == "3":
                e_name = input("Enter Event Name: ")
                self.search_event(e_name)
            elif eM == "4":
                e_name = input("Enter Event Name: ")
                self.cancel_event(e_name)
                input("Press Any Key to Continue....")
            elif eM == "5":
                print('Exiting Programme, Thanks for using our SEO project')
                break
            else:
                print("Invalid Option. Please Choose a Valid Option Because You've Eyes.")

EventManager = SEO("")
print(EventManager.run_events())
