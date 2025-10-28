# Monitoring your AWS IoT Wireless resources using

Amazon CloudWatch Logs

Monitoring is an important part of maintaining the reliability, availability, and
performance of AWS IoT Wireless and your other AWS solutions. You can use monitoring for both
your LoRaWAN and Sidewalk devices and obtain informative messages and errors from when they
are onboarded to AWS IoT Wireless.

We strongly encourage you to collect monitoring data from all parts of your AWS solution
to make it easier to debug a multi-point failure, if one occurs. Start by creating a
monitoring plan that answers the following questions. If you're not sure how to answer
these, you can still continue to enable logging and establish your performance
baselines.

- What are your monitoring goals?
- Which resources will you monitor?
- How often will you monitor these resources?
- Which monitoring tools will you use?
- Who will perform the monitoring tasks?
- Who should be notified when something goes wrong?
  Your next step is to enable logging and establish a baseline of normal AWS IoT Wireless
  performance in your environment by measuring performance at various times and under
  different load conditions. As you monitor AWS IoT Wireless, keep historical monitoring data so
  that you can compare it with current performance data. This will help you identify normal
  performance patterns and performance anomalies, and devise methods to address issues.

## Monitoring tools

You can use the following monitoring tools to watch AWS IoT Wireless, report when something
is wrong, and take automatic actions when appropriate:

- Amazon CloudWatch monitors your AWS resources and and the applications you run on
  AWS in real time. You can collect and track metrics, create customized
  dashboards, and set alarms that notify you or take actions when a specified
  metric reaches a threshold that you specify. For example, you can have CloudWatch
  track CPU usage or other metrics of your Amazon EC2 instances and automatically
  launch new instances when needed. For more information, see the
  [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- Network analyzer enables you to monitor your LoRaWAN resources, which includes
  LoRaWAN devices and gateways. The network analyzer reduces the time that it
  takes to set up a connection to start receiving trace messages, providing you
  with just-in-time log information. For more information, see [Monitoring of LoRaWAN resources using network
  analyzer](network-analyzer-overview.md "network-analyzer-overview.md").

## How to monitor resources using Amazon CloudWatch

You can monitor AWS IoT Wireless using CloudWatch, which collects raw data and processes it
into readable, near real-time metrics. These statistics are kept for 15 months, so that
you can access historical information and gain a better perspective on how your web
application or service is performing. You can also set alarms that watch for certain
thresholds, and send notifications or take actions when those thresholds are met. For
more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

To log and monitor your AWS IoT Wireless resources, perform the following
steps:

1. Create a logging role to log your AWS IoT Wireless resources, as described
   in [Create logging role and policy for
   AWS IoT Wireless monitoring](create-logging-role-policy.md "create-logging-role-policy.md").
2. Log messages in the CloudWatch Logs console have a default log level of
   `ERROR`, which is less verbose and contains only error
   information. If you want to view more verbose messages, we recommend that you
   first configure logging, as described in [Configure resource logging for
   AWS IoT Wireless resources](configure-resource-logging.md "configure-resource-logging.md").
3. Next, you can monitor your resources by viewing the log entries in the CloudWatch Logs
   console. For more information, see [View CloudWatch AWS IoT Wireless log entries](cwl-format.md "cwl-format.md").
4. You can create filter expressions by using **Logs groups**
   but we recommend that you first create simple filters and view log entries in
   the log groups, and then go to CloudWatch Insights to create queries to filter the log
   entries depending on the resource or event you're monitoring. For more
   information, see [Use CloudWatch Insights to filter logs for
   AWS IoT Wireless](cwl-insights.md "cwl-insights.md").
