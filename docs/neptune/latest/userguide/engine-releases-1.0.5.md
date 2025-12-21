# Amazon Neptune Engine Version 1.0.5.0 (2021-07-27)

As of 2021-07-27, engine version 1.0.5.0 is being generally deployed. Please note
that it takes several days for a new release to become available in every region.

## Subsequent Patch Releases for This Release

- [Release: 1.0.5.0.R2 (2021-08-16)](engine-releases-1.0.5.0.md "engine-releases-1.0.5.0.md")
- [Release: 1.0.5.0.R3 (2021-09-15)](engine-releases-1.0.5.0.md "engine-releases-1.0.5.0.md")
- [Maintenance release: 1.0.5.0.R5 (2022-05-16)](engine-releases-1.0.5.0.md "engine-releases-1.0.5.0.md")

## New Features in This Engine Release

- [Neptune ML](machine-learning.md "machine-learning.md") was released
  for production use with many new features, and is no longer in lab mode.
- Added initial support for the [openCypher](access-graph-opencypher.md "access-graph-opencypher.md") query language, in Lab Mode.
  **openCypher** is the open-source standard for
  the Cypher query language. Its syntax is specified in the [Cypher
  Query Language Reference (Version 9)](https://s3.amazonaws.com/artifacts.opencypher.org/openCypher9.pdf "https://s3.amazonaws.com/artifacts.opencypher.org/openCypher9.pdf"), and is maintained by the [openCypher](http://www.opencypher.org/ "http://www.opencypher.org/") project.

See [Accessing the Neptune Graph with openCypher](access-graph-opencypher.md "access-graph-opencypher.md")
for information about the Neptune implementation of the language.

Support for the [Bolt protocol](https://neo4j.com/docs/bolt/current/bolt/ "https://neo4j.com/docs/bolt/current/bolt/"),
which Neptune clients use for openCypher queries, is also supported. See [Using the Bolt protocol to make openCypher queries to Neptune](access-graph-opencypher-bolt.md "access-graph-opencypher-bolt.md").

Support for openCypher is now automatically enabled, but it depends on the [Neptune DFE engine](neptune-dfe-engine.md "neptune-dfe-engine.md"),
which is currently only available in [lab mode](features-lab-mode.md "features-lab-mode.md").
The default `DFEQueryEngine` setting in the `neptune_lab_mode`
DB cluster parameter is now `DFEQueryEngine=viaQueryHint`, which means
that the engine is enabled but only used for queries that have the
`useDFE` query hint present and set to `true`. If you disable
the DFE engine by setting `DFEQueryEngine=disabled`, you will not be able
to use openCypher.

- Added support for the [SPARQL 1.1 Graph
  Store HTTP Protocol](https://www.w3.org/TR/sparql11-http-rdf-update/ "https://www.w3.org/TR/sparql11-http-rdf-update/"). See [Using the SPARQL 1.1 Graph Store HTTP Protocol (GSP) in Amazon Neptune](sparql-graph-store-protocol.md "sparql-graph-store-protocol.md").
- Changed the default lab-mode setting for the [Neptune DFE engine](neptune-dfe-engine.md "neptune-dfe-engine.md") to `viaQueryHint`,
  which means that the DFE engine is now enabled by default, but only used for
  queries that have the `useDFE` query hint present and set to
  `true`.
- Added a new Amazon CloudWatch metric, `StatsNumStatementsScanned`,
  for monitoring the computation of statistics for the Neptune DFE engine.
  See [Using the StatsNumStatementsScanned CloudWatch metric to monitor statistics computation](neptune-dfe-statistics.md#neptune-dfe-statistics-monitoring "neptune-dfe-statistics.md#neptune-dfe-statistics-monitoring").

## Improvements in This Engine Release

- Added support for Apache TinkerPop 3.4.11.

###### Important

A change was made in TinkerPop version 3.4.11 that improves correctness of
how queries are processed, but for the moment can sometimes seriously impact
query performance.

For example, a query of this sort may run significantly slower:

```
g.V().hasLabel('airport').
  order().
    by(out().count(),desc).
  limit(10).
  out()
```

The vertices after the limit step are now fetched in a non-optimal way beause
of the TinkerPop 3.4.11 change. To avoid this, you can modify the query by adding
the barrier() step at any point after the `order().by()`.
For example:

```
g.V().hasLabel('airport').
  order().
    by(out().count(),desc).
  limit(10).
  barrier().
  out()
```

- The [SPARQL
  joinOrder query hint](sparql-query-hints-joinOrder.md "sparql-query-hints-joinOrder.md") is now supported by the Neptune DFE
  alternative query engine.
- The output of the [Neptune status API](access-graph-status.md "access-graph-status.md")
  has been expanded and reorganized to provide more clarity about your DB cluster's
  settings and features.

The new output has a top-level `features` object
that contains status information about your DB cluster's features, and a top-level
`settings` object that contain settings information.
To review the new format, see [Example output from the instance status command](access-graph-status.md#access-graph-status-sample-output "access-graph-status.md#access-graph-status-sample-output").

- Handling of streaming change logs has been improved when
  `AFTER_SEQUENCE_NUMBER` streams are requested with the last event ID on the
  server, when that event ID has already expired. The server no longer throws an expired
  event ID error if the requested event ID is the most recently purged event ID on the
  server.

## Defects Fixed in This Engine Release

- Fixed a Gremlin bug related to the ordering of numeric values.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.0.5.0, make sure that your project is compatible
with these query-language versions:

- _Gremlin version:_ `3.4.11`
- _SPARQL version:_ `1.1`

## Upgrade Paths to Engine Release 1.0.5.0

You can manually upgrade any previous Neptune engine release to this release.

You will not automatically upgrade to this release.

## Upgrading to This Release

Amazon Neptune 1.0.5.0 is now generally available.

If a DB cluster is running an engine version from which there is an upgrade path
to this release, it is eligible to be upgraded now. You can upgrade any eligible cluster
using the DB cluster operations on the console or by using the SDK. The following CLI
command will upgrade an eligible cluster immediately:

For Linux, OS X, or Unix:

```
aws neptune modify-db-cluster \
    --db-cluster-identifier `(your-neptune-cluster)` \
    --engine-version 1.0.5.0 \
    --apply-immediately
```

For Windows:

```
aws neptune modify-db-cluster ^
    --db-cluster-identifier `(your-neptune-cluster)` ^
    --engine-version 1.0.5.0 ^
    --apply-immediately
```

Updates are applied to all instances in a DB cluster simultaneously. An update requires
a database restart on those instances, so you will experience downtime ranging
from 20–30 seconds to several minutes, after which you can resume using the DB cluster.

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
