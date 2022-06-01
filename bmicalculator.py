wt = (input("enter your weight : "))
ht = (input("enter your height : "))

bmi = int(wt)/(float(ht)**2)
print(bmi)

if bmi < 18:
    print("UNDERWEIGHT")
elif bmi < 25.5:
    print("NORMAL")
elif bmi < 30:
    print("OVERWEIGHT")
elif bmi < 35:
    print("OBESE")
else:
    print("CLINICALLYOBESE")