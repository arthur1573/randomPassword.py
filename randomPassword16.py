import random
import clipboard
length = 16
all = "abcdefghjkmnpkrstuvwxyz" + "ABCDEFGHJKMNPKRSTUVWXYZ" + "23456789" + "@#$%^*_" # delete: i l o, I L O, 1 0, !()-=+
sample = random.sample(all, length)
password = "".join(sample)
clipboard.copy(password)