#! /usr/bin/python3

def compute_g(input_temp, input_list, input_average):
    return "nan"

def compute_r(input_temp, input_list, last_period_average, period):
    if (len(input_list) >= period):
        return str(((input_temp - last_period_average) / last_period_average) * 100)
    return "nan"

def compute_s(input_temp, input_list, input_average):
    return "nan"

def groundhog(period):
    print(period)
    input_temp = input()
    input_list = []
    input_average = float
    last_period_average = float
    while (input_temp != "STOP"):
        input_list.append(float(input_temp))
        input_average = (sum(input_list) / len(input_list))
        last_period_average = (sum(input_list[period::-1]) / len(input_list[period::-1]))
        print("g=" + compute_g(float(input_temp), input_list, input_average) + "\tr=" + compute_r(float(input_temp), input_list, last_period_average, period) + "%\ts=" + compute_s(float(input_temp), input_list, input_average))
        input_temp = input()
