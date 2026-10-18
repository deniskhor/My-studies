import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

medical_df = pd.read_csv('medical.csv')

medical_df
medical_df.head()
medical_df.info()
medical_df.describe()
medical_df.isna().sum()

fig = px.histogram(medical_df, x='age', nbins=47)
fig.show()

fig = px.histogram(medical_df, x='bmi', marginal='box')
fig.show()

fig = px.histogram(medical_df, x='charges', marginal='box', color='smoker')
fig.show()

fig = px.histogram(medical_df, x='smoker', color='sex')
fig.show()

fig = px.scatter(
    medical_df,
    x='age',
    y='charges',
    color='smoker',
    opacity=0.8
)
fig.show()

fig = px.scatter(
    medical_df,
    x='bmi',
    y='charges',
    color='smoker',
    opacity=0.8
)
fig.show()

fig = px.violin(
    medical_df,
    x='children',
    y='charges',
    color='smoker',
    box=True
)
fig.show()

medical_df['smoker_code'] = medical_df.smoker.map({
    'no': 0,
    'yes': 1
})

medical_df.select_dtypes(include='number').corr()

non_smoker_df = medical_df[medical_df.smoker == 'no']

ages = non_smoker_df.age
target = non_smoker_df.charges

plt.scatter(ages, target, s=8, alpha=0.8)
plt.xlabel('Age')
plt.ylabel('Charges')
plt.show()

def estimate_charges(age, w, b):
    return w * age + b

w = 50
b = 100

estimated_charges = estimate_charges(ages, w, b)

plt.plot(ages, estimated_charges, 'r', alpha=0.9)
plt.scatter(ages, target, s=8, alpha=0.8)
plt.xlabel('Age')
plt.ylabel('Charges')
plt.legend(['Estimate', 'Actual'])
plt.show()

def rmse(targets, predictions):
    return np.sqrt(np.mean(np.square(targets - predictions)))

rmse(target, estimated_charges)

def try_parameters(w, b):
    ages = non_smoker_df.age
    target = non_smoker_df.charges
    predictions = estimate_charges(ages, w, b)

    plt.plot(ages, predictions, 'r', alpha=0.9)
    plt.scatter(ages, target, s=8, alpha=0.8)
    plt.xlabel('Age')
    plt.ylabel('Charges')
    plt.legend(['Prediction', 'Actual'])
    plt.show()

    loss = rmse(target, predictions)
    print("RMSE Loss: ", loss)

try_parameters(50, 100)
try_parameters(100, 500)
try_parameters(200, 1000)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

help(model.fit)

inputs = non_smoker_df[['age']]
targets = non_smoker_df.charges

print('inputs.shape :', inputs.shape)
print('targets.shape :', targets.shape)

model.fit(inputs, targets)

model.predict(np.array([
    [23],
    [37],
    [61]
]))

predictions = model.predict(inputs)

predictions

rmse(targets, predictions)

model.coef_
model.intercept_

try_parameters(model.coef_, model.intercept_)
