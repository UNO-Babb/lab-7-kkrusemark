#Problem10.py
#Project Euler problem 10

from NumberTests import isPrime

def main():
    limit = 2000000
    total = 0
    
    for n in range(2,limit):
       if isPrime(n):
          total = total + n

    print("The sum of all prime #s below 2 million is:", total)

if __name__ == '__main__':
  main()
