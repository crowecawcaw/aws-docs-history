# Viewing Amazon RDS events

You can retrieve the following event information for your Amazon Aurora resources:

- Resource name
- Resource type
- Time of the event
- Message summary of the event
  You can access events in the following parts of the AWS Management Console:

- The **Events** tab, which shows events from the past 24 hours.
- The **Recent events** table in the **Logs & events**
  section in the **Databases** tab, which can show events for up to the past 2 weeks.
  You can also retrieve events by using the [describe-events](../../../cli/latest/reference/rds/describe-events.md "../../../cli/latest/reference/rds/describe-events.md") AWS CLI command, or the [DescribeEvents](../APIReference/API_DescribeEvents.md "../APIReference/API_DescribeEvents.md") RDS API operation. If you use the AWS CLI or the RDS API to view events,
  you can retrieve events for up to the past 14 days.

###### Note

If you need to store events for longer periods of time, you can send Amazon RDS events to EventBridge. For more information, see [Creating a rule that triggers on an Amazon Aurora event](rds-cloud-watch-events.md "rds-cloud-watch-events.md")

For descriptions of the Amazon Aurora events, see [Amazon RDS event categories and event messagesfor Aurora](USER_Events.md "USER_Events.md").

To access detailed information about events using AWS CloudTrail, including request parameters, see [CloudTrail events](logging-using-cloudtrail.md#service-name-info-in-cloudtrail.events "logging-using-cloudtrail.md#service-name-info-in-cloudtrail.events").

###### To view all Amazon RDS events for the past 24 hours

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Events**.

The available events appear in a list. 3. (Optional) Enter a search term to filter your results.

The following example shows a list of events filtered by the characters `apg`.

![List DB events](images/ListEventsAPG.png)
To view all events generated in the last hour, call [describe-events](../../../cli/latest/reference/rds/describe-events.md "../../../cli/latest/reference/rds/describe-events.md") with
no parameters.

```
aws rds describe-events
```

The following sample output shows that a DB cluster instance has started recovery.

```
{
    "Events": [
        {
            "EventCategories": [
                "recovery"
            ],
            "SourceType": "db-instance",
            "SourceArn": "arn:aws:rds:us-east-1:123456789012:db:mycluster-instance-1",
            "Date": "2022-04-20T15:02:38.416Z",
            "Message": "Recovery of the DB instance has started. Recovery time will vary with the amount of data to be recovered.",
            "SourceIdentifier": "mycluster-instance-1"
        }, ...

```

To view all Amazon RDS events for the past 10080 minutes (7 days), call the [describe-events](../../../cli/latest/reference/rds/describe-events.md "../../../cli/latest/reference/rds/describe-events.md") AWS CLI command and set the `--duration` parameter to `10080`.

```
aws rds describe-events --duration 10080
```

The following example shows the events in the specified time range for DB instance `test-instance`.

```
aws rds describe-events \
    --source-identifier `test-instance` \
    --source-type db-instance \
    --start-time 2022-03-13T22:00Z \
    --end-time 2022-03-13T23:59Z
```

The following sample output shows the status of a backup.

```
{
    "Events": [
        {
            "SourceType": "db-instance",
            "SourceIdentifier": "test-instance",
            "EventCategories": [
                "backup"
            ],
            "Message": "Backing up DB instance",
            "Date": "2022-03-13T23:09:23.983Z",
            "SourceArn": "arn:aws:rds:us-east-1:123456789012:db:test-instance"
        },
        {
            "SourceType": "db-instance",
            "SourceIdentifier": "test-instance",
            "EventCategories": [
                "backup"
            ],
            "Message": "Finished DB Instance backup",
            "Date": "2022-03-13T23:15:13.049Z",
            "SourceArn": "arn:aws:rds:us-east-1:123456789012:db:test-instance"
        }
    ]
}
```

You can view all Amazon RDS instance events for the past 14 days by calling the [DescribeEvents](../APIReference/API_DescribeEvents.md "../APIReference/API_DescribeEvents.md") RDS API operation and setting the
`Duration` parameter to `20160`.
