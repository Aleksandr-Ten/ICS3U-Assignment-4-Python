#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: April 2022
# This program tells user the name of the weekday


def main():
    # this function calculates the name of the weekday

    # input
    user_input_string = input("Enter the number: ")

    # process and output
    try:
        user_input = int(user_input_string)
        if user_input == 1:
            print("Monday")
        elif user_input == 2:
            print("Tuesday")
        elif user_input == 3:
            print("Wednesday")
        elif user_input == 4:
            print("Thursday")
        elif user_input == 5:
            print("Friday")
        elif user_input == 6:
            print("Saturday")
        elif user_input == 7:
            print("Sunday")
        else:
            print("Incorrect integer. Please try again.")
    except Exception:
        print("Please input an integer")
    finally:
        print("\nDone")


if __name__ == "__main__":
    main()
