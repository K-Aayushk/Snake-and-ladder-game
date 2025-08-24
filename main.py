import numpy as np

#create the empty array

table=np.empty(shape=(10,10))
snakes=[5,10,14,24,32,47,54,70,88,91,97]
def createtable():
    count=0
    for i in range(0,len(table)):
        for j in range(0,len(table)):
            count+=1
            table[i,j]=count
    return table
createtable()
#printing the 
print(table[::-1])
print("Remenber there are snakes too on key value:",snakes)

player_position=0
def dice(player_position,snakes):
    inp=input("want to roll dice?? (Y/N):")
    if(inp.lower()=="y"):
        dice_num=np.random.randint(1,7)
        print(f"Dice value is: {dice_num}")
        player_position= player_position + dice_num
        print(f"player is positioned at: {player_position}")
        if(player_position in snakes):
            print("Your have landed on snake:((")
            print("Your position is now zero!!!")
            player_position=0
        if(player_position==100):
            print("You have won the game!!!")
            return
        dice(player_position,snakes)
    elif(inp.lower()=="n"):
        print("Game has been terminated!!!")
    else:
        print("please enter a correct value!!!")
        dice(player_position,snakes)

dice(player_position,snakes)
