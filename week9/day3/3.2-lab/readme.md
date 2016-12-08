---
title: ARIMA Model
type: lab
duration: "1:25"
---
# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) ARIMA Model

## Introduction

> ***Note:*** _This can be a pair programming activity or done independently._

The most common application for AR, ARMA, and ARIMA models is inventory planning. Planning inventory for a small shop can be difficult enough, but you've just been hired to plan inventory for a _big_ store- Walmart!

In this lab, we will be analyzing weekly Walmart sales data over a two year period from 2010 to 2012. The data is separated by store and by department, but we'll focus on analyzing one store for simplicity. Your supervisor has set out the following goals for this project:

1. Record any observed trends in the data
1. Produce a trained model to predict future sales numbers
1. Assemble your findings in a report

Try your best to tune your model. It can be difficult, but don't worry- after this lab, we'll _roll back_ our focus to examine advanced tuning techniques.

## Exercise

#### Requirements

- Code along to the guidelines below
- Assemble observations and graphs supporting your model in a 1-2 page PDF exported from your favorite text editor
- Submit all code and documents, including answers to any questions posed, in a Github PR

**Bonus:**
- Create a Tableau dashboard with various different views of the data and corresponding results of your models

#### Starter code

To setup the data:

```python
import pandas as pd
import numpy as np

%matplotlib inline

data = pd.read_csv('assets/datasets/train.csv')
data.set_index('Date', inplace=True)
data.head()
```

#### Deliverable

1. Filter the dataframe to Store 1 sales and aggregate over departments to compute the total sales per store.
1. Plot the rolling_mean for `Weekly_Sales`. What general trends do you observe?
1. Compute the 1, 2, 52 autocorrelations for `Weekly_Sales` and/or create an autocorrelation plot.
1. What does the autocorrelation plot say about the type of model you want to build?
1. Split the weekly sales data in a training and test set - using 75% of the data for training
1. Create an AR(1) model on the training data and compute the mean absolute error of the predictions. How effective is this model?
1. Plot the residuals - where are their significant errors?
1. Compute and AR(2) model and an ARMA(2, 2) model - does this improve your mean absolute error on the held out set?
1. Finally, compute an ARIMA model to improve your prediction error - iterate on the p, q, and parameters comparing the model's performance.
1. Assemble your findings, including any useful graphs, in a 1-2 page PDF.
1. Submit all code and documents in a Github PR


#### Additional Resources

1. [ARMA Example](http://statsmodels.sourceforge.net/devel/examples/notebooks/generated/tsa_arma.html)
2. [ARMA Models for TSA](https://www.quantstart.com/articles/Autoregressive-Moving-Average-ARMA-p-q-Models-for-Time-Series-Analysis-Part-1)
