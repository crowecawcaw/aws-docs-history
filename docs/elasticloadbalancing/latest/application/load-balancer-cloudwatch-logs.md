

# CloudWatch Logs for your Application Load Balancer
<a name="load-balancer-cloudwatch-logs"></a>

Amazon CloudWatch Logs support Application Load Balancer logs as vended logs, improving observability and simplifying debugging for network traffic patterns. You can analyze Application Load Balancer logs directly in CloudWatch to gain insights into client connections, traffic distribution, connection status, and target health, helping you identify and troubleshoot network and target issues faster.

You can configure delivery of Application Load Balancer access logs to Amazon CloudWatch Logs, Amazon Data Firehose, and Amazon Simple Storage Service (Amazon S3) with support for Apache Parquet format.

This integration supports the following Application Load Balancer log types:
+ Access logs
+ Connection logs
+ Health check logs

**Important**  
Traditional "legacy" logs remain available for Application Load Balancer. To manage configurations for legacy logs, visit your load balancer's **Attributes** tab. For more information on legacy logs, see the specific log type under [Monitor your Application Load Balancers](load-balancer-monitoring.md).

With this CloudWatch Logs integration, you can track detailed access patterns using CloudWatch Logs Insights queries, create metric filters for monitoring, and review traffic patterns in real time using Live Tail.

You can enable CloudWatch Logs for Application Load Balancer logs from the load balancer's **Integrations** tab in the console. To enable logging, you must be logged in as a user that has certain permissions. Additionally, you must grant permissions to AWS to enable the logs to be sent.

For required permissions for each logging destination, see [Enable logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html).

For more information, see the [Amazon CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html).

For pricing information, see [CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).