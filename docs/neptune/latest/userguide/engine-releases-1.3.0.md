# Amazon Neptune Engine Version 1.3.0.0 (2023-11-15)

As of 2023-11-15, engine version 1.3.0.0 is being generally deployed. Please note
that it takes several days for a new release to become available in every region.

###### Note

Engine release 1.3.0.0 introduced
a new format for custom parameter groups and custom cluster parameter
groups. As a result, if you are upgrading from an engine version earlier than 1.3.0.0
to engine version 1.3.0.0 or above, you must re-create all of your existing custom
parameter groups and custom cluster parameter groups using parameter group family
`neptune1.3`. Earlier releases used parameter group family `neptune1`,
or `neptune1.2`. and those parameter groups won't work with release
1.3.0.0 and above. Similarly, you should use 1.4.0.0 cluster parameter groups for engine versions 1.4.0.0 and above.
See [Amazon Neptune parameter groups](parameter-groups.md "parameter-groups.md") for more
information.

## New Features in This Engine Release

- Released the [Neptune data API](data-api.md "data-api.md").

The Amazon Neptune data API provides SDK support for more than 40 of Neptune's data
operations, including data loading, query execution, data inquiry, and machine learning.
It supports all three Neptune query languages (Gremlin, openCypher and SPARQL), and is
available in all SDK languages. It automatically signs API requests and greatly simplifies
integrating Neptune into your applications.

- Added support for integrating [OpenSearch
  Serverless](../../../opensearch-service/latest/developerguide/serverless-overview.md "../../../opensearch-service/latest/developerguide/serverless-overview.md") with Neptune.

## Improvements in This Engine Release

**Improvements to Neptune engine updates**

Neptune has changed the way it releases engine updates so that you can have more
control over the update process. Instead of releasing patches for non-breaking changes,
Neptune now releases minor versions that can be controlled [using
the AutoMinorVersionUpgrade instance field](engine-maintenance-management.md#using-amvu "engine-maintenance-management.md#using-amvu"), and about which you can
receive notifications by [subscribing](events-subscribing.md "events-subscribing.md") to the
[RDS-EVENT-0156](event-lists.md#RDS-EVENT-0156 "event-lists.md#RDS-EVENT-0156") event.

See [Maintaining your Amazon Neptune DB Cluster](cluster-maintenance.md "cluster-maintenance.md")
for more information about these changes.

**Encryption in transit improvement**

Neptune no longer supports the following cipher suites:

- `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`
- `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`

Neptune only supports the following strong cipher suites with TLS 1.2:

- `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`
- `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`
- `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`
- `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`

###### Gremlin Improvements

- Added support in the DFE engine for the following Gremlin steps:
  - `FoldStep`
  - `GroupStep`
  - `GroupCountStep`
  - `TraversalMapStep`
  - `UnfoldStep`
  - `LabelStep`
  - `PropertyKeyStep`
  - `PropertyValueStep`
  - `AndStep`
  - `OrStep`
  - `ConstantStep`
  - `CountGlobalStep`

- Optimized Gremlin DFE query plans to avoid full vertex scans when using
  `by()` modulation.
- Significantly improved performance of low cardinality and low latency queries.
- Added DFE support for TinkerPop `Or` filter predicates.
- Improved DFE support of traversal for filters on the same key, for queries like
  the following:

```
g.withSideEffect("Neptune#useDFE", true)
 .V()
 .has('name', 'marko')
 .and(
   or(
     has('name', eq("marko")),
     has('name', eq("vardas"))
   )
 )
```

- Improved error handling for the `fail()` step.

###### openCypher improvements

- Significantly improved performance of low cardinality and low latency queries.
- Improved query planning performance when query contains many node types.
- Reduced latency of all VLP queries.
- Improved performance by removing redundant pipeline joins for single node pattern queries.
- Improved performance for queries that contain multi-hop patterns with cycles, like
  this one:

```
MATCH (n)-->()-->()-->(m)
RETURN n m
```

###### SPARQL improvements

- Introduced a new SPARQL operator: `PipelineHashIndexJoin`.
- Improved performance of URI validation for SPARQL queries.
- Improved performance of SPARQL full-text search queries by batch resolving dictionary
  terms.

## Defects Fixed in This Engine Release

###### Gremlin fixes

- Fixed a Gremlin bug where a transaction leak would occur when checking
  the Gremlin query status endpoint for queries with predicates in child traversals
  for steps that are not processed natively in the DFE engine.
- Fixed a Gremlin bug where `valueMap()` was not optimized in
  the DFE engine under `by()` traversals.
- Fixed a Gremlin bug where a step label attached to `UnionStep`
  was not propagated to the last path element of its child traversals respectively.
- Fixed a Gremlin bug where a query would fail because it contained too many
  TinkerPop steps and then would not be cleaned up.
- Fixed a Gremlin bug where a `NullPointerException`
  would be thrown in `mergeV` and `mergeE` steps.
- Fixed a Gremlin bug where `order()` would not properly sort
  string outputs when some of them contained a space character.
- Fixed a Gremlin correctness issue that occurred when the `valueMap` step
  was processed in the DFE engine.
- Fixed a Gremlin correctness issue that occurred when `GroupStep`
  or `GroupCountStep` was nested in a key traversal.

###### openCypher fixes

- Fixed an openCypher bug involving error handling around NULL characters.
- Fixed a bug in openCypher Bolt transaction handling.

###### SPARQL fixes

- Fixed a SPARQL bug where values inside recursive functions were
  not properly resolved.
- Fixed a SPARQL bug that caused performance degredation when a large
  number of values were injected using the `VALUES` clause.
- Fixed a SPARQL bug where a call to the `REGEX` operator
  on a language-tagged literal would never succeed.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.3.0.0, make sure that your project is compatible
with these query-language versions:

- _Gremlin earliest version supported:_ `3.6.2`
- _Gremlin latest version supported:_ `3.6.4`
- _openCypher version:_ `Neptune-9.0.20190305-1.0`
- _SPARQL version:_ `1.1`

## Upgrade Paths to Engine Release 1.3.0.0

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
    --engine-version 1.3.0.0 \
    --allow-major-version-upgrade \
    --apply-immediately
```

For Windows:

```
aws neptune modify-db-cluster ^
    --db-cluster-identifier `(your-neptune-cluster)` ^
    --engine-version 1.3.0.0 ^
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
