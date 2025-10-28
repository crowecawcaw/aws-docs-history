# Neptune Lab Mode

You can use Amazon Neptune _lab mode_ to enable new features that are in
the current Neptune engine release, but that aren't yet ready for production use and aren't
enabled by default. This lets you try out these features in your development and test
environments.

###### Note

This feature is available starting with [Release 1.0.1.0.200463.0 (2019-10-15)](engine-releases-1.0.1.0.200463.md "engine-releases-1.0.1.0.200463.md").

## Using Neptune Lab Mode

Use the [neptune_lab_mode
DB cluster parameter](parameters.md#parameters-db-cluster-parameters-neptune_lab_mode "parameters.md#parameters-db-cluster-parameters-neptune_lab_mode") to enable or disable features.
You do this by including ``(feature name)`=enabled`
 or ``(feature name)`=disabled` in the value of the
`neptune_lab_mode` parameter in the DB Cluster Parameter group.

For example, in this engine release you might set the `neptune_lab_mode`
parameter to `Streams=disabled, ReadWriteConflictDetection=enabled`.

For information about how to edit the DB cluster parameter group for your database,
see [Editing a Parameter Group](parameter-groups.md#parameters-editgroup "parameter-groups.md#parameters-editgroup").
Note that you cannot edit the default DB cluster parameter group; if you are using the default
group, you must create a new DB cluster parameter group before you can set the
`neptune_lab_mode` parameter.

###### Note

When you make a change to a static DB cluster parameter such as `neptune_lab_mode`,
you must re-start the primary (writer) instance of the cluster for the change to take effect.
Before [Release: 1.2.0.0 (2022-07-21)](engine-releases-1.2.0.md "engine-releases-1.2.0.md"),
all the read-replicas in a DB cluster would then automatically be rebooted when the primary
instance restarted.

Beginning with [Release: 1.2.0.0 (2022-07-21)](engine-releases-1.2.0.md "engine-releases-1.2.0.md"),
restarting the primary instance does not cause any of the replicas to restart.
This means that you must restart each instance separately
to pick up a DB cluster parameter change (see [Parameter groups](parameter-groups.md "parameter-groups.md")).

###### Important

At present, if you supply the wrong lab-mode parameters or your request
fails for another reason, you may not be notified of the failure. You
should always verify that a lab-mode change request has succeeded by calling the
[status API](access-graph-status.md "access-graph-status.md") as shown below:

```
curl -G https://`your-neptune-endpoint`:`port`/status
```

The status results include lab-mode information which will show whether
or not the changes you requested were made:

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

Neptune can now maintain a fourth index, namely the OSGP index, which is
useful for data sets having a large number of predicates (see [Enabling an OSGP Index](feature-overview-storage-indexing.md#feature-overview-storage-indexing-osgp "feature-overview-storage-indexing.md#feature-overview-storage-indexing-osgp")).

###### Note

This feature is available starting in [Neptune engine release 1.0.2.1](engine-releases-1.0.2.md "engine-releases-1.0.2.md").

You can enable an OSGP index in a new, empty Neptune DB cluster by setting
`ObjectIndex=enabled` in the `neptune_lab_mode` DB cluster
parameter. An OSGP index can **only** be enabled in
a new, empty DB cluster.

By default, the OSGP index is disabled.

###### Note

After setting the `neptune_lab_mode` DB cluster parameter so as
to enable the OSGP index, you must restart the writer instance of the cluster for the
change to take effect.

###### Warning

If you disable an enabled OSGP index by setting `ObjectIndex=disabled`
and then later re-enable it after adding more data, the index will not build correctly.
On-demand rebuilding of the index is not supported, so you should only enable the OSGP
index when the database is empty.

## Enabling dictionary garbage collection

Dictionary garbage collection can be enabled for property graph data when neptune-streams is not enabled via
the `DictionaryGCMode` parameter. The concurrency can be controlled via the
`DictionaryGCConcurrency` parameter. See
[Dictionary garbage collection](storage-gc.md "storage-gc.md") for more details.

## Formalized Transaction Semantics

Neptune has updated the formal semantics for concurrent transactions
(see [Transaction Semantics in Neptune](transactions.md "transactions.md")).

Use `ReadWriteConflictDetection` as the name in the `neptune_lab_mode`
parameter that enables or disables formalized transaction semantics.

By default, formalized transaction semantics are already enabled. If you want
to revert to the earlier behavior, include `ReadWriteConflictDetection=disabled`
in the value set for the DB Cluster `neptune_lab_mode` parameter.

## Extended datetime support

Neptune has extended support for the datetime functionality. To enable datetime with extended formats, include
`DatetimeMillisecond=enabled` in the value set for the DB Cluster `neptune_lab_mode` parameter.

## AccurateQRCMemoryEstimation

###### Note

This feature is available starting in [Neptune engine release 1.4.0.0](engine-releases-1.4.0.md "engine-releases-1.4.0.md").

Default value: disabled

Allowed values: enabled/disabled

[Gremlin query result cache](gremlin-results-cache.md "gremlin-results-cache.md"),
when enabled, allows caching of query results on the database. By deafult the approximate estimate is used to determine
the size of the result cached, with this lab mode param `AccurateQRCMemoryEstimation` enabled, the size
estimation for cached results will use accurate size estimates instead of approximate. This labmode parameter is
available starting from Neptune engine release version 1.4.0.0.
