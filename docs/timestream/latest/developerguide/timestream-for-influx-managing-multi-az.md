For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Configuring and managing a multi-AZ deployment

Timestream for InfluxDB Multi-AZ deployments can only have one standby. When the deployment has one standby DB instance, it's called a Multi-AZ DB instance deployment. A Multi-AZ DB instance deployment has one standby DB instance that provides failover support, but doesn't serve read traffic.

###### Important

Your instance must have at least two subnets associated with it to execute Single-AZ to
Multi-AZ updates. Once the instance is created, you can't modify its deployment
mode from Single-AZ to Multi-AZ .

You can use the AWS Management Console to determine whether your DB instance is a Single-AZ or Multi-AZ deployment.

###### Using the AWS Management Console

1. Sign in to the AWS Management Console and open the [Amazon Timestream for InfluxDB console](https://console.aws.amazon.com/timestream/ "https://console.aws.amazon.com/timestream/").
2. In the navigation pane, choose **InfluxDB databases**, and then choose **DB identifier**.
   A Multi-AZ DB instance deployment has the following characteristics:

- There is only one row for the DB instance.
- The value of Role is Instance or Primary.
- The value of Multi-AZ is Yes.
