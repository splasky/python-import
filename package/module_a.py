#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-09-16 15:53:06


def module_a_print():
    print(__name__)
    print(__loader__)
    print(__package__)
    print(__spec__)
    #  print(__path__)
    print(__cached__)
    print("module_a")
