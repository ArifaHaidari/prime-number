"""https://github.com/ArifaHaidari/prime-number"""
#program to find the Prime and Composite number. by Arifa Haidari
import sympy as smp

try:
    number = int(input('Enter a number : '))
except(ValueError) :
    print('Please enter an integer !')
num = number
prime_factors = []
if smp.isprime(number) :
    prime_factors.append(number)
    print(num, " is Prime number -> ")

else :
    for i in range(2, int(number/2) + 1) :   
        """while figuring out prime factors of a given number, n
        keep in mind that a number can itself be prime or if not, 
        then all its prime factors will be less than or equal to its int(n/2 + 1)"""
        if smp.isprime(i) and number % i == 0 :
            while(number % i == 0) :
                prime_factors.append(i)
                number = number  / i
    print(num, " is Composite number -> ")
    # print('prime factors of ' + str(num) + ' - ')
for i in prime_factors :
    print(i, end = ' ' + " ")
print("With 1st method number of iteration is :", num -2)
print("With 2nd method number of iteration is :", len(prime_factors))
