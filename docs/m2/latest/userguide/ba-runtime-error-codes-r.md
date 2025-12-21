AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Blu Age Runtime Redis Error Codes

Redis error codes, prefixed with `BA-R`.

## Redis Configuration Errors

| Key        | Severity | Text                                                                                                                                                | Additional details                                                                                                                  |
| ---------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `BA-R0001` | Fatal    | Missing Redis configuration for feature through specified path. Either specify the configuration at the given path or define global Redis settings. | [Available Redis cache properties<br>in AWS Blu Age Runtime](ba-runtime-redis-configuration.md "ba-runtime-redis-configuration.md") |
| `BA-R0002` | Fatal    | Missing Redis configuration parameter. Please add the required parameter.                                                                           |                                                                                                                                     |
| `BA-R0003` | Warn     | No explicite Redis configuration found for path. Gapwalk Redis configuration will be used for connection. You can ignore if intended.               |                                                                                                                                     |
| `BA-R0004` | Fatal    | Error retrieving Redis configuration variables from specified path. Check configuration file and environment settings.                              |                                                                                                                                     |
| `BA-R0005` | Fatal    | Missing Redis value for specied parameter. Check configuration file and environment settings.                                                       |                                                                                                                                     |

## Redis Property Validation Errors

| Key        | Severity | Text                                                                                                         | Additional details                                                                                                                  |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| `BA-R0020` | Error    | Redis Configuration Error: Invalid Redis configuration value for parameter.                                  |                                                                                                                                     |
| `BA-R0021` | Fatal    | Redis Configuration Error: Invalid Redis mode. Must be one of the two specified modes.                       |                                                                                                                                     |
| `BA-R0022` | Error    | Error setting property. Check property value format and constraints.                                         | [Available Redis cache properties<br>in AWS Blu Age Runtime](ba-runtime-redis-configuration.md "ba-runtime-redis-configuration.md") |
| `BA-R0023` | Error    | Property key or value is null for entry in properties map. Ensure all property keys and values are non-null. |                                                                                                                                     |
| `BA-R0024` | Error    | Unknown or unsupported Property key.                                                                         | [Available Redis cache properties<br>in AWS Blu Age Runtime](ba-runtime-redis-configuration.md "ba-runtime-redis-configuration.md") |
| `BA-R0025` | Error    | Invalid numeric value for property. Ensure the value can be converted to the required numeric type.          |                                                                                                                                     |

## Redis Connection Errors

| Key                        | Severity | Text                                                                                                                     | Additional details |
| -------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| `BA-R0081`                 | Fatal    | Failed to connect to Redis server<br>• Connection refused. Verify Redis server is running and the host/port are correct. |                    |
| `BA-R0082`                 | Fatal    | Connection timeout while connecting to Redis server. Check network connectivity or increase connection timeout.          |                    |
| `BA-R0083`                 | Fatal    | Read timeout while connecting to Redis server. Check Redis server performance or increase read timeout.                  |                    |
| `BA-R0084`                 | Fatal    | SSL error connecting to Redis. Verify SSL settings and certificates.                                                     |                    |
| `BA-R0085`                 | Fatal    | Failed to establish Redis connection. Check Redis server status and configuration.                                       |                    |
| `BA-R0086`                 | Fatal    | Authentication failed for Redis connection. Verify Redis authentication credentials.                                     |                    |
| `BA-R0087`                 | Fatal    | Redis data exception. Check Redis server logs for more details.                                                          |                    |
| `BA-R0088`<br>• `BA-R0089` | Fatal    | Unexpected error connecting to Redis. Review error message and Redis configuration.                                      |                    |
| `BA-R0090`                 | Fatal    | Failed to create Redis pool configuration. Review error message and Redis configuration.                                 |                    |

## Feature-specific Configuration Errors

