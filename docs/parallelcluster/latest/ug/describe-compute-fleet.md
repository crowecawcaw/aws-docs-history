# describeComputeFleet

Describe the status of the compute fleet.

###### Topics

- [Request syntax](#describe-compute-fleet-request "#describe-compute-fleet-request")
- [Request body](#describe-compute-fleet-request-body "#describe-compute-fleet-request-body")
- [Response syntax](#describe-compute-fleet-response "#describe-compute-fleet-response")
- [Response body](#describe-compute-fleet-response-body "#describe-compute-fleet-response-body")
- [Example](#describe-compute-fleet-example "#describe-compute-fleet-example")

## Request syntax

```
GET /v3/clusters/{`clusterName`}/computefleet
{
  "region": "string"
}
```

## Request body

**clusterName**

The name of the cluster.

Type: string

Required: Yes

**region**

The AWS Region that the cluster is in.

Type: string

Required: No

## Response syntax

```
{
  "status": "START_REQUESTED",
  "lastStatusUpdatedTime": "2019-08-24T14:15:22Z"
}
```

## Response body

**status**

Type: string

Valid values: `START_REQUESTED | STARTING | RUNNING | PROTECTED |
 STOP_REQUESTED | STOPPING | STOPPED | UNKNOWN | ENABLED | DISABLED`

**lastStatusUpdatedTime**

The timestamp representing the last status update time.

Type: datetime

## Example

Python
Request

```
`$` `describe_compute_fleet(`cluster_name_3x`)`
```

200 Response

```
`{
 "last_status_updated_time": datetime.datetime(2022, 3, 28, 22, 27, 14, tzinfo=tzlocal()),
 "status": "RUNNING"
}`
```
