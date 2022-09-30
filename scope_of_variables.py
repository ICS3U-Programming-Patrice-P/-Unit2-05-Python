#!/usr/bin/env python3

# Created by: Patrice Pat-Odita
# Created on: Sep  29,2022
# This program shows assingment statements


def main():
    # variable definition
    number_of_students = 12
    width = 40.5
    length = 10.0
    some_words1 = "Hello"
    some_words2 = "Wordl!"

    # using assignment statements
    number_of_students = number_of_students + 12
    area_of_rectangle = length * width
    hello_world = some_words1 + ", " + some_words2

    # output
    print("The number of students is: " + str(number_of_students))
    print("The area of a rectangle is: " + str(area_of_rectangle) + " cm²")
    print(hello_world)

    print("\nDone.")


if __name__ == "__main__":
    main()
