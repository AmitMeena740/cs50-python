def main():
    time=input("what is the time right now ? ")
    hour=convert(time)
    if 7.00 <= hour <= 8.00 :
      print(" Breakfast time ")
    elif 12.00 <= hour <=13.00 :
         print("Lunch time")
    elif 18.00 <= hour <= 19.00 :
        print("Dinner time ")

def convert(time) :
    hours,minutes = time.split(":")
    hours = int(hours)
    minutes = float(minutes)
    return hours + minutes/60
if __name__ == "__main__":
    main()
