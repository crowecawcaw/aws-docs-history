

# Monitoring AWS Elemental Inference with vended logs
<a name="monitoring-vended-logs"></a>

With AWS Elemental Inference, you can monitor the processing activity of your feeds using application logs. Elemental Inference publishes these logs as *vended logs*. You can deliver vended logs to the destination that works best for your use case.

Elemental Inference supports the following log destinations:
+ Amazon CloudWatch Logs
+ Amazon Simple Storage Service (Amazon S3)
+ Amazon Data Firehose

You must set up log delivery for each individual feed you would like to receive logs for. You can configure log delivery in the console when you create or edit a feed, or with the CloudWatch Logs delivery API. Elemental Inference supports version 2 (V2) of vended logs. For more information about vended logs, see [Enable logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html).

**Topics**
+ [Pricing](vended-logs-pricing.md)
+ [Enabling logs](vended-logs-enabling.md)
+ [Components of a log](vended-logs-components.md)