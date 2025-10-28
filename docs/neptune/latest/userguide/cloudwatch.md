# Monitoring Neptune Using Amazon CloudWatch

Amazon Neptune and Amazon CloudWatch are integrated so that you can gather and analyze performance
metrics. You can monitor these metrics using the CloudWatch console, the AWS Command Line Interface (AWS CLI), or the
CloudWatch API.

CloudWatch also lets you set alarms so that you can be notified if a metric value breaches a
threshold that you specify. You can even set up CloudWatch Events to take corrective action if a breach
occurs. For more information about using CloudWatch and alarms, see the [CloudWatch Documentation](https://aws.amazon.com/documentation/cloudwatch "https://aws.amazon.com/documentation/cloudwatch").

###### Topics

- [Viewing CloudWatch Data (Console)](#Console_Neptune "#Console_Neptune")
- [Viewing CloudWatch Data (AWS CLI)](#CloudwatchCLI_Neptune "#CloudwatchCLI_Neptune")
- [Viewing CloudWatch Data (API)](#CloudwatchAPI_Neptune "#CloudwatchAPI_Neptune")
- [Using CloudWatch to monitor DB instance
  performance in Neptune](cloudwatch-monitoring-instances.md "cloudwatch-monitoring-instances.md")
- [Neptune CloudWatch Metrics](cw-metrics.md "cw-metrics.md")
- [Neptune CloudWatch Dimensions](cw-dimensions.md "cw-dimensions.md")

## Viewing CloudWatch Data (Console)

###### To view CloudWatch data for a Neptune cluster (console)

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. In the **All Metrics** pane, choose **Neptune**, and
   then choose **DBClusterIdentifier**.
4. In the upper pane, scroll down to view the full list of metrics for your cluster. The
   available Neptune metric options appear in the **Viewing** list.

To select or deselect an individual metric, in the results pane, select the check box
next to the resource name and metric. Graphs showing the metrics for the selected items
appear at the bottom of the console. To learn more about CloudWatch graphs, see [Graph Metrics](../../../AmazonCloudWatch/latest/DeveloperGuide/graph_metrics.md "../../../AmazonCloudWatch/latest/DeveloperGuide/graph_metrics.md") in the
_Amazon CloudWatch User Guide_.

## Viewing CloudWatch Data (AWS CLI)

###### To view CloudWatch data for a Neptune cluster (AWS CLI)

1. Install the AWS CLI. For instructions, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").
2. Use the AWS CLI to fetch information. The relevant CloudWatch parameters for Neptune are
   listed in [Neptune CloudWatch Metrics](cw-metrics.md "cw-metrics.md").

The following example retrieves CloudWatch metrics for the number of Gremlin
requests per second for the `gremlin-cluster` cluster.

```
<![CDATA[
aws cloudwatch get-metric-statistics \
    --namespace AWS/Neptune  --metric-name GremlinRequestsPerSec \
    --dimensions Name=DBClusterIdentifier,Value=gremlin-cluster \
    --start-time 2018-03-03T00:00:00Z --end-time 2018-03-04T00:00:00Z \
    --period 60 --statistics=Average
]]>
```

## Viewing CloudWatch Data (API)

CloudWatch also supports a `Query` action so that you can request information
programmatically. For more information, see the [CloudWatch Query API documentation](../../../AmazonCloudWatch/latest/DeveloperGuide/Using_Query_API.md "../../../AmazonCloudWatch/latest/DeveloperGuide/Using_Query_API.md") and [Amazon CloudWatch API Reference](../../../AmazonCloudWatch/latest/APIReference.md "../../../AmazonCloudWatch/latest/APIReference.md").

When a CloudWatch action requires a parameter that is specific to Neptune monitoring,
such as `MetricName`, use the values listed in [Neptune CloudWatch Metrics](cw-metrics.md "cw-metrics.md").

The following example shows a low-level CloudWatch request, using the following
parameters:

- `Statistics.member.1` = `Average`
- `Dimensions.member.1` = `DBClusterIdentifier=gremlin-cluster`
- `Namespace` = `AWS/Neptune`
- `StartTime` = `2013-11-14T00:00:00Z`
- `EndTime` = `2013-11-16T00:00:00Z`
- `Period` = `60`
- `MetricName` = `GremlinRequestsPerSec`

Here is what the CloudWatch request looks like. However, this is just to show the form of
the request; you must construct your own request based on your metrics and timeframe.

```

https://monitoring.amazonaws.com/
      ?SignatureVersion=2
      &Action=GremlinRequestsPerSec
      &Version=2010-08-01
      &StartTime=2018-03-03T00:00:00
      &EndTime=2018-03-04T00:00:00
      &Period=60
      &Statistics.member.1=Average
      &Dimensions.member.1=DBClusterIdentifier=gremlin-cluster
      &Namespace=AWS/Neptune
      &MetricName=GremlinRequests
      &Timestamp=2018-03-04T17%3A48%3A21.746Z
      &AWSAccessKeyId=`AWS Access Key ID`;
      &Signature=`signature`
```