| Key        | Severity | Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Additional details                                                                                                                  |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `BA-R0100` | Error    | Blusam Cache Configuration Error: Blusam cache is configured to use redis (`bluesam.cache : redis`)<br>the required hostName and port configuration missing are missing. Either specify the Redis configuration at path `bluesam.redis`<br>or define global Redis settings using the `gapwalk.redis`. If you don't want to use redis, either remove the `blusam.cache`<br>property for default or set it to a different value.                                                                          | [Available Redis cache properties<br>in AWS Blu Age Runtime](ba-runtime-redis-configuration.md "ba-runtime-redis-configuration.md") |
| `BA-R0200` | Error    | Blusam Locks Configuration Error: Blusam locks is configured to use redis (`bluesam.locks : redis`)<br>the required hostName and port configuration missing are missing. Either specify the Redis configuration at path `bluesam.locks`<br>or define global Redis settings using the `gapwalk.redis`. If you don't want to use redis, either remove the `blusam.locks`<br>property for default or set it to a different value.                                                                          | [Available Redis cache properties<br>in AWS Blu Age Runtime](ba-runtime-redis-configuration.md "ba-runtime-redis-configuration.md") |
| `BA-R0300` | Error    | Gapwalk File Locks Configuration Error: Gapwalk file locks is configured to use redis (`filesLocks.provider : redis`)<br>the required hostName and port configuration missing are missing. Either specify the Redis configuration at path `filesLocks.redis`<br>or define global Redis settings using the `gapwalk.redis`. If you don't want to use redis, either remove the<br>`filesLocks.provider` property for default or set it to a different value.                                              | [Available Redis cache properties<br>in AWS Blu Age Runtime](ba-runtime-redis-configuration.md "ba-runtime-redis-configuration.md") |
| `BA-R0400` | Error    | Dataset Catalog Configuration Error: Dataset catalog is configured to use redis (`datasimplifier.catalogImplementation : redis`)<br>the required hostName and port configuration missing are missing. Either specify the Redis configuration at path<br>`datasimplifier.redis` or define global Redis settings using the `gapwalk.redis`. If you don't want to use redis,<br>either remove the `datasimplifier.catalogImplementation` property for default or set it to a different value.              | [Available Redis cache properties<br>in AWS Blu Age Runtime](ba-runtime-redis-configuration.md "ba-runtime-redis-configuration.md") |
| `BA-R0500` | Error    | Session Cache Configuration Error: Session cache is configured to use redis (`spring.session.store-type : redis`)<br>the required hostName and port configuration missing are missing. Either specify the Redis configuration at path `jics.redis`<br>or define global Redis settings using the `gapwalk.redis`. If you don't want to use redis, either remove the<br>`spring.session.store-type` property for default or set it to a different value.                                                  | [Available Redis cache properties<br>in AWS Blu Age Runtime](ba-runtime-redis-configuration.md "ba-runtime-redis-configuration.md") |
| `BA-R0550` | Error    | Session Tracker Configuration Error: Session tracker is configured to use redis (`session-tracker.store-type : redis`)<br>the required hostName and port configuration missing are missing. Either specify the Redis configuration at path<br>`session-tracker.redis` or define global Redis settings using the `gapwalk.redis`. If you don't want to use redis,<br>either remove the `session-tracker.store-type` property for default or set it to a different value.                                 | [Available Redis cache properties<br>in AWS Blu Age Runtime](ba-runtime-redis-configuration.md "ba-runtime-redis-configuration.md") |
| `BA-R0600` | Error    | JICS Resource Definitions Configuration Error: JICS resource definitions is configured to use<br>redis (`jics.resource-definitions.store-type : redis`) the required hostName and port configuration<br>missing are missing. Either specify the Redis configuration at path `jics.redis` or define global<br>Redis settings using the `gapwalk.redis`. If you don't want to use redis, either remove<br>the `jics.resource-definitions.store-type` property for default or set it to a different value. | [Available Redis cache properties<br>in AWS Blu Age Runtime](ba-runtime-redis-configuration.md "ba-runtime-redis-configuration.md") |
| `BA-R0700` | Error    | JICS TS Queues Configuration Error: JICS TS queues is configured to use redis (`jics.parameters.tsqimpl : redis`)<br>the required hostName and port configuration missing are missing. Either specify the Redis configuration at path<br>`jics.queues.ts.redis` or define global Redis settings using the `gapwalk.redis`. If you don't want to<br>use redis, either remove the `jics.parameters.tsqimpl` property for default or set it to a different value.                                          | [Available Redis cache properties<br>in AWS Blu Age Runtime](ba-runtime-redis-configuration.md "ba-runtime-redis-configuration.md") |
| `BA-R0800` | Error    | JCL Checkpoint Configuration Error: JCL checkpoint is configured to use redis (`jcl.checkpoint.provider : redis`)<br>the required hostname and port configuration missing are missing. Either specify the Redis configuration at<br>path `jcl.redis` or define global Redis settings using the `gapwalk.redis`. If you don't want to use redis,<br>either remove the `jcl.checkpoint.provider` property for default or set it to a different value.                                                     | [Available Redis cache properties<br>in AWS Blu Age Runtime](ba-runtime-redis-configuration.md "ba-runtime-redis-configuration.md") |
| `BA-R0900` | Error    | Blu4iv Locks Configuration Error: Blu4iv locks is configured to use redis (`blu4iv.lock : redis`)<br>the required hostName and port configuration missing are missing. Either specify the Redis configuration<br>at path `blu4iv.lock.redis` or define global Redis settings using the `gapwalk.redis`.<br>If you don't want to use redis, either remove the `blu4iv.lock` property for default or set it to a different value.                                                                         | [Available Redis cache properties<br>in AWS Blu Age Runtime](ba-runtime-redis-configuration.md "ba-runtime-redis-configuration.md") |

