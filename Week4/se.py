print("Welcome to social event organizer!!!")
eventManager = []

while True:
    command = input("Enter: 'create' to create an event, 'cancel' to cancel an event, 'view' to view events, 'search' to search an event, 'exit' to exit: ")
    
    if command == "create":
        title = input("What is the title of your event?: ")
        name = input("What is the organizer's name?: ")
        age = int(input("What is the organizer's age?: "))
        gender = input("What is the organizer's gender?: ")
        date = input("What is the date of the event? (dd/mm/yyyy): ")
        location = input("What is the location of the event?: ")
        number = input("What is the maximum number of attendees?: ")
        eventManager.append({"title": title, "name": name, "age": age, "gender": gender, "date": date, "location": location, "number": number})
        print("You have successfully created your event!!!")
        
    elif command == "cancel":
        title = input("Enter the title of the event to be cancelled: ")
        for event in eventManager:
            if event['title'] == title:
                eventManager.remove(event)
                print(f"You have successfully cancelled the event: {title}")
                break
        else:
            print("Event not found.")
        
    elif command == "view":
        if eventManager:
            print("These are the details of the events:")
            for event in eventManager:
                print(f"title: {event['title']}, name: {event['name']}, age: {event['age']}, gender: {event['gender']}, date: {event['date']}, location: {event['location']}, number: {event['number']}")
        else:
            print("No events to show.")
            
    elif command == "search":
        title = input("Enter the title of the event to search: ")
        for event in eventManager:
            if event['title'] == title:
                print(f"title: {event['title']}, name: {event['name']}, age: {event['age']}, gender: {event['gender']}, date: {event['date']}, location: {event['location']}, number: {event['number']}")
                break
        else:
            print("Event not found.")
            
    elif command == "exit":
        print("Thank you for visiting, we hope to see you soon!!!")
        break
    else:
        print("Invalid command. Please try again.")
