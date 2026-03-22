# Stopping a database activity stream

You can stop an activity stream using the console or AWS CLI.

If you delete your DB cluster, the activity stream is stopped and the underlying Amazon Kinesis stream is deleted automatically.

###### To turn off an activity stream

1.  Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2.  In the navigation pane, choose **Databases**.
3.  Choose a DB cluster
    that you want to stop the database activity stream for.
4.  For **Actions**, choose **Stop activity stream**.
    The **Database Activity Stream** window
    appears.

        1. Choose **Immediately**.


        When you choose **Immediately**, the DB
         cluster restarts right away. If you choose
         **During the next maintenance window**, the DB
         cluster doesn't restart right away. In
         this case, the database activity stream doesn't stop until the next maintenance window.
        2. Choose **Continue**.

    To stop database activity streams for your DB cluster, configure the DB cluster using the AWS CLI command [stop-activity-stream](../../../cli/latest/reference/rds/stop-activity-stream.md "../../../cli/latest/reference/rds/stop-activity-stream.md"). Identify the AWS Region for the
    DB cluster using the
    `--region` parameter. The `--apply-immediately` parameter is optional.

For Linux, macOS, or Unix:

```
aws rds --region `MY_REGION` \
    stop-activity-stream \
    --resource-arn `MY_CLUSTER_ARN` \
    --apply-immediately
```

For Windows:

```
aws rds --region `MY_REGION` ^
    stop-activity-stream ^
    --resource-arn `MY_CLUSTER_ARN` ^
    --apply-immediately
```

To stop database activity streams for your DB cluster, configure the cluster using the [StopActivityStream](../APIReference/API_StopActivityStream.md "../APIReference/API_StopActivityStream.md") operation. Identify the AWS Region for the DB
cluster using the `Region` parameter. The
`ApplyImmediately` parameter is optional.