## Blusam Redis Cache Errors

### Blusam Redis Cache Configuration & Connection Errors

| Key        | Severity | Text                                                                                                                                                                                           | Additional details |
| ---------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R1200` | Error    | Failed to initialize \*\*\*\*\*\*\<br>• Redis cache. Verify Redis connection and configuration parameters.                                                                                     |                    |
| `BA-R1201` | Error    | Failed to close Redis connection. Check Redis connection state and verify that a connection was previously established. This error may occur if attempting to close a non-existent connection. |                    |

### Cache Operations

| Key        | Severity | Text                                                                          | Additional details |
| ---------- | -------- | ----------------------------------------------------------------------------- | ------------------ |
| `BA-R1300` | Error    | Failed to get cache for name. Verify cache name and Redis connection.         |                    |
| `BA-R1301` | Error    | Failed to get cache indexes for name. Verify cache name and Redis connection. |                    |

### Metadata Management

| Key        | Severity | Text                                                                             | Additional details |
| ---------- | -------- | -------------------------------------------------------------------------------- | ------------------ |
| `BA-R1400` | Error    | Failed to retrieve metadata for cache. Check metadata key and Redis connection.  |                    |
| `BA-R1401` | Error    | Failed to store metadata for cache. Verify metadata object and Redis connection. |                    |
| `BA-R1402` | Error    | Failed to remove metadata for cache. Check cache name and Redis connection.      |                    |

### Cache Warm-up

| Key        | Severity | Text                                                                              | Additional details |
| ---------- | -------- | --------------------------------------------------------------------------------- | ------------------ |
| `BA-R1500` | Error    | Failed to check warm-up status for cache. Verify cache name and Redis connection. |                    |
| `BA-R1501` | Error    | Failed to mark cache as warmed up. Check cache name and Redis connection.         |                    |

### Publisher/Subscriber Operations

| Key        | Severity | Text                                                                                                                                                                                                           | Additional details |
| ---------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R1600` | Error    | Failed to create metadata update listener for cache. Check Redis pub/sub properties: subscriptionsPerConnection (default: 10), subscriptionConnectionPoolSize (default: 100), connectTimeout (default: 10000). |                    |
| `BA-R1601` | Error    | Failed to publish metadata update for cache. Check Redis pub/sub properties: connectTimeout (default: 10000), readTimeout (default: 2000).                                                                     |                    |
| `BA-R1602` | Error    | Failed to create cache invalidation listener for cache. Check Redis pub/sub properties and adjust based on invalidation load.                                                                                  |                    |
| `BA-R1603` | Error    | Failed to publish cache invalidation for cache. Consider increasing timeout values for large invalidation sets.                                                                                                |                    |

### Cache Record Operations

| Key        | Severity | Text                                                                                                | Additional details |
| ---------- | -------- | --------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R1710` | Error    | Failed to retrieve record from cache. Verify record exists and Redis connection is active.          |                    |
| `BA-R1711` | Error    | Failed to store record in cache. Check Redis connection and record data.                            |                    |
| `BA-R1712` | Error    | Failed to store multiple records in cache. Verify Redis connection and batch operation settings.    |                    |
| `BA-R1720` | Error    | Batch operation failed during paginated write. Check pageSizeInBytes and connectTimeout properties. |                    |
| `BA-R1721` | Error    | Failed to execute bulk operation. Verify Redis cluster status and connection settings.              |                    |
| `BA-R1730` | Error    | Failed to delete record from cache. Check record exists and Redis connection.                       |                    |
| `BA-R1731` | Error    | Batch delete operation partially failed. Verify Redis cluster status and record existence.          |                    |
| `BA-R1732` | Error    | Failed to clear cache. Check Redis connection and cache name.                                       |                    |

### Cache Index Operations

| Key        | Severity | Text                                                                                                                    | Additional details |
| ---------- | -------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R1801` | Error    | Failed to retrieve index from cache. Verify index exists and Redis connection is active.                                |                    |
| `BA-R1802` | Error    | Failed to store index in cache. Check Redis connection and index data integrity.                                        |                    |
| `BA-R1803` | Error    | Invalid key format encountered while processing index keys in cache. Check for data corruption or invalid key patterns. |                    |
| `BA-R1804` | Error    | Failed to retrieve index keys from cache. Verify Redis connection and cache name.                                       |                    |
| `BA-R1805` | Error    | Failed to delete index from cache. Check index exists and Redis connection.                                             |                    |
| `BA-R1811` | Warn     | Skipped processing of invalid index key. Verify key format and data integrity.                                          |                    |

