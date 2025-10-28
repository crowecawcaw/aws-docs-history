# Amazon Neptune Engine version 1.4.0.0 (2024-11-06)

As of 2024-11-06, engine version 1.4.0.0 is being generally deployed. Please note
that it takes several days for a new release to become available in every region.

###### Note

[Engine release 1.3.0.0](engine-releases-1.3.0.md "engine-releases-1.3.0.md") introduced
a new format for custom parameter groups and custom cluster parameter
groups. As a result, if you are upgrading from an engine version earlier than 1.3.0.0
to engine version 1.3.0.0 or above, you must re-create all of your existing custom
parameter groups and custom cluster parameter groups using parameter group family
`neptune1.3`. Earlier releases used parameter group family `neptune1`,
or `neptune1.2`. and those parameter groups won't work with release
1.3.0.0 and above. Similarly, you should use 1.4.0.0 cluster parameter groups for engine versions 1.4.0.0 and above.
See [Amazon Neptune parameter groups](parameter-groups.md "parameter-groups.md") for more
information.

###### Warning

The query plan cache is temporarily unsupported for the use case of executing parameterized queries involving numeric
parameter values, due to a bug in handling duplicate usages of a numeric type parameter in the query. For example:

```
MATCH (n:movie) WHERE n.runtime>=$minutes RETURN n
      UNION
      MATCH (n:show) WHERE n.duration>=$minutes RETURN n

      parameters={"minutes":130}
```

Queries that do a lot of index searches on statements or dictionary indices could see a 5% performance regression. For
example - getting a count of all vertices, or getting the `id` of all vertices would not be affected. Getting
all properties of all vertices could see up to a 5% regression.

## New features in this engine release

- When an edge is added to a property graph without an explicit ID, by default the server assigns a UUID-based edge ID,
  which is stored in the dictionary. Now by setting a new cluster parameter,
  `neptune_enable_server_generated_edge_id = 1`,
  the server will assign IDs using an internally managed 8-byte integer, without any dictionary overhead. This results
  in storage savings and improved query performance without any changes to queries. This feature is currently supported
  for inserts via the Gremlin query language only.
- Added support for Gremlin limit() step execution in nested traversals for DFE engine.

```
g.V().project("foo").by(out().order().by(T.id).limit(1))
```

## Improvements in this engine release

###### General Improvements

- Neptune will automatically reclaim undo storage held by large transactions once the transaction is complete and
  logs are no longer needed for recovery.
- Support for global database survivable replica. This feature allows secondary cluster to still serve read requests
  during a writer instance restart on the primary cluster. Previously, when a writer instance restarted, all reader
  instances in a secondary cluster also restarted. With this release, secondary cluster reader instances continue to
  serve read requests during a writer instance restart, improving read availability in the cluster.
- Audit logs are now written synchronously, which guarantees that every query is logged. This may affect performance
  for particularly large queries (>100kb) or high-throughput workloads (>1000 qps).

###### Gremlin Improvements

- The per-query timeout is by default enforced to be smaller than the cluster-level timeout. In a previous release,
  this check was introduced but needed to be explicitly enabled via the lab-mode parameter 'StrictTimeoutValidation'.
  With this release, 'StrictTimeoutValidation' will be enabled by default and must be disabled explicitly to keep
  the old behavior.

###### openCypher improvements

- In a previous release we introduced [extended datetime format support](feature-opencypher-compliance.md#opencypher-compliance-time-na "feature-opencypher-compliance.md#opencypher-compliance-time-na"), enabled via a lab mode parameter `DatetimeMillisecond`.
  This extended datetime format support is now enabled by default.

###### SPARQL improvements

- New explicit IAM actions for query permissions.

```
Previously:
COPY: WriteDataViaQuery & ReadDataViaQuery
MOVE: WriteDataViaQuery & DeleteDataViaQuery
DELETEINSERT: ReadDataViaQuery & DeleteDataViaQuery

 Now,
COPY: WriteDataViaQuery & ReadDataViaQuery & DeleteDataViaQuery
MOVE: WriteDataViaQuery & ReadDataViaQuery & DeleteDataViaQuery
DELETEINSERT: ReadDataViaQuery, WriteDataViaQuery if there is INSERT clause, DeleteDataViaQuery if there is DELETE clause.
```

## Defects fixed in this engine release

###### General fixes

- Fixed an issue with Serverless instances that could lead to a database restart while scaling up.
- Fixed an issue related to audit log file management that could cause log files to be inaccessible for
  download or rotation, and in some cases increase CPU usage.
- Fixed a query issue related to optimization delaying map output generation in the DFE engine.
- Fixed an issue which caused mismatched timestamps between the audit logs and slow query logs.

###### Gremlin fixes

- Resolved an issue in Gremlin WebSocket connection management where queries running for time exceeding the
  connection idle timeout were prematurely terminated. This specifically affected Python Gremlin clients using
  the AIOHTTP transport.

###### openCypher fixes

- Fixed an issue in collect step which caused an internal failure exception when null values are present during
  the collect(distinct(n)) query construct.
- Fixed an issue where a `NullPointerException` might occur in queries when the query plan cache is enabled.
- Fixed an issue which evaluated more data than needed when a query contains LIMIT clause.
- Fixed an issue where using range operations (<, <=, >, >=) in a parameterized query with a query plan
  cache would produce duplicate results.
- Fixed an issue that transposes result columns when UNION and UNION ALL operations are performed using bolt connections.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.4.0.0, make sure that your project is compatible
with these query-language versions:

- _Gremlin earliest version supported:_ `3.7.1`
- _Gremlin latest version supported:_ `3.7.1`
- _openCypher version:_ `Neptune-9.0.20190305-1.0`
- _SPARQL version:_ `1.1`

## Upgrade paths to engine release 1.4.0.0

You can upgrade to this release from [engine
release 1.2.0.0](engine-releases-1.2.0.md "engine-releases-1.2.0.md") or above.

## Upgrading to This Release

If a DB cluster is running an engine version from which there is an upgrade path
to this release, it is eligible to be upgraded now. You can upgrade any eligible cluster
using the DB cluster operations on the console or by using the SDK. The following CLI
command will upgrade an eligible cluster immediately:

For Linux, OS X, or Unix:

```
aws neptune modify-db-cluster \
    --db-cluster-identifier `(your-neptune-cluster)` \
    --engine-version 1.4.0.0 \
    --allow-major-version-upgrade \
    --apply-immediately
```

For Windows:

```
aws neptune modify-db-cluster ^
    --db-cluster-identifier `(your-neptune-cluster)` ^
    --engine-version 1.4.0.0 ^
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
