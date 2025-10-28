# Creating CloudWatch alarms for RTB Fabric

You can create CloudWatch alarms to monitor RTB Fabric metrics and automatically notify you when metric values cross specified thresholds. This helps you proactively respond to issues with your RTB gateways and links.

Common alarms you might want to create include:

- _High failure rate_ – Monitor the `failure-request-count` metric to detect when error rates exceed acceptable thresholds. Calculate success rate using (total - failure) / total.
- _High latency_ – Monitor the `total-latency` or `forwarding-latency` metrics to detect performance degradation. Subtract the two to see broker processing time.
- _Low request volume_ – Monitor the `total-request-count` metric to detect unexpected drops in traffic.
- _HTTP error rates_ – Monitor the `request-status-count` metric filtered by HTTP status codes (4xx, 5xx) to detect client or server errors.
  For information about creating CloudWatch alarms, see [Creating Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the _Amazon CloudWatch User Guide_.
