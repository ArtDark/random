import random, string



def random_string(str_len):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(str_len))



str_len = int(input("Enter len string: "))


print(random_string(str_len))