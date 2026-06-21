def main():
    difficulty =input("difficult or casual ? ").lower()
    if not (difficulty == "difficult" or difficulty == "casual"):
       print("enter a valid difficulty ")
       return
    players= input("multiplayers or single player ? ").lower()

    if not (players == "multiplayers" or players== "single player"):
        print("enter a valid number of players ")
        return
    if (difficulty == "difficult" and players == "multiplayers"):
       recommend("hockey")
    elif (difficulty== "difficult" and players == "single player"):
         recommend("chess")
    elif (difficulty == "casual" and players == "multiplayers"):
         recommend("cricket")
    else :
         recommend("ludo")
def recommend(game) :
    print("you might like " + (game))
main()
