import random


# combine all letter, number, signes.
all = "abcdefghjkmnpkrstuvwxyz" + "ABCDEFGHJKMNPKRSTUVWXYZ" + "23456789" + "@#$%^*_" # delete: i l o, I L O, 1 0, !()-=+[]\;',./
password = random.choices(all, k=16)

# convert list to string
password2 = "".join(password)


try:
    import pyperclip
    pyperclip.copy(password2)
    print('The text to be copied to the clipboard.')
except:
    print(password2)
    