def main():
    difficulty = input("difficult or casual ? ").lower()
    players= input("multiplayers or single player ? ").lower()

    if difficulty == "difficult":
        if players == "multiplayer":
           recommend("hockey")
        elif players=="single player":
             recommend("klondike")
        else:
            print("enter valid number of players ")

    elif difficulty =="casual":
        if players == "multiplayer":
           recommend("cricket")
        elif players == "single player":
             recommend("ludo")
        else :
             print("enter valid numbers of players ")
    else :
        print("enter a valid difficulty ")

def recommend(game):
    print("you will like " +(game))
main()
