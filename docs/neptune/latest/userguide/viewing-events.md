# Viewing Neptune events

You can view the following information for each Neptune event:

- Resource name
- Resource type
- Event category
- Time of the event
- A summary message describing the event
  You can access events in the following parts of the AWS Management Console:

- The **Events** page in the Neptune console navigation
  pane, which shows events from the past 24 hours.
- The **Recent events** table in the
  **Logs & events** tab on a DB cluster or DB instance detail page,
  which can show events for up to the past 14 days.
  You can also retrieve events by using the [describe-events](../../../cli/latest/reference/neptune/describe-events.md "../../../cli/latest/reference/neptune/describe-events.md") AWS CLI command or the [DescribeEvents](../apiref/API_DescribeEvents.md "../apiref/API_DescribeEvents.md") API operation. With the AWS CLI or API, you can retrieve
  events for up to the past 14 days.

## Viewing events (console)

###### To view Neptune events in the console

1. Sign in to the AWS Management Console and open the Neptune console at
   [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the navigation pane, choose **Events**.

The page displays events from the past 24 hours. You can filter events
by source type and event category.

## Viewing events (AWS CLI)

To view all Neptune events generated in the past hour, run
`describe-events` with no parameters:

```
aws neptune describe-events
```

To view events for the past 7 days (10,080 minutes), use the
`--duration` parameter:

```
aws neptune describe-events --duration 10080
```

To view events for a specific DB cluster within a time range, use the
`--source-identifier`, `--source-type`,
`--start-time`, and `--end-time` parameters:

```
aws neptune describe-events \
    --source-identifier `my-cluster` \
    --source-type db-cluster \
    --start-time `2026-04-01T00:00Z` \
    --end-time `2026-04-01T23:59Z`
```

For more information, see [describe-events](../../../cli/latest/reference/neptune/describe-events.md "../../../cli/latest/reference/neptune/describe-events.md") in the AWS CLI Command Reference. To retrieve events
programmatically, see [DescribeEvents](../apiref/API_DescribeEvents.md "../apiref/API_DescribeEvents.md") in the Neptune API Reference.
