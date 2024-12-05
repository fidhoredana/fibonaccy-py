import os
import time
from mpmath import mp

def main():
    while True:

        print("""
        ***********************************************
        *                                           *
        *      Fibonacci Calc - by Fidho Redana      *
        *      Just for fun!                         *
        *                                           *
        *     ________________________________      *
        *    |                                |     *
        *    |    Welcome to Fibonacci Land!    |     *
        *    |________________________________|     *
        *                                           *
        ***********************************************
        *   Get ready to calculate some big Fibonacci numbers!   *
        ***********************************************
        """)

        try:
            limit = int(input("Enter the Fibonacci length: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        mp.dps = 10000  
        a = mp.mpf(1)
        b = mp.mpf(0)

        start_time = time.time()

        for i in range(limit):

            c = a + b
            a, b = b, c

        end_time = time.time()

        print(f"Fibonacci Number {limit}: {b}")

        time_taken = end_time - start_time
        print(f"Calculation Time: {time_taken} seconds")

        restart = input("Do you want to calculate another Fibonacci number? (Y/N): ").strip().lower()

        if restart != 'y':
            print("Exiting the program. Goodbye!")
            break

        if os.name == 'nt':  
            os.system('cls')
        else:  
            os.system('clear')

if __name__ == "__main__":
    main()
