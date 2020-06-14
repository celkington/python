import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as sns 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv(r'C:\Users\Chris\Documents\GitHub\python\house_price_project\house_price_data.csv')

##Example of a simple bar chart

# dataset.plot(x='price',y='sqft_living',style='o')
# plt.title('Effect of House Size on House Price')
# plt.xlabel('House Price ($)')
# plt.ylabel('House Size (sqft)')


##Example of a data distribution grpah

#sns.distplot(dataset['price'],hist=False,kde_kws={'clip': (0.0, 2000000)},axlabel='Price of House ($)')


##Example of a single variable linear regression

# Declaring the price as the independent variable we want to predict and 'sqft_living' as the dependent variable
x = dataset['price'].values.reshape(-1,1)
y= dataset['sqft_living'].values.reshape(-1,1)

# Here we are splitting 80% of the data into the training set and 20% of the data will be saved as a testing set for later
price_train, price_test, hsize_train, hsize_test = train_test_split(x, y, test_size=0.2, random_state=0)

# We are declaring a linear regression line here form our training set
regressor = LinearRegression()
regressor.fit(price_train,hsize_train)

# We are declaring variables for the intercept and coef for the y = mx + c formula that defines the linear regression line. This is what in ML is described as the "Hypothesis" for our model. We can now enter new data into this equation and get a prediction.
intercept = (regressor.intercept_)
coefficient = (regressor.coef_)

# Variable predicting the House Price.
hsize_pred = regressor.predict(price_test)

# Producing a dataframe that compares actual values from our training set to predicted values from the testing set
df = pd.DataFrame({'Actual': hsize_test.flatten(), 'Predicted': hsize_pred.flatten()})
# print(df)

# Plotting the dataset again but with the regression line now included
plt.scatter(price_test, hsize_test, color='green')
plt.plot(price_test, hsize_pred, color='red', linewidth=2)
plt.xlabel('House Price ($)')
plt.ylabel('House Size (sqft)')
plt.title('House Price ($) vs House Size (sqft)')
plt.show()

# So we now have the result of a linear regression model successfully plotted. We now need to evaluate the performance of the model. I will perform a Mean Absolute Error (MAE) test, Mean Squared Error (MSE) test & Root Mean Quared Error (RMSE) test. I will use the Scikit Learn Library to do this.#
print('Mean Absolute Error:', metrics.mean_absolute_error(hsize_test, hsize_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(hsize_test, hsize_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(hsize_test, hsize_pred)))
print('r Squared: ', metrics.r2_score(hsize_test, hsize_pred))