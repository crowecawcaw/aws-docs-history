

# Lambda function metrics

Compute Optimizer analyzes the following CloudWatch metrics of your Lambda functions. It uses these metrics to make its Lambda function recommendations.


**Metrics analyzed for Lambda functions**  

| Metric | Description | 
| --- | --- | 
|  Invocations  | The number of times Lambda runs your function code. This includes runs that succeed and runs that end in a function error. | 
|  Duration  | The amount of time that your function code spends processing an event. | 
|  Errors  | The number of invocations that end in a function error, such as an error from your code or from the Lambda runtime. | 
|  Throttles  | The number of invocation requests that are throttled. | 

For more information about these metrics, see [Using Amazon CloudWatch metrics with Lambda](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html) in the *AWS Lambda Developer Guide*.

In addition to these metrics, Compute Optimizer analyzes the memory utilization of your function during the look-back period. For more information about memory utilization for Lambda functions, see [Understanding AWS Lambda behavior using Amazon CloudWatch Logs Insights](https://aws.amazon.com/blogs/mt/understanding-aws-lambda-behavior-using-amazon-cloudwatch-logs-insights/) in the *AWS Management & Governance Blog* and [Using Lambda Insights in CloudWatch](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-insights.html) in the *AWS Lambda Developer Guide*.