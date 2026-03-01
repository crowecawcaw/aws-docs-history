# Monitor CloudFront metrics with Amazon CloudWatch

Amazon CloudFront is integrated with Amazon CloudWatch and automatically publishes operational metrics for
distributions and edge functions (both [Lambda@Edge and
CloudFront Functions](edge-functions.md "edge-functions.md")). You can use these metrics to troubleshoot, track, and debug
issues. Many of these metrics are displayed in a set of graphs in the CloudFront console, and are
also accessible by using the CloudFront API or CLI. All of these metrics are available in the
[CloudWatch console](https://console.aws.amazon.com/cloudwatch/home "https://console.aws.amazon.com/cloudwatch/home") or through the CloudWatch API
or CLI. CloudFront metrics don't count against [CloudWatch quotas (formerly known as limits)](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_limits.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_limits.md") and don't incur any additional
cost.

In addition to the default metrics for CloudFront distributions, you can turn on additional
metrics for an additional cost. The additional metrics apply to CloudFront distributions, and must
be turned on for each distribution separately. For more information about the cost, see
[Estimate the cost for the additional CloudFront metrics](viewing-cloudfront-metrics.md#monitoring-console.distributions-additional-pricing "viewing-cloudfront-metrics.md#monitoring-console.distributions-additional-pricing").

You can also set alarms based on these metrics in the CloudFront console, or in the CloudWatch
console, API, or CLI. For example, you can set an alarm based on the
`5xxErrorRate` metric, which represents the percentage of all viewer requests
for which the response's HTTP status code is in the range of `500` to
`599`, inclusive. When the error rate reaches a certain value for a certain
amount of time, for example, 5% of requests for 5 continuous minutes, the alarm is
triggered. You specify the alarm's value and its time unit when you create the alarm.

###### Notes

- When you create a CloudWatch alarm in the CloudFront console, it creates one for you in the US East (N. Virginia) Region (`us-east-1`). If you create an alarm from the CloudWatch console, you must use the same Region. Because CloudFront is a global service, metrics for the service are sent to US East (N. Virginia).
- When creating alarms, [standard CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/") applies.

###### Topics

- [View CloudFront and edge function metrics](viewing-cloudfront-metrics.md "viewing-cloudfront-metrics.md")
- [Create alarms for metrics](receiving-notifications.md "receiving-notifications.md")
- [Download metrics data in CSV format](cloudwatch-csv.md "cloudwatch-csv.md")
- [Types of metrics for CloudFront](programming-cloudwatch-metrics.md "programming-cloudwatch-metrics.md")
