from art import logo,vs
from game_data import data
import random
#format the acount data to printable format 
def format_data(account):
    """Takes account data and returns the printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from{account_country}"


def check_answer(guess, a_followers,b_followers):
    """Take the user guess and follower count and returns if they got it right. """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


#display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

#make the game repeatable
while game_should_continue:
    #Generate a random account from game data

    #making the accounts at position b become the next account at position A
    account_a = account_b
    account_b = random.choice(data)
    
    while account_b == account_a:
        account_b = random.choice(data)

    print(f"compare A:{format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")


    #ask user for a guess 
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()


    #check if user is correct
    ##get follower count of eacch acccount 
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    ##use if statement to check if user is correct
    if is_correct:
        score += 1
        print(f"you are right! Current score : {score}.")
    else:
        game_should_continue == False
        print(f"Sorry, that's wrong.Final score: {score}")

    #give user feedback on there guess

    #score keeping





#clear the screen