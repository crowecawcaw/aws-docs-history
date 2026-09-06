

# Create an alarm using a PromQL query
<a name="Create_PromQL_Alarm"></a>

You can create a CloudWatch alarm that uses a PromQL instant query to monitor metrics ingested through the CloudWatch OTLP endpoint. All matching time series returned by the query are considered to be breaching, and the alarm tracks each breaching time series as a contributor. For more information about how PromQL alarms work, see [PromQL alarms](alarm-promql.md).

## Creating a PromQL alarm using the AWS Management Console
<a name="promql-alarm-create-console"></a>

This example shows how to create an alarm that monitors a gauge metric and alerts you when its value drops below 20.

**To create a PromQL alarm**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Alarms**, **All Alarms**.

1. Choose **Create alarm**.

1. Choose **PromQL** for the metric type.

1. In **Editor** mode, enter the PromQL query:

   ```
   my_gauge_metric < 20
   ```

1. Under **Conditions**, specify the following:
   + For **Evaluation interval**, choose **1 minute**, to define how often the PromQL query is evaluated.
   + For **Pending period**, enter **120**, duration in seconds a contributor must be breaching before entering ALARM state.
   + For **Recovery period**, enter **300**, duration in seconds a contributor must not be breaching before entering OK state.

1. Configure notifications and actions as needed.

1. Add a name and description for your alarm.

1. Choose **Next**.

1. Choose **Create alarm**.

## Creating a PromQL alarm (AWS CLI)
<a name="promql-alarm-create-cli"></a>

Use the [PutMetricAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html) API action to create a PromQL alarm.

**Example Create a PromQL alarm that triggers when a gauge metric drops below 20**  

```
aws cloudwatch put-metric-alarm \
  --alarm-name MyPromQLAlarm \
  --evaluation-criteria '{"PromQLCriteria":{"Query":"my_gauge_metric < 20"}}' \
  --evaluation-interval 60
```

**Example Create a PromQL alarm with a pending period**  
This alarm waits 300 seconds (5 minutes) before transitioning to `ALARM` state, and waits 600 seconds (10 minutes) before recovering.  

```
aws cloudwatch put-metric-alarm \
  --alarm-name HighLatencyAlarm \
  --evaluation-criteria '{"PromQLCriteria":{"Query":"histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m])) > 0.5","PendingPeriod":300,"RecoveryPeriod":600}}' \
  --evaluation-interval 60
```

**Example Create a PromQL alarm with an SNS notification action**  

```
aws cloudwatch put-metric-alarm \
  --alarm-name MyPromQLAlarmWithAction \
  --evaluation-criteria '{"PromQLCriteria":{"Query":"my_gauge_metric < 20","PendingPeriod":0,"RecoveryPeriod":0}}' \
  --evaluation-interval 60 \
  --alarm-actions arn:aws:sns:us-east-1:123456789012:MyTopic
```

## Creating a PromQL alarm from Query Studio
<a name="promql-alarm-create-query-studio"></a>

This example shows how to create a PromQL alarm from Query Studio that alerts you when the average HTTP request duration for a service exceeds 500 milliseconds.

Unlike standard CloudWatch alarms where the threshold is configured as a separate step, PromQL alarms define the alarm condition (threshold) as part of the query itself. For example, the comparison operator (`>`) and threshold value (`0.5`) are embedded directly in the PromQL expression.

**To create a PromQL alarm from Query Studio**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane below **Metrics**, choose **Query Studio**.

1. Select **PromQL** from the query language drop-down menu.

1. Build your query using one of the following modes:
   + In **Builder** mode, select a metric name from the **Metric** field (for example, `http.server.request.duration`). Add label filters as needed (for example, `@resource.service.name` = `my-api`). To define the alarm threshold, select a **Basic Operation** (for example, `>`) and enter a **Number** (for example, `0.5`).
   + In **Code** mode, enter the PromQL expression directly, for example:

     ```
     histogram_avg({"http.server.request.duration", "@resource.service.name"="my-api"}) > 0.5
     ```

1. Choose **Run** to execute the query and verify it returns the expected results.

1. Choose **Create alarm** from the actions menu.

1. You are redirected to the CloudWatch alarm creation page with your PromQL query pre-populated.

1. Under **Conditions**, specify the following:
   + For **Evaluation interval**, choose **1 minute**, to define how often the PromQL query is evaluated.
   + For **Pending period**, enter **60**, duration in seconds the query must be breaching before entering ALARM state. This means the latency must exceed the threshold for at least 60 seconds before the alarm fires.
   + For **Recovery period**, enter **120**, duration in seconds the query must not be breaching before entering OK state. This means the latency must stay below the threshold for at least 120 seconds before the alarm recovers.

1. Configure notifications and actions as needed.

1. Add a name and description for your alarm.

1. Choose **Next**.

1. Choose **Create alarm**.

**Note**  
The PromQL query must return a single time series to create an alarm. If your query returns multiple time series, use aggregation functions such as `sum`, `avg`, or `topk` to reduce the result to a single series before creating the alarm.