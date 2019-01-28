#! /usr/bin/python3
from math import sqrt

def compute_relative_evo(period = 0, input_list = []):
    if (len(input_list) > period):
        try:
            value = round((input_list[-1] / input_list[-(1 + period)] - 1) * 100)
            return '{}'.format(value)
        except (ValueError, FloatingPointError):
            return "nan"
    return "nan"

def compute_std_deviation(period = 0, input_list = []):
    if (len(input_list) >= period):
        try:
            avg = sum(input_list[-period:]) / period
            std_dev = sqrt(sum(map(lambda x:(x - avg)**2, input_list[-period:])) / period)
            return '{:.2f}'.format(std_dev)
        except (ValueError, FloatingPointError, ZeroDivisionError):
            return "nan"
    return "nan"

def compute_increase_avg(period = 0, input_list = []):
    if (len(input_list) > period):
        try:
            avg_inc = (input_list[-1] - input_list[-(period + 1)]) / period
            return '{:.2f}'.format(avg_inc)
        except (ValueError, FloatingPointError, ZeroDivisionError):
            return "nan"
    return "nan"

def compute_switch_status(period, input_list):
    if (len(input_list) > period + 1):
        try:
            value = round((input_list[-1] / input_list[-(1 + period)] - 1) * 100)
            prevalue = round((input_list[-2] / input_list[-(2 + period)] - 1) * 100)
            if (abs(prevalue + value) != abs(prevalue) + abs(value)):
                return "\ta switch occurs"
        except (ValueError, FloatingPointError):
            return ""
    return ""


def display_final():
    print("OK")

def display_results(period, input_value, input_list):
    print("g={}\tr={}%\ts={}{}".format(
    compute_increase_avg(period, input_list),
    compute_relative_evo(period, input_list),
    compute_std_deviation(period, input_list),
    compute_switch_status(period, input_list)))

def groundhog(period):
    input_value = input()
    input_list = []
    trend_switch_nb = 0
    while (input_value != "STOP"):
        try:
            input_list.append(float(input_value))
            display_results(period, input_value, input_list)
        except ValueError:
            continue
        input_value = input()
    display_final()
