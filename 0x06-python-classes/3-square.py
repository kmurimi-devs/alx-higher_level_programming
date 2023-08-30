#!/usr/bin/python3
""" Define class of Square"""


class Square:
    """ Rep a square"""

    def __init__(self, size=0):
        """initialize new square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate area of square"""
        return (self.__size * self.__size)
