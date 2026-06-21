def main():
    difficulty = input("what type of game you want difficult or casual ? ").lower()
    players = input("multiplayer or single player ? ").lower()
    match difficulty :
        case "difficult":
           match players:
               case "multiplayer":
                  x=input("which multiplayer game you want to play ?")
                  match x:
                      case "hockey"|"football"|"cricket"|"golf"|"basketball":
                         y=input("do you have enough players ?")
                         match y :
                             case"yes":
                                t=input("really want to play ?")
                                print("ok lets start")
                             case"no":
                                t=input("really want to play ? ")
                                print("sorry ! you don't have enough players to play the game  ")
                      case _:
                          print("sorry! this game is not updated in my program ")
        case"casual":
           match players :
               case "single player":
                  y=input("which game you will prefer ")
                  match y :
                      case "chess"|"carrom"|"ludo":
                         t=input("really want to play ? ")
                         print("let's start the game  ")
               case _:
                   print("sorry !! this game is not updated in my program ")



main()
