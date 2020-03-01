from pprint import pprint
from alpha_vantage.timeseries import TimeSeries
API_KEY = 'OQ7O1XM3XG9FF32B'

choice = int(input(
    "\nChoose an option:\n1.Intraday\n2.Daily\n3.Daily Adjusted\n4.Weekly\n5.Weekly Adjusted\n6.Monthly\n7.Monthly Adjusted\n\n"))

ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
symbol = input("\nInput a valid ticker : ")
n = int(input("How many rows to display : "))

if(choice == 1):
    interval = input(
        "\nInput a valid interval '1min, 5min, 15min, 30min, 60min' :")
    data, meta_data = ts.get_intraday(
        symbol=symbol, interval=interval, outputsize='full')

elif(choice == 2):
    data, meta_data = ts.get_daily(
        symbol=symbol, outputsize='full')

elif(choice == 3):
    data, meta_data = ts.get_daily_adjusted(
        symbol=symbol, outputsize='full')

elif(choice == 4):
    data, meta_data = ts.get_weekly(
        symbol=symbol)

elif(choice == 5):
    data, meta_data = ts.get_weekly_adjusted(
        symbol=symbol)

elif(choice == 6):
    data, meta_data = ts.get_monthly(
        symbol=symbol)

elif(choice == 7):
    data, meta_data = ts.get_monthly_adjusted(
        symbol=symbol)

print(f"\n\n{symbol}\n")
pprint(data.head(n))
