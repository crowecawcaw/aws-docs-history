

# Viewing DB cluster metrics in the CloudWatch console and AWS CLI
<a name="metrics_dimensions"></a>

Following, you can find details about how to view metrics for your DB instance using CloudWatch. For information on monitoring metrics for your DB instance's operating system in real time using CloudWatch Logs, see [Monitoring OS metrics with Enhanced Monitoring](USER_Monitoring.OS.md).

When you use Amazon Aurora resources, Amazon Aurora sends metrics and dimensions to Amazon CloudWatch every minute.

For information about monitoring database load in CloudWatch, see [Monitoring Amazon Aurora databases with CloudWatch Database Insights](USER_DatabaseInsights.md).

Use the following procedures to view the metrics for Amazon Aurora in the CloudWatch console and CLI.

## Console
<a name="metrics_dimensions.console"></a>

**To view metrics using the Amazon CloudWatch console**

Metrics are grouped first by the service namespace, and then by the various dimension combinations within each namespace.

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

   The CloudWatch overview home page appears.  
![CloudWatch overview page.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/monitoring-overviewpage-console2.png)

1. If necessary, change the AWS Region. From the navigation bar, choose the AWS Region where your AWS resources are. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).

1. In the navigation pane, choose **Metrics** and then **All metrics**.  
![The metric namespace selection.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/cw-all-metrics.png)

1. Scroll down and choose the **RDS** metric namespace.

   The page displays the Amazon Aurora dimensions. For descriptions of these dimensions, see [Amazon CloudWatch dimensions for Aurora](dimensions.md).  
![The metric namespace selection.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/rds-monitoring-01.png)

1. Choose a metric dimension, for example **By Database Class**.  
![Filter metrics.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/metrics-by-instance-class.png)

1. Do any of the following actions:
   + To sort the metrics, use the column heading.
   + To graph a metric, select the check box next to the metric.
   + To filter by resource, choose the resource ID, and then choose **Add to search**.
   + To filter by metric, choose the metric name, and then choose **Add to search**.

   The following example filters on the **db.t3.medium** class and graphs the **CPUUtilization** metric.  
![Filter metrics.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/rds-monitoring-03.png)

You can find details about how to analyze resource usage for Aurora PostgreSQL using CloudWatch metrics. For more information, see [Using Amazon CloudWatch metrics to analyze resource usage for Aurora PostgreSQL](AuroraPostgreSQL_AnayzeResourceUsage.md) 

## AWS CLI
<a name="metrics_dimensions.CLI"></a>

To obtain metric information by using the AWS CLI, use the CloudWatch command [`list-metrics`](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/list-metrics.html). In the following example, you list all metrics in the `AWS/RDS` namespace.

```
aws cloudwatch list-metrics --namespace AWS/RDS
```

To obtain metric data, use the command [`get-metric-data`](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/get-metric-data.html).

The following example gets `CPUUtilization` statistics for instance `my-instance` over the specific 24-hour period, with a 5-minute granularity.

Create a JSON file `CPU_metric.json` with the following contents.

```
 1. {
 2.    "StartTime" : {{"2023-12-25T00:00:00Z"}},
 3.    "EndTime" : {{"2023-12-26T00:00:00Z"}},
 4.    "MetricDataQueries" : [{
 5.      "Id" : "cpu",	    
 6.      "MetricStat" : {
 7. 	   "Metric" : {	  
 8.   	     "Namespace" : "AWS/RDS",
 9.   	     "MetricName" : "CPUUtilization",
10.   	     "Dimensions" : [{ "Name" : "DBInstanceIdentifier" , "Value" : {{my-instance}}}]
11. 	   },  
12.        "Period" : 360,
13.        "Stat" : "Minimum" 
14.      }
15.    }]
16. }
```

**Example**  
For Linux, macOS, or Unix:  

```
1. aws cloudwatch get-metric-data \
2.     --cli-input-json file://CPU_metric.json
```
For Windows:  

```
1. aws cloudwatch get-metric-data ^
2.      --cli-input-json file://CPU_metric.json
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
For more information, see [Getting statistics for a metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/getting-metric-data.html) in the *Amazon CloudWatch User Guide*.