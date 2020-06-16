''' Importing libraries'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''Custom matplotlib style sheet'''
plt.style.use('seaborn-pastel')

'''Importing data'''
df = pd.read_csv(r'C:\Users\Chris\Documents\GitHub\python\USA_medical_cost\datasets_13720_18513_insurance.csv')

# print(df.head)



'''***This section is initial data analysis intended to provide visual insight into the 
dataset and to comment on any notable correlations or trends that we can see***'''




''' This shows us that there are 1338 rows and 7 columns. This means that there are
1338 training examples in this dataset and 7 features. Using standard notation, we would
say that m = 1338 and n = 7.

The target variable in this case is 'charges'. The features are age, sex, bmi, children, 
smoker and region.

We can now create a 'features' vector for each training example and therefore an m*n 
(ie 1338*7) 'input' matrix, X, that represents the features of the entire training set. 
We say the hypotenuse function (denoted h_theta(x)) is equal to the input matrix multiplied
by the vector of the parameters, denoted theta (this is a vector of length n comprising 
of each parameter).'''

''' Plotting the non-discrete features against the target variable to see if any interesting 
correlations exist.'''


# sns.lmplot(x='age',y='charges',data=df,aspect=2,height=6)
# plt.xlabel('Age$(years)$: as Independent variable')
# plt.ylabel('Insurance Charges: as Dependent variable')
# plt.title('Charge Vs Age');

# sns.lmplot(x='bmi',y='charges',data=df,aspect=2,height=6)
# plt.xlabel('Boby Mass Index$(kg/m^2)$: as Independent variable')
# plt.ylabel('Insurance Charges: as Dependent variable')
# plt.title('Charge Vs BMI');


'''We now plot a graph showing any null or missing values in the dataset'''

# plt.figure(figsize=(12,4))
# sns.heatmap(df.isnull(),cbar=False,cmap='viridis',yticklabels=False)
# plt.title('Missing value in the dataset');

'''We can see that there are no missing values so we do not need to deal with this
 for this dataset.'''
 

'''Now we can see whether a correlation exists between any of the features in relation 
to one another. To do this, we calculate a correlation matrix. Thankfully, Pandas has a 
function corr() that computes this for us. Whilst the .corr() can use either the Pearson 
standard correlation coefficient method, the Kendall Tau correlation coefficiant method, 
or the Spearman rank correlation method, we will use the Pearson (which also happens to 
be the default method for the .corr() function.'''

# print(df.corr())


''' It isn't really necessary in this example but it is a nice exercise anyway. We can
 plot a heatmap of the correlation matrix to visaulise it a little bit better.'''
 
#sns.heatmap(df.corr(),annot=True,cmap='Wistia_r')
 

'''As we are using the Pearson standard correlation coefficient method, each correlation
 coefficient ranges from 0 to 1. 0 meaning there is absolutely no correlation between the 
 two variables and 1 meaning there is a perfect linear relationsihp between the two 
 variables. As we can expect, the entries in the main diagonal of the matrix are 1. But looking 
 outside of this obvious result, we have only low values appearing in the matrix. So we can
  conclude that there are no correlations that exist between the features in this dataset.'''
  
'''Now we will plot the distributions of charges.'''

# f= plt.figure(figsize=(12,4))

# ax=f.add_subplot(121)
# sns.distplot(df['charges'],bins=50,color='r',ax=ax)
# ax.set_title('Distribution of insurance charges')

'''This distribution has a positive skew. So we can apply the log function to this data 
to normalise it. We could also have attempted the square root transform or the box-cox 
transform.'''

# ax=f.add_subplot(122)
# sns.distplot(np.log10(df['charges']),bins=40,color='b',ax=ax)
# ax.set_title('Distribution of insurance charges in $log$ scale')
# ax.set_xscale('log');

'''Since this normalises the data well, we will apply the log function to the target 
variable.'''


'''We will now use violin plots to plot the features sex and smoker against the target 
variable'''

# f = plt.figure(figsize=(14,6))
# ax = f.add_subplot(121)
# sns.violinplot(x='sex', y='charges',data=df,palette='Wistia_r',ax=ax)
# ax.set_title('Violin plot of Charges vs sex')

'''We can clearly see that there is no meaningful difference in the amount charged when 
comparing the two sexes. The mean for both sexes is roughly $5000'''


# ax = f.add_subplot(122)
# sns.violinplot(x='smoker', y='charges',data=df,palette='magma',ax=ax)
# ax.set_title('Violin plot of Charges vs smoker')

