# ML Program to find the equation of a linear regression line
# of the form y = mdays + c and predict the y for given days

# importing modules
import pandas as pd  # to use a .csv file
import matplotlib.pyplot as plt  # for plotting scatter and regression

# functions
def stockinput():
    try:
        global stock_name
        stock_name = input("\nEnter stock name of the company => ")
        global df 	# dataframe
        df = pd.read_csv(stock_name + '.csv')
    except IOError:
        print("That stock is not in our database. Try another")
        stockinput()
#comment

def plotter(x, y, resx, resy, predx, predy):
    print('\nPlotting graphs...')
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.plot(resx, resy)
    plt.scatter(predx, predy)
    plt.show()


# ---main---
stockinput()
days = [x for x in range(1, 31)]  # these will be days
y = list(df['close'].head(30))    # respective stock prices(close)

meandays = sum(days) / 30
meany = sum(y) / 30

numerator = 0
denominator = 0

for i in range(30):
    first = (days[i] - meandays)
    second = (y[i] - meany)
    b = (days[i] - meandays) ** 2
    numerator = numerator + first * second
    denominator = denominator + b
m = numerator / denominator  # Here, m is the slope of the regression line
c = meany - m * meandays  # Here, c is the intercept of the regression line

choice = int(input("\nEnter (1-future value) or (2-when to sell) => "))
if choice == 1:
    predday = int(input("Predict the value after how many days? => "))
    predicted_y = m * (predday + 30) + c
    if predday <= 10:
        print("\nThe predicted value of the ", stock_name,
              " stock after ", predday, " days is $", round(predicted_y, 2))
    else:
        print("WARNING")
        print("Unreliable predictions ahead!")
        print("\nThe predicted value of the ",
              stock_name.upper(), " stock after ",
              str(predday), " days is $", round(predicted_y, 2))

    resx = [1, predday + 30]
    resy = [y[0], predicted_y]
    predx = [predday + 30]
    predy = [predicted_y]
    plotter(days, y, resx, resy, predx, predy)
elif choice == 2:
    req = int(input("\nAt which value would you like to sell? => "))
    next = int((req - c) / m)
    if next > 0:
        print("\nYou should sell your stock after ", next, " days")
    else:
        print("It's not too late! Sell it now!")
else:
    print("\nWrong Choice!")
