"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = [2]
    if number_of_primes == 1:
        return list
    if number_of_primes > 1:
        list.append(3)
    number = list[len(list) - 1]
    while number_of_primes != 2:
        number = number + 2
        stop = False
        for item in list:
            if number % item == 0:
                stop = True
                break
        if not stop:
            list.append(number)
            number_of_primes -= 1
    return list  