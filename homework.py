#!/usr/bin/env python3

# Created by Tong Gong
# Created time December 2020
# This is a Nested Loops program.


def main():
    # This is the function to run Nested Loops.

    counter = 0

    # Process & output
    for counter in range(1000, 2001):
        print(counter, end = " ")
        counter + 1
        if counter % 5 == 4:
            print(end = "\n")


if __name__ == "__main__":
    main()
