import random 
print('''\n  \n
$$\   $$\ $$$$$$$$\ $$\       $$\       $$$$$$\    
$$ |  $$ |$$  _____|$$ |      $$ |     $$  __$$\   
$$ |  $$ |$$ |      $$ |      $$ |     $$ /  $$ |  
$$$$$$$$ |$$$$$\    $$ |      $$ |     $$ |  $$ |  
$$  __$$ |$$  __|   $$ |      $$ |     $$ |  $$ |  
$$ |  $$ |$$ |      $$ |      $$ |     $$ |  $$ |  
$$ |  $$ |$$$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$  |  
\__|  \__|\________|\________|\________|\______/  \n \n''')

rock = '''
   _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
\n '''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
\n '''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
''' 


game_images = [rock , paper , scissors]
user_choice = int(input("What do you want to choose? \n 0 for Rock \n 1 for Paper \n 2 for Scissors:\n "))
if user_choice >=3 or  user_choice<0:
    print ("You typed an invalid number , you lose")
else:
    print(game_images[user_choice])
    computer_choice = int(random.randint(0,2)) 

    print (f"Computer chose :{computer_choice}")
    print("Computer chose: \n")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif user_choice > computer_choice:
        print ("You win!!")
    elif computer_choice > user_choice :
        print("You lose") 
    elif computer_choice == user_choice:
        print("Draw")


