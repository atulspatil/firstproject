# city_name = input('Enter your city name here : ').lower()
#
# if city_name == 'jamner':
#     print('Covid-19 cases in Jamner stands at 250')
# elif city_name == 'pune':
#     print('Covid-19 cases in Pune stands at 5000')
# else:
#     print("Sorry we don't have data for your city")
#
# from greet_module import greeting
#
# print(greeting('Atul'))


word_list = ['hello2', 'bye', 'hello', 'tata', 'tiger']
for i in range(len(word_list)):
    for j in range(i + 1, len(word_list)):
        if len(word_list[i]) >= len(word_list[j]):
            length = len(word_list[j])
            swap = 1
        else:
            length = len(word_list[i])
            swap = 0
        count = 0
        for k in range(length):

            if ord(word_list[i][k]) > ord(word_list[j][k]):

                temp = word_list[i]
                word_list[i] = word_list[j]
                word_list[j] = temp
                break
            elif ord(word_list[i][k]) == ord(word_list[j][k]):
                count += 1
                continue
            else:
                break
        if count == length:
            if swap:
                temp1 = word_list[i]
                word_list[i] = word_list[j]
                word_list[j] = temp1

print(word_list)

def is_prime(num):
    '''
    Naive method of checking for primes.
    '''
    for n in range(2,num):
        if num % n == 0:
            print(num,'is not prime')
            break
    else: # If never mod zero, then prime
        print(num,'is prime!')

print(is_prime(10))

import math

def is_prime2(num):
    '''
    Better method of checking for primes.
    '''
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

print(is_prime(151))

print ('I have aaded this code...please take a pull first')
