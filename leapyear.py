year = int(input("Enter The Year You Want To Check : "))
if year%4==0:
   if year % 100==0:
        if year % 400==0:
           print("leap year") 
        else:
           print("Not a leap Leap Year") 
   else:
        print("Leap year")
else:
    print("Not a leap year")
            