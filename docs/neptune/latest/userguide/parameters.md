# Amazon Neptune parameters

You manage your database configuration in Amazon Neptune by using parameters in
[parameter groups](parameter-groups.md "parameter-groups.md"). The following parameters
are available for configuring your Neptune database:

###### Cluster-level parameters

- [neptune_enable_audit_log](#parameters-db-cluster-parameters-neptune_enable_audit_log "#parameters-db-cluster-parameters-neptune_enable_audit_log")
- [neptune_enable_slow_query_log](#parameters-db-cluster-parameters-neptune_enable_slow_query_log "#parameters-db-cluster-parameters-neptune_enable_slow_query_log")
- [neptune_slow_query_log_threshold](#parameters-db-cluster-parameters-neptune_slow_query_log_threshold "#parameters-db-cluster-parameters-neptune_slow_query_log_threshold")
- [neptune_lab_mode](#parameters-db-cluster-parameters-neptune_lab_mode "#parameters-db-cluster-parameters-neptune_lab_mode")
- [neptune_query_timeout](#parameters-db-cluster-parameters-neptune_query_timeout "#parameters-db-cluster-parameters-neptune_query_timeout")
- [neptune_streams](#parameters-db-cluster-parameters-neptune_streams "#parameters-db-cluster-parameters-neptune_streams")
- [neptune_streams_expiry_days](#parameters-db-cluster-parameters-neptune_streams_expiry_days "#parameters-db-cluster-parameters-neptune_streams_expiry_days")
- [neptune_lookup_cache](#parameters-db-cluster-parameters-neptune_lookup_cache "#parameters-db-cluster-parameters-neptune_lookup_cache")
- [neptune_autoscaling_config](#parameters-db-cluster-parameters-neptune_autoscaling_config "#parameters-db-cluster-parameters-neptune_autoscaling_config")
- [neptune_ml_iam_role](#parameters-db-cluster-parameters-neptune_ml_iam_role "#parameters-db-cluster-parameters-neptune_ml_iam_role")
- [neptune_ml_endpoint](#parameters-db-cluster-parameters-neptune_ml_endpoint "#parameters-db-cluster-parameters-neptune_ml_endpoint")
- [neptune_enable_inline_server_generated_edge_id](#parameters-db-cluster-parameters-neptune_inline_edge_id "#parameters-db-cluster-parameters-neptune_inline_edge_id")

 

###### Instance-level parameters

- [neptune_dfe_query_engine](#parameters-instance-parameters-neptune_dfe_query_engine "#parameters-instance-parameters-neptune_dfe_query_engine")
- [neptune_query_timeout](#parameters-instance-parameters-neptune_query_timeout "#parameters-instance-parameters-neptune_query_timeout")
- [neptune_result_cache](#parameters-db-instance-parameters-neptune_result_cache "#parameters-db-instance-parameters-neptune_result_cache")
- [UndoLogPurgeConfig](#parameters-db-instance-parameters-undo_log_purge_config "#parameters-db-instance-parameters-undo_log_purge_config")

 

###### Deprecated parameters

- [neptune_enforce_ssl](#parameters-db-cluster-parameters-neptune_enforce_ssl "#parameters-db-cluster-parameters-neptune_enforce_ssl")

## `neptune_enable_audit_log` (cluster-level parameter)

This parameter toggles audit logging for Neptune.

Allowed values are `0` (disabled) and `1`
(enabled). The default value is `0`.

This parameter is static, meaning that changes to it do not take
effect on any instance until it has been rebooted.

You can publish audit logs to Amazon CloudWatch, as described in
[Using the CLI to publish Neptune audit logs to CloudWatch Logs](cloudwatch-logs.md#cloudwatch-logs-cli "cloudwatch-logs.md#cloudwatch-logs-cli").

## `neptune_enable_slow_query_log` (cluster-level parameter)

Use this parameter to enable or disable Neptune's [slow-query
logging](slow-query-logs.md "slow-query-logs.md") feature.

This is a dynamic parameter, meaning that changing its value does not
require or cause a restart of your DB cluster.

Allowed values are:

- **`info`**   –  
  Enables slow-query logging and logs selected attributes that might be contributing
  to the slow performance.
- **`debug`**   –  
  Enables slow-query logging and logs all available attributes of the query run.
- **`disable`**   –  
  Disables slow-query logging.

The default value is `disable`.

You can publish slow-query logs to Amazon CloudWatch, as described in
[Using the CLI to publish Neptune slow-query logs to CloudWatch Logs](cloudwatch-logs.md#cloudwatch-slow-query-logs-cli "cloudwatch-logs.md#cloudwatch-slow-query-logs-cli").

## `neptune_slow_query_log_threshold` (cluster-level parameter)

This parameter specifies the execution time threshold, in milliseconds, after
which a query is considered a slow query. If [slow-query
logging](slow-query-logs.md "slow-query-logs.md") is enabled, queries that run longer than this threshold will be logged
together with some of their attributes.

The default value is 5000 milliseconds (5 seconds).

This is a dynamic parameter, meaning that changing its value does not
require or cause a restart of your DB cluster.

## `neptune_lab_mode` (cluster-level parameter)

When set, this parameter enables specific experimental features of
Neptune. See [Neptune Lab Mode](features-lab-mode.md "features-lab-mode.md") for the experimental
features currently available.

This parameter is static, meaning that changes to it do not take
effect on any instance until it has been rebooted.

To enable or disable an experimental feature, include
`(feature name)``=enabled` or
`(feature name)``=disabled` in
this parameter. You can enable or disable multiple features by
separating them with commas, like this:

`(feature #1 name)``=enabled,`
`(feature #2 name)``=enabled`

Lab mode features are typically disabled by default. An exception is the
`DFEQueryEngine` feature, which became enabled by default for use with
query hints (`DFEQueryEngine=viaQueryHint`) starting in [Neptune engine release 1.0.5.0](engine-releases-1.0.5.md "engine-releases-1.0.5.md").
Beginning with [Neptune engine release 1.1.1.0](engine-releases-1.1.1.md "engine-releases-1.1.1.md")
the DFE engine is no longer in lab mode, and is now controlled using
the [neptune_dfe_query_engine](#parameters-instance-parameters-neptune_dfe_query_engine "#parameters-instance-parameters-neptune_dfe_query_engine")
instance parameter in an instance's DB parameter group.

## `neptune_query_timeout` (cluster-level parameter)

Specifies a specific timeout duration for graph queries, in milliseconds.

Allowed values range from `10` to `2,147,483,647`
(231 - 1). The default value is `120,000`
(2 minutes).

This parameter is static, meaning that changes to it do not take
effect on any instance until it has been rebooted.

###### Note

It is possible to incur unexpected costs if you set the query timeout value
too high, particularly on a serverless instance. Without a reasonable timeout
setting, you may inadvertently issue a query that keeps running much longer than
you expected, incurring costs you never anticipated. This is particularly true
on a serverless instance that could scale up to a large, expensive instance type
while running the query.

You can avoid unexpected expenses of this kind by using a query timeout
value that accomodates most of your queries and only causes unexpectedly
long-running ones to time out.

## `neptune_streams` (cluster-level parameter)

Enables or disables [Neptune streams](streams.md "streams.md").

This parameter is static, meaning that changes to it do not take
effect on any instance until it has been rebooted.

Allowed values are `0` (disabled, which is the default), and
`1` (enabled).

## `neptune_streams_expiry_days` (cluster-level parameter)

Specifies how many days elapse before the server deletes stream records.

Allowed values are from `1` to `90`, inclusive. The default
is `7`.

This parameter was introduced in [engine
version 1.2.0.0](engine-releases-1.2.0.md "engine-releases-1.2.0.md").

This parameter is static, meaning that changes to it do not take
effect on any instance until it has been rebooted.

## `neptune_lookup_cache` (cluster-level parameter)

Disables or re-enables the [Neptune
lookup cache.](feature-overview-lookup-cache.md "feature-overview-lookup-cache.md") on `R5d` instances.

This parameter is static, meaning that changes to it do not take
effect on any instance until it has been rebooted.

Allowed values are `1` (enabled) and `0` (disabled). The
default value is `0`, but whenever an `R5d` instance is
created in the DB cluster, the `neptune_lookup_cache` parameter is
automatically set to `1` and a lookup cache is created on that
instance.

## `neptune_autoscaling_config` (cluster-level parameter)

Sets configuration parameters for the read-replica instances that [Neptune auto-scaling](manage-console-autoscaling.md "manage-console-autoscaling.md") creates and
manages.

This parameter is static, meaning that changes to it do not take
effect on any instance until it has been rebooted.

Using a JSON string that you set as the value of the `neptune_autoscaling_config`
parameter, you can specify:

- The instance type that Neptune auto-scaling uses for all the new
  read-replica instances that it creates.
- The maintenance windows assigned to those read-replicas.
- Tags to be associated with all the new read-replicas.

The JSON string has a structure like this:

```
"{
  \"tags\": [
    { \"key\" : \"`reader tag-0 key`\", \"value\" : \"`reader tag-0 value`\" },
    { \"key\" : \"`reader tag-1 key`\", \"value\" : \"`reader tag-1 value`\" },
  ],
  \"maintenanceWindow\" : \"`wed:12:03-wed:12:33`\",
  \"dbInstanceClass\" : \"db.r5.xlarge\"
}"
```

Note that the quotation marks within the string must all be escaped with a backslash
character (`\`).

Any of the three configuration settings not specified in the `neptune_autoscaling_config`
parameter are copied from the configuration of the DB cluster's primary writer instance.

## `neptune_ml_iam_role` (cluster-level parameter)

Specifies the IAM role ARN used in Neptune ML. The value can be any valid IAM
role ARN.

This parameter is static, meaning that changes to it do not take
effect on any instance until it has been rebooted.

You can specify the default IAM role ARN for machine learning on graphs.

## `neptune_ml_endpoint` (cluster-level parameter)

Specifies the endpoint used for Neptune ML. The value can be any valid [SageMaker AI
endpoint name](../../../sagemaker/latest/APIReference/API_CreateEndpoint.md#sagemaker-CreateEndpoint-request-EndpointName "../../../sagemaker/latest/APIReference/API_CreateEndpoint.md#sagemaker-CreateEndpoint-request-EndpointName").

This parameter is static, meaning that changes to it do not take
effect on any instance until it has been rebooted.

You can specify the default SageMaker AI endpoint for machine learning on graphs.

## `neptune_enable_inline_server_generated_edge_id` (cluster-level parameter)

Enable or disable the Neptune inline server-generated Edge ID feature.

This parameter is static, meaning that changes to it do not take
effect on any instance until it has been rebooted.

Allowed values are `1` (enabled), and `0` (disabled). The default value is `0`.

## `neptune_dfe_query_engine` (instance-level parameter)

Starting with [Neptune engine release 1.1.1.0](engine-releases-1.1.1.md "engine-releases-1.1.1.md"),
this DB instance parameter is used to control how the [DFE
query engine](neptune-dfe-engine.md "neptune-dfe-engine.md") is used. Allowed values are as follows:

This parameter is static, meaning that changes to it do not take
effect on any instance until it has been rebooted.

- **`enabled`**   –  
  Causes the DFE engine to be used wherever possible, except where the `useDFE`
  query hint is present and set to `false`.
- **`viaQueryHint`** (the default)   –  
  Causes the DFE engine to be used only for queries that explicitly include the
  `useDFE` query hint set to `true`.

If this parameter has not been explicitly set, the default value, `viaQueryHint`,
is used when the instance is started.

###### Note

All openCypher queries are executed by the DFE engine regardless of how
this parameter is set.

Prior to release 1.1.1.0, this was a lab-mode parameter rather than a DB instance
parameter.

## `neptune_query_timeout` (instance-level parameter)

This DB instance parameter specifies a timeout duration for graph queries,
in milliseconds, for one instance.

This parameter is static, meaning that changes to it do not take
effect on any instance until it has been rebooted.

Allowed values range from `10` to `2,147,483,647`
(231 - 1). The default value is `120,000`
(2 minutes).

###### Note

It is possible to incur unexpected costs if you set the query timeout value
too high, particularly on a serverless instance. Without a reasonable timeout
setting, you may inadvertently issue a query that keeps running much longer than
you expected, incurring costs you never anticipated. This is particularly true
on a serverless instance that could scale up to a large, expensive instance type
while running the query.

You can avoid unexpected expenses of this kind by using a query timeout
value that accomodates most of your queries and only causes unexpectedly
long-running ones to time out.

## `neptune_result_cache` (instance-level parameter)

**`neptune_result_cache`**   –  
This DB instance parameter enables or disables [Caching query results](gremlin-results-cache.md "gremlin-results-cache.md").

This parameter is static, meaning that changes to it do not take
effect on any instance until it has been rebooted.

Allowed values are `0`, (disabled, which is the default), and
`1` (enabled).

## `UndoLogPurgeConfig` (instance-level parameter)

**`UndoLogPurgeConfig`**   –  
Use this parameter to enable or disable aggressive UndoLog purging in Neptune.

Allowed values are `default`, which utilizes the standard number of threads for undo log purging, and
`aggressive`, which uses an increased number of threads to expedite the cleanup of undo logs. When the
`agressive` option is selected, you can expect to observe a hugher value for the
`NumUndoPagesPurged` metric.

## `neptune_enforce_ssl` (DEPRECATED cluster-level parameter)

(**Deprecated**) There used to be regions that
permitted HTTP connections to Neptune, and this parameter was used to force all
connections to use HTTPS when it was set to 1. This parameter is no longer relevant,
however, since Neptune now only accepts HTTPS connections in all regions.
