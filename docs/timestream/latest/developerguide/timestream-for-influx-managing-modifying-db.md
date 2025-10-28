For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Updating DB instances

You can update the following configuration parameters of your Timestream for InfluxDB instance:

- Instance class
- Storage type
- Allocated storage (increase only)
- Deployment type
- Parameter group
- Log delivery configuration

###### Important

We recommend you test all changes on a test instance before modifying the production instance to understand their impact, especially when upgrading database versions. Review the impact on your database and applications before updating settings. Some modifications require a DB instance reboot, resulting in downtime.

###### Using the AWS Management Console

1. Sign in to the AWS Management Console and open the [Amazon Timestream for InfluxDB console](https://console.aws.amazon.com/timestream/ "https://console.aws.amazon.com/timestream/").
2. In the navigation pane, choose **InfluxDB Databases**, and then choose the DB instance that you want to modify.
3. Choose **Modify**.
4. On the **Modify DB instance** page, make the desired changes.
5. Choose **Continue** and check the summary of modifications.
6. Choose **Next**.
7. Review your changes.
8. Choose **Modify instance** to apply your changes.

###### Note

These modifications require a reboot of the Influx DB instance and can cause an outage in some cases.

**Using the AWS Command Line Interface**

To update a DB instance by using the AWS Command Line Interface, call the `update-db-instance` command. Specify the DB instance
identifier and the values for the options that you want to modify. For information about each option, see [Settings for DB instances](timestream-for-influx-configuring.md#timestream-for-influx-configuring-create-db-settings "timestream-for-influx-configuring.md#timestream-for-influx-configuring-create-db-settings").

###### Example

The following code modifies `my-db-instance` by setting a
different `db-parameter-group-name`. Replace each `user input
 placeholder` with your own information. The changes are applied
immediately.

For Linux, macOS, or Unix:

```
aws timestream-influxdb update-db-instance \
    --identifier `my-db-instance` \
    --db-storage-type `desired-storage-type` \
    --allocated-storage `desired-allocated-storage` \
    --db-instance-type `desired-instance-type` \
    --deployment-type `desired-deployment-type` \
    --db-parameter-group-name `new-param-group` \
    --port `8086`

```

For Windows:

```
aws timestream-influxdb update-db-instance ^
    --identifier `my-db-instance` ^
    --db-storage-type `desired-storage-type` ^
    --allocated-storage `desired-allocated-storage` ^
    --db-instance-type `desired-instance-type` ^
    --deployment-type `desired-deployment-type` ^
    --db-parameter-group-name `new-param-group`
    --port `8086`

```
