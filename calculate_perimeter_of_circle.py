#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: April 2021
# This program calculates the circumference of a circle

import math
import constants


def main():
    radius = int(input("What is the radius of the circle in mm?"))
    print()
    print("Circumference: {} mm".format(radius * constants.TAU))


if __name__ == "__main__":
    main()
