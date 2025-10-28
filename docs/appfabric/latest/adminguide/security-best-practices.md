# Security best practices for AWS AppFabric

AWS AppFabric provides several security features to consider as you develop and implement your
own security policies. The following best practices are general guidelines and don't
represent a complete security solution. Because these best practices might not be
appropriate or sufficient for your environment, treat them as helpful considerations rather
than prescriptions.

## Monitor for application

without admin access

With the read-only AWS Identity and Access Management (IAM) permission, anyone can integrate AppFabric with
Amazon Quick Suite and other security information and event management (SIEM) tools, such as
Splunk. To monitor application security, data is delivered to an
Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose delivery stream.

## Monitor for AppFabric events

You can monitor AppFabric using Amazon CloudWatch metrics. CloudWatch collects data from AppFabric every
minute and processes it into metrics. You can set alarms that set off notifications when
metrics match specified thresholds. For more information, see [Monitoring AWS AppFabric with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
