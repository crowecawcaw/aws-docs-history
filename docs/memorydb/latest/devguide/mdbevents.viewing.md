# Viewing MemoryDB events

MemoryDB logs events that relate to your clusters, security groups, and parameter groups.
This information includes the date and time of the event,
the source name and source type of the event,
and a description of the event.
You can easily retrieve events from the log using
the MemoryDB console,
the AWS CLI `describe-events` command, or
the MemoryDB API action `DescribeEvents`.

The following procedures show you how to view all MemoryDB events for the past 24 hours (1440 minutes).

## Viewing MemoryDB events (Console)

The following procedure displays events using the MemoryDB console.

###### To view events using the MemoryDB console

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. In the left navigation pane, choose **Events**.

The _Events_ screen appears listing all available events.
Each row of the list represents one event and displays
the event source,
the event type (such as cluster, parameter-group, acl, security-group or subnet group),
the GMT time of the event, and the description of the event.

Using the **Filter** you can specify whether you want to see all events, or
just events of a specific type in the event list.

## Viewing MemoryDB events (AWS CLI)

To generate a list of MemoryDB events using the AWS CLI,
use the command `describe-events`.
You can use optional parameters to control
the type of events listed,
the time frame of the events listed,
the maximum number of events to list, and more.

The following code lists up to 40 cluster events.

```
aws memorydb describe-events --source-type `cluster` --max-results `40`
```

The following code lists all events for the past 24 hours (1440 minutes).

```
aws memorydb describe-events --duration `1440`
```

The output from the `describe-events` command looks something like this.

```
{
    "Events": [
        {
            "Date": "2021-03-29T22:17:37.781Z",
            "Message": "Added node 0001 in Availability Zone us-east-1a",
            "SourceName": "memorydb01",
            "SourceType": "cluster"
        },
        {
            "Date": "2021-03-29T22:17:37.769Z",
            "Message": "cluster created",
            "SourceName": "memorydb01",
            "SourceType": "cluster"
        }
    ]
}
```

For more information, such as available parameters and permitted parameter values, see [`describe-events`](../../../cli/latest/reference/memorydb/describe-events.md "../../../cli/latest/reference/memorydb/describe-events.md").

## Viewing MemoryDB events (MemoryDB API)

To generate a list of MemoryDB events using the MemoryDB API,
use the `DescribeEvents` action.
You can use optional parameters to control
the type of events listed,
the time frame of the events listed,
the maximum number of events to list, and more.

The following code lists the 40 most recent -cluster events.

```
https://memory-db.us-east-1.amazonaws.com/
   ?Action=DescribeEvents
   &MaxResults=40
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &SourceType=cluster
   &Timestamp=20210802T192317Z
   &Version=2021-01-01
   &X-Amz-Credential=<credential>
```

The following code lists the cluster events for the past 24 hours (1440 minutes).

```
https://memory-db.us-east-1.amazonaws.com/
   ?Action=DescribeEvents
   &Duration=1440
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &SourceType=cluster
   &Timestamp=20210802T192317Z
   &Version=2021-01-01
   &X-Amz-Credential=<credential>
```

The above actions should produce output similar to the following.

```
<DescribeEventsResponse xmlns="http://memory-db.us-east-1.amazonaws.com/doc/2021-01-01/">
    <DescribeEventsResult>
        <Events>
            <Event>
                <Message>cluster created</Message>
                <SourceType>cluster</SourceType>
                <Date>2021-08-02T18:22:18.202Z</Date>
                <SourceName>my-memorydb-primary</SourceName>
            </Event>

 (...output omitted...)

        </Events>
    </DescribeEventsResult>
    <ResponseMetadata>
        <RequestId>e21c81b4-b9cd-11e3-8a16-7978bb24ffdf</RequestId>
    </ResponseMetadata>
</DescribeEventsResponse>
```

For more information, such as available parameters and permitted parameter values, see [`DescribeEvents`](../APIReference/API_DescribeEvents.md "../APIReference/API_DescribeEvents.md").
