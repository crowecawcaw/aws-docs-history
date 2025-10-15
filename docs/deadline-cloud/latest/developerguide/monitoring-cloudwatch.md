# Monitoring with CloudWatch

Amazon CloudWatch (CloudWatch) collects raw data and processes it into readable, near real-time metrics.
 You can open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/") to view and filter Deadline Cloud
 metrics.

These statistics are kept for 15 months so you can access historical information to gain a
 better perspective on how your web application or service is performing. You can also set
 alarms that watch for certain thresholds, and send notifications or take actions when those
 thresholds are met. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ "https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/").

Deadline Cloud has two kinds of logs â task logs and worker logs. A task log is when you run
 execution logs as a script or as DCC runs. A task log might show events such as assets
 loading, tiles rendering, or textures not being found.

A worker log shows worker agent processes. These might include things such as when the
 worker agents starts up, registers itself, reports progress, loads configurations, or
 completes tasks.

The namespace for these logs is `/aws/deadline/*`.

For Deadline Cloud, workers upload these logs to CloudWatch Logs. By default, logs never expire. If a job
 outputs a high volume of data, you can incur extra costs. For more information, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/#Paid_tier "https://aws.amazon.com/cloudwatch/pricing/#Paid_tier").

You can adjust the retention policy for each log group. A shorter retention removes old
 logs and can help reduce storage costs. To keep logs, you can archive them to Amazon Simple Storage Service before
 removing the log. For more information, see  [Export log data to Amazon S3 using
 the console](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3ExportTasksConsole.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3ExportTasksConsole.html")  in the *Amazon CloudWatch user guide*.

###### Note

CloudWatch log reads are limited by AWS. If you plan to onboard many artists, we suggest you
 contact AWS customer support and request an increase for the `GetLogEvents`
 quota in CloudWatch. Additionally, we recommend you close the log tailing portal when you are not
 debugging.

For more information, see [CloudWatch Logs quotas](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.html") in the
 *Amazon CloudWatch user guide*.
