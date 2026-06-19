def area(length , width):
    print(str(length * width) + "  square feet")
    return length * width


def main():
     house = area(40,30)
     yard = area(10,35)
     total    = (house + yard)


     print(str(total ) + " total square feet")



main()
