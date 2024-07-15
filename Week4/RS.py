class Reverse_Flash():
    def __init__(self, team, hello):
        self.team = team
        self.hello = hello

    def reverse_string(self, string):
        # Replace spaces with underscores
        modified_string = string.replace(' ', '_')
        # Reverse the string '::-1' inndicates that it should start from the last letter
        reversed_string = modified_string[::-1]
        return reversed_string
    
    def speak(self): 
        reverse_team = self.reverse_string(self.team)
        reverse_hello = self.reverse_string(self.hello)
        print(f"If I pass '{self.team}' as an argument into the function, it should return '{reverse_team}' as an output")
        print(f"if I pass a string {self.hello} into the function it should return {reverse_hello}")

RedStreak = Reverse_Flash('this team', 'hello')
print(RedStreak.speak())