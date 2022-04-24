#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: April 2022
# This program calculates the total price of croissants


def main():
    # this function calculates the total price

    # this is HST in Ontario
    HST = 1.13

    # input
    number_of_croissants_string = input(
        "Enter the number of croissants you would like to buy: "
    )

    # process & output
    try:
        number_of_croissants = int(number_of_croissants_string)
        total = number_of_croissants * 2.55
        if number_of_croissants < 6:
            print("The total is ${:0.2f}".format(total))
        elif number_of_croissants >= 6:
            print("The total is ${:0.2f}".format(total * HST))
    except Exception:
        print("Invalid input")
    finally:
        print("\nDone")


if __name__ == "__main__":
    main()
