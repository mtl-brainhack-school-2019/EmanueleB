import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

labels = ['02', '04', '05', '11', '13', '14', '15', '16', '17', '19', '20']    # list of strings

freqAvrg = []
totalNotes = []

for participant in labels: # for loop to change folders

    df = pd.read_csv(r'\Users\Emanuele\Desktop\UdeM\PhD\BrainHack\data_analysis\P0' + participant + '.csv') 
    
    freqAvrg.append(df['Frequency Range'].mean())
    totalNotes.append(df['Number of Notes'].sum())


df2 = pd.read_csv(r'\Users\Emanuele\Desktop\UdeM\PhD\BrainHack\ihateexcel.csv')
df2 = df2.dropna(how='all')

x = np.asarray(df2[['Scale','Time','Out of Scale','Global']])
y = np.asarray(freqAvrg)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X_train, y_train)


print('Score: ', regr.score(X_test, y_test))
print('Weights: ', regr.coef_)

plt.plot(regr.predict(X_test), color = 'green')
plt.plot(y_test)
plt.show()


# Scatter plot
#x = totalNotes
#y = freqAvrg

#plt.scatter(x, y, alpha=0.5)
#plt.title('Scatter plot pythonspot.com')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.show()
