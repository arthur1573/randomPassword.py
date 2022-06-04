import random


# combine all letter, number, signes 
# delete something I do not like: i l o, I L O, 1 0, ! ( ) - = + [ ] \ ; ' , . /
all = "abcdefghjkmnpkrstuvwxyz" + "ABCDEFGHJKMNPKRSTUVWXYZ" + "23456789" + "@#$%^*_" 
password = random.choices(all, k=16)


# convert list to string
password2 = "".join(password)


# if the module is not install
# = if the user not run: pip install -r requirements.txt
try:
    import pyperclip
    pyperclip.copy(password2)
    print(password2)
    print('Well done, the password has been copied to the clipboard.')
except:
    print(password2)
    print('Well done, you need to copy the password above manually.')
