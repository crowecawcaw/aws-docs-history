# Querying session statistics aggregated data using the AWS CLI

To track costs, analyze resource usage, or identify which users are consuming the most
resources, you can use the AWS Command Line Interface (AWS CLI) to query aggregated session statistics for your
AWS Deadline Cloud (Deadline Cloud) farms. The session statistics API provides data about costs, runtime, and
usage that you can group by various dimensions such as queue, fleet, instance type, or user.

Querying session statistics is an asynchronous process. First, you start an aggregation
request, then you retrieve the results using the aggregation ID.

## Starting an aggregation request

To start an aggregation request, run the
`start-sessions-statistics-aggregation` command. The following example groups
statistics by user ID for a specific queue. Replace the `placeholder` text with your information.

```
aws deadline start-sessions-statistics-aggregation \
    --farm-id `farm-id` \
    --resource-ids '{"queueIds":["`queue-id`"]}' \
    --start-time `2025-11-24T10:00:00Z` \
    --end-time `2025-11-25T18:00:00Z` \
    --group-by '["`USER_ID`"]' \
    --period `HOURLY` \
    --statistics '["`SUM`"]' \
    --timezone `UTC-08:00` \
    --region `region-name`
```

You can group statistics by other dimensions such as `QUEUE_ID`,
`FLEET_ID`, `JOB_ID`, `INSTANCE_TYPE`, or
`LICENSE_PRODUCT`. For more information about all available parameters, see [start-sessions-statistics-aggregation](../../../cli/latest/reference/deadline/start-sessions-statistics-aggregation.md "../../../cli/latest/reference/deadline/start-sessions-statistics-aggregation.md") in the AWS CLI Command Reference.

The response contains an aggregation ID:

```
{
    "aggregationId": "92b35143f2d04641979bc9b777232f38"
}
```

## Retrieving results

Run the `get-sessions-statistics-aggregation` command with the aggregation ID
to retrieve the results. Replace the `placeholder` text with your information.

```
aws deadline get-sessions-statistics-aggregation \
    --farm-id `farm-id` \
    --aggregation-id `aggregation-id` \
    --region `region-name`
```

The following example shows a response when you group statistics by user ID. The
`userId` field contains a UUID that you must map to a username to identify the
user:

```
{
    "statistics": [
        {
            "userId": "f9c1f3f0-1031-70dc-4d25-30d7225b04a0",
            "count": 1,
            "costInUsd": {
                "sum": 0.0
            },
            "runtimeInSeconds": {
                "sum": 53.773
            },
            "aggregationStartTime": "2025-11-24T22:00:00Z",
            "aggregationEndTime": "2025-11-24T23:00:00Z"
        }
    ],
    "status": "COMPLETED"
}
```

To find the username associated with a `userId`, see
[Retrieving user metadata and attributes using userID in an identity store](query-session-data-map-userid.md "query-session-data-map-userid.md").

For more information about the API, see the [Deadline Cloud API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

###### Topics

- [Retrieving user metadata and attributes using userID in an identity store](query-session-data-map-userid.md "query-session-data-map-userid.md")
