import string
import random

password_chars = string.ascii_letters + string.digits + string.punctuation
length = random.randint(12, 15)

password = "".join([random.choice(password_chars) for _ in range(length)])
print(password)
