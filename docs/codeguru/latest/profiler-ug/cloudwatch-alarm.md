# Monitoring profiling groups with CloudWatch alarms

You can create an Amazon CloudWatch alarm for your profiling groups to monitor their
recommendations.

An alarm watches the number of recommendations for a profiling group over a period of time
that you specify. You set one or more actions that happen when the number of recommendations
for a profiling group exeeds a count over a number of time periods you choose. For example,
you can specify that an Amazon SNS notification is sent when more than five recommendations are
generated for a profiling group within an hour.

A user or role must have CloudWatch `PutMetricAlarm` permissions to create an alarm.
For more information, see [Using
identity-based policies for CodeGuru Profiler](auth-and-access-control-iam-identity-based-access-control.md "auth-and-access-control-iam-identity-based-access-control.md") and [Amazon CloudWatch permissions reference](../../../AmazonCloudWatch/latest/monitoring/permissions-reference-cw.md "../../../AmazonCloudWatch/latest/monitoring/permissions-reference-cw.md") in the _Amazon CloudWatch User Guide_.

###### To create a CloudWatch alarm for CodeGuru Profiler recommendations

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**.
3. Choose **Create alarm**.
4. Choose **Select metric**.
5. Choose **AWS/CodeGuruProfiler**.
6. Choose **ProfilingGroupName**. Then choose a metric to
   create an alarm for.
7. Continue through the process to create your alarm.

For more information about setting up CloudWatch alarms in the CloudWatch console, see [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the _Amazon CloudWatch User Guide_.
