# CloudWatch logs for your Network Load Balancer

Amazon CloudWatch Logs support Network Load Balancer access logs as vended logs, improving observability and simplifying debugging for network traffic patterns. You can analyze Network Load Balancer access logs directly in CloudWatch to gain insights into client connections, traffic distribution, and connection status, helping you identify and troubleshoot network issues faster.

You can configure delivery of Network Load Balancer access logs to Amazon CloudWatch Logs, Amazon Data Firehose, and Amazon Simple Storage Service (Amazon S3) with support for Apache Parquet format.

###### Important

Access logs are created only if the load balancer has a TLS listener, and the logs
contain information about TLS requests only. Access logs record requests on a best-effort
basis. We recommend that you use access logs to understand the nature of the requests,
not as a complete accounting of all requests.

###### Important

Traditional "legacy" access logs remain available for Network Load Balancer. To manage configurations for legacy access logs, visit your load balancer's **Attributes** tab. For more information on "legacy" Access logs, see [Access logs for your Network Load Balancer](load-balancer-access-logs.md "load-balancer-access-logs.md").

With this CloudWatch Logs integration, you can track detailed access patterns using CloudWatch Logs Insights queries, create metric filters for monitoring, and review traffic patterns in real time using Live Tail.

You can enable CloudWatch Logs for Network Load Balancer access logs from the load balancer's **Integrations** tab in the console. To enable logging, you must be logged in as a user that has certain permissions. Additionally, you must grant permissions to AWS to enable the logs to be sent.

For required permissions for each logging destination, see [Enable logging from AWS services.](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md")

For more information, see [What is Amazon CloudWatch Logs?](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md").

For pricing information, see [Amazon CloudWatch Pricing.](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/")
