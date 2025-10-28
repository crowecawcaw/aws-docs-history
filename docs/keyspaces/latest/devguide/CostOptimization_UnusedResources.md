# Identify your unused resources to optimize costs in Amazon Keyspaces

This section provides an overview of how to evaluate your unused resources regularly. As
your application requirements evolve, you should ensure no resources are unused and contributing
to unnecessary Amazon Keyspaces costs. The procedures described below use Amazon CloudWatch metrics to identify
unused resources and take action to reduce costs.

You can monitor Amazon Keyspaces using CloudWatch, which collects and processes raw data from Amazon Keyspaces into
readable, near real-time metrics. These statistics are retained for a period of time, so that
you can access historical information to better understand your utilization. By default, Amazon Keyspaces
metric data is sent to CloudWatch automatically. For more information, see [What is Amazon CloudWatch?](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") and
[Metrics
retention](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#metrics-retention "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#metrics-retention") in the _Amazon CloudWatch User Guide_.

###### Topics

- [How to identify unused
  resources](#CostOptimization_UnusedResources_Identifying "#CostOptimization_UnusedResources_Identifying")
- [Identifying unused table
  resources](#CostOptimization_UnusedResources_Tables "#CostOptimization_UnusedResources_Tables")
- [Cleaning up unused table
  resources](#CostOptimization_UnusedResources_Tables_Cleanup "#CostOptimization_UnusedResources_Tables_Cleanup")
- [Cleaning up unused
  point-in-time recovery (PITR) backups](#CostOptimization_UnusedResources_Backups "#CostOptimization_UnusedResources_Backups")

## How to identify unused

resources

To identify unused tables you can take a look at the following CloudWatch metrics over a
period of 30 days to understand if there are any active reads or writes on a specific table:

###### `ConsumedReadCapacityUnits`

The number of read capacity units consumed over the specified time period, so you can
track how much consumed capacity you have used. You can retrieve the total consumed read
capacity for a table.

###### `ConsumedWriteCapacityUnits`

The number of write capacity units consumed over the specified time period, so you can
track how much consumed capacity you have used. You can retrieve the total consumed write
capacity for a table.

## Identifying unused table

resources

Amazon CloudWatch is a monitoring and observability service which provides the Amazon Keyspaces table metrics
you can use to identify unused resources. CloudWatch metrics can be viewed through the AWS Management Console
as well as through the AWS Command Line Interface.

AWS Command Line Interface
To view your tables metrics through the AWS Command Line Interface, you can use the following
commands.

1. First, evaluate your table's reads:

###### Note

If the table name is not unique within your account,
you must also specify the name of the keyspace.

```
aws cloudwatch get-metric-statistics --metric-name
ConsumedReadCapacityUnits --start-time <start-time> --end-time <end-
time> --period <period> --namespace AWS/Cassandra --statistics Sum --
dimensions Name=TableName,Value=<table-name>
```

To avoid falsely identifying a table as unused, evaluate metrics over a longer
period. Choose an appropriate start-time and end-time range, such as **30 days**, and an appropriate period, such as **86400**.

In the returned data, any **Sum** above **0** indicates that the table you are evaluating received read
traffic during that period.

The following result shows a table receiving read traffic in the evaluated
period:

```
        {
            "Timestamp": "2022-08-25T19:40:00Z",
            "Sum": 36023355.0,
            "Unit": "Count"
        },
        {
            "Timestamp": "2022-08-12T19:40:00Z",
            "Sum": 38025777.5,
            "Unit": "Count"
        },

```

The following result shows a table not receiving read traffic in the evaluated
period:

```
        {
            "Timestamp": "2022-08-01T19:50:00Z",
            "Sum": 0.0,
            "Unit": "Count"
        },
        {
            "Timestamp": "2022-08-20T19:50:00Z",
            "Sum": 0.0,
            "Unit": "Count"
        },

```

2. Next, evaluate your table’s writes:

```
aws cloudwatch get-metric-statistics --metric-name
ConsumedWriteCapacityUnits --start-time <start-time> --end-time <end-
time> --period <period> --namespace AWS/Cassandra --statistics Sum --
dimensions Name=TableName,Value=<table-name>
```

To avoid falsely identifying a table as unused, you will want to evaluate
metrics over a longer period. Choose an appropriate start-time and end-time range,
such as **30 days**, and an appropriate period, such as
**86400**.

In the returned data, any **Sum** above **0** indicates that the table you are evaluating received read
traffic during that period.

The following result shows a table receiving write traffic in the evaluated
period:

```
        {
            "Timestamp": "2022-08-19T20:15:00Z",
            "Sum": 41014457.0,
            "Unit": "Count"
        },
        {
            "Timestamp": "2022-08-18T20:15:00Z",
            "Sum": 40048531.0,
            "Unit": "Count"
        },

```

The following result shows a table not receiving write traffic in the evaluated
period:

```
        {
            "Timestamp": "2022-07-31T20:15:00Z",
            "Sum": 0.0,
            "Unit": "Count"
        },
        {
            "Timestamp": "2022-08-19T20:15:00Z",
            "Sum": 0.0,
            "Unit": "Count"
        },

```

AWS Management Console
The following steps allow you to evaluate your resource utilization through
the AWS Management Console.

1. Log into the AWS Management Console and navigate to the CloudWatch service page at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/"). Select the appropriate AWS Region in the top right of
   the console, if necessary.
2. On the left navigation bar, locate the **Metrics** section and choose
   **All metrics**.
3. The action above opens a dashboard with two panels. In the top panel, you
   can see currently graphed metrics. On the bottom you can select the metrics
   available to graph. Choose Amazon Keyspaces in the bottom panel.
4. In the Amazon Keyspaces metrics selection panel, choose the **Table
   Metrics** category to show the metrics for your tables in the current
   region.
5. Identify your table name by scrolling down the menu, then choose the metrics
   `ConsumedReadCapacityUnits` and `ConsumedWriteCapacityUnits`
   for your table.
6. Choose the **Graphed metrics (2)** tab and adjust
   the **Statistic** column to **Sum**.
7. To avoid falsely identifying a table as unused, evaluate the table metrics
   over a longer period. At the top of the graph panel, choose an appropriate time
   frame, such as 1 month, to evaluate your table. Choose **Custom**, choose **1 Months** in the
   drop-down menu, and choose **Apply**.
8. Evaluate the graphed metrics for your table to determine if it is being used.
   Metrics that have gone above **0** indicate that a
   table has been used during the evaluated time period. A flat graph at **0** for both read and write indicates that a table is
   unused.

## Cleaning up unused table

resources

If you have identified unused table resources, you can reduce their ongoing costs in the
following ways.

###### Note

If you have identified an unused table but would still like to keep it available in case
it needs to be accessed in the future, consider switching it to on-demand mode. Otherwise,
you can consider deleting the table.

###### Capacity modes

Amazon Keyspaces charges for reading, writing, and storing data in your Amazon Keyspaces tables.

Amazon Keyspaces has [two capacity modes](ReadWriteCapacityMode.md "ReadWriteCapacityMode.md"), which
come with specific billing options for processing reads and writes on your tables: on-demand
and provisioned. The read/write capacity mode controls how you are charged for read and write
throughput and how you manage capacity.

For on-demand mode tables, you don't need to specify how much read and write throughput
you expect your application to perform. Amazon Keyspaces charges you for the reads and writes that your
application performs on your tables in terms of read request units and write request units. If
there is no activity on your table, you do not pay for throughput but you still incur
a storage charge.

###### Deleting tables

If you’ve discovered an unused table and would like to delete it, consider to make a
backup or export the data first.

Backups taken through AWS Backup can leverage cold storage tiering, further reducing
cost. Refer to the [Managing backup plans](../../../aws-backup/latest/devguide/about-backup-plans.md "../../../aws-backup/latest/devguide/about-backup-plans.md")
documentation for information on how to use a lifecycle to move your backup to cold
storage.

After your table has been backed up, you may choose to delete it either through the
AWS Management Console or through the AWS Command Line Interface.

## Cleaning up unused

point-in-time recovery (PITR) backups

Amazon Keyspaces offers Point-in-time recovery, which provides continuous backups for
35 days to help you protect against accidental writes or deletes. PITR backups have costs
associated with them.

Refer to the documentation at [Backup and restore data with point-in-time recovery for Amazon Keyspaces](PointInTimeRecovery.md "PointInTimeRecovery.md") to determine if your
tables have backups enabled that may no longer be needed.