### Cache Invalidation Operations

| Key        | Severity | Text                                                                                                               | Additional details |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| `BA-R1900` | Error    | Failed to initialize cache invalidation listener for dataset. Verify subscription parameters in configuration.     |                    |
| `BA-R1901` | Error    | Error processing cache invalidation message for dataset. Check consumer implementation and message format.         |                    |
| `BA-R1902` | Error    | Received invalid invalidation message for dataset. Verify message format and content.                              |                    |
| `BA-R1903` | Error    | Failed to maintain subscriber connection for dataset. Check Redis subscription parameters and connection settings. |                    |

## Blusam Redis Locks Error Codes

### Lock Operations

| Key        | Severity | Text                                                                                                 | Additional details |
| ---------- | -------- | ---------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R2300` | Error    | Invalid parameters for Bluesam lock operation. Verify dataset name and lock parameters are not null. |                    |
| `BA-R2301` | Error    | Failed to save dataset lock. Check Redis connection and lock state.                                  |                    |
| `BA-R2302` | Error    | Failed to save record lock for dataset. Verify record exists and Redis connection is active.         |                    |
| `BA-R2303` | Error    | Failed to remove dataset lock. Check if lock exists and Redis connection is active.                  |                    |
| `BA-R2304` | Error    | Failed to remove record lock for dataset. Verify record and lock exist.                              |                    |

### Lock State Operations

| Key        | Severity | Text                                                                                         | Additional details |
| ---------- | -------- | -------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R2310` | Error    | Invalid lock state cleanup parameters. Provide positive value for maxAge parameter.          |                    |
| `BA-R2311` | Warn     | Lock state integrity warning. Check for data corruption in lock states.                      |                    |
| `BA-R2312` | Error    | Failed to clean lock state. Verify Redis connection and state integrity.                     |                    |
| `BA-R2313` | Error    | Lock state cleanup operation failed. Check Redis connection and available memory.            |                    |
| `BA-R2314` | Error    | Failed to get dataset state. Check Redis connection and dataset existence.                   |                    |
| `BA-R2315` | Error    | Failed to get record state for dataset. Verify record exists and Redis connection is active. |                    |
| `BA-R2316` | Error    | Failed to check dataset write permission. Check Redis connection and lock state.             |                    |
| `BA-R2317` | Error    | Failed to check record write permission for dataset. Verify record and lock state.           |                    |
| `BA-R2318` | Error    | Failed to check dataset read permission. Check Redis connection and lock state.              |                    |
| `BA-R2319` | Error    | Failed to check record read permission for dataset. Verify record and lock state.            |                    |
| `BA-R2320` | Error    | Failed to save state. Check Redis connection and state data integrity.                       |                    |

### Lock Timeout Errors

| Key        | Severity | Text                                                                                                                         | Additional details |
| ---------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R2330` | Error    | Timeout while waiting for dataset write permission. Consider increasing the lock timeout or check for deadlocks.             |                    |
| `BA-R2331` | Error    | Timeout while acquiring lock for dataset. Verify if there are long-running operations holding the lock.                      |                    |
| `BA-R2332` | Error    | Interrupted while waiting to lock dataset. Check for thread interruptions or system issues.                                  |                    |
| `BA-R2333` | Error    | Timeout while acquiring lock for record in dataset. Consider increasing the lock timeout or optimize record access patterns. |                    |
| `BA-R2334` | Error    | Interrupted while waiting to lock record in dataset. Investigate thread interruptions or system-level issues.                |                    |

## GWFileLocks Error Codes

### Configuration and Initialization Errors

| Key        | Severity | Text                                                                                                                                                                | Additional details |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R3099` | Error    | Failed to shutdown GWFileLocks Redisson client. Check for active operations and retry shutdown.                                                                     |                    |
| `BA-R3101` | Fatal    | Failed to create Redission Client For GapWalk Files Locks. Please verify your configuration at 'filesLocks.redis' or global Redis settings 'gapwalk.redis' if used. |                    |
| `BA-R3102` | Fatal    | Redisson client cannot be null For GapWalk Files Locks. Please verify your configuration at 'filesLocks.redis' or global Redis settings 'gapwalk.redis' if used.    |                    |

