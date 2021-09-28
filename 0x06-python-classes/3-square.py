#!/usr/bin/python3
"""
This module defines a Square class
Its implements value and type checks for its attributes
"""


class Square:
        """Square implementation
        """
        def __init__(self, size=0):
            if type(size) != int:
                raise TypeError('size must be an integer')
            elif __size < 0:
                raise ValueError('__size must be >= 0')
            self.__size = __size

            def area(self):
                return (self.__size * self.__size)
