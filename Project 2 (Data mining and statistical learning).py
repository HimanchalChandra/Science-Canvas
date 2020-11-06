import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing


# Function to find outliers using Modified IQR method
def clean_outliers_IQR(df, basis_column):
    outliers_index = []
    outliers_value = []
    chk = df[basis_column]
    first_quartile = chk.quantile(0.25)
    third_quartile = chk.quantile(0.75)
    inter_quartile_range = third_quartile - first_quartile
    lower_threshold = first_quartile - (1.5 * inter_quartile_range)
    upper_threshold = third_quartile + (1.5 * inter_quartile_range)
    for index, value in enumerate(chk):
        if (not (lower_threshold < value < upper_threshold)):
            outliers_index.append(index)
            outliers_value.append(value)
    filtered_df = df.drop(df.index[outliers_index])
    return outliers_index, outliers_value, filtered_df


df = pd.read_csv('abalone.csv')  # loading the data
df1 = pd.read_csv('abalone.csv')  # again loading the data to show label encoding
df['Age'] = df['Rings'] + 1.5  # creating a new attribute using existing attribute

attributes = list(df.columns.values)  # listing the attributes
attributes.remove('Sex')

# creating a new dataframe for statistical data
newdf = pd.DataFrame(index=['Max', 'Min', 'Mean', 'Median', 'Standard Deviation'], columns=attributes)

# computation of various statistics
for index, row in newdf.iterrows():
    for value in attributes:
        if (index == 'Max'):
            row[value] = df[value].max()
        if (index == 'Min'):
            row[value] = df[value].min()
        if (index == 'Mean'):
            row[value] = df[value].mean()
        if (index == 'Median'):
            row[value] = df[value].median()
        if (index == 'Standard Deviation'):
            row[value] = df[value].std()

print("----------------------Statistical derivations----------------------")
print(newdf.T)

print("-------------------------------------------------------------------")
print("")
print("")
print("")
print("-----------------Correlation between different attributes------------------")
corr_df = df.corr()  # creating of another dataframe for correlation matrix between attributes using the corr() function
print(corr_df)
print("---------------------------------------------------------------------------")

print("")
print("")
print("")
print("------------------Correlation Heatmap-------------------")
# masking upper triangular matrix of the correlation matrix
masking_corr_matrix = np.zeros_like(corr_df, dtype=np.bool)
masking_corr_matrix[np.triu_indices_from(masking_corr_matrix)] = True
current_palette = sns.color_palette()
with sns.axes_style("white"):
    sns.heatmap(corr_df, mask=masking_corr_matrix)
    plt.show()
print("--------------------------------------------------------")

print("")
print("")
print("")

# Outlier detection based on various attrbutes
print("-------------Outlier Detection using IQR---------------")
outliers_index, outliers_value, filtered_df = clean_outliers_IQR(df, 'Height')
print("Outlier Detection on the basis of Height")
print("Outlier Index = ", outliers_index)
print("Outlier Value = ", outliers_value)
print("")
print("")
outliers_index, outliers_value, filtered_df = clean_outliers_IQR(df, 'Diameter')
print("Outlier Detection on the basis of Diameter")
print("Outlier Index = ", outliers_index)
print("Outlier Value = ", outliers_value)
print("")
print("")
outliers_index, outliers_value, filtered_df = clean_outliers_IQR(df, 'Length')
print("Outlier Detection on the basis of Length")
print("Outlier Index = ", outliers_index)
print("Outlier Value = ", outliers_value)
print("")
print("")
outliers_index, outliers_value, filtered_df = clean_outliers_IQR(df, 'Whole weight')
print("Outlier Detection on the basis of Whole weight")
print("Outlier Index = ", outliers_index)
print("Outlier Value = ", outliers_value)
print("--------------------------------------------------------------------")

print("")
print("")
print("")

# Various scatter plots with regrssion lines for various attribute combinations
print("----------Scatter plots with Regression line-----------")
sns.regplot(df.Rings, df.Height, color='b')
plt.title('Height VS Rings')
plt.show()
print("")
print("")
sns.regplot(df.Rings, df['Whole weight'], color='orange')
plt.title('Whole weight VS Rings')
plt.show()
print("")
print("")
sns.regplot(df.Rings, df.Length, color='red')
plt.title('Length VS Rings')
plt.show()
print("")
print("")
sns.regplot(df.Rings, df.Diameter, color='pink')
plt.title('Diameter VS Rings')
plt.show()
print("--------------------------------------------------------")

print("")
print("")
print("")

# Using label encoder to encode the Sex attribute (convert from categorical to numerical attribute)
# This encoded data is in another dataframe i.e. df1
print("-------------------------Encoding of categorical features--------------------------")
label_encoder = preprocessing.LabelEncoder()
label_encoder.fit(df['Sex'])
df1['Sex'] = label_encoder.transform(df['Sex'])
print("Original data:-")
print("")
print(df.head())  # Original data
print("")
print("")
print("")
print("Encoded data with the Sex attibute encoded (categorical to numeric feature):-")
print("")
print(df1.head())  # Encoded data (sex attribute encoded)
print("-----------------------------------------------------------------------------------")

print("")
print("")
print("")

# Creating boxplots
print("-------------------------Box plots--------------------------")
df.boxplot(column='Length', by='Rings')
plt.show()
print("")
print("")
df.boxplot(column='Diameter', by='Rings')
plt.show()
print("")
print("")
df.boxplot(column='Height', by='Rings')
plt.show()
print("")
print("")
df.boxplot(column='Whole weight', by='Rings')
plt.show()
print("------------------------------------------------------------")

print("")
print("")
print("")

# Calculations to create histograms on different analysis
Height_variation = []
Length_variation = []
Weight_variation = []
Diameter_variation = []
# Categorising the attributes on the basis of their values
for index, value in enumerate(df['Sex']):
    if (df['Height'][index] < 0.15):
        Height_variation.append('Height less than 0.15 mm')
    if (df['Height'][index] > 0.15):
        Height_variation.append('Height more than 0.15 mm')

    if (df['Length'][index] < 0.5):
        Length_variation.append('Length less than 0.5 mm')
    if (df['Length'][index] > 0.5):
        Length_variation.append('Length more than 0.5 mm')

    if (df['Diameter'][index] < 0.35):
        Diameter_variation.append('Diameter less than 0.35 mm')
    if (df['Diameter'][index] > 0.35):
        Diameter_variation.append('Diameter more than 0.35 mm')

    if (df['Whole weight'][index] < 0.8):
        Weight_variation.append('Weight less than 0.8 grams')
    if (df['Whole weight'][index] > 0.8):
        Weight_variation.append('Weight more than 0.8 grams')

# Creating histograms based on different analysis
print("-------------------------Histograms--------------------------")
plt.hist(df['Sex'], label='Sex wise distribution of data (F - Female, M - Male, I - Infant) ', histtype='stepfilled',
         color='lightseagreen')
plt.legend(loc=2)
plt.show()
print("")
print("")
plt.hist(Height_variation, histtype='stepfilled', color='lightcoral')
plt.title('Height wise distribution')
plt.show()
print("")
print("")
plt.hist(Length_variation, histtype='stepfilled', color='palegreen')
plt.title('Length wise distribution')
plt.show()
print("")
print("")
plt.hist(Weight_variation, histtype='stepfilled', color='orange')
plt.title('Weight wise distribution')
plt.show()
print("")
print("")
plt.hist(Diameter_variation, histtype='stepfilled', color='lightseagreen')
plt.title('Diameter wise distribution')
plt.show()
print("------------------------------------------------------------")