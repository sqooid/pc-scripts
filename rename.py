#!/usr/bin/env python

"""
Renames files incrementally.

Based on file names of the format "int_additional.ext", all files with same "additional.ext" are renamed with their
corresponding integer
"""

import os

__author__ = "Lucas Liu"

# Old name input and parse
int_index = -1
old_name = ""
while int_index == -1:
    old_name = input("Input name format of files to be renamed (eg. example_%.ext): ")
    int_index = old_name.find("%")
old_start = old_name[:int_index]
old_end = old_name[int_index + 1:]

# New name input
int_index = -1
new_name = ""
while int_index == -1:
    new_name = input("Naming for renamed files (eg. example_%.ext): ")
    int_index = new_name.find("%")

cwd = os.getcwd()
# New name parse
for file in os.listdir(cwd):
    print(file)
    if old_start == file[:len(old_start)] and old_end == file[len(file) - len(old_end):]:
        destination = new_name[:int_index] + file[len(old_start):len(file) - len(old_end)] + new_name[int_index + 1:]
        print(destination)
        file = os.path.join(cwd, file)
        destination = os.path.join(cwd, destination)
        os.rename(file, destination)

print("Done")
