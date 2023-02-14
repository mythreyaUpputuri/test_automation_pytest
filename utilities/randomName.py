import names
import random


def user_generator():
    firstName = names.get_first_name('female')
    lastName = names.get_last_name()
    email = firstName + '.' + lastName + str(random.randint(999, 99999)) + "@email.com"

    return firstName, lastName, email
