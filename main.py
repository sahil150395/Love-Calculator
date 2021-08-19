# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
 
name1_lwr = name1.lower()
name2_lwr = name2.lower()
combinedStr = name1_lwr + name2_lwr

tcount = combinedStr.count('t')
rcount = combinedStr.count('r') 
ucount = combinedStr.count('u') 
ecount = combinedStr.count('e') 
trueScore = tcount + rcount + ucount + ecount

lcount = combinedStr.count('l') 
ocount = combinedStr.count('o') 
vcount = combinedStr.count('v') 
ecount = combinedStr.count('e') 
loveScore = lcount + ocount + vcount + ecount

finalScore =  int(str(trueScore) + str(loveScore))

if finalScore < 10 or finalScore > 90:
    print(f"Your score is {finalScore}, you go together like coke and mentos.")
elif finalScore >= 40 and finalScore <= 50:
    print(f"Your score is {finalScore}, you are alright together.")
else:
    print(f"Your score is {finalScore}.")