### GWFileLocks Operations

| Key        | Severity | Text                                                                                                                                                                                     | Additional details |
| ---------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R3200` | Warn     | Lock metadata is null for file. This can cause data inconsistency and lead to locking failures or deadlocks. Verify Redis data integrity and check for outdated/corrupted lock metadata. |                    |
| `BA-R3210` | Error    | Failed to check lock status for file. Check Redis connection and file path.                                                                                                              |                    |
| `BA-R3220` | Error    | Lock acquisition interrupted for file. Check for thread interruptions.                                                                                                                   |                    |
| `BA-R3230` | Error    | Failed to store lock metadata for file. Verify Redis connection and memory availability.                                                                                                 |                    |
| `BA-R3240` | Info     | File is locked by job. Wait for the current operation to complete.                                                                                                                       |                    |
| `BA-R3250` | Error    | Failed to lock file. Check Redis connection and lock configuration.                                                                                                                      |                    |
| `BA-R3260` | Error    | Failed to release lock for file. Verify lock exists and connection is active.                                                                                                            |                    |
| `BA-R3270` | Error    | Failed to release locks for job. Check job context and Redis connection.                                                                                                                 |                    |
| `BA-R3280` | Error    | Failed to retrieve locks for job context. Verify job context exists and Redis connection.                                                                                                |                    |
| `BA-R3290` | Error    | Lock metadata corruption detected for file. Check Redis data integrity.                                                                                                                  |                    |

## Dataset Catalog Error Codes

### Dataset Operations

| Key        | Severity | Text                                                                                  | Additional details |
| ---------- | -------- | ------------------------------------------------------------------------------------- | ------------------ |
| `BA-R4200` | Error    | Failed to register dataset. Check Redis connection and dataset data.                  |                    |
| `BA-R4201` | Error    | Failed to check existence of dataset. Verify dataset identifier and Redis connection. |                    |
| `BA-R4220` | Error    | Failed to retrieve dataset. Check dataset identifier and Redis connection.            |                    |
| `BA-R4221` | Error    | Failed to retrieve all datasets. Verify Redis connection and retry operation.         |                    |
| `BA-R4300` | Error    | Failed to remove dataset. Check Redis connection and dataset existence.               |                    |

## Session & Session Tracker Error Codes

### Session Operations

| Key        | Severity | Text                                                                                                   | Additional details |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------ | ------------------ |
| `BA-R5050` | Error    | Failed to get Redis connection for session tracker. Check Redis connection settings and server status. |                    |
| `BA-R5051` | Error    | Failed to deserialize session data. Verify session data format and integrity.                          |                    |
| `BA-R5052` | Error    | Failed to retrieve sessions for node. Check node ID and Redis connection.                              |                    |
| `BA-R5053` | Error    | Failed to persist session. Verify Redis connection and session data.                                   |                    |
| `BA-R5054` | Error    | Failed to clean up session. Check session ID and Redis connection.                                     |                    |
| `BA-R5055` | Warn     | No sessions found for node. Verify node ID or sessions might have expired.                             |                    |
| `BA-R5056` | Error    | Failed to serialize session list to JSON. Check session data integrity.                                |                    |
| `BA-R5057` | Error    | Invalid session tracker operation parameter. Verify all required parameters are provided.              |                    |
| `BA-R5058` | Error    | Batch operation failed for sessions. Check Redis connection and retry operation.                       |                    |
| `BA-R5059` | Warn     | Session expiration warning. Session timeout might need adjustment.                                     |                    |

## JICS Resources Definitions Error Codes

Redis error codes, prefixed with BA-R.

### Configuration Errors

| Key        | Severity | Text                                                                                           | Additional details |
| ---------- | -------- | ---------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R6101` | Error    | Failed to update Redis resource with ID. Check Redis connection and verify write permissions.  |                    |
| `BA-R6102` | Error    | Failed to retrieve resource from Redis. Check Redis connection and verify the resource exists. |                    |
| `BA-R6110` | Error    | Failed to perform Redis template operation. Check Redis connection and server status.          |                    |

### JICS List Operations

