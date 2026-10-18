

# Neptune storage usage breakdown
<a name="storage-info"></a>

 With the `GetStorageInfo` API, you can get a detailed breakdown of storage usage for your Neptune database, including undo logs, dictionary entries, change-stream data, DFE statistics, property graph schema, other internal metadata tables, and all of the quad indexes – grouped by property graph (PG) and Resource Description Framework (RDF). The response also includes a `totalStorageBytesUsed` value that sums the reported on-disk components. You can use this information to understand how your storage is distributed, to identify storage bloat, and to establish a baseline before and after an [online index rebuild](storage-index-rebuild.md). 

Use `GetStorageInfo` in the following situations:
+ To understand how your storage is distributed across indexes and dictionaries.
+ To identify storage bloat after bulk deletes or data migrations.
+ To establish a baseline before and after an index rebuild.
+ To monitor storage trends over time.

## Prerequisites
<a name="storage-info-prerequisites"></a>

### Engine version
<a name="storage-info-prereq-engine"></a>

The `GetStorageInfo` API requires Neptune engine release 1.5.0.0 or later.

### IAM permissions
<a name="storage-info-prereq-iam"></a>

If your cluster uses IAM authentication, the IAM policy attached to the requesting principal must allow the `neptune-db:GetStorageInfo` action:

```
{
  "Effect": "Allow",
  "Action": ["neptune-db:GetStorageInfo"],
  "Resource": "arn:aws:neptune-db:<region>:<account-id>:<cluster-resource-id>/*"
}
```

For more information about data-plane IAM actions, see [IAM actions for data access in Amazon Neptune](iam-dp-actions.md).

## Request
<a name="storage-info-request"></a>

 To retrieve storage information, send an HTTP `GET` request to the `/storage/info` endpoint. The request takes no body and no query parameters. 

------
#### [ AWS CLI ]

```
aws neptunedata get-storage-info \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}}
```

For more information, see [get-storage-info](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/get-storage-info.html) in the AWS CLI Command Reference.

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

response = client.get_storage_info()

print(json.dumps(response, indent=2, default=str))
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/storage/info \
  --region {{us-east-1}} \
  --service neptune-db
```

**Prerequisites**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl -G https://{{your-neptune-endpoint}}:{{port}}/storage/info
```

------

## Response
<a name="storage-info-response"></a>

 The `GetStorageInfo` API returns a JSON response that reports the on-disk storage used by each Neptune internal component: the dictionaries, undo logs, change streams, DFE statistics, property graph schema, other internal metadata tables, and each quad index. Neptune reports quad index sizes per data model under `PG` (property graph) and `RDF`, and includes an index only when it contains data. Neptune omits the following top-level sections from the response when they are empty: `dictionaries.blobs`, `streams`, `dfeStatistics`, `schema`, and `internals`. 

 The following example shows the response for a property graph cluster. Because this cluster contains only property graph data, the `RDF` object does not appear in the response. 

```
{
  "totalStorageBytesUsed": 955367424,
  "dictionaries": {
    "total": { "sizeInBytes": 259080192, "count": 653990 },
    "blobs": { "sizeInBytes":  54657024, "count":  22323 }
  },
  "undoLogs":      { "sizeInBytes": 150994944, "listSize": 2290 },
  "streams":       { "sizeInBytes":  77594624, "count": 1238185 },
  "dfeStatistics": { "sizeInBytes":    229376, "count":     813 },
  "schema":        { "sizeInBytes":     65536, "count":     154 },
  "internals":     { "sizeInBytes":    753664, "count":     202 },
  "quads": {
    "PG": {
      "SPOG":  { "sizeInBytes": 177995776, "count": 1222436 },
      "POGS":  { "sizeInBytes":  96534528, "count": 1222436 },
      "GPSO":  { "sizeInBytes":  79036416, "count": 1222436 },
      "OSGP":  { "sizeInBytes": 104071168, "count": 1222436 },
      "PZSOG": { "sizeInBytes":   9011200, "count":   61149 }
    }
  }
}
```

The response contains the following fields:


