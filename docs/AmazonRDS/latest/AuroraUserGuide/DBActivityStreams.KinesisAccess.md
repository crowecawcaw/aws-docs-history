# Accessing an activity stream from Amazon Kinesis

When you enable an activity stream for a DB cluster, a Kinesis stream is created for you. From Kinesis, you can monitor your
database activity in real time. To further analyze database activity, you can connect your Kinesis stream to consumer
applications. You can also connect the stream to compliance management applications such as IBM's Security Guardium or Imperva's SecureSphere Database Audit and Protection.

You can access your Kinesis stream either from the RDS console or the Kinesis console.

###### To access an activity stream from Kinesis using the RDS console

1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the DB cluster on which you started an activity stream.
4. Choose **Configuration**.
5. Under **Database activity stream**, choose the link under
   **Kinesis stream**.
6. In the Kinesis console, choose **Monitoring** to begin observing the
   database activity.

###### To access an activity stream from Kinesis using the Kinesis console

1. Open the Kinesis console at
   [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis").
2. Choose your activity stream from the list of Kinesis streams.

An activity stream's name includes the prefix `aws-rds-das-cluster-`
followed by the resource ID of the DB cluster. The following is an example.

```
aws-rds-das-cluster-NHVOV4PCLWHGF52NP
```

To use the Amazon RDS console to find the resource ID for
the DB cluster,
choose your DB cluster from the list of databases, and then choose
the **Configuration** tab.

To use the AWS CLI to find the full Kinesis stream name for an activity stream, use a
[describe-db-clusters](../../../cli/latest/reference/rds/describe-db-clusters.md "../../../cli/latest/reference/rds/describe-db-clusters.md")

CLI request and note the value of `ActivityStreamKinesisStreamName` in the
response. 3. Choose **Monitoring** to begin observing the database activity.
For more information about using Amazon Kinesis, see
[What Is Amazon Kinesis Data Streams?](../../../streams/latest/dev/introduction.md "../../../streams/latest/dev/introduction.md").