| Key        | Severity | Text                                                                                              | Additional details |
| ---------- | -------- | ------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R6200` | Error    | JICS list not found in Redis cache. Verify the list name and ensure it exists in the Redis cache. |                    |
| `BA-R6201` | Error    | Failed to retrieve JICS list from Redis. Check Redis connection and verify the list exists.       |                    |
| `BA-R6202` | Error    | Failed to retrieve all JICS lists. Check Redis connection and server status.                      |                    |
| `BA-R6203` | Error    | Failed to persist JICS list. Check Redis connection and verify write permissions.                 |                    |
| `BA-R6204` | Error    | Failed to delete JICS list. Check Redis connection and verify delete permissions.                 |                    |
| `BA-R6205` | Error    | Failed to find list by ID. Verify the list ID and ensure Redis connection is working.             |                    |
| `BA-R6206` | Error    | Failed to retrieve list with children. Check Redis connection and verify the list exists.         |                    |

### JICS Group Operations

| Key        | Severity | Text                                                                                                | Additional details |
| ---------- | -------- | --------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R6300` | Error    | JICS group not found in Redis cache. Verify the group name and ensure it exists in the Redis cache. |                    |
| `BA-R6301` | Error    | Failed to retrieve JICS group with lists. Check Redis connection and verify the group exists.       |                    |
| `BA-R6302` | Error    | List referenced by group not found. Verify the list exists before associating it with a group.      |                    |
| `BA-R6303` | Error    | Failed to retrieve group list for JICS list. Check Redis connection and verify the list exists.     |                    |
| `BA-R6304` | Error    | Failed to retrieve for group. Check Redis connection and verify the resources exist.                |                    |
| `BA-R6305` | Error    | Failed to retrieve group with all children. Check Redis connection and verify the group exists.     |                    |
| `BA-R6306` | Error    | Failed to retrieve all JICS groups. Check Redis connection and server status.                       |                    |
| `BA-R6307` | Error    | Failed to find groups in list. Check Redis connection and verify the list exists.                   |                    |
| `BA-R6308` | Error    | Failed to check if group is present. Check Redis connection and server status.                      |                    |
| `BA-R6309` | Error    | Failed to count groups. Check Redis connection and server status.                                   |                    |
| `BA-R6310` | Error    | Failed to add groups to list. Check Redis connection and verify write permissions.                  |                    |
| `BA-R6311` | Error    | Failed to persist JICS group. Check Redis connection and verify write permissions.                  |                    |
| `BA-R6312` | Error    | Failed to delete for group. Check Redis connection and verify delete permissions.                   |                    |
| `BA-R6313` | Error    | Failed to delete JICS group. Check Redis connection and verify delete permissions.                  |                    |

## JICS File Operations

| Key        | Severity | Text                                                                                          | Additional details |
| ---------- | -------- | --------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R6400` | Error    | File not found in group. Verify the file name and ensure it exists in the specified group.    |                    |
| `BA-R6401` | Error    | Failed to get file ID for in group. Check Redis connection and verify the file exists.        |                    |
| `BA-R6402` | Error    | Failed to get active file IDs. Check Redis connection and verify the file exists.             |                    |
| `BA-R6403` | Error    | Failed to find files by name. Check Redis connection and verify the files exist.              |                    |
| `BA-R6404` | Error    | Failed to find file by ID. Check Redis connection and verify the file exists.                 |                    |
| `BA-R6405` | Error    | Failed to find files in group. Check Redis connection and verify the group exists.            |                    |
| `BA-R6406` | Error    | Failed to get first file from group. Check Redis connection and verify the file exists.       |                    |
| `BA-R6407` | Error    | Failed to persist file. Check Redis connection and verify write permissions.                  |                    |
| `BA-R6408` | Error    | Failed to delete file with ID. Check Redis connection and verify delete permissions.          |                    |
| `BA-R6409` | Error    | File with ID not found for deletion. Verify the file ID exists before attempting to delete.   |                    |
| `BA-R6410` | Error    | Failed to initialize file list for group. Check Redis connection and verify the group exists. |                    |

## JICS Program Operations

| Key        | Severity | Text                                                                                              | Additional details |
| ---------- | -------- | ------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R6500` | Error    | Program not found in group. Verify the program name and ensure it exists in the specified group.  |                    |
| `BA-R6501` | Error    | Failed to get program ID for in group. Check Redis connection and verify the program exists.      |                    |
| `BA-R6502` | Error    | Failed to get active program IDs. Check Redis connection and verify the program exists.           |                    |
| `BA-R6503` | Error    | Failed to find programs by name. Check Redis connection and verify the programs exists.           |                    |
| `BA-R6504` | Error    | Failed to find program by ID. Check Redis connection and verify the program exists.               |                    |
| `BA-R6505` | Error    | Failed to find programs in group. Check Redis connection and verify the group exists.             |                    |
| `BA-R6506` | Error    | Failed to get first program from group. Check Redis connection and verify the program exists.     |                    |
| `BA-R6507` | Error    | Failed to persist program. Check Redis connection and verify write permissions.                   |                    |
| `BA-R6508` | Error    | Failed to delete program with ID. Check Redis connection and verify delete permissions.           |                    |
| `BA-R6509` | Error    | Program with ID not found for deletion. Verify the program ID exists before attempting to delete. |                    |
| `BA-R6510` | Error    | Failed to initialize program list for group. Check Redis connection and verify the group exists.  |                    |

