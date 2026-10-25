

# Create an alarm using a PromQL query
<a name="Create_PromQL_Alarm"></a>

You can create a CloudWatch alarm that uses a PromQL instant query to monitor metrics ingested through the CloudWatch OTLP endpoint. All matching time series returned by the query are considered breaching, and the alarm tracks each breaching time series as a contributor. For more information about how PromQL alarms work, see [PromQL alarms](alarm-promql.md).

## Creating a PromQL alarm using the AWS Management Console
<a name="promql-alarm-create-console"></a>

This example creates an alarm that monitors the HTTP 5xx server-error rate for the checkout-api service and alerts you when the error rate exceeds 5 percent.

**To create a PromQL alarm**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Alarms**, **All alarms**.

1. Choose **Create alarm**.

1. Choose **PromQL** for the metric type.

1. In **Editor** mode, enter the PromQL query:

   ```
   sum(rate({"http.server.request.count", "@resource.service.name"="checkout-api", "http.response.status_code"=~"5.."}[5m])) / sum(rate({"http.server.request.count", "@resource.service.name"="checkout-api"}[5m])) * 100 > 5
   ```

1. Under **Conditions**, specify the following:
   + For **Evaluation interval**, choose **1 minute**. This value defines how often CloudWatch evaluates the PromQL query.
   + For **Pending period**, enter **120**. This value is the number of seconds that a contributor must breach before it enters the `ALARM` state.
   + For **Recovery period**, enter **300**. This value is the number of seconds that a contributor must stop breaching before it enters the `OK` state.

1. Configure notifications and actions as needed.

1. Add a name and description for your alarm.

1. Choose **Next**.

1. Choose **Create alarm**.

## Creating a PromQL alarm (AWS CLI)
<a name="promql-alarm-create-cli"></a>

Use the [PutMetricAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html) API action to create a PromQL alarm.

**Example: PromQL alarm that triggers when the 5xx error rate for a service exceeds 5 percent**  
This alarm notifies an Amazon SNS topic when the 5xx error rate exceeds 5 percent. It waits 60 seconds (the pending period) before entering the `ALARM` state, and 300 seconds (the recovery period) before returning to `OK`.  

```
aws cloudwatch put-metric-alarm \
  --alarm-name MyPromQLAlarm \
  --evaluation-criteria '{"PromQLCriteria":{"Query":"sum(rate({\"http.server.request.count\", \"@resource.service.name\"=\"checkout-api\", \"http.response.status_code\"=~\"5..\"}[5m])) / sum(rate({\"http.server.request.count\", \"@resource.service.name\"=\"checkout-api\"}[5m])) * 100 > 5","PendingPeriod":60,"RecoveryPeriod":300}}' \
  --evaluation-interval 60 \
  --alarm-actions arn:aws:sns:us-east-1:123456789012:MyTopic
```

**Example: PromQL alarm for p99 request latency with a pending period**  
This alarm waits 300 seconds (5 minutes) before transitioning to the `ALARM` state, and waits 600 seconds (10 minutes) before recovering.  

```
aws cloudwatch put-metric-alarm \
  --alarm-name HighLatencyAlarm \
  --evaluation-criteria '{"PromQLCriteria":{"Query":"histogram_quantile(0.99, {\"http.server.request.duration\", \"@resource.service.name\"=\"checkout-api\"}) > 0.5","PendingPeriod":300,"RecoveryPeriod":600}}' \
  --evaluation-interval 60
```

**Example Create a PromQL alarm with an SNS notification action**  

```
aws cloudwatch put-metric-alarm \
  --alarm-name MyPromQLAlarmWithAction \
  --evaluation-criteria '{"PromQLCriteria":{"Query":"avg by (\"@resource.k8s.pod.name\") (rate(container_cpu_usage_seconds_total{\"@resource.k8s.namespace.name\"=\"production\"}[5m])) * 100 > 80","PendingPeriod":0,"RecoveryPeriod":0}}' \
  --evaluation-interval 60 \
  --alarm-actions arn:aws:sns:us-east-1:123456789012:MyTopic
```

**Example: PromQL anomaly-detection alarm using a statistical band**  
A PromQL alarm can detect anomalies without a separate anomaly detector. Instead of the `ANOMALY_DETECTION_BAND` metric-math function that standard metric alarms use, you build the expected range directly in the query with functions such as `quantile_over_time` and `stddev_over_time`. The following query alerts when the request count for the checkout-api service moves more than three standard deviations from its one-hour median in either direction. The `clamp_min` function keeps the lower bound from going negative.  

```
aws cloudwatch put-metric-alarm \
  --alarm-name RequestCountAnomaly \
  --evaluation-criteria '{"PromQLCriteria":{"Query":"1 * {\"http.server.request.count\", \"@resource.service.name\"=\"checkout-api\"} > quantile_over_time(0.5, {\"http.server.request.count\", \"@resource.service.name\"=\"checkout-api\"}[60m] offset 1m) + 3 * stddev_over_time({\"http.server.request.count\", \"@resource.service.name\"=\"checkout-api\"}[60m] offset 1m) or 1 * {\"http.server.request.count\", \"@resource.service.name\"=\"checkout-api\"} < clamp_min(quantile_over_time(0.5, {\"http.server.request.count\", \"@resource.service.name\"=\"checkout-api\"}[60m] offset 1m) - 3 * stddev_over_time({\"http.server.request.count\", \"@resource.service.name\"=\"checkout-api\"}[60m] offset 1m), 0)"}}' \
  --evaluation-interval 60
```

**Example: PromQL alarm that triggers an Application Auto Scaling step scaling policy**  
You can attach a PromQL alarm to an Application Auto Scaling step scaling policy. First, create the step scaling policy with the `put-scaling-policy` command. The command returns a policy ARN.  

```
aws application-autoscaling put-scaling-policy \
  --service-namespace ecs \
  --scalable-dimension ecs:service:DesiredCount \
  --resource-id service/my-cluster/my-service \
  --policy-name promql-5xx-scale-out \
  --policy-type StepScaling \
  --step-scaling-policy-configuration '{"AdjustmentType":"ChangeInCapacity","StepAdjustments":[{"MetricIntervalLowerBound":0,"ScalingAdjustment":1}],"Cooldown":60}'
```
Then create the PromQL alarm, setting `--alarm-actions` to the policy ARN from the previous output. This alarm scales out the service when the 5xx error rate for the checkout-api service exceeds 5 percent. When a PromQL alarm triggers an Auto Scaling action, the query must return a single time series and include a comparison. Wrap the expression in an aggregation function such as `avg`, `sum`, `max`, or `min`, followed by the comparison, as shown in the following command.  

```
aws cloudwatch put-metric-alarm \
  --alarm-name checkout-5xx-scale-out \
  --evaluation-criteria '{"PromQLCriteria":{"Query":"avg(sum(rate({\"http.server.request.count\", \"@resource.service.name\"=\"checkout-api\", \"http.response.status_code\"=~\"5..\"}[5m])) / sum(rate({\"http.server.request.count\", \"@resource.service.name\"=\"checkout-api\"}[5m])) * 100) > 5","PendingPeriod":60,"RecoveryPeriod":300}}' \
  --evaluation-interval 60 \
  --alarm-actions arn:aws:autoscaling:us-east-1:123456789012:scalingPolicy:abcd1234-5678-90ab-cdef-example11111:resource/ecs/service/my-cluster/my-service:policyName/promql-5xx-scale-out
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