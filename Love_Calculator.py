print("****WELCOME TO LOVE THE CALCULATOR!!")
name1 = input("ENTER YOUR NAME :\n")
name2 = input("ENTER THEIR NAME :\n")
combine_name = name1+name2
lower_string= combine_name.lower()

t = lower_string.count("t")
r = lower_string.count("r")
u = lower_string.count("u")
e = lower_string.count("e")

true = t+r+u+e
l = lower_string.count("l")
o = lower_string.count("o")
v = lower_string.count("v")
e = lower_string.count("e")

love = l+v+o+e

love_score = int(str(true)+str(love))

if (love_score<10) or (love_score>90):
    print(f"your love score is {love_score},You go together like coke and mentos!!")
elif (love_score>=40) and (love_score<=50):
    print(f"your love score is {love_score},You are alright together!!")
else:
    print(f"your love score is {love_score}")
    
        