# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lwr = name1.lower()
name2_lwr = name2.lower()

tcount = name1_lwr.count('t') + name2_lwr.count('t')
rcount = name1_lwr.count('r') + name2_lwr.count('r')
ucount = name1_lwr.count('u') + name2_lwr.count('u')
ecount = name1_lwr.count('e') + name2_lwr.count('e')
trueScore = tcount + rcount + ucount + ecount

lcount = name1_lwr.count('l') + name2_lwr.count('l')
ocount = name1_lwr.count('o') + name2_lwr.count('o')
vcount = name1_lwr.count('v') + name2_lwr.count('v')
ecount = name1_lwr.count('e') + name2_lwr.count('e')
loveScore = lcount + ocount + vcount + ecount

finalScore =  int(str(trueScore) + str(loveScore))

if finalScore < 10 or finalScore > 90:
    print(f"Your score is {finalScore}, you go together like coke and mentos.")
elif finalScore >= 40 and finalScore <= 50:
    print(f"Your score is {finalScore}, you are alright together.")
else:
    print(f"Your score is {finalScore}.")
