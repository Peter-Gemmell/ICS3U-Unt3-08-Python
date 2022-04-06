#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on April 2022
# This program calculates if leap year
def main():
    # this function calculates if leap year

    # input
    year_number_string = input("What is the year number: ")

    # process & output
    try:
        year_number = int(year_number_string)

        if year_number % 4 == 0:

            if year_number % 100 == 0:

                if year_number % 400 == 0:
                    print("Is a leap year.")

                else:
                    print("Is not a leap year.")

            else:
                print("Is a leap year.")

        else:
            print("Is not a leap year.")

    except Exception:
        print("Invalid year entered, please try again.")
    print("Done.")


if __name__ == "__main__":
    main()
