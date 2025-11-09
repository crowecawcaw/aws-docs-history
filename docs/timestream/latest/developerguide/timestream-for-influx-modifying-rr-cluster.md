For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Modifying a read replica cluster

for Amazon Timestream for InfluxDB

A read replica cluster has a writer DB instance and a reader DB instance
in separate Availability Zones. Read replica clusters provide high availability,
increased capacity for read workloads, and faster failover when compared to Multi-AZ
deployments. For more information about read replica clusters, see [Overview of Amazon Timestream for InfluxDB read replica clusters](timestream-for-influx-read-replica-overview.md "timestream-for-influx-read-replica-overview.md").

You can modify a read replica cluster to change its settings.

###### Important

You can't modify the DB instances within a read replica cluster. All modifications must be done at the DB cluster level.

You can modify a read replica cluster using the AWS Management Console, the AWS CLI, or the Amazon Timestream for InfluxDB API.

## Modify a read replica cluster

for Amazon Timestream for InfluxDB

Using the AWS Management Console
To modify a read replica DB cluster using the console:

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/timestream "https://console.aws.amazon.com/timestream") and open the Amazon Timestream console.
2. In the navigation pane, choose **InfluxDB
   databases** and then choose the read replica
   cluster you want to modify.
3. Choose **Modify**. The **Modify DB
   cluster** page appears.
4. Choose any of the settings that you want. For information
   about each setting, see [Settings for
   modifying read replica clusters](#timestream-for-influx-rr-modify-settings "#timestream-for-influx-rr-modify-settings").
5. After you have made your changes, choose
   **Continue** and check the summary of
   modifications.
6. On the confirmation page, review your changes. If they're
   correct, choose **Modify DB cluster** to save
   your changes. Alternatively, choose **Back**
   to edit your changes or **Cancel** to cancel
   your changes.

###### Important

Currently Amazon Timestream for InfluxDB only supports **Apply
Immediately** updates for the read replica cluster. If
you confirm the changes, your DB cluster will incur downtime while the changes are being applied.

Using the AWS CLI
To modify a DB instance using the AWS Command Line Interface, use the
`update-db-cluster` command with the following parameters.
Replace each `user input placeholder` with your own information.

```
aws timestream-influxdb update-db-cluster \
      --region `region` \
      --db-cluster-id `db-cluster-id` \
      --db-instance-type db.influx.4xlarge \
      --port 10000 \
      --failover mode NO_FAILOVER

```

## Settings for

modifying read replica clusters

For details about settings that you can use to modify a read replica cluster, see
the following table. For more information about
the AWS CLI options, see [update-db-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-influxdb/update-db-cluster.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-influxdb/update-db-cluster.html").

| Console setting            | Setting description                                                                                                                                                                                                                                                                                                                                                                                                                                                 | CLI option and Timestream for InfluxDB API parameter                                                         |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Database port              | The port number on which InfluxDB accepts connections.<br>Valid Values: 1024-65535<br>Default: 8086<br>Constraints: The value can't be 2375-2376,<br>7788-7799, 8090, or 51678-51680.                                                                                                                                                                                                                                                                               | **CLI option:**<br>`--port`<br>\*_API parameter:_<br>• `port`                                                |
| DB instance type           | The compute and memory capacity of each DB instance<br>in your Timestream for InfluxDB DB cluster, for example `db.influx.xlarge`.<br>If possible, choose a DB instance class large enough<br>that a typical query working set can be held in memory. When working sets are held in memory, the system can avoid writing to disk, which improves performance.                                                                                                       | **CLI option:**<br>`--db-instance-type`<br>\*_API parameter:_<br>• `dbInstanceType`                          |
| DB cluster parameter group | The ID of the DB parameter group to assign to your DB cluster. DB parameter groups specify how the database is configured. For example, DB parameter groups can specify the limit for query concurrency.                                                                                                                                                                                                                                                            | **CLI option:**<br>`--db-parameter-group-identifier`<br>\*_API parameter:_<br>• `dbParameterGroupIdentifier` |
| Log exports                | Configuration for sending InfluxDB engine logs to a<br>specified S3 bucket.<br>Configuration for S3 bucket log delivery: `s3Configuration -> (structure)`<br>The name of the S3 bucket to deliver logs to: `bucketName -> (string)`<br>Indicate whether log delivery to the S3 bucket is<br>enabled: `enabled -> (boolean)`<br>Shorthand syntax: `s3Configuration={bucketName=string,<br>enabled=boolean}`                                                          | **CLI option:**<br>`--log-delivery-configuration`<br>\*_API parameter:_<br>• `logDeliveryConfiguration`      |
| Failover mode              | Configure how your cluster responds to a primary<br>instance failure using the following options:<br>`AUTOMATIC`: If the primary instance fails, the<br>system automatically promotes a read replica to become the new<br>primary instance.<br>`NO_FAILOVER`: If the primary instance fails, the<br>system attempts to restore the primary instance without<br>promoting a read replica. The cluster remains unavailable until<br>the primary instance is restored. | **CLI option:**<br>`--failover-mode`<br>\*_API parameter:_<br>• `failoverMode`                               |
