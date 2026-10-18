

# Neptune online index rebuild
<a name="storage-index-rebuild"></a>

 With online index rebuild, you can defragment Neptune indexes and reclaim unused storage space while your database stays fully operational. This lets you optimize storage costs and improve query performance without taking your database offline. Over time, insert, update, and delete operations create gaps of unused space within data pages, which fragments the indexes. Fragmentation keeps the `VolumeBytesUsed` metric high even after you delete data. It also increases I/O costs, because the same logical data spreads across more physical storage pages. An online index rebuild compacts the indexes to reclaim this space and reduce fragmentation. 

During the online rebuild, your database remains fully available. You can continue running concurrent read and write queries in Gremlin, openCypher, and SPARQL.

 You can rebuild all indexes (quads and dictionaries), only the quad indexes, or only the dictionary indexes. The online index rebuild APIs are available starting with Neptune engine release 1.5.0.0. 

## Prerequisites
<a name="storage-index-rebuild-prerequisites"></a>

### Engine version
<a name="storage-index-rebuild-prereq-engine"></a>

The online index rebuild APIs require Neptune engine release 1.5.0.0 or later.

### Writer instance
<a name="storage-index-rebuild-prereq-instance"></a>

You must initiate a rebuild on the writer instance, and the writer must be a provisioned instance. Online index rebuild is not supported on a Neptune Serverless writer instance. Read replicas are unaffected by the rebuild and can be either serverless or provisioned.

### IAM permissions
<a name="storage-index-rebuild-prereq-iam"></a>

If your cluster uses IAM authentication, the IAM policy attached to the requesting principal must allow the index rebuild actions:

```
{
  "Effect": "Allow",
  "Action": [
    "neptune-db:StartIndexRebuild",
    "neptune-db:GetIndexRebuildStatus",
    "neptune-db:ListIndexRebuilds",
    "neptune-db:CancelIndexRebuild"
  ],
  "Resource": "arn:aws:neptune-db:<region>:<account-id>:<cluster-resource-id>/*"
}
```

For more information about data-plane IAM actions, see [IAM actions for data access in Amazon Neptune](iam-dp-actions.md).

## When to use it
<a name="storage-index-rebuild-when"></a>
+ After significant data deletions (from queries or dictionary garbage collection), when `VolumeBytesUsed` stays high despite less data.
+ When your database is approaching the storage limit and you need to reclaim space.
+ As periodic maintenance (for example, quarterly or yearly) to keep indexes optimized.

What to expect during a rebuild:
+ **Your database stays online.** Read queries and write queries continue to work on the writer instance. Read replicas are unaffected.
+ **Transient query errors are possible.** During the rebuild, some queries can fail with a retriable `CancelledByMaintenanceException`. Your application must catch this exception, treat it like a `ConcurrentModificationException`, and retry with exponential backoff.
+ **There can be a small performance impact** on queries. The rebuild competes for resources such as the buffer cache and I/O.
+ **Neptune rejects bulk load API calls during a rebuild.** If you call the [bulk load API](load-api-reference-load.md) (`POST /loader`) while an index rebuild is in progress, the request fails with a `CancelledByMaintenanceException`. Cancel the rebuild with `CancelIndexRebuild` and wait for it to reach `CANCELLED`, or wait for the rebuild to complete, and then retry the load.
+ **Neptune rejects fast reset API calls during a rebuild.** A call to the [fast reset API](manage-console-fast-reset.md) (`ExecuteFastReset`) fails with a `CancelledByMaintenanceException` while an index rebuild is in progress. Cancel the rebuild with `CancelIndexRebuild` and wait for it to reach `CANCELLED`, or wait for the rebuild to complete, and then retry.

