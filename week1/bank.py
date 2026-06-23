#greet the user and takes input from him/her
#for making the upper case letters lower case and removing whitw space
greetings = input("Greetings : ").strip().lower()
#if starts with hello=o
if greetings.startswith("hello"):
    print("$0")
#if starts with h = 20
elif greetings.startswith("h"):
     print("$20")
else :
     print("$100")
