# Evaluate your provisioned capacity for

right-sized provisioning

This section provides an overview of how to evaluate if you have right-sized provisioning on
your Amazon Keyspaces tables. As your workload evolves, you should modify your operational procedures
appropriately, especially when your Amazon Keyspaces table is configured in provisioned mode and you
have the risk to over-provision or under-provision your tables.

The procedures described in this section require statistical information that should be captured from
the Amazon Keyspaces tables that are supporting your production application. To understand your application
behavior, you should define a period of time that is significant enough to capture the data
seasonality of your application. For example, if your application shows weekly patterns, using
a three week period should give you enough room for analysing application throughput
needs.

If you don’t know where to start, use at least one month’s worth of data usage for the
calculations below.

While evaluating capacity, for Amazon Keyspaces tables you can configure **Read Capacity
Units (RCUs)** and **Write Capacity Units (WCU)**
independently.

###### Topics

- [How to retrieve
  consumption metrics from your Amazon Keyspaces tables](#CostOptimization_RightSizedProvisioning_ConsumptionMetrics "#CostOptimization_RightSizedProvisioning_ConsumptionMetrics")
- [How to
  identify under-provisioned Amazon Keyspaces tables](#CostOptimization_RightSizedProvisioning_UnderProvisionedTables "#CostOptimization_RightSizedProvisioning_UnderProvisionedTables")
- [How to
  identify over-provisioned Amazon Keyspaces tables](#CostOptimization_RightSizedProvisioning_OverProvisionedTables "#CostOptimization_RightSizedProvisioning_OverProvisionedTables")

## How to retrieve

consumption metrics from your Amazon Keyspaces tables

To evaluate the table capacity, monitor the following CloudWatch metrics and select the
appropriate dimension to retrieve table information:

| Read Capacity Units            | Write Capacity Units            |
| ------------------------------ | ------------------------------- |
| `ConsumedReadCapacityUnits`    | `ConsumedWriteCapacityUnits`    |
| `ProvisionedReadCapacityUnits` | `ProvisionedWriteCapacityUnits` |
| `ReadThrottleEvents`           | `WriteThrottleEvents`           |

You can do this either through the AWS CLI or the AWS Management Console.

AWS CLI
Before you retrieve the table consumption metrics, you need to start by capturing
some historical data points using the CloudWatch API.

Start by creating two files: `write-calc.json` and
`read-calc.json`. These files represent the calculations for the table.
You need to update some of the fields, as indicated in the table below, to
match your environment.

###### Note

If the table name is not unique within your account,
you must also specify the name of the keyspace.

| Field Name     | Definition                                                                                    | Example                                      |
| -------------- | --------------------------------------------------------------------------------------------- | -------------------------------------------- |
| `<table-name>` | The name of the table that you are analysing                                                  | SampleTable                                  |
| `<period>`     | The period of time that you are using to evaluate the utilization<br>target, based in seconds | For a 1-hour period you should specify: 3600 |
| `<start-time>` | The beginning of your evaluation interval, specified in ISO8601<br>format                     | 2022-02-21T23:00:00                          |
| `<end-time>`   | The end of your evaluation interval, specified in ISO8601 format                              | 2022-02-22T06:00:00                          |

The write calculations file retrieves the number of WCU provisioned and consumed
in the time period for the date range specified. It also generates a utilization
percentage that can be used for analysis. The full content of the
`write-calc.json` file should look like in the following example.

```
{
  "MetricDataQueries": [
    {
      "Id": "provisionedWCU",
      "MetricStat": {
        "Metric": {
          "Namespace": "AWS/Cassandra",
          "MetricName": "ProvisionedWriteCapacityUnits",
          "Dimensions": [
            {
              "Name": "TableName",
              "Value": "<table-name>"
            }
          ]
        },
        "Period": <period>,
        "Stat": "Average"
      },
      "Label": "Provisioned",
      "ReturnData": false
    },
    {
      "Id": "consumedWCU",
      "MetricStat": {
        "Metric": {
          "Namespace": "AWS/Cassandra",
          "MetricName": "ConsumedWriteCapacityUnits",
          "Dimensions": [
            {
              "Name": "TableName",
              "Value": "<table-name>""
            }
          ]
        },
        "Period": <period>,
        "Stat": "Sum"
      },
      "Label": "",
      "ReturnData": false
    },
    {
      "Id": "m1",
      "Expression": "consumedWCU/PERIOD(consumedWCU)",
      "Label": "Consumed WCUs",
      "ReturnData": false
    },
    {
      "Id": "utilizationPercentage",
      "Expression": "100*(m1/provisionedWCU)",
      "Label": "Utilization Percentage",
      "ReturnData": true
    }
  ],
  "StartTime": "<start-time>",
  "EndTime": "<end-time>",
  "ScanBy": "TimestampDescending",
  "MaxDatapoints": 24
}
```

The read calculations file uses a similar metrics. This file retrieves how many RCUs
were provisioned and consumed during the time period for the date range specified. The
contents of the `read-calc.json` file should look like in this
example.

```
{
  "MetricDataQueries": [
    {
      "Id": "provisionedRCU",
      "MetricStat": {
        "Metric": {
          "Namespace": "AWS/Cassandra",
          "MetricName": "ProvisionedReadCapacityUnits",
          "Dimensions": [
            {
              "Name": "TableName",
              "Value": "<table-name>"
            }
          ]
        },
        "Period": <period>,
        "Stat": "Average"
      },
      "Label": "Provisioned",
      "ReturnData": false
    },
    {
      "Id": "consumedRCU",
      "MetricStat": {
        "Metric": {
          "Namespace": "AWS/Cassandra",
          "MetricName": "ConsumedReadCapacityUnits",
          "Dimensions": [
            {
              "Name": "TableName",
              "Value": "<table-name>"
            }
          ]
        },
        "Period": <period>,
        "Stat": "Sum"
      },
      "Label": "",
      "ReturnData": false
    },
    {
      "Id": "m1",
      "Expression": "consumedRCU/PERIOD(consumedRCU)",
      "Label": "Consumed RCUs",
      "ReturnData": false
    },
    {
      "Id": "utilizationPercentage",
      "Expression": "100*(m1/provisionedRCU)",
      "Label": "Utilization Percentage",
      "ReturnData": true
    }
  ],
  "StartTime": "<start-time>",
  "EndTime": "<end-time>",
  "ScanBy": "TimestampDescending",
  "MaxDatapoints": 24
}
```

Once you've created the files, you can start retrieving utilization data.

1. To retrieve the write utilization data, issue the following command:

```
aws cloudwatch get-metric-data --cli-input-json file://write-calc.json
```

2. To retrieve the read utilization data, issue the following command:

```
aws cloudwatch get-metric-data --cli-input-json file://read-calc.json
```

The result for both queries is a series of data points in JSON format that can be
used for analysis. Your results depend on the number of data points you specified, the
period, and your own specific workload data. It could look like in the following
example.

```
{
    "MetricDataResults": [
        {
            "Id": "utilizationPercentage",
            "Label": "Utilization Percentage",
            "Timestamps": [
                "2022-02-22T05:00:00+00:00",
                "2022-02-22T04:00:00+00:00",
                "2022-02-22T03:00:00+00:00",
                "2022-02-22T02:00:00+00:00",
                "2022-02-22T01:00:00+00:00",
                "2022-02-22T00:00:00+00:00",
                "2022-02-21T23:00:00+00:00"
            ],
            "Values": [
                91.55364583333333,
                55.066631944444445,
                2.6114930555555556,
                24.9496875,
                40.94725694444445,
                25.61819444444444,
                0.0
            ],
            "StatusCode": "Complete"
        }
    ],
    "Messages": []
}
```

###### Note

If you specify a short period and a long time range, you might need to modify the
`MaxDatapoints` value, which is by default set to 24 in the script. This
represents one data point per hour and 24 per day.

AWS Management Console

1. Log into the AWS Management Console and navigate to the CloudWatch service page at [Getting Started with the AWS Management Console](../../../awsconsolehelpdocs/latest/gsg/getting-started.md "../../../awsconsolehelpdocs/latest/gsg/getting-started.md").
   Select the appropriate AWS Region if necessary.
2. Locate the Metrics section on the left navigation bar and choose **All metrics**.
3. This opens a dashboard with two panels. The top panel shows you the
   graphic, and the bottom panel has the metrics that you want to graph. Choose the
   Amazon Keyspaces panel.
4. Choose the **Table Metrics** category from the sub
   panels. This shows you the tables in your current AWS Region.
5. Identify your table name by scrolling down the menu and selecting the write
   operation metrics: `ConsumedWriteCapacityUnits` and
   `ProvisionedWriteCapacityUnits`

###### Note

This example talks about write operation metrics, but you can also use these
steps to graph the read operation metrics. 6. Select the **Graphed metrics (2)** tab to modify
the formulas. By default CloudWatch chooses the statistical function **Average** for the graphs. 7. While having both graphed metrics selected (the checkbox on the left) select the
menu **Add math**, followed by **Common**, and then select the **Percentage** function. Repeat the procedure twice.

First time selecting the **Percentage**
function.

Second time selecting the **Percentage**
function. 8. At this point you should have four metrics in the bottom menu. Let’s work on the
`ConsumedWriteCapacityUnits` calculation. To be consistent, you need to
match the names with the ones you used in the AWS CLI section. Click on the
**m1 ID** and change this value to **consumedWCU**. 9. Change the statistic from **Average** to **Sum**.
This action automatically creates another metric
called **ANOMALY_DETECTION_BAND**. For the scope of
this procedure, you can ignore this by removing the checkbox on the newly generated
**ad1 metric**. 10. Repeat step 8 to rename the **m2 ID** to
**provisionedWCU**. Leave the statistic set to **Average**. 11. Choose the **Expression1** label and update the
value to **m1** and the label to **Consumed WCUs**.

###### Note

Make sure you have only selected **m1** (checkbox
on the left) and **provisionedWCU** to properly
visualize the data. Update the formula by clicking in **Details** and changing the formula to **consumedWCU/PERIOD(consumedWCU)**. This step might also generate
another **ANOMALY_DETECTION_BAND** metric, but for
the scope of this procedure you can ignore it. 12. You should now have two graphics: one that indicates your provisioned WCUs
on the table and another that indicates the consumed WCUs. 13. Update the percentage formula by selecting the Expression2 graphic
(**e2**). Rename the labels and IDs to **utilizationPercentage**. Rename the formula to match **100\*(m1/provisionedWCU)**. 14. Remove the checkbox from all the metrics except **utilizationPercentage** to visualize your utilization patterns. The
default interval is set to 1 minute, but feel free to modify it as needed.

The results you get depend on the actual data from your workload. Intervals with
more than 100% utilization are prone to low throughput capacity error events. Amazon Keyspaces
offers [burst capacity](throughput-bursting.md "throughput-bursting.md"), but as soon as the
burst capacity is exhausted, anything above 100% experiences low throughput capacity
error events.

## How to

identify under-provisioned Amazon Keyspaces tables

For most workloads, a table is considered under-provisioned when it constantly consumes
more than 80% of its provisioned capacity.

[Burst capacity](throughput-bursting.md "throughput-bursting.md") is an Amazon Keyspaces feature that allow
customers to temporarily consume more RCUs/WCUs than originally provisioned (more than the
per-second provisioned throughput that was defined for the table). The burst capacity was
created to absorb sudden increases in traffic due to special events or usage spikes. This
burst capacity limited, for more information, see [Use burst
capacity effectively in Amazon Keyspaces](throughput-bursting.md "throughput-bursting.md"). As
soon as the unused RCUs and WCUs are depleted, you can experience low capacity throughput
error events if you try to consume more capacity than provisioned. When your application
traffic is getting close to the 80% utilization rate, your risk of experiencing low capacity
throughput error events is significantly higher.

The 80% utilization rate rule varies from the seasonality of your data and your traffic
growth. Consider the following scenarios:

- If your traffic has been **stable** at ~90% utilization
  rate for the last 12 months, your table has just the right capacity
- If your application traffic is **growing** at a rate of
  8% monthly in less than 3 months, you will arrive at 100%
- If your application traffic is **growing** at a rate of
  5% in a little more than 4 months, you will still arrive at 100%

The results from the queries above provide a picture of your utilization rate. Use them as
a guide to further evaluate other metrics that can help you choose to increase your table
capacity as required (for example: a monthly or weekly growth rate). Work with your operations
team to define what is a good percentage for your workload and your tables.

There are special scenarios where the data is skewed when you analyse it on a daily or
weekly basis. For example, with seasonal applications that have spikes in usage during working
hours (but then drop to almost zero outside of working hours), you could benefit from [scheduling application auto-scaling](../../../autoscaling/application/userguide/examples-scheduled-actions.md "../../../autoscaling/application/userguide/examples-scheduled-actions.md"), where you specify the hours of the day (and the days of
the week) to increase the provisioned capacity, as well as when to reduce it. Instead of
aiming for higher capacity so you can cover the busy hours, you can also benefit from [Amazon Keyspaces table auto-scaling](autoscaling.md "autoscaling.md") configurations if your seasonality is
less pronounced.

## How to

identify over-provisioned Amazon Keyspaces tables

The query results obtained from the scripts above provide the data points required to
perform some initial analysis. If your data set presents values lower than 20% utilization for
several intervals, your table might be over-provisioned. To further define if you need to
reduce the number of WCUs and RCUS, you should revisit the other readings in the
intervals.

When your table contains several low usage intervals, you can benefit from using
Application Auto Scaling policies, either by scheduling Application Auto Scaling or by just configuring the default
Application Auto Scaling policies for the table that are based on utilization.

If you have a workload with a low utilization to high throttle ratio (**Max(ThrottleEvents)/Min(ThrottleEvents)** in the interval), this could
happen when you have a very spiky workload where traffic increases significantly on specific
days (or times of day), but is otherwise consistently low. In these scenarios, it might be
beneficial to use [scheduled
Application Auto Scaling](../../../autoscaling/application/userguide/examples-scheduled-actions.md "../../../autoscaling/application/userguide/examples-scheduled-actions.md").
