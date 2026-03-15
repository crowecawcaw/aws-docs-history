# Amazon Neptune Engine Version 1.2.0.0.R2 (2022-10-14)

As of 2022-10-14, engine version 1.2.0.0.R2 is being generally deployed. Please note
that it takes several days for a new release to become available in every region.

###### Note

**If upgrading from an engine version earlier than 1.2.0.0:**

- [Engine release 1.2.0.0](engine-releases-1.2.0.md "engine-releases-1.2.0.md") introduced
  a new format for custom parameter groups and custom cluster parameter
  groups. As a result, if you are upgrading from an engine version earlier than 1.2.0.0
  to engine version 1.2.0.0 or above, you must re-create all your existing custom
  parameter groups and custom cluster parameter groups using parameter group family
  `neptune1.2`. Earlier releases used parameter group family `neptune1`,
  and those parameter groups won't work with release 1.2.0.0 and above.
  See [Amazon Neptune parameter groups](parameter-groups.md "parameter-groups.md") for more
  information.
- Engine release 1.2.0.0 also introduced a new format for undo logs. As a result,
  any undo logs created by an earlier engine version must be purged and the [UndoLogsListSize](cw-metrics.md#cw-metrics-UndoLogListSize "cw-metrics.md#cw-metrics-UndoLogListSize") CloudWatch metric
  must fall to zero before any upgrade from a version earlier than 1.2.0.0 can get
  started. If there are too many undo log records (200,000 or more) when you try to
  start an update, the upgrade attempt can time out while waiting for purging of the
  undo logs to complete.

You can speed up the purge rate by upgrading the cluster's writer instance,
which is where the purging occurs. Doing that before trying to upgrade can bring
down the number of undo logs before you start. Increasing the size of the writer
to a 24XL instance type can increase your purge rate to more than a million
records per hour.

If the `UndoLogsListSize` CloudWatch metric is extremely large, opening
a support case may help you explore additional strategies for bringing it down.

- Finally, there was a breaking change in release 1.2.0.0 affecting earlier code
  that used the Bolt protocol with IAM authentication. Starting with release 1.2.0.0,
  Bolt needs a resource path for IAM signing. In Java, setting the resource path
  might look like this: `request.setResourcePath("/openCypher"));`.
  In other languages, the `/openCypher` can be appended to the endpoint
  URI. See [Using the Bolt protocol](access-graph-opencypher-bolt.md "access-graph-opencypher-bolt.md") for examples.

## Improvements in This Engine Release

- Improved performance of Gremlin `order-by` queries. Gremlin
  queries with an `order-by` at the end of a `NeptuneGraphQueryStep`
  now use a larger chunk size for better performance. This does not apply to
  `order-by` on an internal (non-root) node of the query plan.
- Improved performance of Gremlin update queries. Vertices and edges
  must now be locked against deletion while adding edges or properties. This change
  eliminates duplicate locks within a transaction, which improves performance.
- Improved performance of Gremlin queries that use `dedup()`
  inside of a `repeat()` subquery by pushing the `dedup` down
  to the native execution layer.
- Added the Gremlin `Neptune#cardinalityEstimates` query
  hint. When set to `false`, this disables cardinality estimates.
- Added user-friendly error messages for IAM authentication errors. These
  messages now show the your IAM user or role ARN, the resource ARN, and a list of
  unauthorized actions for the request. The list of unauthorized actions helps you
  see what might be missing or explicitly denied in the IAM policy that you're using.

## Defects Fixed in This Engine Release

- Fixed a Gremlin correctness bug involving `WherePredicateStep`
  translation, where Neptune's query engine was producing incorrect results for queries
  using `where(P.neq('x'))` and variations of that.
- Fixed a Gremlin bug where using `PartitionStrategy` after
  upgrading to TinkerPop 3.5 incorrectly resulted an error with the message,
  "PartitionStrategy does not work with anonymous Traversals," which prevented
  the traversal from being executed.
- Fixed various Gremlin bugs related to the `joinTime` of
  a final join and to statistics inside of `Project.ASK` subgroups.
- Fixed an openCypher bug in the `MERGE` clause that in some
  cases caused duplicate node and edge creation.
- Fixed a transaction bug where a session could insert graph data
  and commit even when the corresponding concurrent dictionary inserts got rolled back.
- Fixed a bulk loader bug that caused performance regressions under heavy
  insertion loads.
- Fixed a SPARQL bug in the handling of queries that contain
  `(NOT) EXISTS` within an `OPTIONAL` clause, where
  in some cases query results were missing.
- Fixed a bug where drivers could appear to hang in cases where requests
  were cancelled due to a timeout prior to their start of evaluation. It was possible
  to get into this state if all query processing threads on the server were consumed
  while timeouts occurred to items in the request queue. Because the timeouts from the
  request queue were not immediately sending messages, the responses appeared to the
  client to remain pending.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.2.0.0.R2, make sure that your project is compatible
with these query-language versions:

- _Gremlin earliest version supported:_ `3.5.2`
- _Gremlin latest version supported:_ `3.5.4`
- _openCypher version:_ `Neptune-9.0.20190305-1.0`
- _SPARQL version:_ `1.1`

## Upgrade Paths to Engine Release 1.2.0.0.R2

Your cluster will be upgraded to this patch release automatically during your next
maintenance window if you are running engine version `1.2.0.0`.

You can only upgrade to release `1.2.0.0` manually from the latest
patch release of [engine release 1.1.1.0](engine-releases-1.1.1.md "engine-releases-1.1.1.md").
Earlier engine releases must first be upgraded to the latest release of
`1.1.1.0` before they can be upgraded to `1.2.0.0`.

If you are upgrading first to release `1.1.1.0` and then immediately to
`1.2.0.0`, you may encounter an error such as the following:

```
   **We're sorry, your request to modify DB cluster (cluster identifier) has failed.**
   Cannot modify engine version because instance (instance identifier) is
   running on an old configuration. Apply any pending maintenance actions on the instance before
   proceeding with the upgrade.
```

If you encounter this error, wait for the pending action to finish, or trigger
a maintenance window immediately to let the previous upgrade complete.

## Upgrading to This Release

If a DB cluster is running an engine version from which there is an upgrade path
to this release, it is eligible to be upgraded now. You can upgrade any eligible cluster
using the DB cluster operations on the console or by using the SDK. The following CLI
command will upgrade an eligible cluster immediately:

For Linux, OS X, or Unix:

```
aws neptune modify-db-cluster \
    --db-cluster-identifier `(your-neptune-cluster)` \
    --engine-version 1.2.0.0 \
    --allow-major-version-upgrade \
    --apply-immediately
```

For Windows:

```
aws neptune modify-db-cluster ^
    --db-cluster-identifier `(your-neptune-cluster)` ^
    --engine-version 1.2.0.0 ^
    --allow-major-version-upgrade ^
    --apply-immediately
```

Instead of `--apply-immediately`, you can specify
`--no-apply-immediately`. To perform a major version upgrade, the
allow-major-version-upgrade parameter is required. Also, be sure to include
the engine version or your engine may be upgraded to a different version.

If your cluster uses a custom cluster parameter group, be sure to include this paramater
to specify it:

```
    --db-cluster-parameter-group-name `(name of the custom DB cluster parameter group)`
```

Similarly, if any instances in the cluster use a custom DB parameter group, be sure
to include this parameter to specify it:

```
    --db-instance-parameter-group-name `(name of the custom instance parameter group)`
```

### Always test before you upgrade

When a new major or minor Neptune engine version is released, always test your
Neptune applications on it first before upgrading to it. Even a minor upgrade could
introduce new features or behavior that would affect your code.

Start by comparing the release notes pages from your current version to those
of the targeted version to see if there will be changes in query language versions
or other breaking changes.

The best way to test a new version before upgrading your production DB cluster is
to clone your production cluster so that the clone is running the new engine version.
You can then run queries on the clone without affecting the production DB cluster.

### Always create a manual snapshot before you upgrade

Before performing an upgrade, we strongly recommend that you always create
a manual snapshot of your DB cluster. Having an automatic snapshot only offers
short-term protection, whereas a manual snapshot remains available until you
explicitly delete it.

In certain cases Neptune creates a manual snapshot for you as a part of the
upgrade process, but you should not rely on this, and should create your own manual
snapshot in any case.

When you are certain that you won't need to revert your DB cluster to its
pre-upgrade state, you can explicitly delete the manual snapshot that you created
yourself, as well as the manual snapshot that Neptune might have created. If Neptune
creates a manual snapshot, it will have a name that begins with `preupgrade`,
followed by the name of your DB cluster, the source engine version, the target engine
version, and the date.

###### Note

If you are trying to upgrade while [a
pending action is in process](manage-console-maintaining.md "manage-console-maintaining.md"), you may encounter an error such as the
following:

```
   **We're sorry, your request to modify DB cluster (cluster identifier) has failed.**
   Cannot modify engine version because instance (instance identifier) is
   running on an old configuration. Apply any pending maintenance actions on the instance before
   proceeding with the upgrade.
```

If you encounter this error, wait for the pending action to finish, or trigger
a maintenance window immediately to let the previous upgrade complete.

For more information about upgrading your engine version, see [Maintaining your Amazon Neptune DB Cluster](cluster-maintenance.md "cluster-maintenance.md"). If you have any questions or concerns, the AWS Support
team is available on the community forums and through [AWS Premium Support](http://aws.amazon.com/support "http://aws.amazon.com/support").
