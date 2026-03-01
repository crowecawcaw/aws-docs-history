# Metrics and events for Memcached caches and clusters

This section describes the metrics and events that you can monitor when working with Memcached node-based and serverless caches.

###### Topics

- [Metrics for ElastiCache Serverless for Memcached](#serverless-metrics-memcached "#serverless-metrics-memcached")
- [Events for ElastiCache Serverless for Memcached](#serverless-events.memcached "#serverless-events.memcached")
- [Metrics for node-based Memcached clusters](#node-based-metrics-memcached "#node-based-metrics-memcached")
- [Events for node-based Memcached clusters](#node-based-events-memcached "#node-based-events-memcached")

## Metrics for ElastiCache Serverless for Memcached

This section describes the metrics and events that you can monitor when working with ElastiCache Serverless for Memcached.

The `AWS/ElastiCache` namespace includes the following CloudWatch metrics for your Memcached serverless caches.

| Metric                        | Description                                                                                                                   | Unit         |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------ |
| BytesUsedForCache             | The total number of bytes used by the data stored in your cache.                                                              | Bytes        |
| ElastiCacheProcessingUnits    | The total number of ElastiCacheProcessingUnits (ECPUs) consumed by the requests executed on your cache                        | Count        |
| SuccessfulReadRequestLatency  | Latency of successful read requests.                                                                                          | Microseconds |
| SuccessfulWriteRequestLatency | Latency of successful write requests                                                                                          | Microseconds |
| TotalCmdsCount                | Total count of all commands executed on your cache                                                                            | Count        |
| CurrConnections               | The number of client connections to your cache.                                                                               | Count        |
| ThrottledCmds                 | The number of requests that were throttled by ElastiCache because the workload was scaling faster than ElastiCache can scale. | Count        |
| NewConnections                | The total number of connections that have been accepted by the server during this period.                                     | Count        |
| CurrItems                     | The number of items in the cache.                                                                                             | Count        |
| NetworkBytesIn                | Total bytes transferred in to cache                                                                                           | Bytes        |
| NetworkBytesOut               | Total bytes transferred out of cache                                                                                          | Bytes        |
| Evictions                     | The count of keys evicted by the cache                                                                                        | Count        |
| Reclaimed                     | The number of keys expired by the cache                                                                                       | Count        |

**Command level metrics**

ElastiCache also emits the following Memcached command level metrics

| Metric       | Description                                                                                                    | Unit  |
| ------------ | -------------------------------------------------------------------------------------------------------------- | ----- |
| CmdGet       | The number of get commands the cache has received.                                                             | Count |
| CmdSet       | The number of set commands the cache has received.                                                             | Count |
| CmdTouch     | The number of touch commands the cache has received.                                                           | Count |
| GetHits      | The number of get requests the cache has received where the key requested was found.                           | Count |
| GetMisses    | The number of get requests the cache has received where the key requested was not found.                       | Count |
| IncrHits     | The number of increment requests the cache has received where the key requested was found.                     | Count |
| IncrMisses   | The number of increment requests the cache has received where the key requested was not found.                 | Count |
| DecrHits     | The number of decrement requests the cache has received where the requested key was found.                     | Count |
| DecrMisses   | The number of decrement requests the cache has received where the requested key was not found.                 | Count |
| DeleteHits   | The number of delete requests the cache has received where the requested key was found.                        | Count |
| DeleteMisses | The number of delete requests the cache has received where the requested key was not found.                    | Count |
| TouchHits    | The number of keys that have been touched and were given a new expiration time.                                | Count |
| TouchMisses  | The number of keys that have been touched, but were not found.                                                 | Count |
| CasHits      | The number of cas requests the cache has received where the requested key was found and the cas value matched. | Count |
| CasMisses    | The number of cas requests the cache has received where the key requested was not found.                       | Count |
| CasBadval    | The number of cas requests the cache has received where the cas value did not match the cas value stored.      | Count |
| CmdFlush     | The number of flush commands the cache has received.                                                           | Count |

## Events for ElastiCache Serverless for Memcached

ElastiCache logs events that relate to your serverless cache. This information includes the date and time of the event,
the source name and source type of the event, and a description of the event. You can easily retrieve events from the log
using the ElastiCache console, the AWS CLI describe-events command, or the ElastiCache API action `DescribeEvents`.

You can choose to monitor, ingest, transform, and act on ElastiCache events using Amazon EventBridge. Learn more in the
Amazon EventBridge [getting started guide](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md").

**Viewing ElastiCache events (Console)**

To view events using the ElastiCache console:

1. Sign in to the AWS Management Console and open the ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/")
2. To see a list of all available events, in the navigation pane, choose **Events**.
3. On the _Events_ screen each row of the list represents one event and displays the event source, the event type, the GMT time of the event,
   and a description of the event. Using the **Filter** you can specify whether you want to see all events, or just events of a specific type
   in the event list.

**Viewing ElastiCache events (AWS CLI)**

To generate a list of ElastiCache events using the AWS CLI, use the command describe-events. You can use optional parameters to
control the type of events listed, the time frame of the events listed, the maximum number of events to list, and more.

The following code lists up to 40 serverless cache events.

```
aws elasticache describe-events --source-type serverless-cache --max-items 40
```

The following code lists all events for serverless caches for the past 24 hours (1440 minutes).

```
aws elasticache describe-events --source-type serverless-cache --duration 1440
```

**Serverless Events**

This section documents the different types of events that you may receive for your serverless caches.

**Serverless Cache Creation Events**

| Detail-Type           | Description | Unit     | Source           | Message                                                                                     |
| --------------------- | ----------- | -------- | ---------------- | ------------------------------------------------------------------------------------------- |
| Cache created         | Cache arn   | creation | serverless-cache | Cache <cache-name> is created and ready to use.                                             |
| Cache creation failed | Cache arn   | failure  | serverless-cache | Failed to create cache <cache-name>. Insufficient free IP addresses to create VPC endpoint. |
| Cache creation failed | Cache arn   | failure  | serverless-cache | Failed to create cache <cache-name>. Invalid subnets provided in the request.               |
| Cache creation failed | Cache arn   | failure  | serverless-cache | Failed to create cache <cache-name>. Quota limit reached for creating VPC endpoint.         |
| Cache creation failed | Cache arn   | failure  | serverless-cache | Failed to create cache <cache-name>. You do not have permissions to create a VPC endpoint.  |

**Serverless Cache Update Events (Memcached)**

| Detail-Type          | Resources list | Category             | Source           | Message                                                                                                          |
| -------------------- | -------------- | -------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------- |
| Cache updated        | Cache arn      | configuration change | serverless-cache | SecurityGroups updated for the cache <cache-name>.                                                               |
| Cache updated        | Cache arn      | configuration change | serverless-cache | Tags updated for the cache <cache-name>.                                                                         |
| Cache updated failed | Cache arn      | configuration change | serverless-cache | An update to the cache <cache-name> failed. SecurityGroups update failed.                                        |
| Cache updated failed | Cache arn      | configuration change | serverless-cache | An update to the cache <cache-name> failed. SecurityGroups update failed because of insufficient permissions.    |
| Cache updated failed | Cache arn      | configuration change | serverless-cache | An update to the cache <cache-name> failed. SecurityGroups update failed because the SecurityGroups are invalid. |

**Serverless Cache Deletion Events (Memcached)**

| Detail-Type   | Resources list | Category | Source           | Message                         |
| ------------- | -------------- | -------- | ---------------- | ------------------------------- |
| Cache deleted | Cache arn      | deletion | serverless-cache | Cache <cache-name> was deleted. |

**Serverless Cache Usage Limit Events (Memcached)**

| Detail-Type          | Description | Unit                 | Source           | Message                                                                        |
| -------------------- | ----------- | -------------------- | ---------------- | ------------------------------------------------------------------------------ |
| Cache updated        | Cache arn   | configuration change | serverless-cache | Limits updated for the cache <cache-name>.                                     |
| Cache updated failed | Cache arn   | failure              | serverless-cache | A limit update to the cache <cache-name> failed because the cache was deleted. |
| Cache updated failed | Cache arn   | failure              | serverless-cache | A limit update to the cache <cache-name> failed due to invalid configuration.  |

**Serverless Cache Snapshot Events (Memcached)**

| Detail-Type              | Resources-list                   | Category | Source                    | Message                                                                                                                                                                                                                                                                                                      |
| ------------------------ | -------------------------------- | -------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Snapshot created         | Cache arn<br>Snapshot arn        | creation | serverless-cache-snapshot | Snapshot <snapshot-name> created for cache <cache-name>.                                                                                                                                                                                                                                                     |
| Snapshot creation failed | Cache arn<br>Snapshot arn        | failure  | serverless-cache-snapshot | Failed to create snapshot for cache <cache-name>.<br>Snapshot <snapshot-name> creation failed with Customer Managed Key <key-id><br><reason>.<br>Failure reason messages:<br>• because Customer Managed Key is disabled<br>• because Customer Managed Key cannot be found<br>• because the request timed out |
| Snapshot creation failed | Cache arn<br>Snapshot arn        | failure  | serverless-cache-snapshot | Failed to create snapshot for cache <cache-name>.<br>Snapshot <snapshot-name> creation failed because <reason>.<br>Default reason:<br>• because of an internal error                                                                                                                                         |
| Snapshot export failed   | Snapshot arn                     | failure  | serverless-cache-snapshot | Failed to export snapshot for cache <cache-name>.<br>Could not export snapshot to bucket %s because ElastiCache does not have permissions to the bucket.                                                                                                                                                     |
| Snapshot export failed   | Snapshot arn                     | failure  | serverless-cache-snapshot | Failed to export snapshot for cache <cache-name>.<br>Could not export snapshot to bucket '%s' because there is already an object with the same name in the bucket.                                                                                                                                           |
| Snapshot export failed   | Snapshot arn                     | failure  | serverless-cache-snapshot | Failed to export snapshot for cache <cache-name>.<br>Could not export snapshot to bucket '%s' because bucket owner account Id has changed.                                                                                                                                                                   |
| Snapshot export failed   | Snapshot arn                     | failure  | serverless-cache-snapshot | Failed to export snapshot for cache <cache-name>.<br>Could not export snapshot to bucket '%s' because the S3 bucket is not accessible.                                                                                                                                                                       |
| Snapshot export failed   | Snapshot arn                     | failure  | serverless-cache-snapshot | Failed to export snapshot for cache <cache-name>.<br>Could not export snapshot to bucket '%s' because the bucket is not accessible.                                                                                                                                                                          |
| Snapshot export failed   | Snapshot arn                     | failure  | serverless-cache-snapshot | Failed to export snapshot for cache <cache-name>.<br>Could not export snapshot to bucket '%s' because bucket does not exist.                                                                                                                                                                                 |
| Snapshot export failed   | Snapshot arn                     | failure  | serverless-cache-snapshot | Failed to export snapshot for cache <cache-name>.<br>Could not export snapshot to bucket '%s' with source snapshot Customer Managed Key %s <reason>.                                                                                                                                                         |
| Snapshot export failed   | Snapshot arn                     | failure  | serverless-cache-snapshot | Failed to export snapshot for cache <cache-name>.<br>Could not export snapshot to bucket '%s'.                                                                                                                                                                                                               |
| Snapshot copy failed     | Snapshot arn-1<br>Snapshot arn-2 | failure  | serverless-cache-snapshot | Failed to copy snapshot <snapshot-name>.<br>Could not copy snapshot '%s' to snapshot '%s' with source snapshot Customer Managed Key <key-id> <reason-name>.                                                                                                                                                  |
| Snapshot copy failed     | Snapshot arn-1<br>Snapshot arn-2 | failure  | serverless-cache-snapshot | Failed to copy snapshot <snapshot-name>. Could not copy<br>snapshot '%s' to snapshot '%s' with target snapshot Customer<br>Managed Key '%s' '%s'.                                                                                                                                                            |

## Metrics for node-based Memcached clusters

This section describes the CloudWatch metrics that you can monitor when working with node-based Memcached clusters. These metrics are measured per cache node in 60-second intervals.

**Host-level metrics**

| Metric              | Description                                                                                                                                                                                                                                                | Unit    |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `CPUUtilization`    | Percentage of CPU utilization for the entire host. Because Memcached is multi-threaded, this metric can be as high as 90%. If you exceed this threshold, scale your cluster up by using a larger cache node type, or scale out by adding more cache nodes. | Percent |
| `FreeableMemory`    | Amount of free memory available on the host, derived from RAM, buffers, and cache that the OS reports as freeable.                                                                                                                                         | Bytes   |
| `NetworkBytesIn`    | Number of bytes the host has read from the network.                                                                                                                                                                                                        | Bytes   |
| `NetworkBytesOut`   | Number of bytes sent out on all network interfaces by the instance.                                                                                                                                                                                        | Bytes   |
| `NetworkPacketsIn`  | Number of packets received on all network interfaces by the instance.                                                                                                                                                                                      | Count   |
| `NetworkPacketsOut` | Number of packets sent out on all network interfaces by the instance.                                                                                                                                                                                      | Count   |
| `SwapUsage`         | Amount of swap used on the host.                                                                                                                                                                                                                           | Bytes   |

**Memcached metrics**

| Metric                         | Description                                                               | Unit  |
| ------------------------------ | ------------------------------------------------------------------------- | ----- |
| `BytesReadIntoMemcached`       | Number of bytes read from the network by the cache node.                  | Bytes |
| `BytesUsedForCacheItems`       | Number of bytes used to store cache items.                                | Bytes |
| `BytesWrittenOutFromMemcached` | Number of bytes written to the network by the cache node.                 | Bytes |
| `CasBadval`                    | Number of CAS requests where the Cas value did not match.                 | Count |
| `CasHits`                      | Number of Cas requests where the key was found and the Cas value matched. | Count |
| `CasMisses`                    | Number of Cas requests where the key was not found.                       | Count |
| `CmdFlush`                     | Number of flush commands received.                                        | Count |
| `CmdGet`                       | Number of get commands received.                                          | Count |
| `CmdSet`                       | Number of set commands received.                                          | Count |
| `CurrConnections`              | Number of connections connected to the cache at an instant in time.       | Count |
| `CurrItems`                    | Number of items currently stored in the cache.                            | Count |
| `DecrHits`                     | Number of decrement requests where the key was found.                     | Count |
| `DecrMisses`                   | Number of decrement requests where the key was not found.                 | Count |
| `DeleteHits`                   | Number of delete requests where the key was found.                        | Count |
| `DeleteMisses`                 | Number of delete requests where the key was not found.                    | Count |
| `Evictions`                    | Number of non-expired items evicted to allow space for new writes.        | Count |
| `GetHits`                      | Number of get requests where the key was found.                           | Count |
| `GetMisses`                    | Number of get requests where the key was not found.                       | Count |
| `IncrHits`                     | Number of increment requests where the key was found.                     | Count |
| `IncrMisses`                   | Number of increment requests where the key was not found.                 | Count |
| `NewConnections`               | Number of new connections the cache has received.                         | Count |
| `NewItems`                     | Number of new items the cache has stored.                                 | Count |
| `Reclaimed`                    | Number of expired items evicted to allow space for new writes.            | Count |
| `UnusedMemory`                 | Amount of memory not used by data.                                        | Bytes |

## Events for node-based Memcached clusters

ElastiCache sends notifications for significant cluster events using Amazon Simple Notification Service. You can monitor events using the ElastiCache console, the AWS CLI `describe-events` command, or the ElastiCache API `DescribeEvents` action.

To view events using the AWS CLI, use the `--source-type cache-cluster` parameter.

The following examples show how to use the AWS CLI to list cache cluster events:

List up to 40 cache cluster events:

```
aws elasticache describe-events --source-type cache-cluster --max-items 40
```

List cache cluster events for the past 24 hours:

```
aws elasticache describe-events --source-type cache-cluster --duration 1440
```

For more information about managing Amazon SNS notifications for events, see the Amazon SNS event monitoring topic.
