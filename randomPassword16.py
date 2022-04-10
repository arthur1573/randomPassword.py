import random
#import string
import clipboard



#print('Hello, Welcome...')

# length = int(input('\nEnter the length of password: (Suggestion number: 16)'))
length = 16

# lower = string.ascii_lowercase
# upper = string.ascii_uppercase

letter = string.ascii_letters
number = string.digits
# symbols = string.punctuation
# print("All lowercase letters: " + letter)
# print("All numbers : " + number)
# print("All punctuations: "+ symbols)




# i do not like all punctuation, so i choose this.
symbols2 = "!@#$%^*()"
#print("The punctuations which I like: " + symbols2)



#all = lower + upper + number + symbols2
all = letter + number + symbols2
#print("All letters: " + all)


# delete: i l o, I L O, 1 0
all2 = "abcdefghjkmnpkrstuvwxyz" + "ABCDEFGHJKMNPKRSTUVWXYZ" + "23456789"
#print("All letter which I select: " + all2)


# temp = random.sample(all, length)
# temp2 = random.sample(all2, length)
temp3 = random.sample(all2, length)


# password = "".join(temp)
# password2 = "".join(temp2)
password3 = "".join(temp3)

# print("")
# print("Here is your password:\n" + password)
# print("")
# print("Here is your password2:\n" + password2)
# print("")
#print("Here is your password3:\n" + password3)




#clipboard.copy(password2)
#print("Your password2:  " + password2 + "   has been copied...\nTry to paste it now.")

clipboard.copy(password3)

# input('Type enter exit...')

