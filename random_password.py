import random
import string
def generator_pass(length):
    character=string.ascii_letters+ string.digits +string.punctuation
    password="".join(random.choice(character) for _ in range(length))
    return password
length=int(input("Enter the length of th password: "))
print("Generated password: ", generator_pass(length))