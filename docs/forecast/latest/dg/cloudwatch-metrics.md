Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# CloudWatch Metrics for Amazon Forecast

This section contains information about the Amazon CloudWatch metrics available for Amazon Forecast.

The following table lists the Amazon Forecast metrics.

| Metric                        | Dimension                      | Unit      | Statistics             | Description                                                                                                                                                                                                       |
| ----------------------------- | ------------------------------ | --------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DatasetSize                   |                                | Kilobytes | Average, Sum, Min, Max | The total size of the datasets imported by Amazon Forecast into the customer's account.                                                                                                                           |
| DatasetSize                   | DatasetArn DatasetImportJobArn | Kilobytes | Average, Sum           | The size of the dataset imported by the [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md") operation.                                                                        |
| CreatePredictorEvaluationTime | PredictorArn                   | Seconds   | Average, Sum           | The time taken for training, inference, and metrics for a specific predictor. Amazon Forecast normalizes the compute costs to a c5.xlarge instance to arrive at the number of hours consumed by the training job. |
| CreateForecastEvaluationTime  | ForecastArn                    | Seconds   | Average, Sum           | The time taken for training and inference during forecast generation. Amazon Forecast normalizes the compute costs to a c5.xlarge instance to arrive at the number of hours consumed by the training job.         |
| TimeSeriesForecastsGenerated  |                                | Count     | Average, Sum, Min, Max | The number of unique time series forecasts generated for each quantile across all predictors in the account. Forecasts are billed to the nearest 1000 and charged on a per 1,000 basis.                           |
| TimeSeriesForecastsGenerated  | PredictorArn                   | Count     | Average, Sum, Min, Max | The number of unique time series forecasts generated for each quantile across all predictors in the account. Forecasts are billed to the nearest 1,000 and charged on a per 1,000 basis.                          |
| TimeSeriesForecastsGenerated  | PredictorArn ForecastArn       | Count     | Average, Sum, Min, Max | The number of unique time series forecasts generated for each quantile across all predictors in the account. Forecasts are billed to the nearest 1,000 and charged on a per 1,000 basis.                          |
| ForecastDataPointsGenerated   | PredictorArn ForecastArn       | Count     | Average, Sum, Min, Max | The number of unique datapoints generated for each forecast across all predictors in the account. Forecasts are billed to the nearest 1,000 and charged on a per 1,000 basis.                                     |
