#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def sr_geom(*args):
    if args:
        values = [float(arg) for arg in args]
        n = len(values)
        pr = 1
        k = 0
        for k in range(n):
            pr *= values[k]
            k += 1
        g = math.pow(pr, 1 / k)
        return g
    else:
        return None


def sr_garm(*args):
    if args:
        values = [float(arg) for arg in args]
        n = len(values)
        s = 0
        for k in range(n):
            s += 1/values[k]
        g = n / s
        return g
    else:
        return None


def intro(**kwargs):
    for key, value in kwargs.items():
        print("{} is {}".format(key, value))


if __name__ == "__main__":
    print(sr_geom(1, 2, 3, 4))
    print(sr_garm(1, 2, 3, 4))

    print('\n')
    intro(
        Firstname="Sita",
        Lastname="Sharma",
        Phone=1234567890,
        Age=22
    )

    print('\n')
    intro(
        Firstname="John",
        Lastname="Wood",
        Email="john@mail.com",
        Country="Wakanda",
        Phone=9876543210,
        Age=25
    )
