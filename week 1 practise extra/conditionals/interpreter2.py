def calculate(num1, operator,num2):
    if operator == "+" :
       return  num1+num2
    elif operator == "-" :
         return num1-num2
    elif operator == "*" :
         return num1*num2
    elif operator == "/" :
         if num2==0:
            return "cannot be divide by zero"
         else :
               return num1/num2
    else :
         return "invalid operator ! "
def main():
    print("   simple python calculator   ")


    first_number=float(input("enter first number "))
    operator=input("enter operator (+,_,*,/)")
    second_number=float(input("enter second number "))

    answer=calculate(first_number,operator,second_number)

    print("result" , answer )
main()

