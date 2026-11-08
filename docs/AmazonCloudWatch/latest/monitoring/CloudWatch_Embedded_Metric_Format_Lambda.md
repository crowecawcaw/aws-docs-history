

# Using the embedded metric format with Lambda
<a name="CloudWatch_Embedded_Metric_Format_Lambda"></a>

You do not need to install the CloudWatch agent to publish embedded metric format logs from Lambda functions. Lambda automatically sends everything that your function writes to standard output (STDOUT) to a CloudWatch Logs log group, and CloudWatch Logs extracts metrics from any log events that follow the embedded metric format specification. On hosts and containers, the agent forwards logs to CloudWatch Logs, but Lambda delivers the logs for you, so you do not need the agent.

To publish metrics from a function, write embedded metric format logs to STDOUT. Make sure that your logs follow the [Specification: Embedded metric format](CloudWatch_Embedded_Metric_Format_Specification.md), or use the [Creating logs in embedded metric format using the client libraries](CloudWatch_Embedded_Metric_Format_Libraries.md) to generate them for you.

**Note**  
Lambda does not handle function timeouts automatically. If your function times out before it flushes its metrics, CloudWatch Logs does not capture the metrics for that invocation.

**Note**  
For Node.js with the Lambda JSON log format, use version 4.1.1 or later of the embedded metric format client library. Earlier versions cause metric loss in Lambda environments. For more information, see [Accessing Amazon CloudWatch logs for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html).