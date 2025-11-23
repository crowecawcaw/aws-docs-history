# Aggregating data events

Data events provide information about the resource operations performed on or in a resource. These are also known as data plane operations. Data events are often high-volume activities.

By enabling aggregation on your data events, you can efficiently monitor high-volume data access patterns without processing massive amounts of individual events. This feature automatically consolidates data events into 5-minute summaries, showing key trends like access frequency, error rates, and most-used actions. For example, instead of processing thousands of individual S3 bucket access events to understand usage patterns, you receive consolidated summaries showing top users and actions.

You can enable aggregation on data events when creating a new trail or updating an existing trail that collects data events. You can select one or all of the three out-of-the-box templates to aggregate your data events on:

- **API Activity** to get a 5-minute summary of your data events based on the API calls made. Use this to understand your API usage patterns, including frequency, callers, and source.
- **Resource Access** to get the activity patterns on your AWS resources. Use this to understand how your AWS resources are being accessed, how many times they are being accessed in the 5-minute window, who is accessing the resource, and what actions are being performed.
- **User Actions** to get activity patterns based on the IAM principal making API calls in your account.

## Enabling aggregations for data events for Amazon S3 objects using the AWS CLI

You can configure your trails to aggregate events using the AWS CLI.

To see whether your trail is aggregating data events, run the `get-event-configurations` command.

```
aws cloudtrail get-event-configuration --region us-east-1 --trail-name `TrailName`
```

The command returns the aggregation configuration for the trail.

Before you enable event aggregation, you must create a trail and configure data events in it.

To enable event aggregation on a trail, follow the step below. The trail will aggregate events based on the `API_ACTIVITY` and `RESOURCE_ACCESS` aggregation templates.

```
aws cloudtrail put-event-configuration --region us-east-1 --trail `TrailName` \
--aggregation-configurations \
'[
    {
        "EventCategory": "Data",
        "Templates":
        [
            "API_ACTIVITY",
            "RESOURCE_ACCESS"
        ]
    }
]'
```

### Example: API_ACTIVITY aggregated event

The following shows an example of an aggregated event for the `API_ACTIVITY` template:

```
{
    "eventVersion": "1.0",
    "accountId": "111122223333",
    "eventId": "62759c1a-6248-48e1-a6b3-d5fb7e6c4bc0",
    "eventCategory": "Aggregated",
    "eventType": "AwsAggregatedEvent",
    "awsRegion": "us-west-2",
    "eventSource": "s3.amazonaws.com",
    "timeWindow":
    {
        "windowStart": "2025-11-17T19:20:00Z",
        "windowEnd": "2025-11-17T19:25:00Z",
        "windowSize": "PT5M"
    },
    "summary":
    {
        "primaryDimension":
        {
            "dimension": "eventName",
            "statistics":
            [
                {
                    "name": "PutObject",
                    "value": 1000
                }
            ],
            "aggregationType": "Count"
        },
        "details":
        [
            {
                "dimension": "resourceARN",
                "statistics":
                [
                    {
                        "name": "arn:aws:s3:::bucket-1",
                        "value": 800
                    },
                    {
                        "name": "arn:aws:s3:::bucket-2",
                        "value": 150
                    },
                    {
                        "name": "arn:aws:s3:::bucket-3",
                        "value": 50
                    }
                ],
                "aggregationType": "Count"
            }
        ]
    }
}
```

### Example: RESOURCE_ACCESS aggregated event

The following shows an example of an aggregated event for the `RESOURCE_ACCESS` template:

```
{
    "eventVersion": "1.0",
    "accountId": "111122223333",
    "eventId": "2ed87efa-45c1-412d-bc38-7e0879faa6df",
    "eventCategory": "Aggregated",
    "eventType": "AwsAggregatedEvent",
    "awsRegion": "us-west-2",
    "eventSource": "s3.amazonaws.com",
    "timeWindow":
    {
        "windowStart": "2025-11-17T19:20:00Z",
        "windowEnd": "2025-11-17T19:25:00Z",
        "windowSize": "PT5M"
    },
    "summary":
    {
        "primaryDimension":
        {
            "dimension": "resourceARN",
            "statistics":
            [
                {
                    "name": "arn:aws:s3:::bucket-1",
                    "value": 800
                }
            ],
            "aggregationType": "Count"
        },
        "details":
        [
            {
                "dimension": "eventName",
                "statistics":
                [
                    {
                        "name": "PutObject",
                        "value": 800
                    }
                ],
                "aggregationType": "Count"
            }
        ]
    }
}
```
