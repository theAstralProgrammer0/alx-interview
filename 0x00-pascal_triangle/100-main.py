#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('100-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    triangle = pascal_triangle(5)
    print_triangle(pascal_triangle(5))

