# Logging and monitoring in AWS Global Accelerator

Monitoring is an important part of maintaining the availability and performance of Global Accelerator
and your AWS solutions. You should collect monitoring data from all of the parts of your AWS solution
so that you can more easily debug a multi-point failure if one occurs. AWS provides several tools for
monitoring your Global Accelerator resources and activity, and responding to potential incidents:

Global Accelerator provides the following three main avenues for logging and tracking:

**Amazon CloudWatch metrics and alarms**
Using CloudWatch, you can monitor, in real time, your AWS resources and the applications that
you run on AWS. As soon as your accelerator is deployed, CloudWatch begins collect and tracking metrics for Global Accelerator. Metrics
are variables that you can view for confirmation that traffic is flowing, or that you can measure over time.

You can use metrics, for example, to verify that traffic is flowing through Global Accelerator to your endpoints, and back out
to clients, and to help troubleshoot issues. You can also create alarms that watch specific metrics,
and then send notifications or automatically make changes to the resources you are monitoring when the metric
exceeds a certain threshold for a period of time.

For more information, see [Using Amazon CloudWatch with AWS Global Accelerator](cloudwatch-monitoring.md "cloudwatch-monitoring.md").

**Global Accelerator flow logs**
Server flow logs are logs that you set up in Global Accelerator that provide detailed
records about traffic that flows through an accelerator to an
endpoint. Server flow logs are useful for many applications, for example, for security and access audits. For more
information, see [Configuring and using flow logs in AWS Global Accelerator](monitoring-global-accelerator.md "monitoring-global-accelerator.md").

**AWS CloudTrail logs**
CloudTrail provides a record of actions taken by a user, role, or an AWS service in Global Accelerator. CloudTrail
captures all API calls for Global Accelerator as events, including calls from the Global Accelerator console and from code calls to the Global Accelerator API.
For more information, see [Using AWS CloudTrail to log AWS Global Accelerator API calls](logging-using-cloudtrail.md "logging-using-cloudtrail.md").
