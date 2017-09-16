#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-09-16 16:03:09

from package.module_a import module_a_print


def module_b_print():
    print("module b")


if __name__ == "__main__":
    print("module b execute!")
    module_b_print()
