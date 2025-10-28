# Amazon Q Business API operation metrics

The following table shows the API operation metrics that Amazon Q Business sends to CloudWatch.

| Metric name | Unit         | Description                                                                                                                                                             |
| ----------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `success`   | Count        | The number of successful API operation calls. This metric is emitted for each successful API operation execution. Valid dimensions: `MethodType`, `ApplicationId`       |
| `failure`   | Count        | The number of failed API operation calls. This metric is emitted for each failed API operation execution. Valid dimensions: `MethodType`, `ApplicationId`               |
| `latency`   | Milliseconds | The time taken to complete an API operation call. This metric measures the response time for individual API operations. Valid dimensions: `MethodType`, `ApplicationId` | The `MethodType` dimension can include values such as: <br>• `ListPlugins` <br>• (Additional method types may be available depending on API usage) |
