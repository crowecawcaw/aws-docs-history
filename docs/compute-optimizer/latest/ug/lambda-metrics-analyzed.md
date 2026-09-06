

# Lambda function metrics
<a name="lambda-metrics-analyzed"></a>

Compute Optimizer analyzes the following CloudWatch metrics of your Lambda functions.


| Metric | Description | 
| --- | --- | 
|  Invocations  | The number of times your function code is executed, including successful executions and executions that result in a function error. | 
|  Duration  | The amount of time that your function code spends processing an event. | 
|  Errors  | The number of invocations that result in a function error. Function errors include exceptions thrown by your code and exceptions thrown by the Lambda runtime. The runtime returns errors for issues such as timeouts and configuration errors. | 
|  Throttles  | The number of invocation requests that are throttled. | 

For more information about these metrics, see [Working with AWS Lambda function metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html) in the *AWS Lambda Developer Guide*.

In addition to these metrics, Compute Optimizer analyzes the memory utilization of your function during the look-back period. For more information about memory utilization for Lambda functions, see [Understanding AWS Lambda behavior using Amazon CloudWatch Logs Insights](https://aws.amazon.com/blogs/mt/understanding-aws-lambda-behavior-using-amazon-cloudwatch-logs-insights/) in the *AWS Management & Governance Blog* and [Using Lambda Insights in CloudWatch](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-insights.html) in the *AWS Lambda Developer Guide*.