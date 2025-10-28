# getClusterLogEvents

Retrieve the events that are associated with a log stream.

###### Topics

- [Request syntax](#get-cluster-log-events-request "#get-cluster-log-events-request")
- [Request body](#get-cluster-log-events-request-body "#get-cluster-log-events-request-body")
- [Response syntax](#get-cluster-log-events-response "#get-cluster-log-events-response")
- [Response body](#get-cluster-log-events-response-body "#get-cluster-log-events-response-body")
- [Example](#get-cluster-log-events-example "#get-cluster-log-events-example")

## Request syntax

```
GET /v3/clusters/{`clusterName`}/logstreams/{`logStreamName`}
{
  "endTime": datetime,
  "limit": float,
  "nextToken": "string",
  "region": "string",
  "startFromHead": boolean,
  "startTime": datetime
}
```

## Request body

**clusterName**

The name of the cluster.

Type: string

Required: Yes

**logStreamName**

The name of the log stream.

Type: string

Required: Yes

**endTime**

The end of the time range, expressed in ISO 8601 format. Events with a timestamp
equal to or later than this time are not included.

Type: datetime

Format: `2021-01-01T20:00:00Z`

Required: No

**limit**

The maximum number of log events returned. If you don't specify a value, the maximum
is the number of log events that can fit in a response size of 1 MB, or up to 10,000 log
events.

Type: float

Required: No

**nextToken**

The token for the next set of results.

Type: string

Required: No

**region**

The AWS Region that the cluster is in.

Type: string

Required: No

**startFromHead**

If set to `true`, the earliest log events are returned first. If
the value is `false`, the latest log events are returned first. The default
is `false`.

Type: boolean

Required: No

**startTime**

The start of the time range, expressed in ISO 8601 format. Events with a timestamp
equal to this time or later than this time are included.

Type: datetime

Format: `2021-01-01T20:00:00Z`

Required: No

## Response syntax

```
{
  "nextToken": "string",
  "prevToken": "string",
  "events": [
    {
      "timestamp": "2019-08-24T14:15:22Z",
      "message": "string"
    }
  ]
}
```

## Response body

**events**

List of filtered events.

**message**

The event message.

Type: string

**timestamp**

The event timestamp.

Type: datetime

**nextToken**

A token that can be used to retrieve the next set of results, or `null` if there are no additional results.

Type: string

**prevToken**

A token that can be used to retrieve the previous set of results, or `null` if there are no additional results.

Type: string

## Example

Python
Request

```
`$` `get_cluster_log_events(`cluster_name_3x`, `log_stream_name=ip-192-0-2-26.i-abcdef01234567890.cfn-init`)`
```

200 Response

```
`"events": [
 {
 "message": "2022-09-22 16:40:15,127 [DEBUG] CloudFormation client initialized with endpoint https://cloudformation.us-east-1.amazonaws.com",
 "timestamp": "2022-09-22T16:40:15.127Z"
 },
 {
 "message": "2022-09-22 16:40:15,127 [DEBUG] Describing resource HeadNodeLaunchTemplate in stack cluster_name_3x",
 "timestamp": "2022-09-22T16:40:15.127Z"
 },
 ...
]`
```