## JICS Transaction Operations

| Key        | Severity | Text                                                                                                     | Additional details |
| ---------- | -------- | -------------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R6600` | Error    | Transaction not found in group. Verify the transaction name and ensure it exists in the specified group. |                    |
| `BA-R6601` | Error    | Failed to get transaction ID for in group. Check Redis connection and verify the transaction exists.     |                    |
| `BA-R6602` | Error    | Failed to get active transaction IDs. Check Redis connection and verify the transaction exists.          |                    |
| `BA-R6603` | Error    | Failed to find transactions by name. Check Redis connection and verify the transactions existS.          |                    |
| `BA-R6604` | Error    | Failed to find transaction by ID. Check Redis connection and verify the transaction exists.              |                    |
| `BA-R6605` | Error    | Failed to find transactions in group. Check Redis connection and verify the group exists.                |                    |
| `BA-R6606` | Error    | Failed to persist transaction. Check Redis connection and verify write permissions.                      |                    |
| `BA-R6607` | Error    | Failed to delete transaction with ID. Check Redis connection and verify delete permissions.              |                    |
| `BA-R6608` | Error    | Failed to initialize transaction list for group. Check Redis connection and verify the group exists.     |                    |

## JICS TDQueue Operations

| Key        | Severity | Text                                                                                             | Additional details |
| ---------- | -------- | ------------------------------------------------------------------------------------------------ | ------------------ |
| `BA-R6700` | Error    | TDQueue not found in group. Verify the TDQueue name and ensure it exists in the specified group. |                    |
| `BA-R6701` | Error    | Failed to get TDQueue ID for in group. Check Redis connection and verify the TDQueue exists.     |                    |
| `BA-R6702` | Error    | Failed to get active TDQueue IDs. Check Redis connection and verify the TDQueue exists.          |                    |
| `BA-R6703` | Error    | Failed to find TDQueues by name. Check Redis connection and verify the TDQueues exists.          |                    |
| `BA-R6704` | Error    | Failed to find TDQueue by ID. Check Redis connection and verify the TDQueue exists.              |                    |
| `BA-R6705` | Error    | Failed to find TDQueues in group. Check Redis connection and verify the group exists.            |                    |
| `BA-R6706` | Error    | Failed to persist TDQueue. Check Redis connection and verify write permissions.                  |                    |
| `BA-R6707` | Error    | Failed to delete TDQueue with ID. Check Redis connection and verify delete permissions.          |                    |
| `BA-R6708` | Error    | Failed to initialize TDQueue list for group. Check Redis connection and verify the group exists. |                    |

## JICS TSModel Operations

| Key        | Severity | Text                                                                                             | Additional details |
| ---------- | -------- | ------------------------------------------------------------------------------------------------ | ------------------ |
| `BA-R6800` | Error    | TSModel not found in group. Verify the TSModel name and ensure it exists in the specified group. |                    |
| `BA-R6801` | Error    | Failed to get TSModel ID for in group. Check Redis connection and verify the TSModel exists.     |                    |
| `BA-R6802` | Error    | Failed to get active TSModel IDs. Check Redis connection and verify the TSModel exists.          |                    |
| `BA-R6803` | Error    | Failed to find TSModels by name. Check Redis connection and verify the TSModels exists.          |                    |
| `BA-R6804` | Error    | Failed to find TSModel by ID. Check Redis connection and verify the TSModel exists.              |                    |
| `BA-R6805` | Error    | Failed to find TSModels in group. Check Redis connection and verify the group exists.            |                    |
| `BA-R6806` | Error    | Failed to persist TSModel. Check Redis connection and verify write permissions.                  |                    |
| `BA-R6807` | Error    | Failed to delete TSModel with ID. Check Redis connection and verify delete permissions.          |                    |
| `BA-R6808` | Error    | Failed to initialize TSModel list for group. Check Redis connection and verify the group exists. |                    |

## Authentication Errors

| Key        | Severity | Text                                                                                                           | Additional details |
| ---------- | -------- | -------------------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R6900` | Error    | Failed to get connected username. Check security context and authentication status.                            |                    |
| `BA-R6901` | Error    | Authentication error while accessing Redis resource. Verify user permissions and authentication configuration. |                    |

