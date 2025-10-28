# Logging and monitoring in DataBrew

Monitoring is an important part of maintaining the reliability, availability, and
performance of DataBrew and your AWS solutions. You should collect monitoring data from all
of the parts of your AWS solution so that you can more easily debug a multipoint failure
if one occurs. AWS provides several tools for monitoring your DataBrew resources and
responding to potential incidents:

**Amazon CloudWatch Alarms**

Using Amazon CloudWatch alarms, you watch a single metric over a time period that you
specify. If the metric exceeds a given threshold, a notification is sent to an
Amazon SNS topic or AWS Auto Scaling policy. CloudWatch alarms don't invoke actions because
they are in a particular state. Rather, the state must have changed and been
maintained for a specified number of periods.

**AWS CloudTrail Logs**

CloudTrail provides a record of actions taken by a user, role, or an AWS service
in DataBrew. Using the information collected by CloudTrail, you can determine the request
that was made to DataBrew, the IP address from which the request was made, who made
the request, when it was made, and additional details.
