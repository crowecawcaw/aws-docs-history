

# CloudWatch metrics for Amazon Textract

This section contains information about the Amazon CloudWatch metrics and the *Operation* dimension that are available for Amazon Textract Core.

You can also see an aggregate view of Amazon Textract Core metrics from the Amazon Textract Core console.

## CloudWatch metrics for Amazon Textract
<a name="cloudwatch-metrics"></a>

The following table summarizes the Amazon Textract Core metrics:


| **Metric** | **Description** | 
| --- | --- | 
| SuccessfulRequestCount | The number of successful requests. The response code range for a successful request is 200 to 299. <br />Unit: Count<br />Valid statistics: `Sum,Average` | 
| ThrottledCount | The number of throttled requests. Amazon Textract Core throttles a request when it receives more requests than the limit of transactions per second set for your account. If the limit set for your account is frequently exceeded, you can request a limit increase. To change a limit, select the Amazon Textract Core option in the Service Quotas console. For the throttling errors that Amazon Textract Insights returns, see [Troubleshooting](insights-troubleshooting.md).<br />Unit: Count<br />Valid statistics: `Sum,Average` | 
| ResponseTime | The time in milliseconds for Amazon Textract Core to compute the response. <br />Units:1.  Count for `Data Samples` statistics <br />2.  Milliseconds for `Average` statistics <br />Valid statistics: `Data Samples,Average`The `ResponseTime` metric isn't included in the Amazon Textract Core metric pane. | 
| ServerErrorCount | The number of server errors. The response code range for a server error is 500 to 599.<br />Unit: Count<br />Valid statistics: `Sum,Average` | 
| UserErrorCount | The number of user errors (invalid parameters, invalid image, no permission, and so on). The response code range for a user error is 400 to 499.<br />Unit: Count<br />Valid statistics: `Sum,Average` | 
| InProgressJobs | The number of asynchronous jobs in progress for the operation, recorded each time a new job is successfully started. The metric is published only for the asynchronous Start operations (`StartDocumentTextDetection`, `StartDocumentAnalysis`, `StartExpenseAnalysis`, `StartLendingAnalysis`, and `StartDocumentInsights`).<br />Unit: Count<br />Valid statistics: `Maximum,Average` | 

## CloudWatch dimension for Amazon Textract
<a name="cloudwatch-dimensions"></a>

To retrieve operation-specific metrics, use the `AWS/Textract` namespace and provide an operation dimension. For more information about dimensions, see [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension) in the *Amazon CloudWatch User Guide*. 

The *Operation* dimension also includes the Amazon Textract Insights operations, such as `StartDocumentInsights` and `GetDocumentInsights`.