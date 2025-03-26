import math

# def greet(name):
#     print(f"hello {name}")
#     print(f"how are you doing today {name}")


# greet('joseph')

# def greet_with(name, location):
#     print(f"hello {name}")
#     print(f"What is it like in {location}")
    
# greet_with(name='Marion', location='Limbe')


# test_h = int(input('Height of wall: '))
# test_w = int(input('Width of wall: '))
# coverage = 5 


# def paint_calc(height, width, cover):
#     number_of_cans = (height * width)/cover
#     rounded_number_of_cans = math.ceil(number_of_cans)
#     print(f"You'll need {rounded_number_of_cans} cans of paint.")

# paint_calc(height=test_h, width=test_w, cover=coverage)

n = int(input("Check this number: "))

def prime_checker(number):
    is_prime = True
    
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number. ")
    else:
        print("It's not a prime number.")
            

prime_checker(number=n)


