
# coding: utf-8

# <img src="https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png" style="float: left; margin: 15px">
# 
# ## ARIMA and Timeseries Modeling
# 
# Week 9 | Lesson 3.1
# 
# ---

# ## Opening: What are Time Series Models?
# 
# So far, we focused on exploring time-series data and common statistics for time-series analysis. 
# 
# In this class, we'll advance those techniques to show how to predict or forecast from time series data.

# ## Agenda:
# 
# - Training/test splits.
# - Stationarity and differencing.
# - AR Models.
# - MA Models.
# - ARIMA Models.
# - ACF and PACF plots.

# ## Training and Test set.
# 
# - We can't randombly sample our data to create a train/test split.
# 
# - Our training and testing sets need to be ordered by time.

# ## Stationarity and differencing.
# 
# _A stationary time series is one whose properties do not depend on the time at which the series is observed_
# 
# - The long running mean and variance are constant if the TS is stationary.
# - TS with trends or seasonality are NOT stationary.
# - TS with cyclic behaviour can be stationary (as cycles are not of fixed length.

# ## Why care about stationarity?
# 
# - Most statistical forecasting methods are based on the assumption that the time series can be rendered approximately stationary (i.e., "stationarized") through the use of mathematical transformations. 
# 
# - A stationarized series is relatively easy to predict: you simply predict that its statistical properties will be the same in the future as they have been in the past!

# What quantities are we typically interested in when we perform statistical analysis on a time series? We want to know:
# 
# Its expected value,
# Its variance, and
# The correlation between values s periods apart for a set of s values.
# How do we calculate these things? Using a mean across many time periods.
# 
# The mean across many time periods is only informative if the expected value is the same across those time periods. If these population parameters can vary, what are we really estimating by taking an average across time?
# 
# (Weak) stationarity requires that these population quantities must be the same across time, making the sample average a reasonable way to estimate them.

# _Stationary time series will have no predictable patterns in the long term._

# ![](./assets/images/stationary.png)

# ### Which of the series was stationary?
# 
# - Obvious seasonality rules out (d), (h) and (i).
# 
# - Trend rules out series (a), (c), (e), (f) and (i).
# 
# - Increasing variance also rules out (f).
# 
# - Only (b) and (g) are stationary series.

# ## Differencing
# 
# - By computing the difference between consecutive observations we can make a series stationary. (a and b in the previous image correspond the the Down Jones and the differnce in values respectively).
# 
# - Logarithms can help stabilize the variance of a time series.

# ## ACF plots.
# 
# - ACF plots are also useful for identifying non-stationary time series. 
# - In stationary time series ACF will drop to zero relatively quickly.
# 
# ![](./assets/images/acfstationary.png)

# ## ARIMA MODELS.
# 
# Throughout this lesson, we are going to build up to the **ARIMA** time-series model. 
# 
# This models combines the ideas of differencing and two models we will see below: **AR** or autoregressive models and **MA** or moving average models.

# _First lets introduce the data set we are going to be using_

# In[30]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import statsmodels as sm

sns.set_style('whitegrid')

get_ipython().magic(u'matplotlib inline')
get_ipython().magic(u"config InlineBackend.figure_format = 'retina'")


# In[186]:

data = pd.read_csv('assets/datasets/rossmann.csv', skipinitialspace=True)
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)


# In[32]:

data.head(2)


# In[33]:

# Filter to Store 1
store1_data = data[data.Store == 1]

# Filter to open days
store1_open_data = store1_data[store1_data.Open==1]

store1_open_data.head(2)


# In[34]:

# Plot the sales over time
store1_open_data[['Sales']].plot()


# ---
# 
# ## Autoregressive (AR) models
# 
# Autoregressive (AR) models use data from previous time-points to predict the next time-point. These are essentially regression models where the predictors are previous timepoints of the outcome.
# 
# Typically, AR models are denoted `AR(p)`, where _p_ indicates the number of previous time points to incorporate. `AR(1)` is the most common.
# 
# In an autoregressive model we learn regression coefficients on the features that are the previous _p_ values.
# 
# ### $$y_i = c + \beta_1 * y_{i-1} + \beta_2 * y_{i-2}\ +\ ...\ +\ \beta_p * y_{i-p}\ +\ \epsilon$$
# 
# 

# As with other linear models, interpretation becomes more complex as we add more factors; as we go from AR(1) to AR(2) we begin to have significant _multi-collinearity_.
# 
# Recall, _autocorrelation_ is the correlation of a value with itself. A timeseries with high autocorrelation implies that the data is highly dependent on previous values and an autoregressive model would perform well.
# 
# Autoregressive models are useful for learning falls or rises in our series. Typically, this model type is useful for small-scale trends, such as an increase in demand that will gradually increase the series.

# In[38]:

# Lets check for correlation in the sales dataset:
from pandas.tools.plotting import autocorrelation_plot

print store1_data.Sales.autocorr(lag=1)
print store1_data.Sales.autocorr(lag=2)

autocorrelation_plot(store1_data.Sales)


# In[78]:

# Lets plot the ACF
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plot_acf(store1_data.Sales, lags=10)
print "Why do we have a spike at 7?"


# ## PACF (partial autocorrelation function) 
# 
# Is essentially the autocorrelation of a signal with itself at different points in time, with linear dependency with that signal at shorter lags removed, as a function of lag between points of time. 
# 
# Informally, the partial correlation between x(t) and x(t+h) is the autocorrelation between x(t) and x(t+h) without the contribution of x(t+1),x(t+2),....,x(t+h−1).
# 
# Or, if we have x1, x2, x3, PACF is that portion of the correlation between x1 and x3, which is not explained by the correlation between x3 in x2.

