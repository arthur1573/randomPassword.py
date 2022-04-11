import random
import clipboard
all = "abcdefghjkmnpkrstuvwxyz" + "ABCDEFGHJKMNPKRSTUVWXYZ" + "23456789" + "@#$%^*_" # delete: i l o, I L O, 1 0, !()-=+[]\;',./
password = random.choices(all, k=16)
password2 = "".join(password)
clipboard.copy(password2)
print(password2)