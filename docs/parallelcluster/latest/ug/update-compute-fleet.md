# updateComputeFleet

Update the status of the cluster compute fleet.

###### Topics

- [Request syntax](#update-compute-fleet-request "#update-compute-fleet-request")
- [Request body](#update-compute-fleet-request-body "#update-compute-fleet-request-body")
- [Response syntax](#update-compute-fleet-response "#update-compute-fleet-response")
- [Response body](#update-compute-fleet-response-body "#update-compute-fleet-response-body")
- [Example](#update-compute-fleet-example "#update-compute-fleet-example")

## Request syntax

```
PATCH /v3/clusters/{`clusterName`}/computefleet
{
  "status": "string",
  "region": "string"
}
```

## Request body

**clusterName**

The name of the cluster.

Type: string

Required: Yes

**status**

The compute fleet status.

Type: string

Valid values: `START_REQUESTED | STOP_REQUESTED | ENABLED |
 DISABLED`

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

The compute fleet status.

Type: string

Valid values: `START_REQUESTED | STARTING | RUNNING | PROTECTED |
 STOP_REQUESTED | STOPPING | STOPPED | UNKNOWN | ENABLED | DISABLED`

**lastStatusUpdatedTime**

The timestamp that represents the last status update time.

Type: datetime

## Example

Python
Request

```
`$` `update_compute_fleet(`cluster_name_3x`, "START_REQUESTED")`
```

200 Response

```
`{
 'last_status_updated_time': datetime.datetime(2022, 3, 28, 22, 27, 14, tzinfo=tzlocal()),
 'status': 'START_REQUESTED'
}`
```
