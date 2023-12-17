import random

print('Welcome to our game!!')
Choice1=int(input('choose which game you want to play:\n1-guessing Game\n2-Rock,Paper,Scissors\n3-Baloot paper'))

if Choice1 ==1:
   
   def guess_the_number():
  
    the_number = random.randint(1, 100)
    
   
    numberOfAttempts = 3
    attempts_left = numberOfAttempts
    
    while attempts_left > 0:
       
        user_guess = int(input("Guess the number between 1 and 100: "))
        
       
        if user_guess == the_number:
            print(f"Congratulations! You guessed the correct number in {numberOfAttempts - attempts_left + 1} attempts.")
            break
        elif user_guess < the_number:
            print(f"Too low! Try again. Attempts left: {attempts_left - 1}.")
        else:
            print(f"Too high! Try again. Attempts left: {attempts_left - 1}.")
        
       
        attempts_left -= 1
    
    
    if attempts_left == 0:
        print(f"Sorry, you're out of attempts. The correct number was {the_number}.")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        guess_the_number()

elif Choice1 == 2:
    List = ['Rock','Paper','Scissors']
    z = random.choice(List)
    print(z)

elif Choice1 == 3:
    Paper = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
    random.shuffle(Paper)
    print(Paper)

guess_the_number()
guess_the_number()
guess_the_number()






