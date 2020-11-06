#Fitting a line to a given data points
import matplotlib.pyplot as plt
from statistics import mean

#Function to calculate the slope and y_intercept of the regression line
def slope_intercept_best_fit_line(year, house_prices):
    x_mean = mean(year)
    y_mean = mean(house_prices)
    num = 0
    den = 0
    for index, value in enumerate(year):
        num = num + (year[index]-x_mean)*(house_prices[index]-y_mean)
        den = den + (year[index]-x_mean)**2
    slope = num/den
    y_intercept = y_mean - (slope*x_mean)
    return slope, y_intercept

#Feeding the given data
year = [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002]
year_encoded = [1, 2, 3, 4, 5, 6, 7, 8]
house_prices = [53807, 55217, 55209, 55415, 63100, 63206, 63761, 65766]

slope, y_intercept = slope_intercept_best_fit_line(year, house_prices)
print ("Slope of best-fit line = ", slope)
print ("Y intercept of best-fit line = ", y_intercept)


y_bestfitline = []
for i in year:
    y_bestfitline.append((slope*i)+y_intercept)

predict_x = [2010,2017]
predict_y = []
for i in predict_x:
    predict_y.append((slope*i)+y_intercept)
    print ("The predicted house price for year ", i, " is ",(slope*i)+y_intercept)

plt.scatter(year, house_prices, label = 'DATA')
plt.scatter(predict_x, predict_y, label = 'PREDICTION', color = 'g')
plt.plot(year+predict_x, y_bestfitline+predict_y, color = 'r', label = 'BEST FIT LINE')
plt.legend(loc=4)
plt.style.use('ggplot')
plt.show()