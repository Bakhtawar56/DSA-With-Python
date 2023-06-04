sub1=int(input("Enter marks first subject"))
sub2=int(input("Enter marks of second subject:"))
sub3=int(input("Enter marks of third subject:"))
sub4=int(input("Enter marks of fourth:"))
sub5=int(input("Enter marks of fifth subject:"))
avg=(sub1+sub2+sub3+sub4+sub5)/5
if(avg>=90):
    print("grade A:")
elif(avg>=80 & avg<90):
    print("Grade B:")
elif(avg>=70&avg<80):
    print("Grade C:")
elif(avg>=60&avg<70):
    print("Grade D:")
else:
    print("grade F :")