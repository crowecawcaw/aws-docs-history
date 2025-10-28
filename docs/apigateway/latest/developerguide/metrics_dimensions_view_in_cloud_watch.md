# View API Gateway metrics in the

CloudWatch console

Metrics are grouped first by the service namespace, and then by the various dimension combinations within each
namespace. To view the metrics at the method-level for your API, turn on detailed metrics. For more information,
see [Modify stage settings](set-up-stages.md#how-to-stage-settings "set-up-stages.md#how-to-stage-settings").

###### To view API Gateway metrics using the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. If necessary, change the AWS Region. From the navigation bar, select the
   Region where your AWS resources reside.
3. In the navigation pane, choose **Metrics**.
4. In the **All metrics** tab, choose **API
   Gateway**.
5. To view metrics by stage, choose the **By Stage** panel.
   Then, select your APIs and metric names.
6. To view metrics by specific API, choose the **By Api
   Name** panel. Then, select your APIs and metric names.

###### To view metrics using the AWS CLI

1. Use the following
   [list-metrics](../../../cli/latest/reference/cloudwatch/list-metrics.md "../../../cli/latest/reference/cloudwatch/list-metrics.md") command to list metrics:

```
aws cloudwatch list-metrics --namespace "AWS/ApiGateway"
```

After you create a metric, allow up to 15 minutes for the metric to appear. To see metric statistics
sooner, use [get-metric-data](../../../cli/latest/reference/cloudwatch/update-domain-name.md "../../../cli/latest/reference/cloudwatch/update-domain-name.md") or [get-metric-statistics](../../../cli/latest/reference/cloudwatch/update-domain-name.md "../../../cli/latest/reference/cloudwatch/update-domain-name.md"). 2. Use the following [get-metrics-statistics](../../../cli/latest/reference/cloudwatch/get-metric-statistics.md "../../../cli/latest/reference/cloudwatch/get-metric-statistics.md") command to view the average over a period of time using 5 minute
intervals:

```
aws cloudwatch get-metric-statistics --namespace AWS/ApiGateway --metric-name Count --start-time 2011-10-03T23:00:00Z --end-time 2017-10-05T23:00:00Z --period 300 --statistics Average
```
