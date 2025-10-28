# CloudWatch

Metrics for Amazon Textract

This section contains information about the Amazon CloudWatch metrics and the
_Operation_ dimension that are available for
Amazon Textract.

You can also see an aggregate view of Amazon Textract metrics from the Amazon Textract console.

## CloudWatch Metrics for Amazon Textract

The following table summarizes the Amazon Textract metrics.

| Metric                 | Description                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SuccessfulRequestCount | The number of successful requests. The response code range for a successful request is 200 to 299. Unit: Count Valid statistics: `Sum,Average`                                                                                                                                                                                                                                                   |
| ThrottledCount         | The number of throttled requests. Amazon Textract throttles a request when it receives more requests than the limit of transactions per second set for your account. If the limit set for your account is frequently exceeded, you can request a limit increase. To change a limit, select the Amazon Textract option in the Service Quotas console. Unit: Count Valid statistics: `Sum,Average` |
| ResponseTime           | The time in milliseconds for Amazon Textract to compute the response. Units: 1. Count for `Data Samples` statistics 2. Milliseconds for `Average` statistics Valid statistics: `Data Samples,Average` NoteThe `ResponseTime` metric isn't included in the Amazon Textract metric pane.                                                                                                           |
| ServerErrorCount       | The number of server errors. The response code range for a server error is 500 to 599. Unit: Count Valid statistics: `Sum,Average`                                                                                                                                                                                                                                                               |
| UserErrorCount         | The number of user errors (invalid parameters, invalid image, no permission, and so on). The response code range for a user error is 400 to 499. Unit: Count Valid statistics: `Sum,Average`                                                                                                                                                                                                     | ## CloudWatch Dimension for Amazon Textract To retrieve operation-specific metrics, use the `AWS/Textract` namespace and provide an operation dimension. For more information about dimensions, see [Dimensions](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension") in the _Amazon CloudWatch User Guide_. |
