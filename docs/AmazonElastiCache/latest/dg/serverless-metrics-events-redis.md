# Metrics and events for Valkey and Redis OSS serverless caches

ElastiCache offers a wide variety of metrics and events for monitoring when working with serverless caches.
This includes CloudWatch metrics, command level metrics, and event logs which can be ingested via Amazon EventBridge.

###### Topics

- [Serverless cache metrics](#serverless-metrics "#serverless-metrics")
- [Serverless cache events](#serverless-events "#serverless-events")

## Serverless cache metrics

The `AWS/ElastiCache` namespace includes the following CloudWatch metrics for your Valkey or Redis OSS serverless caches.

_Metric codes for Valkey or Redis OSS_

| Metric                        | Description                                                                                                                                                                                                | Unit         |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| BytesUsedForCache             | The total number of bytes used by the data stored in your cache.                                                                                                                                           | Bytes        |
| ElastiCacheProcessingUnits    | The total number of ElastiCacheProcessingUnits (ECPUs) consumed by the requests executed on your cache                                                                                                     | Count        |
| SuccessfulReadRequestLatency  | Latency of successful read requests.                                                                                                                                                                       | Microseconds |
| SuccessfulWriteRequestLatency | Latency of successful write requests                                                                                                                                                                       | Microseconds |
| TotalCmdsCount                | Total count of all commands executed on your cache                                                                                                                                                         | Count        |
| CacheHitRate                  | Indicates the hit rate of your cache. This is calculated<br>using `cache_hits` and `cache_misses` statistics in the following way:<br>`cache_hits /(cache_hits + cache_misses)`.                           | Percent      |
| CacheHits                     | The number of successful read-only key lookups in the cache.                                                                                                                                               | Count        |
| CurrConnections               | The number of client connections to your cache.                                                                                                                                                            | Count        |
| ThrottledCmds                 | The number of requests that were throttled by ElastiCache because the workload was scaling faster than ElastiCache can scale.                                                                              | Count        |
| NewConnections                | The total number of connections that have been accepted by the server during this period.                                                                                                                  | Count        |
| CurrItems                     | The number of items in the cache.                                                                                                                                                                          | Count        |
| CurrVolatileItems             | The number of items in the cache with TTL.                                                                                                                                                                 | Count        |
| NetworkBytesIn                | Total bytes transferred in to cache                                                                                                                                                                        | Bytes        |
| NetworkBytesOut               | Total bytes transferred out of cache                                                                                                                                                                       | Bytes        |
| Evictions                     | The count of keys evicted by the cache                                                                                                                                                                     | Count        |
| IamAuthenticationExpirations  | The total number of expired IAM-authenticated Valkey or Redis OSS connections.<br>You can find more information about [Authenticating with IAM](auth-iam.md "auth-iam.md") in the user guide.              | Count        |
| IamAuthenticationThrottling   | The total number of throttled IAM-authenticated Valkey or Redis OSS AUTH or HELLO requests.<br>You can find more information about [Authenticating with IAM](auth-iam.md "auth-iam.md") in the user guide. | Count        |
| KeyAuthorizationFailures      | The total number of failed attempts by users to access keys they don’t have permission to access.<br>We suggest setting an alarm on this to detect unauthorized access attempts.                           | Count        |
| AuthenticationFailures        | The total number of failed attempts to authenticate to Valkey or Redis OSS using the AUTH command.<br>We suggest setting an alarm on this to detect unauthorized access attempts.                          | Count        |
| CommandAuthorizationFailures  | The total number of failed attempts by users to run commands they don’t have permission to call.<br>We suggest setting an alarm on this to detect unauthorized access attempts.                            | Count        |

**Command level metrics**

ElastiCache also emits the following command level metrics. For each command type, ElastiCache emits the total count of commands and the number of ECPUs consumed by that command type.

| Metric                    | Description                                                                                                                                                                                                                                                                                           | Unit  |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| EvalBasedCmds             | The number of get commands the cache has received.                                                                                                                                                                                                                                                    | Count |
| EvalBasedCmdsECPUs        | ECPUs consumed by eval-based commands.                                                                                                                                                                                                                                                                | Count |
| GeoSpatialBasedCmds       | The total number of commands for geospatial-based commands.<br>This is derived from the Valkey or Redis OSS commandstats statistic.<br>It's derived by summing all of the geo type of commands:<br>geoadd, geodist, geohash, geopos, georadius, and georadiusbymember.                                | Count |
| GeoSpatialBasedCmdsECPUs  | ECPUs consumed by geospatial-based commands.                                                                                                                                                                                                                                                          | Count |
| GetTypeCmds               | The total number of read-only type commands. This is derived from the Valkey or Redis OSS commandstats statistic by summing all of the read-only type commands (get, hget, scard, lrange, and so on.)                                                                                                 | Count |
| GetTypeCmdsECPUs          | ECPUs consumed by read commands.                                                                                                                                                                                                                                                                      | Count |
| HashBasedCmds             | The total number of commands that are hash-based. This is derived from the Valkey or Redis OSS commandstats statistic by summing all of the commands that act upon one or more hashes (hget, hkeys, hvals, hdel, and so on).                                                                          | Count |
| HashBasedCmdsECPUs        | ECPUs consumed by hash-based commands.                                                                                                                                                                                                                                                                | Count |
| HyperLogLogBasedCmds      | The total number of HyperLogLog-based commands. This is derived from the Valkey or Redis OSS commandstats statistic by summing all of the pf type of commands (pfadd, pfcount, pfmerge, and so on.).                                                                                                  | Count |
| HyperLogLogBasedCmdsECPUs | ECPUs consumed by HyperLogLog-based commands.                                                                                                                                                                                                                                                         | Count |
| JsonBasedCmds             | The total number of JSON commands, including both read and write commands. This is derived from the Valkey or Redis OSS commandstats statistic by summing all JSON commands that act upon JSON keys.                                                                                                  | Count |
| JsonBasedCmdsECPUs        | ECPUs consumed by all JSON commands, including both read and write commands.                                                                                                                                                                                                                          | Count |
| JsonBasedGetCmds          | The total number of JSON read-only commands. This is derived from the Valkey or Redis OSS commandstats statistic by summing all JSON read commands that act upon JSON keys.                                                                                                                           | Count |
| JsonBasedGetCmdsECPUs     | ECPUs consumed by JSON read-only commands.                                                                                                                                                                                                                                                            | Count |
| JsonBasedSetCmds          | The total number of JSON write commands. This is derived from the Valkey or Redis OSS commandstats statistic by summing all JSON write commands that act upon JSON keys.                                                                                                                              | Count |
| JsonBasedSetCmdsECPUs     | ECPUs consumed by JSON write commands.                                                                                                                                                                                                                                                                | Count |
| KeyBasedCmds              | The total number of commands that are key-based. This is derived from the Valkey or Redis OSS commandstats statistic by summing all of the commands that act upon one or more keys across multiple data structures (del, expire, rename, and so on.).                                                 | Count |
| KeyBasedCmdsECPUs         | ECPUs consumed by key-based commands.                                                                                                                                                                                                                                                                 | Count |
| ListBasedCmds             | The total number of commands that are list-based. This is derived from the Valkey or Redis OSS commandstats statistic by summing all of the commands that act upon one or more lists (lindex, lrange, lpush, ltrim, and so on).                                                                       | Count |
| ListBasedCmdsECPUs        | ECPUs consumed by list-based commands.                                                                                                                                                                                                                                                                | Count |
| NonKeyTypeCmds            | The total number of commands that are not key-based. This is derived from the Valkey or Redis OSS commandstats statistic by summing all of the commands that do not act upon a key, for example, acl, dbsize or info.                                                                                 | Count |
| NonKeyTypeCmdsECPUs       | ECPUs consumed by non-key-based commands.                                                                                                                                                                                                                                                             | Count |
| PubSubBasedCmds           | The total number of commands for pub/sub functionality. This is derived from the Valkey or Redis OSS commandstatsstatistics by summing all of the commands used for pub/sub functionality: psubscribe, publish, pubsub, punsubscribe, ssubscribe, sunsubscribe, spublish, subscribe, and unsubscribe. | Count |
| PubSubBasedCmdsECPUs      | ECPUs consumed by pub/sub-based commands.                                                                                                                                                                                                                                                             | Count |
| SetBasedCmds              | The total number of commands that are set-based. This is derived from the Valkey or Redis OSS commandstats statistic by summing all of the commands that act upon one or more sets (scard, sdiff, sadd, sunion, and so on).                                                                           | Count |
| SetBasedCmdsECPUs         | ECPUs consumed by set-based commands.                                                                                                                                                                                                                                                                 | Count |
| SetTypeCmds               | The total number of write types of commands. This is derived from the Valkey or Redis OSS commandstats statistic by summing all of the mutative types of commands that operate on data (set, hset, sadd, lpop, and so on.)                                                                            | Count |
| SetTypeCmdsECPUs          | ECPUs consumed by write commands.                                                                                                                                                                                                                                                                     | Count |
| SortedSetBasedCmds        | The total number of commands that are sorted set-based. This is derived from the Valkey or Redis OSS commandstats statistic by summing all of the commands that act upon one or more sorted sets (zcount, zrange, zrank, zadd, and so on).                                                            | Count |
| SortedSetBasedCmdsECPUs   | ECPUs consumed by sorted-based commands.                                                                                                                                                                                                                                                              | Count |
| StringBasedCmds           | The total number of commands that are string-based. This is derived from the Valkey or Redis OSS commandstats statistic by summing all of the commands that act upon one or more strings (strlen, setex, setrange, and so on).                                                                        | Count |
| StringBasedCmdsECPUs      | ECPUs consumed by string-based commands.                                                                                                                                                                                                                                                              | Count |
| StreamBasedCmds           | The total number of commands that are stream-based. This is derived from the Valkey or Redis OSS commandstats statistic by summing all of the commands that act upon one or more streams data types (xrange, xlen, xadd, xdel, and so on).                                                            | Count |
| StreamBasedCmdsECPUs      | ECPUs consumed by stream-based commands.                                                                                                                                                                                                                                                              | Count |

## Serverless cache events

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

| Detail-Type           | Description                     | Unit     | Source           | Message                                                                                                                                                                                                                                                       |
| --------------------- | ------------------------------- | -------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cache created         | Cache arn                       | creation | serverless-cache | Cache <cache-name> is created and ready to use.                                                                                                                                                                                                               |
| Cache created         | Cache arn<br>Snapshot arn       | creation | serverless-cache | Cache <cache-name> is created and data was restored from snapshot. Your cache is ready to use.                                                                                                                                                                |
| Cache creation failed | Cache arn                       | failure  | serverless-cache | Failed to create cache <cache-name>. Insufficient free IP addresses to create VPC endpoint.                                                                                                                                                                   |
| Cache creation failed | Cache arn                       | failure  | serverless-cache | Failed to create cache <cache-name>. Invalid subnets provided in the request.                                                                                                                                                                                 |
| Cache creation failed | Cache arn                       | failure  | serverless-cache | Failed to create cache <cache-name>. Quota limit reached for creating VPC endpoint.                                                                                                                                                                           |
| Cache creation failed | Cache arn                       | failure  | serverless-cache | Failed to create cache <cache-name>. You do not have permissions to create a VPC endpoint.                                                                                                                                                                    |
| Cache creation failed | Cache arn                       | failure  | serverless-cache | Failed to create cache <cache-name>.<br>A user with an incompatible Valkey or Redis OSS version is present in user group <user-group-name>.                                                                                                                   |
| Cache creation failed | Cache arn<br>Cache snapshot arn | failure  | serverless-cache | Failed to create cache <cache-name>.<br>The provided user group <user-group-name> does not exist.                                                                                                                                                             |
| Cache creation failed | Cache arn                       | failure  | serverless-cache | Failed to create cache <cache-name>.<br>Data restoration from snapshot failed because <reason>.<br>Failure reasons:<br>• failed to retrieve file from S3.<br>• expected md5 does not match actual md5.<br>• the provided RDB file has an unsupported version. |

**Serverless Cache Update Events (Valkey or Redis OSS)**

| Detail-Type          | Resources list | Category             | Source           | Message                                                                                                                                            |
| -------------------- | -------------- | -------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cache updated        | Cache arn      | configuration change | serverless-cache | SecurityGroups updated for the cache <cache-name>.                                                                                                 |
| Cache updated        | Cache arn      | configuration change | serverless-cache | Tags updated for the cache <cache-name>.                                                                                                           |
| Cache updated failed | Cache arn      | configuration change | serverless-cache | An update to the cache <cache-name> failed.<br>A user with an incompatible Valkey or Redis OSS version is present in user group <user-group-name>. |
| Cache updated failed | Cache arn      | configuration change | serverless-cache | An update to the cache <cache-name> failed. SecurityGroups update failed.                                                                          |
| Cache updated failed | Cache arn      | configuration change | serverless-cache | An update to the cache <cache-name> failed. SecurityGroups update failed because of insufficient permissions.                                      |
| Cache updated failed | Cache arn      | configuration change | serverless-cache | An update to the cache <cache-name> failed.<br>SecurityGroups update failed because the SecurityGroups are invalid.                                |

**Serverless Cache Deletion Events (Valkey or Redis OSS)**

| Detail-Type   | Resources list | Category | Source           | Message                         |
| ------------- | -------------- | -------- | ---------------- | ------------------------------- |
| Cache deleted | Cache arn      | deletion | serverless-cache | Cache <cache-name> was deleted. |

**Serverless Cache Usage Limit Events (Valkey or Redis OSS)**

| Detail-Type             | Description | Unit                 | Source           | Message                                                                                                                                                  |
| ----------------------- | ----------- | -------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cache updated           | Cache arn   | configuration change | serverless-cache | Limits updated for the cache <cache-name>.                                                                                                               |
| Cache limit approaching | Cache arn   | notification         | serverless-cache | Slot <X> is using more than <Y>% of the per-slot limit of 32 GB.<br>For example, Slot 10 is using more than 90% of the per-slot limit of 32 GB.          |
| Cache updated failed    | Cache arn   | failure              | serverless-cache | A limit update to the cache <cache-name> failed because the cache was deleted.                                                                           |
| Cache updated failed    | Cache arn   | failure              | serverless-cache | A limit update to the cache <cache-name> failed due to invalid configuration.                                                                            |
| Cache updated failed    | Cache arn   | failure              | serverless-cache | A limit update to the cache <cache-name> failed because<br>current cached data exceeds new limits. Please flush some data<br>before applying the limits. |

**Serverless Cache Snapshot Events (Valkey or Redis OSS)**

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
