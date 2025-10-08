#Problem7.py
#Project Euler problem 7

from NumberTests import isPrime

def main():
    limit = 10001
    count = 1 #primes found so far (already including 2)
    num = 1 #current number being tested
    
    while count < limit:
       num = num + 2 #will only check odd numbers
       if isPrime(num):
          count = count + 1

    print("The 10001st prime number is:", num)

if __name__ == '__main__':
  main() 
