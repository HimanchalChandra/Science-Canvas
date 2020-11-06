#REGRESSION ANALYSIS OF FOREST FIRE DATASET
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mean
from math import sqrt
import statsmodels.formula.api as smap

df = pd.read_csv('forestfires.csv')#loading the data
df1 = pd.read_csv('forestfires.csv')#loading the data

def slope_intercept_best_fit_line(year, house_prices):#Function to calculate the slope and y-intercept of the regression line
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

def find_rmse(y, Y):#Function to calculate the ROOT MEAN SQUARE ERROR
    rmse = 0
    for index, value in enumerate(y):
        rmse = rmse + (value - Y[index]) ** 2
    rmse = sqrt(rmse/len(y))
    return rmse

def find_R_squared(y, Y):#Function to calculate R SQUARED VALUE
    squared_error_mean =  0
    squared_error_line = 0
    y_mean = y.mean()
    for index, value in enumerate(y):
        squared_error_mean = squared_error_mean+(y[index] - y_mean) ** 2
        squared_error_line = squared_error_line+(y[index] - Y[index]) ** 2
    R_squared = 1 - (squared_error_line/squared_error_mean)
    return R_squared


def predict_simple_linear_regression(temperature, slope, y_intercept):
    predicted_value = (slope*temperature)+y_intercept
    
    return predicted_value


#Converting categorical features to numerical features for analysis (ENCODING)
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun','jul', 'aug', 'sep', 'oct', 'nov', 'dec']
days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
df1['month'] = [months.index(month) for month in df['month'] ]
df1['day'] = [days.index(day) for day in df['day'] ]
df1['month'] = df1['month'] + 1
df1['day'] = df1['day'] + 1

attributes = list(df.columns.values)
attributes1 = list(df.columns.values)
attributes1.remove('area' )#Getting rid of unnecessary columns
attributes1.remove('day' )#Getting rid of unnecessary columns
attributes.remove('month')#Getting rid of unnecessary columns
attributes.remove('day')#Getting rid of unnecessary columns

#New dataframe for to show statistical analysis    
newdf = pd.DataFrame(index = ['max','min','mean','median','standard deviation'], columns = attributes)

#Calculation for statistical analysis of data
for index ,row in newdf.iterrows():  
    for value in attributes:
        if(index == 'max'):
            row[value] = df[value].max()
        if(index == 'min'):
            row[value] = df[value].min()
        if(index == 'mean'):
            row[value] = df[value].mean()
        if(index == 'median'):
            row[value] = df[value].median()
        if(index == 'standard deviation'):
            row[value] = df[value].std()

print("---------------------STATISTICS------------------")        
print(newdf.T)

#Calculation of correlation between area attribute and other attributes
df_corr = df.corr()
area_corr = df_corr['area'].drop('area')
print("")
print("")
print("-------------Correlation between area and other attributes-----------")
print (area_corr)
area_corr_absolute = area_corr.abs()
max_area_corr = area_corr_absolute.max()#To check the attribute which is highly correlated to area burnt
max_area_corr_index = list(area_corr_absolute).index(max_area_corr)
print("")
print("")
print("--------------------------------------------------------")
print("The attribute which is most correlated to area is",attributes[max_area_corr_index])
print("--------------------------------------------------------")


#Lists to store the rmse and R squared values for different regression models
rmse = []
R_squared = []

#Creating different regression models using the slope_intercept_best_fit_line function
#Also calculating the rmse and R squared values for different models
for index, value in enumerate(attributes1):
    m, y_intercept = slope_intercept_best_fit_line(df1[value], df1['area'])
    print ("")
    print ("")
    print ("")
    print ("---------------------AREA VS",value,"---------------------")    
    print ("Linear Model For Area vs",value," is [area = " , m, "*" , value," + ", y_intercept, "]")
    print ("")
    x_values = df1[value]
    y_values = df1['area']
    Y_values = m * x_values + y_intercept
    rmse.append(find_rmse(y_values,Y_values))
    print ("Root Mean Squared Error is ", find_rmse(y_values,Y_values))
    print ("")
    R_squared.append(find_R_squared(y_values,Y_values))
    print ("")
    print ("R-Squared Value is ", find_R_squared(y_values,Y_values))
    plt.scatter(x_values, y_values, label = 'data')
    title = 'area VS ' + value + '  GRAPH'
    plt.suptitle(title)
    plt.style.use('ggplot')
    plt.plot(x_values, Y_values, color = 'b', label = 'Regression Line')
    plt.legend()
    plt.show()
    print ("-------------------------------------------------------")

#Final analysis on the basis of R squared value
#R-Squared value simply tells us the percentage of dependent variable's change that can be predicted
#by the independent variable
#Conclusion is on the basis that higher the R squared value, the better the model fits the data
 
print("FINAL CONCLUSION :-")
print("More",attributes1[list(R_squared).index(max(R_squared))], "More Area Burnt")
print ("-------------------------------------------------------")

#Prediction on basis of temperature
#Collecting data for linear regression model on basis of temp
print ("")
print ("")
print ("")
print ("---------------Prediction on basis of simple linear regression---------------")
slope, y_intercept = slope_intercept_best_fit_line(df1['temp'], df1['area'])#Collecting data for linear regression model on basis of temp
temp = 40
print ("Value of temp for which area burnt is to be predicted is : ", temp)
print ("Predicted value of area burnt is ", predict_simple_linear_regression(temp, slope, y_intercept))
print ("-----------------------------------------------------------------------------")

#using statsmodel libraray to do multivariate linear regression
print ("")
print ("")
print ("")
print ("------------------------Multivariate linear regression-----------------------")
multivariate_linear_regression = smap.ols(formula = 'area~X+Y+month+day+FFMC+DMC+DC+ISI+temp+RH+wind+rain', data = df1).fit()
print(multivariate_linear_regression.summary())

#prediction on bais of the above created model
data = [4,4,12,2,85.4,25.4,349.7,2.6,4.6,21,8.5,0]
predictions = multivariate_linear_regression.predict()
print ("")
print ("")
print ("")
print ("")
print ("")
print ("------------Prediction on basis of Multivariate linear regression-----------")
X = 2
Y = 4
month = 8
day = 1
FFMC = 81.6
DMC = 56.7
DC = 665.6
ISI = 1.9
temperature = 21.9
RH = 71
wind = 5.8
rain = 0
print ("Value of attributes for which area burnt is to be predicted is : ")
print ("X = 6, Y = 3, month = 11, day = 3, FFMC = 79.5, DMC = 3, DC = 106.7, ISI = 1.1, temperature = 11.8, RH = 31, wind = 4.5, rain = 0")
print ("Predicted value of area burnt is ", 1.9002*X + 0.3241*Y + 2.9004*month + 1.3269*day - 0.1127*FFMC + 0.0966*DMC - 0.0315*DC - 0.7305*ISI + 0.9546*temperature - 0.1758*RH +1.2321*wind - 3.1958*rain)
print ("-----------------------------------------------------------------------------")