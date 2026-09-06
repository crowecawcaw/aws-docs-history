

# Creating CloudWatch alarms for RTB Fabric
<a name="monitoring-cloudwatch-alarms"></a>

You can create CloudWatch alarms to monitor RTB Fabric metrics and automatically notify you when metric values cross specified thresholds. This helps you proactively respond to issues with your RTB gateways and links.

Common alarms you might want to create include:
+ *High failure rate* – Monitor the `failure-request-count` metric to detect when error rates exceed acceptable thresholds. Calculate success rate using (total - failure) / total.
+ *High latency* – Monitor the `total-latency` or `forwarding-latency` metrics to detect performance degradation. Subtract the two to see service processing time.
+ *Low request volume* – Monitor the `total-request-count` metric to detect unexpected drops in traffic.
+ *HTTP error rates* – Monitor the `request-status-count` metric filtered by HTTP status codes (4xx, 5xx) to detect client or server errors.
+ *High filter rate* – Monitor the `filter-transaction` metric to detect unexpected increases in filtered traffic.

For information about creating CloudWatch alarms, see [Creating Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.