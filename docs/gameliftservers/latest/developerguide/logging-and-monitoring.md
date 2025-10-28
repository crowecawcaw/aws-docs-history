# Logging and monitoring with Amazon GameLift Servers

Monitoring is an important part of maintaining the reliability, availability, and
performance of Amazon GameLift Servers and your AWS solutions. You should collect monitoring data from
all of the parts of your AWS solution so that you can more easily debug a multi-point
failure if one occurs.

AWS and Amazon GameLift Servers provide several tools for monitoring your game hosting resources and
responding to potential incidents.

###### Amazon CloudWatch Alarms

Using Amazon CloudWatch alarms, you watch a single metric over a time period that you
specify. If the metric exceeds a given threshold, a notification is sent to an Amazon
SNS topic or AWS Auto Scaling policy. CloudWatch alarms are triggered when their state
changes and is maintained for a specified number of periods, not by being in a
particular state. For more information, see [Monitor Amazon GameLift Servers with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

###### AWS CloudTrail Logs

CloudTrail provides a record of actions taken by a user, role, or an AWS service in
Amazon GameLift Servers. Using the information collected by CloudTrail, you can determine the request
that was made to Amazon GameLift Servers, the IP address from which the request was made, who made the
request, when it was made, and additional details. For more information, see [Logging Amazon GameLift Servers API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").
