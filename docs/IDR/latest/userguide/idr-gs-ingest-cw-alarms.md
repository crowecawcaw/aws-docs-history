

# Ingesting CloudWatch alarms
<a name="idr-gs-ingest-cw-alarms"></a>

AWS Incident Detection and Response can ingest Amazon CloudWatch alarms to provide proactive monitoring for your critical workloads. By ingesting your Amazon CloudWatch alarms for monitoring, AWS Incident Detection and Response can:
+ Automatically detect when your alarms enter the "Alarm" state.
+ Engage your teams to collaboratively respond and resolve incidents.

To ensure the alarms you onboard are effective, AWS Incident Detection and Response recommends the following best practices:
+ Configure alarms with [metric math expressions](https://docs.aws.amazon.com/IDR/latest/userguide/suppress-alarms-at-source.html) to suppress them during periods of regular maintenance or batch job executions to avoid false positive alarm engagements.
+ Set the Missing Data Treatment on alarms based on the expected datapoint delivery frequency. For example, alarms monitoring metrics that generate a continuous stream of datapoints should treat missing data as "Breaching" (bad) as missing datapoints could indicate an issue with the underlying resource monitored. Inversely, alarms monitoring metrics that infrequently report datapoints, for example alarms monitoring metrics that only record datapoints when a failure or error occurs, should treat missing data as NotBreaching (good).
+ Define alarms that enter the "Alarm" state when there is critical, ongoing impact to your workload. For example, configure alarms to trigger after the expected time required to automatically replace unhealthy resources, rather than on the initial detection of unhealthy resources.
+ Identify and create alarms for [custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) that directly represent the customer experience for your workload.

For a list of recommended Amazon CloudWatch alarms for common AWS services, see the [Incident Detection and Response Alarm Best Practices on AWS re:Post](https://repost.aws/selections/KP6FA7iQgVSVeSNq1jAcjwxg/incident-detection-and-response-idr).