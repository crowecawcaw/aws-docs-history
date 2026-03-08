# Amazon Neptune Engine Version 1.2.0.0 (2022-07-21)

As of 2022-07-21, engine version 1.2.0.0 is being generally deployed. Please note
that it takes several days for a new release to become available in every region.

###### Note

**If upgrading from an engine version earlier than 1.2.0.0:**

- Engine release 1.2.0.0 introduced
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

## Subsequent Patch Releases for This Release

- [Release: 1.2.0.0.R2 (2022-10-14)](engine-releases-1.2.0.0.md "engine-releases-1.2.0.0.md")
- [Release: 1.2.0.0.R3 (2022-12-15)](engine-releases-1.2.0.0.md "engine-releases-1.2.0.0.md")
- [Release: 1.2.0.0.R4 (2023-09-29)](engine-releases-1.2.0.0.md "engine-releases-1.2.0.0.md")

## New Features in This Engine Release

- Added support for [global
  databases](neptune-global-database.md "neptune-global-database.md"). A Neptune global database spans multiple AWS Regions, and
  consists of a primary DB cluster in one region, and up to five secondary DB clusters
  in other regions.
- Added support for more granular access control in Neptune IAM
  policies than has been available previously, based on data plane actions. This is a
  breaking change in that existing IAM policies that are based on the deprecated
  `connect` action must be adjusted to use the more granular data plane
  actions. See [Types of IAM policies](security-iam-access-manage.md#iam-auth-policy "security-iam-access-manage.md#iam-auth-policy").
- Improved reader instance availability. Previously, when a writer instance
  restarted, all reader instances in the Neptune cluster automatically restarted too.
  Starting with engine release 1.2.0.0, reader instances remain active after a writer restart,
  which improves reader availability. Reader instances can be restarted separately to pick
  up parameter group changes. See [Rebooting a DB instance in Amazon Neptune](manage-console-instances-reboot.md "manage-console-instances-reboot.md").
- Added a new [neptune_streams_expiry_days](parameters.md#parameters-db-cluster-parameters-neptune_streams_expiry_days "parameters.md#parameters-db-cluster-parameters-neptune_streams_expiry_days") DB cluster parameter which lets you set the
  number of days that stream records are kept on the server before being deleted.
  The range is 1 through 90, and the default is 7.

## Improvements in This Engine Release

- Improved Gremlin serialization performance for ByteCode queries.
- Neptune now processes text predicates using the DFE engine, for
  improved performance.
- Neptune now processes Gremlin `limit()` steps using the
  DFE engine, including non-terminal and child traversal limits.
- Changed DFE handling of the Gremlin `union()` step
  to work with other new features, which means that reference nodes show up in query
  profiles as expected.
- Improved performance by up to a factor of 5 of some expensive join
  operations within DFE by parallelizing them.
- Added `by()` modulation support for `OrderGlobalStep
order(global)` for the Gremlin DFE engine.
- Added display of injected static values in explain details for DFE.
- Improved performance when pruning duplicate patterns.
- Added order preservation support in the Gremlin DFE engine.
- Improved the performance of Gremlin queries having empty filters, such as these:

```
g.V().hasId(P.within([]))
```

```
g.V().hasId([])
```

- Improved error messaging when a SPARQL query uses a numeric value that
  is too large for Neptune to represent internally.
- Improved performance for dropping vertices with associated edges by
  reducing index searches when streams are disabled.
- Extended DFE support to more variants of the `has()` step,
  in particular to `hasKey()`, `hasLabel()`, and to range
  predicates for strings/URIs within `has()`. This affects queries
  such as the following:

```
// hasKey() on properties
g.V().properties().hasKey("name")
g.V().properties().has(T.key, TextP.startingWith("a"))
g.E().properties().hasKey("weight")
g.E().properties().hasKey(TextP.containing("t"))

// hasLabel() on vertex properties
g.V().properties().hasLabel("name")

// range predicates on ID and Label fields
g.V().has(T.label, gt("person"))
g.E().has(T.id, lte("`(an ID value)`"))
```

- Added a Neptune-specific openCypher [join()](access-graph-opencypher-extensions.md#opencypher-compliance-join-function "access-graph-opencypher-extensions.md#opencypher-compliance-join-function")
  function that concatenates strings in a list into a single string.
- Updated the [Neptune
  managed policies](security-iam-access-managed-policies.md "security-iam-access-managed-policies.md") to include data-access permissions and permissions for
  the new global database APIs.

## Defects Fixed in This Engine Release

- Fixed a bug where an HTTP request with no content-type specified would
  automatically fail.
- Fixed a SPARQL bug in the query optimizer that prevented use of a
  service call inside a query.
- Fixed a SPARQL bug in the Turtle RDF parser where a particular
  combination of Unicode data caused failure.
- Fixed a SPARQL bug where a particular combination of `GRAPH`
  and`SELECT` clauses produced incorrect query results.
- Fixed a Gremlin bug that caused a correctness issue for queries that
  used any filter step within a union step, such as the following:

```
g.V("1").union(hasLabel("person"), out())
```

- Fixed a Gremlin bug where `count()` of
  `both().simplePath()` would result in double the actual number
  of results returned without `count()`.
- Fixed an openCypher bug where a faulty signature mismatch exception
  was generated by the server for Bolt requests to clusters with IAM authentication
  enabled.
- Fixed an openCypher bug where a query using HTTP keep-alive could
  be incorrectly closed if it was submitted after a failed request.
- Fixed an openCypher bug that could cause an internal error
  to be thrown when a query that returns a constant value is submitted.
- Fixed a bug in the explain details so that DFE subquery
  `Time(ms)` now correctly sums the CPU times of operators within the
  DFE subquery. Consider the following excerpt of explain output as an example:

```
subQuery1
╔════╤════════╤════════╤═══════════════════════╤═══════════════════════════════════╤══════╤══════════╤═══════════╤═══════╤═══════════╗
║ ID │ Out #1 │ Out #2 │ Name                  │ Arguments                         │ Mode │ Units In │ Units Out │ Ratio │ Time (ms) ║
╠════╪════════╪════════╪═══════════════════════╪═══════════════════════════════════╪══════╪══════════╪═══════════╪═══════╪═══════════╣
  ...
╟────┼────────┼────────┼───────────────────────┼───────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 1  │ 2      │ -      │ DFEChunkLocalSubQuery │ subQuery=...graph#336e.../graph_1 │ -    │ 1        │ 1         │ 1.00  │ 0.38      ║
║    │        │        │                       │ coordinationTime(ms)=0.026        │      │          │           │       │           ║
╟────┼────────┼────────┼───────────────────────┼───────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
  ...
subQuery=...graph#336e.../graph_1
╔════╤════════╤════════╤═══════════════════════╤═══════════════════════════════════╤══════╤══════════╤═══════════╤═══════╤═══════════╗
║ ID │ Out #1 │ Out #2 │ Name                  │ Arguments                         │ Mode │ Units In │ Units Out │ Ratio │ Time (ms) ║
╠════╪════════╪════════╪═══════════════════════╪═══════════════════════════════════╪══════╪══════════╪═══════════╪═══════╪═══════════╣
║ 0  │ 1      │ -      │ DFESolutionInjection  │ solutions=[?100 -> [-10^^<LONG>]] │ -    │ 0        │ 1         │ 0.00  │ 0.04      ║
║    │        │        │                       │ outSchema=[?100]                  │      │          │           │       │           ║
╟────┼────────┼────────┼───────────────────────┼───────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 1  │ 3      │ -      │ DFERelationalJoin     │ joinVars=[]                       │ -    │ 2        │ 1         │ 0.50  │ 0.29      ║
╟────┼────────┼────────┼───────────────────────┼───────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 2  │ 1      │ -      │ DFESolutionInjection  │ outSchema=[]                      │ -    │ 0        │ 1         │ 0.00  │ 0.01      ║
╟────┼────────┼────────┼───────────────────────┼───────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 3  │ -      │ -      │ DFEDrain              │ -                                 │ -    │ 1        │ 0         │ 0.00  │ 0.02      ║
╚════╧════════╧════════╧═══════════════════════╧═══════════════════════════════════╧══════╧══════════╧═══════════╧═══════╧═══════════╝
```

The subQuery times in the last column of the lower table add up to 0.36 ms (`.04 + .29 + .01 + .02 = .36`).
When you add in to the coordination time for that subquery (`.36 + .026 = .386`),
you get a result that is close to the time for the subQuery recorded in the last column of the upper table,
namely `0.38` ms.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.2.0.0, make sure that your project is compatible
with these query-language versions:

- _Gremlin earliest version supported:_ `3.5.2`
- _Gremlin latest version supported:_ `3.5.4`
- _openCypher version:_ `Neptune-9.0.20190305-1.0`
- _SPARQL version:_ `1.1`

## Upgrade Paths to Engine Release 1.2.0.0

Because this is a major engine release, there is no automatic upgrade to it.

You can only upgrade to release `1.2.0.0` manually, from the latest
patch release of [engine release 1.1.1.0](engine-releases-1.1.1.md "engine-releases-1.1.1.md").
Earlier engine releases must first be upgraded to the latest release of
`1.1.1.0` before they can be upgraded to `1.2.0.0`.

Therefore, before you try to upgrade to this release, please confirm that you
are currently running the latest patch release of release `1.1.1.0`.
If you are not, start by upgrading to the latest patch release of `1.1.1.0`.

Before upgrading, you must also re-create any custom DB cluster parameter group that
you have been using with your previous version, using parameter group family
`neptune1.2`. See [Amazon Neptune parameter groups](parameter-groups.md "parameter-groups.md") for more information.

If you are upgrading first to release `1.1.1.0` and then immediately to
`1.2.0.0`, you may encounter an error such as the following:

```
   **We're sorry, your request to modify DB cluster (cluster identifier) has failed.**
   Cannot modify engine version because instance (instance identifier) is
   running on an old configuration. Apply any pending maintenance actions on the instance before
   proceeding with the upgrade.
```

If you encounter this error, wait for the pending action to finish, or trigger
a maintenance window immediately to let the previous upgrade complete (see [Maintaining your Amazon Neptune DB Cluster](cluster-maintenance.md "cluster-maintenance.md")).

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
