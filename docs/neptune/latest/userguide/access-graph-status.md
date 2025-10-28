# Check the Health Status of a Neptune Instance

Amazon Neptune provides a mechanism to check the status of the graph database on the host.
It's also a good way to confirm that you are able to connect to an instance.

To check the health of an instance and get DB cluster status using `curl`:

```
curl -G https://`your-neptune-endpoint`:`port`/status
```

Or, starting with [engine release 1.2.1.0.R6](engine-releases-1.2.1.0.md "engine-releases-1.2.1.0.md"),
you can use the following CLI command instead:

```
aws neptunedata get-engine-status
```

If the instance is healthy, the `status` command returns a [JSON object](#access-graph-status-sample-output "#access-graph-status-sample-output") with the following fields:

- **`status`**   –  
  Set to `"healthy"` if the instance is not experiencing problems.

If the instance is recovering from a crash or from being rebooted and
there are active transactions running from the latest server shutdown,
`status` is set to `"recovery"`.

- **`startTime`**   –  
  Set to the UTC time at which the current server process started.
- **`dbEngineVersion`**   –  
  Set to the Neptune engine version running on your DB cluster.

If this engine version has been manually patched since it was released, the
version number is prefixed by `"Patch-"`.

- **`role`**   –  
  Set to `"reader"` if the instance is a read-replica,
  or to `"writer"` if the instance is the primary instance.
- **`dfeQueryEngine`**   –  
  Set to `"enabled"` if the [DFE
  engine](neptune-dfe-engine.md "neptune-dfe-engine.md") is fully enabled, or to `viaQueryHint` if the DFE engine
  is only used with queries that have the `useDFE` query hint set to
  `true` (`viaQueryHint` is the default).
- **`gremlin`**   –  
  Contains information about the Gremlin query language available on your cluster.
  Specifically, it contains a `version` field that specifies
  the current TinkerPop version being used by the engine.
- **`sparql`**   –  
  Contains information about the SPARQL query language available on your cluster.
  Specifically, it contains a `version` field that specifies
  the current SPARQL version being used by the engine.
- **`opencypher`**   –  
  Contains information about the openCypher query language available on your cluster.
  Specifically, it contains a `version` field that specifies
  the current operCypher version being used by the engine.
- **`labMode`**   –  
  Contains [Lab Mode](features-lab-mode.md "features-lab-mode.md")
  settings being used by the engine. This is a selective list of Lab Mode settings and not the complete set.
  Consult the [cluster parameter group](parameter-groups.md "parameter-groups.md") for the full set in use.
- **`rollingBackTrxCount`**   –  
  If there are transactions being rolled back, this field is set to the number
  of such transactions. If there are none, the field doesn't appear at all.
- **`rollingBackTrxEarliestStartTime`**   –  
  Set to the start time of the earliest transaction being rolled back.
  If no transactions are being rolled back, the field doesn't appear at all.
- **`features`**   –  
  Contains status information about the features enabled on your DB cluster:
  - **`lookupCache`**   –   The current status
    of the [Lookup cache](feature-overview-lookup-cache.md "feature-overview-lookup-cache.md"). This field
    only appears on `R5d` instance types, since those are the only
    instances where a lookup cache can exist. The field is a JSON object
    in the form:

  ```
  "lookupCache": {
    "status": "`current lookup cache status`"
  }
  ```

  On an `R5d` instance:

      - If the lookup cache is enabled, the status is listed as
       `"Available"`.
      - If the lookup cache has been disabled, the status
       is listed as `"Disabled"`.
      - If the disk limit has been reached on the instance, the
       status is listed as `"Read Only Mode - Storage Limit
       Reached"`.

  - **`ResultCache`**   –  
    The current status of the [Caching query results](gremlin-results-cache.md "gremlin-results-cache.md"). This field is a JSON object
    in the form:

  ```
  "ResultCache": {
    "status": "`current results cache status`"
  }
  ```

      - If the results cache has been enabled, the status
       is listed as `"Available"`.
      - If the cache is disabled, the status is listed as
       `"Disabled"`.

  - **`IAMAuthentication`**   –  
    Specifies whether or not AWS Identity and Access Management (IAM) authentication has been
    enabled on your DB cluster:
    - If IAM authentication been enabled, the status
      is listed as `"enabled"`.
    - If IAM authentication is disabled, the status
      is listed as `"disabled"`.

  - **`Streams`**   –  
    Specifies whether or not Neptune streams have been
    enabled on your DB cluster:
    - If streams are enabled, the status
      is listed as `"enabled"`.
    - If streams are disabled, the status
      is listed as `"disabled"`.

  - **`AuditLog`**   –  
    Equal to `enabled` if audit logs are enabled, or otherwise `disabled`.
  - **`SlowQueryLogs`**   –  
    Equal to `info` or `debug` if [slow-query
    logging](slow-query-logs.md "slow-query-logs.md") is enabled, or otherwise `disabled`.
  - **`QueryTimeout`**   –  
    The value, in milliseconds, of the query timeout.

- **`settings`**   –  
  Settings applied to the instance:
  - **`clusterQueryTimeoutInMs`**   –  
    The value, in milliseconds, of the query timeout, set for the whole cluster.
  - **`SlowQueryLogsThreshold`**   –  
    The value, in milliseconds, of the query timeout, set for the whole cluster.

- **`serverlessConfiguration`**   –  
  Serverless settings for a cluster if it is running as serverless:
  - **`minCapacity`**   –  
    The smallest size to which a serverless instance in your DB cluster can shrink, in
    Neptune Capacity Units (NCUs).
  - **`maxCapacity`**   –  
    The largest size to which a serverless instance in your DB cluster can grow, in
    Neptune Capacity Units (NCUs).

## Example output from the instance status command

The following is an example of the output from the instance status command,
(in this case, run on an `R5d` instance):

```
{
  'status': 'healthy',
  'startTime': 'Thu Aug 24 21:47:12 UTC 2023',
  'dbEngineVersion': '1.2.1.0.R4',
  'role': 'writer',
  'dfeQueryEngine': 'viaQueryHint',
  'gremlin': {'version': 'tinkerpop-3.6.2'},
  'sparql': {'version': 'sparql-1.1'},
  'opencypher': {'version': 'Neptune-9.0.20190305-1.0'},
  'labMode': {
    'ObjectIndex': 'disabled',
    'ReadWriteConflictDetection': 'enabled'
  },
  'features': {
    'SlowQueryLogs': 'disabled',
    'ResultCache': {'status': 'disabled'},
    'IAMAuthentication': 'disabled',
    'Streams': 'disabled',
    'AuditLog': 'disabled'
  },
  'settings': {
    'clusterQueryTimeoutInMs': '120000',
    'SlowQueryLogsThreshold': '5000'
  },
  'serverlessConfiguration': {
    'minCapacity': '1.0',
    'maxCapacity': '128.0'
  }
}
```

If there is a problem with the instance, the status command returns the `HTTP
 500` error code. If the host is unreachable, the request times out. Ensure that you are
accessing the instance from within the virtual private cloud (VPC), and that your
security groups allow you access to it.
