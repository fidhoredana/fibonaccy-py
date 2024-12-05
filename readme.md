# Fibonacci Calculator

This script calculates Fibonacci numbers up to a specified length using the `mpmath` library, which supports large number computations. This is just a fun little project, so feel free to explore and enjoy the power of Fibonacci numbers!

## Description

This program calculates Fibonacci numbers using an iterative approach, and thanks to the `mpmath` library, it can compute very large Fibonacci numbers with high precision. The script allows you to calculate multiple Fibonacci numbers in one go, so you don't need to restart the program every time. It's a simple and fun way to work with Fibonacci numbers — nothing fancy, just a program for fun!

## Requirements

To run this script, you’ll need:

1. **Python 3.x**  
   Make sure you have Python installed. If you don’t, you can grab it from [python.org](https://www.python.org/).

2. **`mpmath` Library**  
   This script uses the `mpmath` library for large number computations. Install it with pip by running:

   ```bash
   pip install mpmath
   ```

## How to Run

1. Clone or download this project to your local directory.
2. Install the necessary libraries by running:

   ```bash
   pip install mpmath
   ```

3. Once that's done, run the script with this command:

   ```bash
   python3 fibonaccy.py
   ```

4. The program will ask you to enter the Fibonacci length you want to calculate. For example, if you want the 1000th Fibonacci number, just enter `1000` when prompted:

   ```bash
   Enter the Fibonacci length: 1000
   ```

5. After the calculation, the program will show you the Fibonacci number and how long it took to calculate it.

6. Once it’s done, the program will ask if you want to calculate another Fibonacci number. If you choose `Y`, it will clear the screen and restart, showing the welcome message again and letting you input a new Fibonacci length. If you choose `N`, it will exit.

## Example Output

```bash
   ***********************************************
   *                                             *
   *      Fibonacci Calc - by Fidho Redana       *
   *      Just for fun!                          *
   *                                             *
   *     ________________________________        *
   *    |                                |       *
   *    |    Welcome to Fibonacci Land!  |       *
   *    |________________________________|       *
   *                                             *
   ***********************************************
* Get ready to calculate some big Fibonacci numbers! *
   ***********************************************
Enter the Fibonacci length: 1000
Fibonacci Number 1000: 7033036771142281582183525487718354978018087...
Calculation Time: 0.0035 seconds
Do you want to calculate another Fibonacci number? (Y/N): Y
```

## Code Explanation

- **Input**: The program asks you for the Fibonacci length you want to calculate.
- **Fibonacci Calculation**: It calculates the Fibonacci number iteratively.
- **`mpmath`**: The `mpmath` library makes sure the calculation can handle large Fibonacci numbers with high precision.
- **Calculation Time**: The program also tracks and displays how long it took to compute the Fibonacci number.
- **Restart**: After each calculation, it asks if you want to calculate another Fibonacci number. If you type `Y`, the program will restart with a cleared screen. If `N`, it exits.
