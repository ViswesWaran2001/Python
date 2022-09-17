marks=int(input("Enter the Marks:"))
if(marks<=100 and marks>90):
    print("The Grade is: 'O'")
elif(marks<=90 and marks>80):
    print("The Grade is: A+")
elif(marks<=80 and marks>70):
    print("The Grade is: A")
elif(marks<=70 and marks>60):
    print("The Grade is: B+")
elif(marks<=60 and marks>=50):
    print("The Grade is: B")
elif(marks<50):
    print("The Grade is: RA")
else:
    print("Enter the correct marks!")