# In[81]:

plot_pacf(store1_data.Sales, lags=10)
print ""


# In[139]:

#Now let's try to fit a AR model with statsmodels.
ar2 = sm.tsa.arima_model.AR(data['Sales']).fit(maxlag=2, trend="nc")
ar2.params


# ---
# 
# ## Moving Average (MA) models
# 
# Rather than use past values of the forecast variable in a regression, a moving average model uses past forecast errors in a regression-like model.
# 
# ### $$y_i = mean + \beta_1 * \epsilon_i + ... \beta_q * \epsilon_q$$
# 
# where e(i) is white noise. We refer to this as an MA(q) model. Of course, we do not observe the values of e(i), so it is not really regression in the usual sense.
# 
# Notice that each value of y(i) can be thought of as a weighted moving average of the past few forecast errors.

# MA models require a more complex fitting procedure where we iteratively fit a model, compute the errors, and then refit, over and over again.
# 
# MA includes the mean of the time series. The behavior of the model is therefore characterized by random jumps around the mean value.
# 
# In an `MA(1)` model, there is one coefficient on the error of our previous prediction impacting our estimate for the next value in the timeseries.

# ---
# 
# ## ARMA models
# 
# The final stepping stone before **ARIMA** models are **ARMA** models.
# 
# _ARMA_ models combine the autoregressive models and moving average models. We combine both, parameterizing the behavior of the model with `p` and `q` terms corresponding to the `AR(p)` model and `MA(q)` model.
# 
# Autoregressive models slowly incorporate changes in preferences, tastes, and patterns. Moving average models base their prediction not on the prior value but the prior error, allowing us to correct sudden changes based on random events - supply, popularity spikes, etc.
# 

# In[140]:

from statsmodels.tsa.arima_model import ARMA

store1_sales_data = store1_open_data[['Sales']][:len(store1_open_data)/2].astype(float)
arma10 = ARMA(store1_sales_data, (1, 0)).fit()
arma10.summary()


# _The previous model was the equivalent of a AR(1) model, since the order for MA is zero._
# 

# In[143]:

# We can now try fitting a AR(2) model, in which we are modeling a month of sales based
# on the values for the previous two months.
arma20 = ARMA(store1_sales_data, (2, 0)).fit()
arma20.summary()


# In[144]:

# Now we check the residuals of our model to see how well our model is capturing the 
# phenomena. 

# Ideally we don't want to see any pattern in the residual plot.
arma20.resid.plot()


# In[148]:

# By plotting the PACF of the residuals we can check if they are independent.
plot_pacf(model.resid, lags=50)
print ""


# In[149]:

# We can also fit a full ARMA model, adding a degree to the MA component.
arma11 = ARMA(store1_sales_data, (1, 1)).fit()
arma11.summary()

# The coefficients here are 0.72 for the AR component and -0.03 for the MA component. 
# The AR coefficient is the same as before (decreasing values) and 
# the MA component is fairly small (which we should have expected from the autocorrelation plots).


# ---
# 
# ## Autoregressive Ingegrated Moving Average (ARIMA) models
# 
# ARIMA is just like the `ARMA(p, q)` model, but instead of predicting the value of the series it predicts the _differenced_ series or changes in the series. The order of differencing is set by an _d_ term as in `ARIMA(p, d, q)`, or alternatively you can just fit an `ARMA(p, q)` model on a differenced timeseries.
# 
# Recall the pandas `diff` function. This computes the difference between two consecutive values. In an ARIMA model, we attempt to predict this difference instead of the actual values.
# 
# ### $$y_t - y_{(t-1)} = ARMA(p, q)$$
# 
# This handles the stationarity assumption: instead of detrending or differencing manually, the model does this via the differencing term.

# For a higher value of _d_, for example, d=2, an `ARIMA(p, 2, q)` model is equivalent to:
# 
#     diff(diff(y)) = ARMA(p, q)
# 
# The order of differencing is the same as applying the `diff` function _d_ times.

# Compared to an ARMA model, ARIMA models _do not rely on the underlying series being stationary._ The differencing operation can _convert_ the series to one that is stationary.
# 
# Since ARIMA models automatically include differencing, we can use this on a broader set of data without assumptions of a constant mean.

# In[163]:

from statsmodels.tsa.arima_model import ARIMA

# We can see that this model in fact simplifies automatically to an ARMA model.
arima101 = ARIMA(store1_sales_data, (1, 0, 1)).fit()
arima101.summary()


# In[168]:

# Let's remove the moving average component since it wasn't particularly useful before.
# Also, lets add the differencing parameter.
# Now this is equivalent to a AR(1) model on the differenced data.
arima110 = ARIMA(store1_sales_data, (1, 1, 0)).fit()

# Note the value of the coeffient.
arima110.summary()


# In[169]:

# We can compute the lag 1 auto correlation of the difference series and see if they match!
store1_sales_data.Sales.diff(1).autocorr(1) 


# _Another example_

# In[192]:

# Another worked out example, using the sunspots dataset.
import statsmodels as sm
import matplotlib.pyplot as plt
import pandas as pd

dta = sm.datasets.sunspots.load_pandas().data[['SUNACTIVITY']]
dta.index = pd.DatetimeIndex(start='1700', end='2009', freq='A')
res = sm.tsa.arima_model.ARIMA(dta, (3,1, 0)).fit()
fig, ax = plt.subplots()
ax = dta.ix['1950':].plot(ax=ax)
fig = res.plot_predict('1990', '2012', dynamic=True, ax=ax,
                        plot_insample=False)
plt.show()


# Unfortunately ARIMA models quickly converge to the mean of the TS. 
