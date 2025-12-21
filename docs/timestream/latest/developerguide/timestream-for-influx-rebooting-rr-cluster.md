For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Rebooting a read replica cluster

in Amazon Timestream for InfluxDB

You can reboot a read replica cluster in the event of any health issues.

## Rebooting a read replica cluster

for Amazon Timestream for InfluxDB

Using the AWS Management Console
To reboot a read replica DB cluster using the console:

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/timestream "https://console.aws.amazon.com/timestream") and open the Amazon Timestream console.
2. In the navigation pane, choose **InfluxDB
   databases** and then choose the read replica
   cluster you want to reboot.
3. Choose **Restart database**.
4. Choose **Confirm and Restart**.

Using the AWS CLI
To reboot a DB instance using the AWS Command Line Interface, use the
`reboot-db-cluster` command with the following parameters.
Replace each `user input placeholder` with your own information.

```
aws timestream-influxdb reboot-db-cluster \
      --region `region` \
      --db-cluster-id `db-cluster-id` \

```
