#!usr/bin/env python

# Created by: Cameron Teed
# Created On: September 2019
# this program gets you to guess my number

import random


def main():
    # this program gets you to guess my number

    # input
    very_secret = random.randint(1, 50+1)

    input("Please press enter ")

    while True:

        try:

            secret_number = input("Try to guess my number: ")

            secret_number = int(secret_number)

            while True:

                # process
                if secret_number < very_secret:
                    # output
                    print("")
                    print("Go higher.")
                    break

                if secret_number > very_secret:
                    print("")
                    print("Go lower.")
                    break

                # process
                else:
                    # output
                    print("")
                    print("Thats my number! (It was {})".format(very_secret))
                    break

            if secret_number == very_secret:
                break

        except ValueError:
            print("")
            print("")
            print("Please enter a integer.")


if __name__ == "__main__":
    main()
