# Monitoring AWS FIS experiments

You can use the following tools to monitor the progress and impact of your AWS Fault Injection Service (AWS FIS)
experiments.

**AWS FIS console and AWS CLI**

Use the AWS FIS console or the AWS CLI to monitor the progress of a
running experiment. You can view the status of each action in the
experiment, and the results of each action. For more information, see [View your experiments](view-experiment-progress.md "view-experiment-progress.md").

**CloudWatch usage metrics and alarms**

Use CloudWatch usage metrics to provide visibility into your account's usage of
resources. AWS FIS usage metrics correspond to AWS service quotas. You can configure
alarms that alert you when your usage approaches a service quota. For more information,
see [Monitor using CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

You can also create stop conditions for your AWS FIS experiments by creating CloudWatch alarms
that define when an experiment goes out of bounds. When the alarm is triggered, the
experiment stops. For more information, see [Stop conditions](stop-conditions.md "stop-conditions.md"). For more information about creating CloudWatch alarms,
see [Create a CloudWatch Alarm Based on a Static Threshold](../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md "../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md") and [Creating
a CloudWatch Alarm Based on Anomaly Detection](../../../AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.md "../../../AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.md") in the _Amazon CloudWatch User Guide_.

**AWS FIS experiment logging**

Enable experiment logging to capture detailed information about your
experiment as it runs. For more information see [Experiment logging](monitoring-logging.md "monitoring-logging.md").

**Experiment state change events**

Amazon EventBridge enables you to respond automatically to system events or resource
changes. AWS FIS emits a notification when the state of an experiment changes.
You can create rules for the events that you are interested in that specify
the automated action to take when an event matches a rule. For example, sending
a notification to an Amazon SNS topic or invoking a Lambda function. For more
information, see [Monitor using EventBridge](monitoring-eventbridge.md "monitoring-eventbridge.md").

**CloudTrail logs**

Use AWS CloudTrail to capture detailed information about the calls made to
the AWS FIS API and store them as log files in Amazon S3. CloudTrail also logs calls
made to service APIs for the resources on which you're running experiments. You
can use these CloudTrail logs to determine which calls were made, the source IP
address where the call came from, who made the call, when the call was made, and
so on.

**AWS Health Dashboard Notifications**

AWS Health provides ongoing visibility into your resource performance and the
availability of your AWS services and accounts. When you start an experiment,
AWS FIS emits a notification to your AWS Health Dashboard. The notification is
present for the duration of the experiment in each account that contains resources
targeted in an experiment, including multi-account experiments. Multi-account experiments with only
actions that do not include targets, such as `aws:ssm:start-automation-execution` and `aws:fis:wait`,
will not emit a notification. Information about the role used to allow the experiment
will be listed under **Affected resources**. To learn more about the AWS Health Dashboard,
see [AWS Health Dashboard](../../../health/latest/ug/cloudwatch-events-health.md "../../../health/latest/ug/cloudwatch-events-health.md") in the AWS Health User Guide.

###### Note

AWS Health delivers events on a _best effort_ basis.
