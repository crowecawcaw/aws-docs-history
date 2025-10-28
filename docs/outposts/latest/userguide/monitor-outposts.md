# Monitor your Outposts rack

AWS Outposts integrates with the following services that offer monitoring and logging
capabilities:

**CloudWatch metrics**

Use Amazon CloudWatch to retrieve statistics about data points for your Outposts rack
as an ordered set of time series data, known as _metrics_. You can use
these metrics to verify that your system is performing as expected. For more information,
see [CloudWatch metrics for Outposts racks](outposts-cloudwatch-metrics.md "outposts-cloudwatch-metrics.md").

**CloudTrail logs**

Use AWS CloudTrail to capture detailed information about the calls
made to AWS APIs. You can store these calls as log files in Amazon S3. You can use these CloudTrail
logs to determine such information as which call was made, the source IP address where the
call came from, who made the call, and when the call was made.

The CloudTrail logs contain information about the calls to API actions for AWS Outposts. They
also contain information for calls to API actions from services on an Outpost, such as
Amazon EC2 and Amazon EBS. For more information, see [Log API calls using CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

**VPC Flow Logs**

Use VPC Flow Logs to capture detailed information about the traffic going to and from
your Outpost and within your Outpost. For more information, see [VPC Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") in the
_Amazon VPC User Guide_.

**Traffic Mirroring**

Use Traffic Mirroring to copy and forward network traffic from your
Outposts rack to out-of-band security and monitoring appliances. You can use the
mirrored traffic for content inspection, threat monitoring, or troubleshooting. For more
information, see the [Amazon VPC Traffic Mirroring
Guide](../../../vpc/latest/mirroring/what-is-traffic-mirroring.md "../../../vpc/latest/mirroring/what-is-traffic-mirroring.md").

**AWS Health Dashboard**

The AWS Health Dashboard displays information and notifications that are initiated by changes in the
health of AWS resources. The information is presented in two ways: on a dashboard that
shows recent and upcoming events organized by category, and in a full event log that shows
all events from the past 90 days. For example, a connectivity issue on the service link
would initiate an event that would appear on the dashboard and event log, and remain in
the event log for 90 days. A part of the AWS Health service, AWS Health Dashboard requires no setup
and can be viewed by any user that is authenticated in your account. For more information,
see [Getting started with the
AWS Health Dashboard](../../../health/latest/ug/getting-started-health-dashboard.md "../../../health/latest/ug/getting-started-health-dashboard.md").
