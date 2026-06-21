maths = float(input("how many marks get in math "))

physics= float(input("how many marks get in physics "))

chemistry = float(input("how many marks get in chemistry "))
#float is use because marks can be in decimal form .

english = float(input("how many marks get in english "))

it = float(input("how many marks get in it "))
# as maximum marks in each subject is 100  so , total marks is out of 500 .

score = ((maths + english + chemistry + physics + it)*100)/500

print(str(score ) + " percent ")

if score <= 100  and score >= 90 :
    print("Grade : A+ ")

if score < 90 and score >= 80 :
    print("Grade : A ")

if score <= 80 and score >=70 :
    print("Grade : B ")
if score < 50 :
    print("Fail")
