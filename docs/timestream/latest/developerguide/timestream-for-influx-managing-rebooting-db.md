For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Rebooting a DB instance

You can reboot a DB instance using the AWS Management Console, the AWS Command Line Interface, or the Timestream API. You must provide the ID of the DB instance:

###### Using the AWS Management Console

1. Sign in to the AWS Management Console and open the [Amazon Timestream for InfluxDB console](https://console.aws.amazon.com/timestream/ "https://console.aws.amazon.com/timestream/").
2. In the navigation pane, choose **InfluxDB Databases**, and then choose the DB instance that you want to reboot.
3. Choose **Restart database**.
4. Choose **Confirm and Restart**.
   **Using the AWS Command Line Interface**

To reboot a DB instance by using the AWS CLI, call the `reboot-db-instance` command with the following options:

###### Example Commands

For Linux, macOS, or Unix:

```
aws timestream-influxdb reboot-db-instance \
    --region YOUR_REGION \
    --identifier YOUR_INSTANCE_ID
```

For Windows:

```
aws timestream-influxdb reboot-db-instance ^
    --region YOUR_REGION ^
    --identifier YOUR_INSTANCE_ID
```
