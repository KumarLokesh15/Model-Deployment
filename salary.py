import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def salary_exp_pred(exp):

    df = pd.read_csv('Salary_Data-1.csv')
    x = df.iloc[:,0]
    y = df.iloc[:,1]

    x = x.values
    y = y.values

    model = LinearRegression()

    x_new = x.reshape(-1,1)
    y_new = y.reshape(-1,1)
    model.fit(x_new,y_new)


    x_test = np.array(exp)
    x_test = x_test.reshape((1,-1))

    return model.predict(x_test)[0][0]
