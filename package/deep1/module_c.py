#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-09-16 16:01:41


from module_b import module_b_print


def module_c_print():
    print("module c")


if __name__ == "__main__":
    module_b_print()