'''We can see there is a definitive difference in the charge distributions between 
individuals of the smoker vs non-smoker groups. Smokers almost exclusively contribute 
to all charges over $30,000 and almost all smokers have charges that are above the mean 
value charged overall for all individuals in this dataset. It would seem that we should 
investigate further into this correlation seen in smokers vs non-smokers. We will do this 
later on by also comparing smoking status vs age and bmi.'''


'''Now we will plot box-plots for charges vs children sorted by sex'''

# plt.figure(figsize=(14,6))
# sns.boxplot(x='children', y='charges',hue='sex',data=df,palette='Wistia_r')
# plt.title('Box plot of charges vs children');


'''Now we will plot a violin plot to compare charge against regions'''

# plt.figure(figsize=(14,6))
# sns.violinplot(x='region', y='charges',hue='sex',data=df,palette='magma',split=True)
# plt.title('Violin plot of charges vs Region')

'''We can see that there is no meaningful difference in regions when we look at the amount 
charged.'''


'''We will now plot scatter diagrams of age vs charges (sorted by smoker vs non-smoker) 
and bmi vs charges (sorted by smoker) respectively.'''

# f = plt.figure(figsize=(14,6))
# ax = f.add_subplot(121)
# sns.scatterplot(x='age',y='charges',data=df,palette='magma',hue='smoker',ax=ax)
# ax.set_title('Scatter plot of Charges vs age')

# ax = f.add_subplot(122)
# sns.scatterplot(x='bmi',y='charges',data=df,palette='viridis',hue='smoker')
# ax.set_title('Scatter plot of Charges vs bmi')
# plt.savefig('sc.png')

'''We can see that in a relitively uniform manner, both smokers and non-smokers are 
charged more as their age increases. It would also appear that there are different 
policy bands that range between charges of ~0$ - ~$18000, ~$10000 - ~$30000, and 
~$30000 - ~$50000 respectively.
 
We can also see from the second graph that bmi and charge are positively correlated 
for smokers but there is no correlation for non-smokers. bmi ranges from 16 and 53.'''



'''***This section is dedicated to the pre-processing of the data before we apply our 
model to it.***'''


'''Since much of our data is categorical, we must apply some transformations to the data 
before we can apply a model to it. The features that are comprised of categorical data are 
sex, children, smoker and region. Since sex and region are comprised of ordinal data, we 
must apply 'label encoding' to convert the data to numbers. 

Now that all of our categorical features are represented as integar values, we can now 
represent our categorical data in binary vectors. This seems unintuitive initially. 
How can we represent a value such as region in binary vectors when there are 4 categories? 
In a case like this, we can create new 'dummy variables' called 'southwest', 'northwest', 
'southeast' and ' northeast' and so in a row that is in region southwest, there will be a 
1 in the 'southwest' column and 0s in the rest of the region columns. This process will 
be applied to children also. This process is called 'one hot encoding'. 

But now we must be mindful of the 'dummy variable trap'. This is a situation in which we 
have two variables that are highly correlated to one another to the point in which we can 
predict the result of one variable from the other. A good example of this is the sexes 
variables. In the 'one hot encoding' step, we have separated these variables into two 
dummy variables, male and female. We can obviously predict the instance of one from the 
instance of the other, or lack thereof. We therefore do not need both these variables. 

Luckily, we can apply label encoding, one hot encoding and deal with the dummy variable 
trap all in a one line of code by using the pandas get_dummy function.'''

df_encoded = pd.get_dummies(data = df, prefix = 'OHE', prefix_sep='_', 
                            columns = ['sex','children', 'smoker', 'region'], 
                            drop_first =True, dtype='int8')


'''We now take the natural log transformation of the charges data to normalise it.'''

df_encoded['charges'] = np.log(df_encode['charges'])


'''The next step is to perform the Train-Test split. The purpose of this is to split 
the data into two datasets: Data for training and data for testing. This can be conducted 
using the train_test_split module within the sklearn.model_selection import. By default 
this function splits the dataset randomly into their two subsets. The test_size option 
is set at 0.3 meaning that 30% of the data is split into the test dataset. The train-size 
is set to 'None' which means that it will automatically take the compliment of whatever 
the test_size is (this is simply so we do not have to change both options when we wish to 
make a change. We have set the random_state to be equal to a number meaning that every 
time we run this code, the same split will occur each time.'''

