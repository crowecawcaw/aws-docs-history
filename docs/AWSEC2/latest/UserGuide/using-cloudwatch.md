# Monitor your instances using CloudWatch

You can monitor your instances using Amazon CloudWatch, which collects and processes raw data from
Amazon EC2 into readable, near real-time metrics. These statistics are recorded for a period of 15
months, so that you can access historical information and gain a better perspective on how your
web application or service is performing.

By default, Amazon EC2 sends metric data to CloudWatch in 5-minute periods. To send metric data for
your instance to CloudWatch in 1-minute periods, you can enable detailed monitoring on the instance.
For more information, see [Manage detailed monitoring for your EC2 instances](manage-detailed-monitoring.md "manage-detailed-monitoring.md").

The Amazon EC2 console displays a series of graphs based on the raw data from Amazon CloudWatch. Depending
on your needs, you might prefer to get data for your instances from Amazon CloudWatch instead of the
graphs in the console.

For Amazon CloudWatch billing and cost information, see [CloudWatch billing and cost](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_billing.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_billing.md") in the _Amazon CloudWatch User Guide_.

###### Contents

- [Manage CloudWatch alarms for your EC2 instances in the Amazon EC2 console](ec2-instance-alarms.md "ec2-instance-alarms.md")
- [Manage detailed monitoring for your EC2 instances](manage-detailed-monitoring.md "manage-detailed-monitoring.md")
- [CloudWatch metrics that are available for your
  instances](viewing_metrics_with_cloudwatch.md "viewing_metrics_with_cloudwatch.md")
- [Install and configure the CloudWatch
  agent using the Amazon EC2 console to add additional metrics](install-and-configure-cloudwatch-agent-using-ec2-console.md "install-and-configure-cloudwatch-agent-using-ec2-console.md")
- [Statistics for CloudWatch metrics for your
  instances](monitoring_get_statistics.md "monitoring_get_statistics.md")
- [View the monitoring graphs for your instances](graphs-in-the-aws-management-console.md "graphs-in-the-aws-management-console.md")
- [Create a CloudWatch alarm for an instance](using-cloudwatch-createalarm.md "using-cloudwatch-createalarm.md")
- [Create alarms that stop, terminate, reboot, or recover an
  instance](UsingAlarmActions.md "UsingAlarmActions.md")
