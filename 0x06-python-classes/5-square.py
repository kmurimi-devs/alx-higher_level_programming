#!/usr/bin/python3
""" Define class of Square"""


class Square:
    """ Rep a square"""

    def __init__(self, size=0):
        """initialize new square"""

        self.__size = size

    @property
    def size(self):
        """Get size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print square using #"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
