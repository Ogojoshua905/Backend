#Encryption Ceaser Cipher

alphabets = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

def encrypt(word):
    length_of_list = len(alphabets)
    pattern = 10  # Define the pattern value for encryption
    encrypted_word = ""

    for letter in word:
        capitalized_letter = letter.upper()
        if capitalized_letter in alphabets:
            index = alphabets.index(capitalized_letter)
            new_index = (index + pattern) % length_of_list  # Pattern Module and wrap around
            encrypted_word += alphabets[new_index]
        else:
            encrypted_word += letter

    return encrypted_word

print(encrypt("Reak Rhuqt"))

# class CC:
#     def __init__(self):
#         self.alphabets = "ABCDEFGHIJKLMNOPQRSTUVWSYZ"

#     def encrypt(self, text, pattern):
#         length_of_list = len(self.alphabets)
#         cipher = ""
#         for letter in text:
#             capitalized_letter = letter.upper()
#             if capitalized_letter in self.alphabets:
#                 index = self.alphabets.index(capitalized_letter)
#                 new_index = (index + pattern) % length_of_list
#                 cipher += self.alphabets[new_index]
#             else:
#                 cipher += letter

#         return cipher
    
#     def cipherprogramme(self, text, pattern):
#         while True:
#             print("Encrypt and Decrypt a Words: ")
#             command = input("Choose E for Encrypt and D for Decrypt a Word: ")
#             if command == "E":
#                 pattern = int(input("Enter the Encryption Pattern Wagwan: "))
#                 text = input("Enter Text for Encryption: ")
#                 print("The Encrypted Text is: ", CC.encrypt(text, pattern))

#             if command == "D":
#                 pattern = int(input("Enter the Decryption Pattern Wagwan: "))
#                 text = input("Enter Text for Decryption: ")
#                 print("The Encrypted Text is: ", CC.encrypt(text, pattern))
#             else:
#                 print("Invalid Command")
# cp = CC()
# print(cp.cipherprogramme())