Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Data Aggregation Assumptions

Forecast doesn't assume that your data is from any specific time zone. However, it makes the following
assumptions when aggregating time series data:

- All data is from the same time zone.
- All forecasts are in the same time zone as the data in the dataset.
- If you specify the [SupplementaryFeature](API_SupplementaryFeature.md "API_SupplementaryFeature.md") holiday feature in the [InputDataConfig](API_InputDataConfig.md "API_InputDataConfig.md") parameter for the [CreatePredictor](API_CreatePredictor.md "API_CreatePredictor.md") operation, the input
  data is from the same country.
