import string 
import random 

def password_generator(): 
  
    char_pool = ""

    while True:
      length = int(input("How long should the password be? "))
      uppercase = input("Include uppercase? (y/n): ")
      numbers = input("Include numbers? (y/n): ")
      symbols = input("Include symbols? (y/n): ")


      if uppercase.lower() == "y": 
        char_pool += string.ascii_uppercase 

      if numbers.lower() == "y": 
        char_pool += string.digits

      if symbols.lower() == "y": 
        char_pool += string.punctuation

      password = ''.join(random.choices(char_pool, k=length))
      print("Generated password: ", password)

      break

def test_password_strength():
    password = input("Enter a password to test: ")
    score = 0

    if len(password) >= 8: 
      score += 1 

    if any(char.isupper() for char in password):
      score += 1

    if any(char.isdigit() for char in password):
      score += 1 

    if any(char in string.punctuation for char in password):
      score += 1

    print("""Based on score 
          5 - Strong
          3-4 = Medium 
          1-2 = Weak 
          0 - Very weak""")

    if score == 5:
      result = "Strong"

    elif score >= 3:
      result = "Medium"

    elif score >= 1: 
      result = "Weak"

    else:
      result = "Very Weak"

    print(f"Your password strength is {result}, the score resulted {score}/5.")


print("Welcome to the Password Generator!")

while True:

  print("""Choose the following options
      1. Generate a random password
      2. Test the strength of your current password
      3. Exit""")
  options = int(input("Choose your options (1-3): "))

  if options == 1:  
    password_generator()

  elif options == 2:
    test_password_strength()

  elif options == 3:
    print("Thank you for using our program")
    break

  else:
    print("Invalid input. Try again")

