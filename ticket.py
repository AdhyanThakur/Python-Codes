age=int(input("enter the age:"))
is_student=input("Are you a student(YES/NO):").lower

if age<=5:
    if is_student=="YES":
        price="FREE"
    else:
        price="$1"
elif age<=18:
    if is_student=="YES":
        price="$10"
    else:
        price="$12"
elif age<=40:
    if is_student=="YES":
        price="$15"
    else:
        price="$17"
else:
    price="$20" 
print("The Price of the ticket:",price)                                       