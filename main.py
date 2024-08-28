medicalcause=input("Did u have a medical cause Y or N")
atten=int(input("Enter your attendence"))
if medicalcause=="Y":
    print("you are allowed")
else:
    if atten>=75:
        print("allowed")
    else:
        print("not allowed")