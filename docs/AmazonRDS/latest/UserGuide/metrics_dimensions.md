# Viewing DB instance metrics in the CloudWatch console and AWS CLI

Following, you can find details about how to view metrics for your DB instance using CloudWatch. For information on
monitoring metrics for your DB instance's operating system in real time using CloudWatch Logs, see [Monitoring OS metrics with Enhanced Monitoring](USER_Monitoring.md "USER_Monitoring.md").

When you use Amazon RDS resources,
Amazon RDS sends metrics and
dimensions to Amazon CloudWatch every minute.

You can now export Performance Insights metrics dashboards from Amazon RDS
to Amazon CloudWatch and view these metrics in the CloudWatch console. For more information on how to export the
Performance Insights metrics dashboards to CloudWatch, see [Exporting Performance Insights metrics to CloudWatch](PI_metrics_export_CW.md "PI_metrics_export_CW.md").

Use the following procedures to view the metrics for Amazon RDS in the CloudWatch console and
CLI.

###### To view metrics using the Amazon CloudWatch console

Metrics are grouped first by the service namespace, and then by the various dimension
combinations within each namespace.

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").

The CloudWatch overview home page appears.

![CloudWatch overview page](images/monitoring-overviewpage-console2.png) 2. If necessary, change the AWS Region. From the navigation bar, choose
the AWS Region where your AWS resources are. For more information, see
[Regions
and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md"). 3. In the navigation pane, choose **Metrics** and then **All
metrics**.

![Choose metric namespace](images/cw-all-metrics.png) 4. Scroll down and choose the **RDS** metric
namespace.

The page displays the Amazon RDS dimensions. For descriptions of these dimensions, see [Amazon CloudWatch dimensions for Amazon RDS](dimensions.md "dimensions.md").

![Choose metric namespace](images/rds-monitoring-01.png) 5. Choose a metric dimension, for example **By Database
Class**.

![Filter metrics](images/metrics-by-instance-class.png) 6. Do any of the following actions:

    * To sort the metrics, use the column heading.
    * To graph a metric, select the check box next to the metric.
    * To filter by resource, choose the resource ID, and then choose **Add to
     search**.
    * To filter by metric, choose the metric name, and then choose **Add to
     search**.

The following example filters on the **db.t3.medium** class and graphs the
**CPUUtilization** metric.

![Filter metrics](images/rds-monitoring-03.png)
To obtain metric information by using the AWS CLI, use the CloudWatch command [`list-metrics`](../../../cli/latest/reference/cloudwatch/list-metrics.md "../../../cli/latest/reference/cloudwatch/list-metrics.md"). In the following
example, you list all metrics in the `AWS/RDS` namespace.

```
aws cloudwatch list-metrics --namespace AWS/RDS
```

To obtain metric data, use the command [`get-metric-data`](../../../cli/latest/reference/cloudwatch/get-metric-data.md "../../../cli/latest/reference/cloudwatch/get-metric-data.md").

The following example gets `CPUUtilization` statistics for instance `my-instance`
over the specific 24-hour period, with a 5-minute granularity.

Create a JSON file `CPU_metric.json` with the following contents.

```
{
   "StartTime" : `"2023-12-25T00:00:00Z"`,
   "EndTime" : `"2023-12-26T00:00:00Z"`,
   "MetricDataQueries" : [{
     "Id" : "cpu",
     "MetricStat" : {
	   "Metric" : {
  	     "Namespace" : "AWS/RDS",
  	     "MetricName" : "CPUUtilization",
  	     "Dimensions" : [{ "Name" : "DBInstanceIdentifier" , "Value" : `my-instance`}]
	   },
       "Period" : 360,
       "Stat" : "Minimum"
     }
   }]
}
```

###### Example

For Linux, macOS, or Unix:

```
aws cloudwatch get-metric-data \
    --cli-input-json file://CPU_metric.json

```

For Windows:

```
aws cloudwatch get-metric-data ^
     --cli-input-json file://CPU_metric.json

```

Sample output appears as follows:

```
{
    "MetricDataResults": [
        {
            "Id": "cpu",
            "Label": "CPUUtilization",
            "Timestamps": [
                "2023-12-15T23:48:00+00:00",
                "2023-12-15T23:42:00+00:00",
                "2023-12-15T23:30:00+00:00",
                "2023-12-15T23:24:00+00:00",
                ...
            ],
            "Values": [
                13.299778337027714,
                13.677507543049558,
                14.24976250395827,
                13.02521708695145,
                ...
            ],
            "StatusCode": "Complete"
        }
    ],
    "Messages": []
}
```

For more information, see [Getting statistics for a metric](../../../AmazonCloudWatch/latest/monitoring/getting-metric-data.md "../../../AmazonCloudWatch/latest/monitoring/getting-metric-data.md") in the _Amazon CloudWatch User Guide_.
