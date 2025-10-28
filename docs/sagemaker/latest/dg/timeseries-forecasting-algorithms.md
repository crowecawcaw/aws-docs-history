# Algorithms support for time-series

forecasting

Autopilot trains the following six built-in algorithms with your target time-series. Then,
using a stacking ensemble method, it combines these model candidates to create an optimal
forecasting model for a given objective metric.

- **Convolutional Neural Network - Quantile Regression
  (CNN-QR)** – CNN-QR is a proprietary machine learning algorithm for
  forecasting time-series using causal convolutional neural networks (CNNs). CNN-QR works
  best with large datasets containing hundreds of time-series.
- **DeepAR+** – DeepAR+ is a proprietary machine
  learning algorithm for forecasting time-series using recurrent neural networks (RNNs).
  DeepAR+ works best with large datasets containing hundreds of feature time-series.
- **Prophet** – [Prophet](https://facebook.github.io/prophet/ "https://facebook.github.io/prophet/") is a popular local Bayesian
  structural time series model based on an additive model where non-linear trends are fit
  with yearly, weekly, and daily seasonality. The Autopilot Prophet algorithm uses the [Prophet
  class](https://facebook.github.io/prophet/docs/quick_start.html#python-ap "https://facebook.github.io/prophet/docs/quick_start.html#python-ap") of the Python implementation of Prophet. It works best with time-series
  with strong seasonal effects and several seasons of historical data.
- **Non-Parametric Time Series (NPTS)** – The NPTS
  proprietary algorithm is a scalable, probabilistic baseline forecaster. It predicts the
  future value distribution of a given time-series by sampling from past observations. NPTS
  is especially useful when working with sparse or intermittent time series.
- **Autoregressive Integrated Moving Average (ARIMA)**
  – ARIMA is a commonly used statistical algorithm for time-series forecasting. The
  algorithm captures standard temporal structures (patterned organizations of time) in the
  input dataset. It is especially useful for simple datasets with under 100 time series.
- **Exponential Smoothing (ETS)** – ETS is a
  commonly used statistical algorithm for time-series forecasting. The algorithm is
  especially useful for simple datasets with under 100 time series, and datasets with
  seasonality patterns. ETS computes a weighted average over all observations in the time
  series dataset as its prediction, with exponentially decreasing weights over time.
