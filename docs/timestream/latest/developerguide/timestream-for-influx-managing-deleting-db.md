For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Deleting a DB instance

Deleting a DB instance has an effect on instance recoverability, and snapshot availability. Consider the following issues:

- If you want to delete all Timestream for InfluxDB resources, note that the DB instances resources incur billing charges.
- When the status for a DB instance is deleting, its CA certificate value doesn't appear in the Timestream for InfluxDB console or in output for
  AWS Command Line Interface commands or Timestream API operations.
- The time required to delete a DB instance varies depending on how much data is deleted, and whether a final snapshot is taken.
  You can delete a DB instance using the AWS Management Console, the AWS Command Line Interface, or the Timestream API. You must provide the name of the DB instance:

###### Using the AWS Management Console

1. Sign in to the AWS Management Console and open the [Amazon Timestream for InfluxDB console](https://console.aws.amazon.com/timestream/ "https://console.aws.amazon.com/timestream/").
2. In the navigation pane, choose **InfluxDB Databases**, and then choose the DB instance that you want to delete.
3. Choose **Delete**.
4. Enter _confirm_ in the box.
5. Choose **Delete**.
   **Using the AWS Command Line Interface**

To find the instance IDs of the DB instances in your account, call the `list-db-instances` command:

```
aws timestream-influxdb list-db-instances \
--endpoint-url YOUR_ENDPOINT \
--region YOUR_REGION
```

To delete a DB instance by using the AWS CLI, call the `delete-db-instance` command with the following options:

```
aws timestream-influxdb list-db-instances \
--identifier YOUR_DB_INSTANCE \

```

###### Example

For Linux, macOS, or Unix:

```
aws timestream-influxdb delete-db-instance \
    --identifier mydbinstance
```

For Windows:

```
aws timestream-influxdb delete-db-instance ^
    --identifier mydbinstance
```
