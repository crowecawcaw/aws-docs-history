End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Security event logging and monitoring in AWS SimSpace Weaver

Monitoring is an important part of maintaining the reliability, availability, and
performance of SimSpace Weaver and your AWS solutions. You should collect monitoring data from all
of the parts of your AWS solution so that you can more easily debug a multi-point failure if one
occurs.

AWS and SimSpace Weaver provide several tools for monitoring your simulation resources and responding to potential incidents.

###### Logs in Amazon CloudWatch

SimSpace Weaver stores its logs in CloudWatch. You can use these logs to monitor events in your simulation
(such as starting and stopping apps) as well as for debugging. For more information, see
[SimSpace Weaver logs in Amazon CloudWatch Logs](cloudwatch-logs.md "cloudwatch-logs.md").

###### Amazon CloudWatch Alarms

Using Amazon CloudWatch alarms, you watch a single metric over a time period that you specify. If the metric exceeds a given threshold,
a notification is sent to an Amazon SNS topic or AWS Auto Scaling policy. CloudWatch alarms are triggered when their state changes
and is maintained for a specified number of periods, not by being in a particular state. For more information, see
[Monitoring SimSpace Weaver with Amazon CloudWatch](monitoring-with-cloudwatch.md "monitoring-with-cloudwatch.md").

###### AWS CloudTrail Logs

CloudTrail provides a record of actions taken by a user, role, or an AWS service in SimSpace Weaver. Using the information collected by CloudTrail,
you can determine the request that was made to SimSpace Weaver, the IP address from which the request was made, who made the request, when it was made,
and additional details. For more information, see [Logging AWS SimSpace Weaver API calls using AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").
