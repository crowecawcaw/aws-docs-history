# Logging metrics for AWS AppConfig data plane

calls

If you configured AWS CloudTrail to log AWS AppConfig data events, you can enable Amazon CloudWatch Logs to log
metrics for calls to the AWS AppConfig data plane. You can then search and filter log data in CloudWatch Logs
by creating one or more metric filters. Metric filters define the terms and patterns to look
for in log data as it is sent to CloudWatch Logs. CloudWatch Logs uses metric filters to turn log data into
numerical CloudWatch metrics. You can graph metrics or configure them with an alarm.

###### Before you begin

Enable logging of AWS AppConfig data events in AWS CloudTrail. The following procedure describes how
to enable metric logging for an _existing AWS AppConfig trail_ in CloudTrail. For
information about how to enable CloudTrail logging for AWS AppConfig data plan calls, see [AWS AppConfig data events in CloudTrail](logging-using-cloudtrail.md#cloudtrail-data-events "logging-using-cloudtrail.md#cloudtrail-data-events").

Use the following procedure to enable CloudWatch Logs to log metrics for calls to the AWS AppConfig data
plane.

###### To enable CloudWatch Logs to log metrics for calls to the AWS AppConfig data plane

1. Open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. On the dashboard, choose your AWS AppConfig trail.
3. In the **CloudWatch Logs** section, choose **Edit**.
4. Choose **Enabled**.
5. For **Log group name**, either leave the default name or enter a
   name. Make a note of the name. You will choose the log group in the CloudWatch Logs console
   later.
6. For **Role name**, enter a name.
7. Choose **Save changes**.
   Use the following procedure to create a metric and a metric filter for AWS AppConfig in CloudWatch Logs.
   The procedure describes how to create a metric filter for calls by `operation` and
   (optionally) calls by `operation` and `Amazon Resource Name
 (ARN)`.

###### To create a metric and a metric filter for AWS AppConfig in CloudWatch Logs

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, and then choose
   **Log groups**.
3. Choose the checkbox beside the AWS AppConfig log group.
4. Choose **Actions**, and then choose **Create metric
   filter**.
5. For **Filter name**, enter a name.
6. For **Filter pattern**, enter the following:

```
{ $.eventSource = "appconfig.amazonaws.com" }
```

7. (Optional) In the **Test pattern** section, choose your log group
   from the **Select log data to test** list. If CloudTrail hasn't logged any
   calls, you can skip this step.
8. Choose **Next**.
9. For **Metric namespace**, enter `AWS AppConfig`.
10. For **Metric name**, enter `Calls`.
11. For **Metric value**, enter `1`.
12. Skip **Default value** and **Unit**.
13. For **Dimension name**, enter
    `operation`.
14. For **Dimension value**, enter
    `$.eventName`.

(Optional) You can enter a second dimension that includes the Amazon Resource Name
(ARN) making the call. To add a second dimension, for **Dimension name**,
enter `resource`. For **Dimension value**, enter
`$.resources[0].ARN`.

Choose **Next**. 15. Review the details of the filter and **Create metric filter**.
(Optional) You can repeat this procedure to create a new metric filter for a specific
error code like _AccessDenied_. If you do, enter the following
details:

1. For **Filter name**, enter a name.
2. For **Filter pattern**, enter the following:

```
{ $.errorCode = "`codename`" }
```

For example

```
{ $.errorCode = "`AccessDenied`" }
```

3. For **Metric namespace**, enter `AWS AppConfig`.
4. For **Metric name**, enter `Errors`.
5. For **Metric value**, enter `1`.
6. For **Default value**, enter a zero (0).
7. Skip **Unit**, **Dimensions**, and
   **Alarms**.
   After CloudTrail logs API calls, you can view metrics in CloudWatch. For more information, see [Viewing
   your metrics and logs in the console](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_View.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_View.md") in the _Amazon CloudWatch User Guide_.
   For information about how to locate a metric you created, see [Search for
   available metrics](../../../AmazonCloudWatch/latest/monitoring/finding_metrics_with_cloudwatch.md "../../../AmazonCloudWatch/latest/monitoring/finding_metrics_with_cloudwatch.md").

###### Note

If you set up the error metric with no dimension, as described here, you can view those
metrics on the **Metrics with no dimension** page.

## Creating an alarm for a CloudWatch

metric

After you create metrics, you can create metric alarms in CloudWatch. For example, you can
create an alarm for the _AWS AppConfig calls_ metric you created in the previous
procedure. Specifically, you can create an alarm for calls to the AWS AppConfig
`StartConfigurationSession` API action that surpass a threshold. For
information about how to create an alarm for a metric, see [Create a CloudWatch alarm based on a
static threshold](../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md "../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md") in the _Amazon CloudWatch User Guide_. For information
about default limits for calls to the AWS AppConfig data plane, see [Data plane default limits](../../../general/latest/gr/appconfig.md#limits_appconfig "../../../general/latest/gr/appconfig.md#limits_appconfig")
in the _Amazon Web Services General Reference_.