## API reference
<a name="storage-index-rebuild-api"></a>

 Online index rebuild includes four APIs: `StartIndexRebuild`, `GetIndexRebuildStatus`, `ListIndexRebuilds`, and `CancelIndexRebuild`. All of them must be sent to the writer instance. For the complete request and response members of each operation, see the [Neptune data plane API reference](https://docs.aws.amazon.com/neptune/latest/userguide/data-api.html). 

### StartIndexRebuild
<a name="storage-index-rebuild-start"></a>

Initiates a rebuild operation. Send an HTTP `POST` request to the `/storage/indexes/rebuilds` endpoint.

```
POST https://{{your-neptune-endpoint}}:{{port}}/storage/indexes/rebuilds
POST https://{{your-neptune-endpoint}}:{{port}}/storage/indexes/rebuilds?scope=QUADS
POST https://{{your-neptune-endpoint}}:{{port}}/storage/indexes/rebuilds?scope=DICTIONARIES
```

The request accepts the following optional query parameters:
+ **`scope`**—The scope of the rebuild.

  *Type*: String. *Valid values*: `ALL` (quads and dictionaries), `QUADS` (quad indexes only), or `DICTIONARIES` (dictionary indexes only). *Default*: `ALL`.
+ **`concurrency`**—The number of parallel workers used for the rebuild.

  *Type*: Integer. *Valid values*: An integer between `1` and the maximum number of vCPUs available on the writer instance type. If the value exceeds the maximum available vCPUs, Neptune caps it at the maximum rather than returning an error. *Default*: `1`.

  If your workload is heavy, use a lower concurrency to reduce contention with your other workloads.
+ **`writeBufferSize`**— Controls the size of the buffer that tracks concurrent write operations during the rebuild. If your database has high write traffic during the rebuild, a larger buffer helps prevent the operation from failing due to buffer overflow.

  *Type*: String. *Valid values*: `LOW` (light to moderate write activity), `MEDIUM` (sustained write traffic), or `HIGH` (heavy write workloads). *Default*: `LOW`.

The following examples show several ways to start a rebuild:

------
#### [ AWS CLI ]

```
# Rebuild everything (default)
aws neptunedata start-index-rebuild \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}}

# Rebuild quad indexes only
aws neptunedata start-index-rebuild \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --scope QUADS

# Rebuild with 4 workers and a high write buffer
aws neptunedata start-index-rebuild \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --scope ALL \
  --concurrency 4 \
  --write-buffer-size HIGH
```

For more information, see [start-index-rebuild](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/start-index-rebuild.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

```
import boto3
import json
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

# Rebuild everything (default)
response = client.start_index_rebuild()

# Rebuild quad indexes only
response = client.start_index_rebuild(Scope='QUADS')

# Rebuild with 4 workers and a high write buffer
response = client.start_index_rebuild(
    Scope='ALL',
    Concurrency=4,
    WriteBufferSize='HIGH'
)

print(json.dumps(response, indent=2, default=str))
```

------
#### [ awscurl ]

```
# Rebuild everything (default)
awscurl https://{{your-neptune-endpoint}}:{{port}}/storage/indexes/rebuilds \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST

# Rebuild quad indexes only
awscurl "https://{{your-neptune-endpoint}}:{{port}}/storage/indexes/rebuilds?scope=QUADS" \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST

# Rebuild with 4 workers and a high write buffer
awscurl "https://{{your-neptune-endpoint}}:{{port}}/storage/indexes/rebuilds?concurrency=4&writeBufferSize=HIGH" \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST
```

**Prerequisites**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
# Rebuild everything (default)
curl -X POST https://{{your-neptune-endpoint}}:{{port}}/storage/indexes/rebuilds

# Rebuild quad indexes only
curl -X POST "https://{{your-neptune-endpoint}}:{{port}}/storage/indexes/rebuilds?scope=QUADS"

# Rebuild with 4 workers and a high write buffer
curl -X POST "https://{{your-neptune-endpoint}}:{{port}}/storage/indexes/rebuilds?concurrency=4&writeBufferSize=HIGH"
```

------

A successful request returns HTTP 200 with the initial rebuild state:

```
{
  "status": "PREPARING",
  "rebuildId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "scope": "ALL",
  "concurrency": 1,
  "writeBufferSize": "LOW",
  "startTime": "2026-04-22T22:58:45Z"
}
```

Save the `rebuildId` from the response—you use it to query status and to cancel the rebuild. Only one rebuild can run at a time. If you start a rebuild while one is already in progress, you receive a `409 ConflictException`.

#### Errors
<a name="storage-index-rebuild-start-errors"></a>

The following table lists the errors that `StartIndexRebuild` can return.


| HTTP status | Error code | Description | 
| --- | --- | --- | 
| 400 | InvalidParameterException | One or more parameters are invalid. | 
| 409 | ConflictException | A rebuild is already in progress for this database. | 
| 429 | ThrottlingException | The request was denied due to request throttling. | 
| 500 | InternalServerException | An internal service error occurred. | 

### GetIndexRebuildStatus
<a name="storage-index-rebuild-status"></a>

Returns the status and progress of a rebuild operation. Send an HTTP `GET` request with the `rebuildId` appended to the path.

------
#### [ AWS CLI ]

```
aws neptunedata get-index-rebuild-status \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --rebuild-id {{rebuildId}}
```

For more information, see [get-index-rebuild-status](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/get-index-rebuild-status.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

```
import boto3
import json
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.get_index_rebuild_status(
    RebuildId='{{rebuildId}}'
)

print(json.dumps(response, indent=2, default=str))
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/storage/indexes/rebuilds/{{rebuildId}} \
  --region {{us-east-1}} \
  --service neptune-db
```

**Prerequisites**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl -G https://{{your-neptune-endpoint}}:{{port}}/storage/indexes/rebuilds/{{rebuildId}}
```

------

The response reports the current state of the rebuild:

```
{
  "status": "REBUILDING",
  "rebuildId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "scope": "ALL",
  "concurrency": 1,
  "writeBufferSize": "LOW",
  "startTime": "2026-04-22T02:00:05Z",
  "estimatedEndTime": "2026-04-23T02:00:05Z",
  "progressPercentage": 45
}
```

The response contains the following fields:


| Field | Description | 
| --- | --- | 
| status | The current status: PREPARING, REBUILDING, COMPLETED, FAILED, CANCELLING, or CANCELLED. | 
| rebuildId | The unique identifier for the rebuild operation (UUID). | 
| scope | The scope of the rebuild (ALL, QUADS, or DICTIONARIES). | 
| concurrency | The concurrency of the rebuild operation. | 
| writeBufferSize | The write buffer size of the rebuild operation (LOW, MEDIUM, or HIGH). | 
| startTime | When the rebuild started (ISO-8601). | 
| estimatedEndTime | The estimated completion time (ISO-8601). Present during REBUILDING and CANCELLING. | 
| endTime | When the rebuild reached a terminal state (ISO-8601). Present for COMPLETED, FAILED, or CANCELLED. | 
| progressPercentage | The percentage of rebuild completion (0–100). | 
| failureReason | The reason for failure. Present only when status is FAILED. | 

#### Errors
<a name="storage-index-rebuild-status-errors"></a>

The following table lists the errors that `GetIndexRebuildStatus` can return.


| HTTP status | Error code | Description | 
| --- | --- | --- | 
| 404 | ResourceNotFoundException | The rebuild ID was not found. | 
| 429 | ThrottlingException | The request was denied due to request throttling. | 
| 500 | InternalServerException | An internal service error occurred. | 

### ListIndexRebuilds
<a name="storage-index-rebuild-list"></a>

Returns the list of rebuild operation IDs. Send an HTTP `GET` request to the `/storage/indexes/rebuilds` endpoint.

------
#### [ AWS CLI ]

```
aws neptunedata list-index-rebuilds \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}}
```

For more information, see [list-index-rebuilds](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/list-index-rebuilds.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

```
import boto3
import json
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.list_index_rebuilds()

print(json.dumps(response, indent=2, default=str))
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/storage/indexes/rebuilds \
  --region {{us-east-1}} \
  --service neptune-db
```

**Prerequisites**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl -G https://{{your-neptune-endpoint}}:{{port}}/storage/indexes/rebuilds
```

------

The response contains a `rebuildIds` array. Use each ID with `GetIndexRebuildStatus` to retrieve detailed status.

```
{
  "rebuildIds": [
    "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
  ]
}
```

**Rebuild history**  
Only the most recent rebuild is retained. For details, see [Limitations](#storage-index-rebuild-limitations).

#### Errors
<a name="storage-index-rebuild-list-errors"></a>

The following table lists the errors that `ListIndexRebuilds` can return.


| HTTP status | Error code | Description | 
| --- | --- | --- | 
| 429 | ThrottlingException | The request was denied due to request throttling. | 
| 500 | InternalServerException | An internal service error occurred. | 

### CancelIndexRebuild
<a name="storage-index-rebuild-cancel"></a>

Cancels an in-progress rebuild. Send an HTTP `POST` request to the `cancel` sub-resource of the rebuild.

------
#### [ AWS CLI ]

```
aws neptunedata cancel-index-rebuild \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --rebuild-id {{rebuildId}}
```

For more information, see [cancel-index-rebuild](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/cancel-index-rebuild.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

```
import boto3
import json
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.cancel_index_rebuild(
    RebuildId='{{rebuildId}}'
)

print(json.dumps(response, indent=2, default=str))
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/storage/indexes/rebuilds/{{rebuildId}}/cancel \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST
```

**Prerequisites**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl -X POST https://{{your-neptune-endpoint}}:{{port}}/storage/indexes/rebuilds/{{rebuildId}}/cancel
```

------

 The `CancelIndexRebuild` API makes a best-effort attempt to cancel the rebuild. When you call it, the rebuild transitions to `CANCELLING` status. During this phase, work that is already in progress must finish before the rebuild reaches `CANCELLED` status. This can take from minutes to hours depending on what is currently in flight. If the rebuild is still in `PREPARING` (no work has started), it transitions directly to `CANCELLED`. Your database remains fully operational throughout. 

```
{
  "status": "CANCELLING",
  "rebuildId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "scope": "ALL",
  "concurrency": 1,
  "writeBufferSize": "LOW",
  "startTime": "2026-04-22T02:00:05Z",
  "estimatedEndTime": "2026-04-22T22:00:00Z",
  "progressPercentage": 37
}
```

#### Errors
<a name="storage-index-rebuild-cancel-errors"></a>

The following table lists the errors that `CancelIndexRebuild` can return.


| HTTP status | Error code | Description | 
| --- | --- | --- | 
| 400 | InvalidParameterException | The rebuild is not in a cancellable state (for example, it is already COMPLETED, FAILED, or CANCELLED). | 
| 404 | ResourceNotFoundException | The rebuild ID was not found. | 
| 429 | ThrottlingException | The request was denied due to request throttling. | 
| 500 | InternalServerException | An internal service error occurred. | 

## Status lifecycle
<a name="storage-index-rebuild-lifecycle"></a>

The following description shows the possible state transitions from initiation through completion or cancellation:

A rebuild starts in `PREPARING`. From `PREPARING`, it either transitions directly to `CANCELLED` (if you cancel before any work starts) or advances to `REBUILDING`. From `REBUILDING`, the rebuild can complete successfully (`COMPLETED`), fail (`FAILED`), or enter `CANCELLING`. A `CANCELLING` rebuild eventually reaches `CANCELLED`.
+ `PREPARING`—The rebuild is initializing.
+ `REBUILDING`—Index tables are actively being rebuilt. Your database remains fully operational.
+ `COMPLETED`—The rebuild finished successfully.
+ `FAILED`—The rebuild encountered an error. Your database is fully operational. Check `failureReason` for details.
+ `CANCELLING`—A cancel was requested and in-flight work is draining. This can take minutes to hours depending on what is currently in flight.
+ `CANCELLED`—The rebuild was cancelled. Your database is fully operational.

## Storage safety mechanisms
<a name="storage-index-rebuild-safety"></a>

The online index rebuild includes built-in safety mechanisms to prevent storage exhaustion during the rebuild process:
+ **Storage budget with safety margin.** The rebuild applies an 80% safety margin against available volume space. A rebuild also requires additional scratch space while it runs. At maximum concurrency, this is up to roughly 25% of the data being rebuilt; the amount decreases proportionally at lower concurrency. The budget reserves headroom for this scratch space plus the concurrent writes and transaction-log growth that occur during the rebuild.
+ **Adaptive scheduling.** The rebuild continuously checks how much free volume space is available and adjusts its parallelism accordingly. When free space is tight, the rebuild slows down to reduce peak storage consumption. When more space is available, the rebuild runs more work in parallel to finish faster.
+ **Fail-fast on storage exhaustion.** If the rebuild cannot proceed after all in-flight work completes and the budget refreshes, it fails immediately. Neptune sets the `failureReason` message to `Insufficient storage to perform index rebuild`. The rebuild does not skip work silently.
+ **100 TB default limit.** By default, an index rebuild request fails immediately on a cluster with more than 100 TB of `VolumeBytesUsed`. This limit is a safety precaution. A rebuild on a large cluster can require significant additional scratch space (up to roughly 25% of the data being rebuilt at maximum concurrency). This can push a cluster near or over its storage limit.

If your cluster exceeds 100 TB and you need to run an index rebuild, contact AWS Support to open a case with the Neptune team. We can review your cluster's size, growth rate, and workload, and work with you to plan the rebuild safely. Depending on the situation, we might recommend running the rebuild at reduced concurrency to lower scratch-space needs, scoping the rebuild to only the indexes that need it (`scope=QUADS` or `scope=DICTIONARIES`), or scheduling it during a lower-traffic window.

## Typical workflow
<a name="storage-index-rebuild-workflow"></a>

Use the following workflow to assess and optimize your Neptune storage.

1. **Assess storage usage.** Call [GetStorageInfo](storage-info.md) to understand your current storage distribution and look for large index sizes relative to entry counts, which indicate fragmentation. Note the current `VolumeBytesUsed` value as a baseline.

------
#### [ AWS CLI ]

   ```
   aws neptunedata get-storage-info \
     --endpoint-url https://{{your-neptune-endpoint}}:{{port}}
   ```

------
#### [ SDK ]

   ```
   response = client.get_storage_info()
   ```

------
#### [ awscurl ]

   ```
   awscurl https://{{your-neptune-endpoint}}:{{port}}/storage/info \
     --region {{us-east-1}} \
     --service neptune-db
   ```

------
#### [ curl ]

   ```
   curl -G https://{{your-neptune-endpoint}}:{{port}}/storage/info
   ```

------

1. **Start an index rebuild.** If you identify fragmentation or bloat, initiate a rebuild and save the `rebuildId` from the response.

------
#### [ AWS CLI ]

   ```
   aws neptunedata start-index-rebuild \
     --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
     --scope QUADS
   ```

------
#### [ SDK ]

   ```
   response = client.start_index_rebuild(Scope='QUADS')
   ```

------
#### [ awscurl ]

   ```
   awscurl "https://{{your-neptune-endpoint}}:{{port}}/storage/indexes/rebuilds?scope=QUADS" \
     --region {{us-east-1}} \
     --service neptune-db \
     -X POST
   ```

------
#### [ curl ]

   ```
   curl -X POST "https://{{your-neptune-endpoint}}:{{port}}/storage/indexes/rebuilds?scope=QUADS"
   ```

------

1. **Monitor progress.** Poll the rebuild status periodically. The `progressPercentage` field tracks completion and `estimatedEndTime` estimates when the rebuild will finish.

------
#### [ AWS CLI ]

   ```
   aws neptunedata get-index-rebuild-status \
     --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
     --rebuild-id {{rebuildId}}
   ```

------
#### [ SDK ]

   ```
   response = client.get_index_rebuild_status(
       RebuildId='{{rebuildId}}'
   )
   ```

------
#### [ awscurl ]

   ```
   awscurl https://{{your-neptune-endpoint}}:{{port}}/storage/indexes/rebuilds/{{rebuildId}} \
     --region {{us-east-1}} \
     --service neptune-db
   ```

------
#### [ curl ]

   ```
   curl -G https://{{your-neptune-endpoint}}:{{port}}/storage/indexes/rebuilds/{{rebuildId}}
   ```

------

1. **Verify results.** After the rebuild completes, call `GetStorageInfo` again to confirm that storage sizes decreased. You can also track the `VolumeBytesUsed` and `VolumeBytesLeftTotal` CloudWatch metrics over time.

------
#### [ AWS CLI ]

   ```
   aws neptunedata get-storage-info \
     --endpoint-url https://{{your-neptune-endpoint}}:{{port}}
   ```

------
#### [ SDK ]

   ```
   response = client.get_storage_info()
   ```

------
#### [ awscurl ]

   ```
   awscurl https://{{your-neptune-endpoint}}:{{port}}/storage/info \
     --region {{us-east-1}} \
     --service neptune-db
   ```

------
#### [ curl ]

   ```
   curl -G https://{{your-neptune-endpoint}}:{{port}}/storage/info
   ```

------

## Best practices
<a name="storage-index-rebuild-best-practices"></a>
+ **Implement retry logic.** During the rebuild, some queries can fail with a transient `CancelledByMaintenanceException`, which you should treat like a `ConcurrentModificationException`. Retry failed queries with exponential backoff.
+ **Monitor progress.** Poll `GetIndexRebuildStatus` to track progress and estimated completion time.
+ **Run GetStorageInfo before and after.** This lets you quantify the space reclaimed and track storage efficiency over time. You can also track the `VolumeBytesUsed` and `VolumeBytesLeftTotal` CloudWatch metrics during the rebuild.
+ **Target the scope to the component that holds the reclaimable space.** Use [GetStorageInfo](storage-info.md) to see whether your quad indexes or your dictionaries account for the most reclaimable space, and rebuild only that component with `scope=QUADS` or `scope=DICTIONARIES` for a faster, lower-impact rebuild. Use `scope=ALL` only when both need optimization.
+ **Tune concurrency to balance speed against workload impact.** A higher `concurrency` finishes faster. However, it competes far more aggressively for buffer cache and I/O. This competition can noticeably slow your concurrent queries. Start with a low concurrency (the default is `1`) when the rebuild runs alongside production traffic, and increase it only when you have spare instance capacity or are running in a maintenance window.
+ **Consider the write buffer size.** If you have a heavy write workload during the rebuild, use `writeBufferSize=HIGH` so that all of the write workload can be tracked and applied to the rebuilt indexes.
+ **Consider scaling up the writer instance for the duration of the rebuild.** Rebuilds run faster on larger writer instances because parallel workers scale with available vCPUs and a larger buffer pool reduces I/O when the graph exceeds the pool size on a smaller instance. If wall-clock time matters, temporarily use a larger writer during the rebuild and scale back afterward.
+ **Plan for cancellation.** Cancellation is best-effort. When you call `CancelIndexRebuild`, work that is already in progress must finish before the rebuild reaches `CANCELLED` status. The time this takes can range from minutes to hours, depending on what is currently in flight.

## Limitations
<a name="storage-index-rebuild-limitations"></a>
+ **One rebuild at a time.** Only one index rebuild can run at a time for each cluster.
+ **Transient query failures.** During brief internal commit phases of the rebuild, some queries can fail with a retriable `CancelledByMaintenanceException`. Implement retry logic with exponential backoff.
+ **Rebuild history.** Currently, only the most recent rebuild is retained in memory. Persistent rebuild history is planned for a future release. If the engine restarts or crashes, the most recent rebuild record is lost.
+ **100 TB limit.** If your cluster exceeds a `VolumeBytesUsed` of 100 TB, contact AWS Support to coordinate the index rebuild with the Neptune team.
+ **Estimated end time is approximate.** The `estimatedEndTime` returned by `GetIndexRebuildStatus` is a best-effort estimate. Actual completion time can vary depending on data sizes, concurrent workload, and storage conditions. A writer instance with a larger buffer pool can complete the rebuild significantly faster.
+ **Extremely heavy workload can fail the rebuild.** A very heavy concurrent workload (through read or write queries) can cause the rebuild to fail, either from heavy contention for hardware resources such as the buffer cache and I/O, or because the write buffer fills up. To resolve this, reduce your workload, or reduce the scope and concurrency of the rebuild and raise its `writeBufferSize` (up to the `HIGH` maximum). If the rebuild still fails at `writeBufferSize=HIGH`, reduce the concurrent write workload, or run the rebuild during a lower-traffic window.

## Frequently asked questions
<a name="storage-index-rebuild-faq"></a>

### Does the index rebuild take my database offline?
<a name="storage-index-rebuild-faq-offline"></a>

No. During an online index rebuild, you can run concurrent read and write queries. Your database remains fully operational throughout the rebuild, regardless of the `scope` you specify.

### Does the index rebuild support the OSGP and PZSOG indexes?
<a name="storage-index-rebuild-faq-osgp-pzsog"></a>

Yes. If you have the OSGP index and/or the PZSOG index (for geospatial data) enabled, the rebuild rebuilds them too when `scope` is `ALL` or `QUADS`.

### How long does an index rebuild take?
<a name="storage-index-rebuild-faq-duration"></a>

The duration depends on the total size of your indexes and the volume of write operations during the rebuild, because those writes must be reapplied to the new indexes as well. You can monitor progress with `GetIndexRebuildStatus`, which provides `progressPercentage` and `estimatedEndTime`. Under heavy concurrent write activity, `estimatedEndTime` might not be accurate.

### Will I lose data during the rebuild?
<a name="storage-index-rebuild-faq-data-loss"></a>

No. The online rebuild is designed to preserve all data. Concurrent writes during the rebuild are committed normally.

### What happens if the rebuild fails?
<a name="storage-index-rebuild-faq-failure"></a>

Your database remains fully operational. `GetIndexRebuildStatus` shows `status=FAILED` with a `failureReason`. Common failure causes include:
+ **Insufficient storage.** The volume cannot provide enough scratch space to run the rebuild within its safety margin. See [Storage safety mechanisms](#storage-index-rebuild-safety).
+ **Write buffer overflow.** A sustained very heavy write workload during the rebuild can exhaust the internal buffer that tracks changes. Increase `writeBufferSize` (up to `HIGH`) or reduce the concurrent write workload and retry.

After investigating the cause, you can start a new rebuild.

A writer restart or failover does not produce a `FAILED` status. In those cases, Neptune loses the in-progress rebuild and its record, so `GetIndexRebuildStatus` returns `ResourceNotFoundException` for that `rebuildId`. For details, see [What happens if my engine restarts during a rebuild?](#storage-index-rebuild-faq-engine-restart) and [What happens if a failover occurs during the rebuild?](#storage-index-rebuild-faq-failover)

### Can I cancel a rebuild?
<a name="storage-index-rebuild-faq-cancel"></a>

Yes. Use the `CancelIndexRebuild` API. Cancellation is best-effort— in-flight work must drain before the rebuild reaches `CANCELLED`. Your database remains operational throughout.

### What happens if my engine restarts during a rebuild?
<a name="storage-index-rebuild-faq-engine-restart"></a>

The rebuild stops, and the engine restart discards its progress and `rebuildId`. Your database recovers to normal operation, and you can start a new rebuild.

### What happens if a failover occurs during the rebuild?
<a name="storage-index-rebuild-faq-failover"></a>

If a failover switches the writer to a read replica during an active rebuild, the in-progress rebuild is lost. The new writer is healthy and fully operational, and you can start a new rebuild after the failover completes.

### Can I run other Neptune APIs during the rebuild?
<a name="storage-index-rebuild-faq-other-apis"></a>

Yes for most APIs. `GetStorageInfo`, the query APIs (Gremlin, openCypher, SPARQL), and export continue to work. The [bulk load API](load-api-reference-load.md) (`POST /loader`) and the [fast reset API](manage-console-fast-reset.md) (`ExecuteFastReset`) are rejected during a rebuild.

### How often should I run an index rebuild?
<a name="storage-index-rebuild-faq-frequency"></a>

Consider running a rebuild when you observe significant storage bloat (through `GetStorageInfo`) or degraded query performance after heavy delete operations. Quarterly reviews are a reasonable starting point, but the optimal frequency depends on your workload patterns.

### Does the rebuild affect my read replicas?
<a name="storage-index-rebuild-faq-read-replicas"></a>

No. Read replicas are not affected by the rebuild and continue to serve read queries normally.

### My cluster only receives read queries—should I clone it, run the rebuild on the clone, and switch to the clone?
<a name="storage-index-rebuild-faq-clone"></a>

Cloning is a valid alternative only if you can pause all writes to the original cluster for the duration of the rebuild, or the cluster has no writes at all. Neptune does not replicate to the clone any writes made to the original cluster after the clone point — those writes are lost when you switch to the clone as your new primary. For workloads with ongoing writes, run the rebuild online on the primary instead.

If you can pause writes, follow this approach:

1. Use the Neptune fast-clone feature to create a point-in-time copy of the cluster.

1. Run the rebuild on the clone at your chosen concurrency without affecting the live cluster.

1. Update your application to point at the clone's endpoint once the rebuild completes.

For more information about cluster cloning, see [Database Cloning in Neptune](manage-console-cloning.md).

### Why does the rebuild take longer, or why do my queries slow down, when other workloads run at the same time?
<a name="storage-index-rebuild-faq-competition"></a>

The rebuild relies heavily on the buffer cache and I/O, so it competes for those resources with your other workloads. Monitor the `BufferCacheHitRatio` CloudWatch metric, which is the percentage of requests served by the buffer cache. If the cache hit ratio drops under 99.9%, consider upgrading the instance type to cache more data in memory, or reduce the concurrency of the rebuild to lessen competition with other workloads.