## TS Queue Redis Error Codes

### TS Queue General Operations

| Key        | Severity | Text                                                                                                                                              | Additional details |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R7000` | Warn     | TS Queue operation warning : Fetching from task-scoped registry instead of Redis storage. Configure Redis TS Queue storage if you want to use it. |                    |

### Configuration Errors

| Key        | Severity | Text                                                                                                                 | Additional details |
| ---------- | -------- | -------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R7110` | Error    | Jics TS Queue Redis initialization error: Failed to initialize list operations. Verify Redis template configuration. |                    |

### Queue Operations

| Key        | Severity | Text                                                                       | Additional details |
| ---------- | -------- | -------------------------------------------------------------------------- | ------------------ |
| `BA-R7711` | Error    | Failed to read from TS Queue. Verify queue exists and data integrity.      |                    |
| `BA-R7712` | Error    | Failed to write to TS Queue. Check Redis connection and write permissions. |                    |
| `BA-R7713` | Error    | Failed to delete TS Queue. Verify queue exists and delete permissions.     |                    |
| `BA-R7714` | Error    | TS Queue list operation failed. Check Redis list operations availability.  |                    |
| `BA-R7715` | Error    | Invalid index access for TS Queue. Verify index is within bounds.          |                    |
| `BA-R7716` | Warn     | TS Queue size operation warning. Check queue existence and connection.     |                    |

## AWS Blu Age Runtime JCL Checkpoint Error Codes

### Configuration Errors

| Key        | Severity | Text                                                                                                                  | Additional details |
| ---------- | -------- | --------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R8110` | Error    | JCL Checkpoint Redis initialization error: Failed to initialize list operations. Verify Redis template configuration. |                    |

### Checkpoint Retrieval Operations

| Key        | Severity | Text                                                                                         | Additional details |
| ---------- | -------- | -------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R8200` | Error    | Failed to retrieve JCL checkpoints for job. Check Redis connection and job name.             |                    |
| `BA-R8210` | Error    | Error in retrieving JCL checkpoint(s) from persistence. Check Redis connection and job name. |                    |
| `BA-R8600` | Warn     | No checkpoints found for job. Verify job name and checkpoint existence.                      |                    |

### Checkpoint Persistence Operations

| Key        | Severity | Text                                                                                           | Additional details |
| ---------- | -------- | ---------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R8300` | Error    | Failed to persist JCL checkpoints for job. Verify Redis connection and write permissions.      |                    |
| `BA-R8305` | Error    | Failed to set expiration for job checkpoints. Verify Redis connection and expiration settings. |                    |
| `BA-R8400` | Error    | Checkpoint deserialization failed. Verify checkpoint data integrity.                           |                    |

### Checkpoint Purge Operations

| Key        | Severity | Text                                                                                                     | Additional details |
| ---------- | -------- | -------------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-R8500` | Error    | Failed to purge JCL checkpoints from redis persistence. Check Redis connection and deletion permissions. |                    |
| `BA-R8501` | Error    | Failed to purge JCL checkpoint from redis persistence. Check Redis connection and deletion permissions.  |                    |

## Blu4iv Lock Error Codes

### Lock Operations

| Key        | Severity | Text                                                                                  | Additional details |
| ---------- | -------- | ------------------------------------------------------------------------------------- | ------------------ |
| `BA-R9200` | Error    | Failed to save Blu4iv lock for record. Check Redis connection and lock data.          |                    |
| `BA-R9201` | Error    | Failed to check lock repository status. Verify Redis connection and repository state. |                    |
| `BA-R9210` | Error    | Failed to check lock permission. Verify Redis connection and timeout settings.        |                    |
| `BA-R9220` | Error    | Failed to remove Blu4iv lock. Check Redis connection and lock existence.              |                    |
| `BA-R9225` | Error    | Failed to clear Blu4iv locks. Check Redis connection and permissions.                 |                    |
| `BA-R9900` | Warn     | Lock already exists for record. Verify lock status and record identifier.             |                    |
