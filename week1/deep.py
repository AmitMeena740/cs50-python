#str and lower are added to make upper case letter lower case and remove white space
question=input( " what is the answer to the great question of life , the universe and everything else ?").strip().lower()
#if input is found to be one of this from the followings than ,yes
if ( question == "42" or  question == "forty-two" or  question == "forty two"):
   print("Yes")
else:
   print("No")
