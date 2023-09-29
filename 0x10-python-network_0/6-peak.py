#!/usr/bin/python3
"""Python script that Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Function definition"""
    if not list_of_integers:
        return None

    my_list = list_of_integers
    peak_tmp = peak = my_list[0]
    length = len(my_list) - 1
    for i in range(0, length // 2 + 1):
        peak_tmp = my_list[i] if (
                my_list[i] > my_list[length - i]) else my_list[length - i]
        peak = peak_tmp if peak_tmp > peak else peak

    return peak
