

# Neptune Lab Mode
<a name="features-lab-mode"></a>

You can use Amazon Neptune *lab mode* to enable new features that are in the current Neptune engine release, but that aren't yet ready for production use and aren't enabled by default. This lets you try out these features in your development and test environments.

## Using Neptune Lab Mode
<a name="features-lab-mode-using"></a>

Use the [`neptune_lab_mode` DB cluster parameter](parameters.md#parameters-db-cluster-parameters-neptune_lab_mode) to enable or disable features. You do this by including `{{(feature name)}}=enabled` or `{{(feature name)}}=disabled` in the value of the `neptune_lab_mode` parameter in the DB Cluster Parameter group.

For example, in this engine release you might set the `neptune_lab_mode` parameter to `Streams=disabled, ReadWriteConflictDetection=enabled`.

For information about how to edit the DB cluster parameter group for your database, see [Editing a Parameter Group](parameter-groups.md#parameters-editgroup). Note that you cannot edit the default DB cluster parameter group; if you are using the default group, you must create a new DB cluster parameter group before you can set the `neptune_lab_mode` parameter.

**Note**  
When you make a change to a static DB cluster parameter such as `neptune_lab_mode`, you must re-start the primary (writer) instance of the cluster for the change to take effect. Before [Release: 1.2.0.0 (2022-07-21)](engine-releases-1.2.0.0.md), all the read-replicas in a DB cluster would then automatically be rebooted when the primary instance restarted.  
Beginning with [Release: 1.2.0.0 (2022-07-21)](engine-releases-1.2.0.0.md), restarting the primary instance does not cause any of the replicas to restart. This means that you must restart each instance separately to pick up a DB cluster parameter change (see [Parameter groups](parameter-groups.md)).

**Important**  
At present, if you supply the wrong lab-mode parameters or your request fails for another reason, you may not be notified of the failure. You should always verify that a lab-mode change request has succeeded by calling the [status API](access-graph-status.md) as shown below:  

```
curl -G https://{{your-neptune-endpoint}}:{{port}}/status
```
The status results include lab-mode information which will show whether or not the changes you requested were made:  

```
{
  "status":"healthy",
  "startTime":"Wed Dec 29 02:29:24 UTC 2021",
  "dbEngineVersion":"development",
  "role":"writer",
  "dfeQueryEngine":"viaQueryHint",
  "gremlin":{"version":"tinkerpop-3.5.2"},
  "sparql":{"version":"sparql-1.1"},
  "opencypher":{"version":"Neptune-9.0.20190305-1.0"},
  "labMode":{
    "ObjectIndex":"disabled",
    "ReadWriteConflictDetection":"enabled"
  },
  "features":{
    "LookupCache":{"status":"Available"},
    "ResultCache":{"status":"disabled"},
    "IAMAuthentication":"disabled",
    "Streams":"disabled",
    "AuditLog":"disabled"
  },
  "settings":{"clusterQueryTimeoutInMs":"120000"}
}
```

The following features are currently accessed using lab mode:

## The OSGP index
<a name="features-lab-mode-features-osgp-index"></a>

Neptune can now maintain a fourth index, namely the OSGP index, which is useful for data sets having a large number of predicates (see [Enabling an OSGP Index](feature-overview-storage-indexing.md#feature-overview-storage-indexing-osgp)).

You can enable an OSGP index in a new, empty Neptune DB cluster by setting `ObjectIndex=enabled` in the `neptune_lab_mode` DB cluster parameter. An OSGP index can **only** be enabled in a new, empty DB cluster.

By default, the OSGP index is disabled.

**Note**  
After setting the `neptune_lab_mode` DB cluster parameter so as to enable the OSGP index, you must restart the writer instance of the cluster for the change to take effect.

**Warning**  
If you disable an enabled OSGP index by setting `ObjectIndex=disabled` and then later re-enable it after adding more data, the index will not build correctly. On-demand rebuilding of the index is not supported, so you should only enable the OSGP index when the database is empty.

## Enabling dictionary garbage collection
<a name="features-lab-mode-features-gc"></a>

Dictionary garbage collection can be enabled for property graph data when neptune-streams is not enabled via the `DictionaryGCMode` parameter. The concurrency can be controlled via the `DictionaryGCConcurrency` parameter. See [Dictionary garbage collection](storage-gc.md) for more details.

## Formalized Transaction Semantics
<a name="features-lab-mode-features-transaction-semantics"></a>

Neptune has updated the formal semantics for concurrent transactions (see [Transaction Semantics in Neptune](transactions.md)).

Use `ReadWriteConflictDetection` as the name in the `neptune_lab_mode` parameter that enables or disables formalized transaction semantics.

By default, formalized transaction semantics are already enabled. If you want to revert to the earlier behavior, include `ReadWriteConflictDetection=disabled` in the value set for the DB Cluster `neptune_lab_mode` parameter.

## Extended datetime support
<a name="labmode-extended-datetime-support"></a>

 Neptune has extended support for the datetime functionality. To enable datetime with extended formats, include `DatetimeMillisecond=enabled` in the value set for the DB Cluster `neptune_lab_mode` parameter. 

## StrictTimeoutValidation
<a name="labmode-StrictTimeoutValidation"></a>

**Note**  
This feature is available starting in [Neptune engine release 1.3.2.0](engine-releases-1.3.2.0.md).

 Default value: enabled (disabled by default prior to [Neptune engine release 1.4.0.0](engine-releases-1.4.0.0.md)) 

 Allowed values: enabled/disabled 

 When this parameter is `enabled`, a per-query timeout value specified as a request option or a query hint cannot exceed the value set globally in the [`neptune_query_timeout`](parameters.md#parameters-db-cluster-parameters-neptune_query_timeout) parameter group setting. If the per-query timeout exceeds the global setting, Neptune throws an `InvalidParameterException`. In engine versions prior to 1.4.0.0, this parameter was `disabled` by default and had to be explicitly enabled. 

 This setting can be confirmed in a response on the `/status` endpoint when the value is `disabled`. 

 For more information, see [Per-query timeouts](best-practices-gremlin-java-per-query-timeout.md). 

## AccurateQRCMemoryEstimation
<a name="labmode-AccurateQRCMemoryEstimation"></a>

**Note**  
This feature is available starting in [Neptune engine release 1.4.0.0](engine-releases-1.4.0.0.md).

 Default value: disabled 

 Allowed values: enabled/disabled 

 [Gremlin query result cache](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-results-cache.html), when enabled, allows caching of query results on the database. By deafult the approximate estimate is used to determine the size of the result cached, with this lab mode param `AccurateQRCMemoryEstimation` enabled, the size estimation for cached results will use accurate size estimates instead of approximate. This labmode parameter is available starting from Neptune engine release version 1.4.0.0. 