#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 16:09:20 2022

@author: Yixuan (Yvonne) Feng, Jingya Cheng, Tiya Zhang
"""


def get_data(path: str) -> list:
    """read the txt file and gives a list of lists of integers"""
    res_list = []
    with open(path, "r") as f:
        for line in f:
            int_list = [int(i) for i in line.split()]
            res_list.append(int_list)
        return res_list


get_data("/Users/chloehiddleston/Desktop/BIOSTAT821/example.txt")
# outcome list
x1 = get_data("/Users/chloehiddleston/Desktop/BIOSTAT821/example.txt")


import math


def analyze_data(mylist: list, string_option: str) -> float:
    """read a list of lists of intergers and return a string option that can be average, standard deviation, covariance or correlation"""
    list_elements = [item for sublist in mylist for item in sublist]
    count = 0
    for listElem in mylist:
        count += len(listElem)
        mean = sum(list_elements) / count
        average = round(mean, 1)
        variance = sum([((x - mean) ** 2) for x in list_elements]) / count
        sd = variance ** 0.5
        standard_deviation = round(sd, 1)

    covariance_temp_sum = 0
    x0_mean = math.fsum(mylist[0]) / len(mylist[0])
    x1_mean = math.fsum(mylist[1]) / len(mylist[1])
    for n in range(len(mylist[0])):
        covariance_temp_sum += (mylist[0][n] - x0_mean) * (mylist[1][n] - x1_mean)
    covariance = round((covariance_temp_sum / len(mylist[0])), 3)

    mean1 = sum(mylist[0]) / len(mylist[0])
    mean2 = sum(mylist[1]) / len(mylist[1])
    variance1 = sum([((x - mean1) ** 2) for x in mylist[0]]) / len(mylist[0])
    sd1 = variance1 ** 0.5
    variance2 = sum([((x - mean2) ** 2) for x in mylist[1]]) / len(mylist[1])
    sd2 = variance2 ** 0.5
    correlation = round((covariance / (sd1 * sd2)), 3)

    if string_option == "average":
        return average
    elif string_option == "standard deviation":
        return standard_deviation
    elif string_option == "covariance":
        return covariance
    elif string_option == "correlation":
        return correlation

    return 0.0


if __name__ == "__main__":
    print(analyze_data(x1, "average"))
    print(analyze_data(x1, "standard deviation"))
    print(analyze_data(x1, "covariance"))
    print(analyze_data(x1, "correlation"))
    print(analyze_data(x1, "average"))  
