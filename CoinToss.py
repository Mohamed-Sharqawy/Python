import random

print("""Welcome to the Coin Toss Game!
Chosing the method to toss the coin:
1. Using random.random()
2. Using random.randint()""")

choice = int(input("Chose a method (1 or 2) :"))
player = input("Enter your Guess (Heads or Tails): ").lower().strip()

if choice == 1:
    coin_res = "heads" if random.random() > 0.5 else 'tails'
  
    if coin_res == player:
        print(f"Congratulations! You won!")
    else :
        print("Sorry, You Lost!")
      
    print(f"The computer's result was : {coin_res}")
  
elif choice == 2:
    coin_res = 'heads' if random.randint(0,1) == 0 else 'tails'
  
    if coin_res == player:
            print("Congratulations! You Won!")
    else :
            print("Sorry, You Lost!")
      
    print(f"The computer's result was: {coin_res}")
  
else :
    print("Invalid Choice")
