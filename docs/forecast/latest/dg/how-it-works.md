Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# How Amazon Forecast Works

When creating forecasting projects in Amazon Forecast, you work with the following
resources:

- **[Importing Datasets](howitworks-datasets-groups.md "howitworks-datasets-groups.md")** – _Datasets_ are collections of your
  input data. Dataset groups are collections of datasets that contain complimentary
  information. Forecast algorithms use your dataset groups to train custom forecasting models,
  called predictors.
- **[Training Predictors](howitworks-predictor.md "howitworks-predictor.md")** – _Predictors_ are custom models trained
  on your data. You can train a predictor by choosing a prebuilt algorithm,or by choosing the
  AutoML option to have Amazon Forecast pick the best algorithm for you.
- **[Generating Forecasts](howitworks-forecast.md "howitworks-forecast.md")** – You can generate forecasts for your time-series data, query them using
  the [QueryForecast](API_forecastquery_QueryForecast.md "API_forecastquery_QueryForecast.md") API,
  or visualize them in the console.
