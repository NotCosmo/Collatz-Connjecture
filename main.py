import time

'''

The Collatz Algorithm states that you can take a random number x:

if x is an odd number, you use the formula 3x+1 or you multiply it by 3 and add one.

else, if it's an even number, you divide the number by 2.

no matter what number you start with, you'll end up with the combination 4 -> 2 -> 1, which loop back to eachother.

'''

def check(n: int):

    steps = 0
    _n = n
    while True:

        # Number is 1 (Algorithm Stops & Moves on)
        if n == 1:
            break

        # Number is even (Divide by 2)
        elif n % 2 == 0:
            n = n / 2
            steps += 1

        # Number is odd (Multiply by 3, add 1)
        else:
            n = n*3 + 1
            steps += 1
    
    # print(str(_n) + " took " + str(steps) + " steps to end.")
    # My original code uses the format above as my VSC does not like f-strings.
    print(f"{_n} took {steps} steps to end.")
    
''' Algorithm Variables/Setup '''

def main():

    print("\n")
    lm = int(input(">> How many numbers do you want to cycle through? (Algorithm will stop at this number.): "))
    x = int(input(">> Enter starting number (Advised to start with 1): "))
    delay = int(input(">> Enter delay (Recommended to leave at 0 unless you want a slow algorithm.): "))
    print("\n")

    while x < (lm+1):

        check(x)
        x += 1
        time.sleep(delay)

if __name__ == "__main__":
    main()
