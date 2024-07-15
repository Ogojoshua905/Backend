data = [
        {
            "question": "Which of these is not a renewable energy source?",
            "options": ["Solar", "Wind", "Coal", "Hydroelectric"],
            "answer": "3"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Earth", "Jupiter", "Mars", "Saturn"],
            "answer": "2"
        },
        {
            "question": "Which country hosted the 2016 Summer Olympics?",
            "options": ["China", "Brazil", "United Kingdom", "Japan"],
            "answer": "2"
        },
        {
            "question": "What is the main gas found in the Earth's atmosphere?",
            "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"],
            "answer": "3"
        },
        {
            "question": "Who was the first President of the United States?",
            "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"],
            "answer": "3"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["O2", "H2O", "CO2", "HO"],
            "answer": "2"
        },
        {
            "question": "Which planet is known as the Morning Star?",
            "options": ["Venus", "Mars", "Mercury", "Jupiter"],
            "answer": "1"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Great White Shark"],
            "answer": "2"
        },
        {
            "question": "Who wrote the play 'Hamlet'?",
            "options": ["William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"],
            "answer": "1"
        },
        {
            "question": "What is the capital city of Canada?",
            "options": ["Toronto", "Vancouver", "Ottawa", "Montreal"],
            "answer": "3"
        }
    ]

def game():
    score = 0
    index = 0
    # print(data[0]["question"])

    while index < len(data):
        print(input(data[index][str("question")]))
        print(f"1. {(data[index][str("options")][0])}")
        print(f"2. {(data[index][str("options")][1])}")
        print(f"3. {(data[index][str("options")][2])}")
        print(f"4. {(data[index][str("options")][3])}")

        answer = str(input(f"Choose 1/2/3/4: "))
        print(index, ":INDEX")
        # print(answer)

        if answer  == data[index]["answer"]:
            index +=1
            score +=1
            print(f"NERD Alert!!!. Score: {score + 1}/{len(data)}")
        else:
            index +=1
            print(f"You Suck. Score: {score}/{len(data)}")
    else:
        print(f"Done!!! Your Score: {score}/{len(data)}")
        



game()