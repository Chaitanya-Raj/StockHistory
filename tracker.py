from pprint import pprint
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('seaborn-poster')  # sets the size of the charts
style.use('ggplot')
API_KEY = 'OQ7O1XM3XG9FF32B'


choices = {1: 'Intraday', 2: "Daily", 3: "Daily Adjusted", 4: "Weekly",
           5: "Weekly Adjusted", 6: "Monthly", 7: "Monthly Adjusted"}


while(True):
    choice = int(input(
        "\n\n\n\nChoose an option:\n1.Intraday\n2.Daily\n3.Daily Adjusted\n4.Weekly\n5.Weekly Adjusted\n6.Monthly\n7.Monthly Adjusted\n0.Exit\n\n"))

    if choice == 0:
        exit("Exiting the program...")

    ts = TimeSeries(key=API_KEY, output_format='pandas')

    symbol = input("\nInput a valid ticker : ")
    n = int(input("How many rows to display : "))

    if choice == 1:
        interval = input(
            "\nInput a valid interval '1min, 5min, 15min, 30min, 60min' : ")
        data, meta_data = ts.get_intraday(
            symbol=symbol, interval=interval, outputsize='compact')

    elif choice == 2:
        data, meta_data = ts.get_daily(
            symbol=symbol, outputsize='compact')

    elif choice == 3:
        data, meta_data = ts.get_daily_adjusted(
            symbol=symbol, outputsize='compact')

    elif choice == 4:
        data, meta_data = ts.get_weekly(
            symbol=symbol)

    elif choice == 5:
        data, meta_data = ts.get_weekly_adjusted(
            symbol=symbol)

    elif choice == 6:
        data, meta_data = ts.get_monthly(
            symbol=symbol)

    elif choice == 7:
        data, meta_data = ts.get_monthly_adjusted(
            symbol=symbol)

    print(f"\n\n{symbol}\n")
    pprint(data.head(n))
    graph = input("\nDo you want to plot a graph? (y/n) ")
    if graph == 'y':
        data['4. close'].plot()
        if choice == 1:
            plt.title(
                f'{choices[choice]} Time Series for the {symbol} stock ({interval})')
        else:
            plt.title(
                f'{choices[choice]} Time Series for the {symbol} stock')
        plt.show()
