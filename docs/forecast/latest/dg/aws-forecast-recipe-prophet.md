Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Prophet Algorithm

[Prophet](https://facebook.github.io/prophet/ "https://facebook.github.io/prophet/")
is a popular local Bayesian structural time series model.
The Amazon Forecast Prophet algorithm uses the
[Prophet class](https://facebook.github.io/prophet/docs/quick_start.html#python-ap "https://facebook.github.io/prophet/docs/quick_start.html#python-ap")
of the Python implementation of Prophet.

## How Prophet Works

Prophet is especially useful for datasets that:

- Contain an extended time period (months or years) of detailed historical
  observations (hourly, daily, or weekly)
- Have multiple strong seasonalities
- Include previously known important, but irregular, events
- Have missing data points or large outliers
- Have non-linear growth trends that are approaching a limit

Prophet is an additive regression model with a piecewise linear or logistic growth
curve trend. It includes a yearly seasonal component modeled using Fourier series and a
weekly seasonal component modeled using dummy variables.

For more information, see [Prophet:
forecasting at scale](https://research.facebook.com/blog/2017/2/prophet-forecasting-at-scale/ "https://research.facebook.com/blog/2017/2/prophet-forecasting-at-scale/").

## Prophet Hyperparameters and Related

Time Series

Amazon Forecast uses the default Prophet
[hyperparameters](https://facebook.github.io/prophet/docs/quick_start.html#python-ap "https://facebook.github.io/prophet/docs/quick_start.html#python-ap").
Prophet also supports related time-series as features, provided to Amazon Forecast in the related
time-series CSV file.
