name = input("what's your name ?")
match name :
     case "Harry"  | "Ron" :
        print("Griffindor")
     case "Draco":
        print("Slytherin")
     case _:
        print("who ?" )