| Section | Field | Description | 
| --- | --- | --- | 
| (top-level) | totalStorageBytesUsed | Total on-disk storage used by Neptune. This is the sum of the sizeInBytes values of dictionaries.total, undoLogs, streams, dfeStatistics, schema, internals, and every quad index. dictionaries.blobs is already included in dictionaries.total, so it is not added again. The total also includes components that are omitted from the response because they are empty, so it can be slightly larger than the sum of the values shown. | 
| dictionaries.total | count / sizeInBytes | Approximate number of distinct dictionary entries and their total storage size. Neptune persists unique dictionary entries indefinitely, so this count might not reflect the number of entries currently referenced by your data. | 
| dictionaries.blobs | count / sizeInBytes | Approximate number of dictionary entries stored as blobs (values too large to inline) and their storage size. These entries are a subset of dictionaries.total. Omitted when no blob entries exist. | 
| undoLogs | sizeInBytes | Storage allocated for the Neptune transactional system to track modifications. This value reflects the current on-disk size of the undo tablespace, which grows over time and does not shrink automatically. | 
| undoLogs | listSize | Current number of uncommitted undo records not yet purged. This value mirrors the [`UndoLogListSize` CloudWatch metric](cw-metrics.md#cw-metrics-UndoLogListSize). Because Neptune purges undo entries asynchronously in the background, this value can fluctuate rapidly under active write workloads. | 
| streams | count / sizeInBytes | Approximate number of records in the Neptune change-log stream and their storage size. For more information, see [Capturing graph changes in real time using Neptune streams](streams.md). Omitted when Neptune streams are not enabled or the stream is empty. | 
| dfeStatistics | count / sizeInBytes | Approximate number of rows in the DFE statistics tables and their storage size. For more information, see [Managing statistics for the Neptune DFE to use](neptune-dfe-statistics.md). Omitted when no statistics have been computed. | 
| schema | count / sizeInBytes | Approximate number of rows in the property graph schema tables (label, property-key, and edge metadata) and their storage size. Omitted when the cluster contains no property graph data. | 
| internals | count / sizeInBytes | Approximate number of rows in other Neptune internal metadata tables and their storage size. Omitted when empty. | 
| quads.PG.\* | count / sizeInBytes | Entry count and storage size for each property graph index (Gremlin and openCypher): [SPOG](feature-overview-storage-indexing.md), [POGS](feature-overview-storage-indexing.md), [GPSO](feature-overview-storage-indexing.md), [OSGP](feature-overview-storage-indexing.md), and [PZSOG](feature-overview-storage-indexing.md). | 
| quads.RDF.\* | count / sizeInBytes | Entry count and storage size for each RDF index (SPARQL): SPOG, POGS, GPSO, OSGP, and PZSOG. | 

Note the following about the response:
+ Neptune omits any top-level section or per-index entry whose `count` is `0`. An absent entry means that the component holds no data. Both the `PG` and `RDF` objects can appear if your cluster has data in both data models.
+ The `OSGP` index is optional. For more information about Neptune storage, see [Neptune storage](feature-overview-storage.md).
+ The `PZSOG` index is absent unless it is populated on your cluster. Starting with engine release [1.4.7.0](https://docs.aws.amazon.com/releases/release-1.4.7.0.xml), the `PZSOG` index is enabled by default for all customers.

**Interpreting the values**  
The `sizeInBytes` values reflect the on-disk allocation for each component at the time of the response. The `count` values are approximations. Neptune derives them from InnoDB row-count statistics, which Neptune refreshes periodically. These statistics can drift from true values, particularly after large ingestion or deletion workloads. For the `SPOG`, `POGS`, `GPSO`, and `OSGP` quad indexes, `count` is a uniform approximation across those four indexes; the `PZSOG` index reports its own count. For details on how Neptune refreshes these statistics, see [Managing statistics for the Neptune DFE to use](neptune-dfe-statistics.md). Use `GetStorageInfo` to understand the relative distribution of storage across your indexes and dictionaries, and use `VolumeBytesUsed` for billing and capacity planning.

**Counting graph elements**  
If you need counts of the vertices, edges, or other elements in your graph, use the graph summary API instead of `GetStorageInfo`. The graph summary API reports node, edge, and property counts for property graphs, or quad, subject, and predicate counts for RDF graphs. You can manually trigger a statistics update right before calling it to get the freshest values possible. For more information, see [Getting a quick summary report about your graph](neptune-graph-summary.md).

**GetStorageInfo vs VolumeBytesUsed**  
 The sizes reported by `GetStorageInfo` are not expected to add up to the CloudWatch `VolumeBytesUsed` metric. `GetStorageInfo` reports the logical storage consumed by specific Neptune components, whereas `VolumeBytesUsed` reflects the total physical storage billed at the volume level. The volume also contains internal overhead that is not attributed to any component in the `GetStorageInfo` response, including:   
Block-level allocation
System metadata
Transaction and redo logs
Temporary space for ongoing operations
Space that has been allocated but not yet reclaimed
Use `GetStorageInfo` to understand the relative distribution of storage across your indexes and dictionaries, and use `VolumeBytesUsed` for billing and capacity planning.

## Errors
<a name="storage-info-errors"></a>

The following table lists the errors that `GetStorageInfo` can return.


| HTTP status | Error code | Description | 
| --- | --- | --- | 
| 403 | AccessDeniedException | The request does not have the required IAM permission. | 
| 404 | ResourceNotFoundException | The specified database was not found. | 
| 429 | ThrottlingException | The request was denied due to request throttling. | 
| 500 | InternalServerException | An internal service error occurred. | 