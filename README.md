# Paralel Primes

The goal of this project is to compute all prime numbers below 1,000,000,000
(1B). To do this I will use the most popular method for calculating primes: The
[Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).
The **time complexity** of this algorithm is O(nlogn) where n is the limit of
primes. In the case above n 1 billion, totalling in almost 30 billion
operations. The **space complexity** is O(n) which for this example is
equivalent to 1 Gigabit though Python's overhead brings this closer to
3 Gigabytes. In gathering primes for problem solving I have used
[this code](https://github.com/jshams/mini-projects/tree/master/primes/sieve-of-eratosthenes). Let's make it faster!

## Methods for speeding up prime generator

### 1. Use a lower level language

Using a lower level language will decrease overhead and make programs run more
efficiently. Java's speeds can be up to
[25 times faster](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/python3-java.html)
than Python's. For even better performance, C++. It's estimated to be up to
[100 times faster](https://stackoverflow.com/questions/801657/is-python-faster-and-lighter-than-c)
than Python. Using these three languages I will benchmark their performances
using the sieve method.

### 2. Use PySpark for multicore processing

Usiing parallel processing, the task can be distributed among multiple
processors cutting down runtime speeds.

### 3. Use PySpark to save memory

One way to save memory is to use Python's bitmap which is smaller than an
actual array of booleans.

Further research is required to figure out how to use PySpark for this.

### 4. Combine 2 and 3 to Master Time and Space

By saving space and time this program will be able to run far more efficiently.
Hopefully by the end of this my expectations will be exceeded. For now, I code.
