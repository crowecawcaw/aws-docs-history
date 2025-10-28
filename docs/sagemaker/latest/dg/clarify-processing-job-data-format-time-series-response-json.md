# Endpoint

response for time series data

The SageMaker Clarify processing job deserializes the entire payload as JSON.
It then extracts predictions from the deserialized data using JMESPath
expressions provided in the analysis configuration. The records in the
response payload must match the records in the request payload.

The following table is an example response from an endpoint that
only outputs the mean prediction value. The value of `forecast` used
in the `predictor` field in the [analysis
config](clarify-processing-job-configure-analysis.md#clarify-processing-job-configure-analysis-parameters "clarify-processing-job-configure-analysis.md#clarify-processing-job-configure-analysis-parameters") should be provided as a
JMESPath expression to find the prediction result for the processing job.

| Endpoint request payload                                                                                                    | Endpoint response payload (string representation)                           | JMESPath expression for forecast in the analysis config |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------- |
| Single record example. Config should be `TimeSeriesModelConfig(forecast="prediction.mean")` to extract prediction properly. | `'{"prediction": {"mean": [1, 2, 3, 4, 5]}'`                                | `'prediction.mean'`                                     |
| Multiple records. An AWS deepAR endpoint response.                                                                          | `'{"predictions": [{"mean": [1, 2, 3, 4, 5]}, {"mean": [1, 2, 3, 4, 5]}]}'` | `'predictions[*].mean'`                                 |
