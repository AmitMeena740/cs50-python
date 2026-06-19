def main() :
    x  = int(input("what's x ? "))

    print("Even") if is_even(x) else print("Odd")

def is_even(n):
#     return True if n % 2 ==0 else  False (this can be use but it is a litte big)
      return n % 2 ==0
main()
