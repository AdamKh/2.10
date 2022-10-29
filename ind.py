#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sum_mod_min(*args):
    if args:
        mni = 0
        mn = abs(args[0])
        s = 0
        i = 0
        for ch in args:
            if abs(ch) < mn:
                mni = i
                mn = ch
            i += 1
        for ch in args[mni + 1:]:
            s += abs(ch)
        return s
    else:
        return None


if __name__ == "__main__":
    print(sum_mod_min(-100, 2, -3, 4))
