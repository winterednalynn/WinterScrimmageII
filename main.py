import random   #import random to initialized random power in this main class.

# ("\u2744")  # snowflake unicode

# To create a square in unicode : \u2510 , \u2514, \u2518,  u250c, u2500


snowdiceDisplay = {
    1: ("┌─────────┐",
        "│         │",
        "│    1❄  │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│         │",
        "│    2❄  │",
        "│         │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│         │",
        "│    3❄  │",
        "│         │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│         │",
        "│    4❄  │",
        "│         │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│         │",
        "│    5❄  │",
        "│         │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│         │",
        "│    6❄  │",
        "│         │",
        "└─────────┘")
}

#def is to define a function, similar to method.
def playerroll(): #produced a method dedicated to player roll.
    dice = [] #creating an empty list
    total = 0 #variable total starts on 0
    numofdiceroll = int(input("Enter the number '6' to roll the 6 dices"))#instructing player to enter 6 to prompt dices

#using a for loop
    for _ in range(numofdiceroll): #6 dices
        dice.append(random.randint(1, 6)) # 1 roll , 6 dices concluding to numbers 1-6 (randomize)

#Format dice display horizontally. This for loop express a sequence of the function. This will loop 5 times.
# Iteration from 0, 1, 2, 3, 4, 5
# set print calling the Display.get - GET retrieves the pattern from the display dictionary
    for line in range(5):
        for snowflake in dice:
            print(snowdiceDisplay.get(snowflake)[line], end="")
        print()

#snowflake in this for loop element means INT. This focuses on the integer of what is being looped.
#total += snowflake lines up to add current value of snowflakes to total.
#return total - this line passes the total sum of the code
    for snowflake in dice:
        total += snowflake
    print(f"Player's total {total}")
    return total

#Produced when a bot rolls, same methods as player. Replaced some keywords to correspond bot's action.
def winterbotroll():
    dice = []
    total = 0
    botdiceroll = 6

    for _ in range(botdiceroll):
        dice.append(random.randint(1, 6))

    for line in range(5):
        for snowflake in dice:
            print(snowdiceDisplay.get(snowflake)[line], end="")
        print()

    for snowflake in dice:
        total += snowflake
    print(f"WinterBot total {total}")
    return total

#THE GAME GAME.
def winterscrimmage():
    #Displaying title of the game
    print("-------------------------------------")
    print("❄❄❄❄Winter Number Scrimmage II❄❄❄❄")
    print("-------------------------------------")

    playername = input("Enter your name: ") #Capturing player's name.
    print(f"Great! {playername}, you roll first!") #Greeting player
    print() #Just for spacing, Easy read.
    print("❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄") # A line of snowflakes to provide division.

#initializing score for player & bot
    playerscore = 0
    winterbotscore = 0

    for _ in range(5): #Going in out of 5 rounds
        playertotal = playerroll() #the playertotal will be based on player's roll. Function called.
        winterbottotal = winterbotroll() #the winterbot total will be based on the execution of bot roll
        winterbotname = "Winterbot" #Gotta name the bot. Same name as version I

        # if player dice roll is greater than bot roll, a score will accumulated per round
        if playertotal > winterbottotal:
            print(f"{playername} rolled {playertotal} - You win")
            playerscore += 1
        # if player dice roll is lesser than the bot , then the bot gets the score.
        elif playertotal<winterbottotal:
            print(f"{winterbotname} rolled {winterbottotal} - Bot wins")
            winterbotscore += 1
        # Generate random total matches, it will be deemed as a draw. No winners.
        else:
            print("It's a draw")
# if player tally score is over bot tally score (wins each round) , we recognize player win
    if playerscore > winterbotscore:
        print(f"{playername} wins with {playerscore} wins!❄ & {winterbotname} loses with a score of {winterbotscore}")
# if bot tally score is over player tally score (wins each round) , we recognize bot win
    elif playerscore < winterbotscore:
        print(f"{winterbotname} wins with {winterbotscore} wins!❄ & {playername} loses with a score of {playerscore}")

    else:
        print(f"It's a tie! {playername} score : {playerscore} & {winterbotname} score {winterbotscore}")


if __name__ == "__main__":
    winterscrimmage()
