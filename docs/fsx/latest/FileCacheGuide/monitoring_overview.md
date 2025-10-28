# Monitoring Amazon File Cache

You can use the following automated monitoring tools to watch Amazon File Cache and report
when something is wrong:

- **Monitoring using Amazon CloudWatch** – CloudWatch collects and processes
  raw data from Amazon File Cache into readable, near real-time metrics. You can create a CloudWatch alarm that
  sends an Amazon SNS message when the alarm changes state.
- **Log monitoring using AWS CloudTrail** – You can share log files between
  accounts, monitor CloudTrail log files in real time by sending them to CloudWatch Logs, write log processing
  applications in Java, and validate that your log files have not changed after delivery by
  CloudTrail.

###### Topics

- [Monitoring with CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Logging Amazon File Cache API calls with CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