from sklearn.model_selection import train_test_split
X = df_encoded.drop('charges',axis=1) # Independent variables
y = df_encoded['charges'] # Dependent variable

X_train, X_test, y_train, y_test = train_test_split(X,y,train_size = None, 
                                                    test_size=0.3,random_state=1)



'''***This section is where we will build the actual model. To do this, we use the Normal 
Equation θ=(X^T * X)^(−1) * X^T * y where θ is the parameter vector (1 x (n+1)), X is the 
(m x (n+1)) design matrix (otherwise known as the model matrix or the regressor matrix) 
that is made up of the training examples, X_train, and y is the (1 x m) target variable 
vector. 

θ and X have dimension (n+1) rather than n because by convention, the first column of 
the design matrix consists of all 1s. θ is of dimension (n+1) because similarly θ_0 = 1. 
With that being said, we need to firstly make this change. So our first step is to add 
X_0 = 1 into our dataset.***'''

X_train_0 = np.c_[np.ones((X_train.shape[0], 1)), X_train]
X_test_0 = np.c_[np.ones((X_test.shape[0], 1)), X_test]

'''We have made the aforementioned changes to X_0 in both the training dataset and the 
testing dataset. we used the numpy's concatenate function (np.c_) to add this extra 
column.''' 


'''Now we must build the model. Take time to think through how the syntax of this code 
works here. It's fairly simple when you write it out.'''

theta = np.matmul(np.linalg.inv( np.matmul(X_train_0.T,X_train_0) ), 
                  np.matmul(X_train_0.T,y_train)) 

'''We will now create a new dataframe to display our parameters and their theta values as 
calculated from this model. We firstly assign our theta_0, ..., theta_12 to our different 
parameters and give their theta values based on our above model. We will then use sklearn's 
Linear Regression function from the linear_model module and compare it against those 
figures to see if our model is successfully calculating theta from the Normal Equation.'''

parameter = ['theta_'+str(i) for i in range(X_train_0.shape[1])]
columns = ['intersect:x_0=1'] + list(X.columns.values)
parameter_df = pd.DataFrame({'Parameter':parameter,'Columns':columns,'theta':theta})

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_train,y_train) 


sk_theta = [lin_reg.intercept_]+list(lin_reg.coef_)
parameter_df = parameter_df.join(pd.Series(sk_theta, name='Sklearn_theta'))
print(parameter_df)

'''Our values for theta are the same as from Sklearn's module designed to do this so we 
have built a successful model.'''



'''***This section is designed to evaluate our model's accuracy. We will use our test 
dataset and run it through our model and then compare the predicted values against the 
actual values. We will use the Mean Squared Error method (MSE). We will also use the 
r-squared method to calculate how close our regression line is to the actual set of 
values. This value is always between 0 and 1. A value near 1 would mean that our model 
predicts our data very well.

The equation for R^2 is R^2 = 1 - ("Sum of Squared Error" / "Sum of Square Total") where:

SSE = ∑(i=1 -> m) [(y^hat_i−yi)^2]        
 
SST = ∑(i=1 -> m) [(y_i−y^vectori)^2]

Here we have y_i^vector being the mean value of y and y^hat being the predicted value.'''

# Normal equation
y_pred_norm =  np.matmul(X_test_0,theta)

#Calculating Mean Squared Error
J_mse = np.sum((y_pred_norm - y_test)**2)/ X_test_0.shape[0]

# R_square 
sse = np.sum((y_pred_norm - y_test)**2)
sst = np.sum((y_test - y_test.mean())**2)
R_square = 1 - (sse/sst)
print('The Mean Square Error(MSE) or J(theta) is: ',J_mse)
print('R square obtain for normal equation method is: ',R_square)

'''We now want to compare this to the built-in method of doing this in the sklearn 
regression module.'''


# sklearn regression module
y_pred_sk = lin_reg.predict(X_test)

#Evaluvation: MSE
from sklearn.metrics import mean_squared_error
J_mse_sk = mean_squared_error(y_pred_sk, y_test)

# R_square
R_square_sk = lin_reg.score(X_test,y_test)
print('The Mean Square Error(MSE) or J(theta) is: ',J_mse_sk)
print('R square obtain for scikit learn library is :',R_square_sk)

'''We can see that our values for the MSE and R Squared using our model is the same as 
sklearn's values. Moreover, we can see that because the MSE is very low and R squared is 
fairly high (78%), the model is actually fairly accurate!'''









 


