#!/usr/bin/env python3
import DarkSky
import argparse

def main():

    cmd_parser = argparse.ArgumentParser(description='Get the weather forecast')
    cmd_parser.add_argument('-p', action='store_true', help='print the forecast request')
    cmd_parser.add_argument('-s', action='store_true', help='save the forecast request to a json file')
    cmd_parser.add_argument('-M', action='store_true', help='print the minutely forecast request')
    cmd_parser.add_argument('-H', action='store_true', help='print the hourly forecast request')
    cmd_parser.add_argument('-D', action='store_true', help='print the daily forecast request')
    cmd_parser.add_argument('-F', action='store_true', help='print the flags ')

    args = cmd_parser.parse_args()

    # always print (lat, lon), timezone, offset; currently data; weather alerts
    report = DarkSky.ForecastRequest()
    print(report)  # prints (lat, lon), timezone, offset
    report.printCurrentlyWeatherData()  # print the currently forecast
    report.printAlerts()  # print any forecast weather alerts

    if args.p:
        report.printForecastRequest()  # prints requested JSON file
        print()
    
    if args.s:
        report.saveForecastRequest()  # saves requested JSON file to folder
        print()

    if args.M:
        report.formattedMinutelyWeatherData()
        print()

    if args.H:
        report.formattedHourlyWeatherData()
        print()

    if args.D:
        report.formattedDailyWeatherData()
        print()

    if args.F:
        report.printFlags()
        print()

    print('Powered by Dark Sky: https://darksky.net/poweredby/')
    
    
if __name__ == '__main__':
    main()
