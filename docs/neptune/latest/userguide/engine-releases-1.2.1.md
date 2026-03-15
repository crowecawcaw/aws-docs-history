# Amazon Neptune Engine Version 1.2.1.0 (2023-03-08)

As of 2023-03-08, engine version 1.2.1.0 is being generally deployed. Please note
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

## Subsequent Patch Releases for This Release

- [Release: 1.2.1.0.R2 (2023-05-02)](engine-releases-1.2.1.0.md "engine-releases-1.2.1.0.md")
- [Release: 1.2.1.0.R3 (2023-06-13)](engine-releases-1.2.1.0.md "engine-releases-1.2.1.0.md")
- [Release: 1.2.1.0.R4 (2023-08-10)](engine-releases-1.2.1.0.md "engine-releases-1.2.1.0.md")
- [Release: 1.2.1.0.R5 (2023-09-02)](engine-releases-1.2.1.0.md "engine-releases-1.2.1.0.md")
- [Release: 1.2.1.0.R6 (2023-09-12)](engine-releases-1.2.1.0.md "engine-releases-1.2.1.0.md")
- [Release: 1.2.1.0.R7 (2023-10-06)](engine-releases-1.2.1.0.md "engine-releases-1.2.1.0.md")

## New Features in This Engine Release

- Added support for [TinkerPop 3.6.2](https://tinkerpop.apache.org/docs/3.6.2-SNAPSHOT/dev/provider/ "https://tinkerpop.apache.org/docs/3.6.2-SNAPSHOT/dev/provider/"), which
  adds many new Gremlin features such as the new `mergeV()`, `mergeE()`,
  `element()`, and `fail()` steps. The `mergeV()` and
  `mergeE()` steps are of particular note as they offer a long-awaited
  declarative option for performing upsert-like operations, which should greatly
  simplify existing code patterns and make Gremlin easier to read. The 3.6.x
  version also added regex predicates, a new overload to the `property()`
  step which takes a `Map`, and a major revision of `by()`
  modulation behavior that is far more consistent across all steps which use it.

See the [TinkerPop
change log](https://github.com/apache/tinkerpop/blob/3.6.0/CHANGELOG.asciidoc#release-3-6-0 "https://github.com/apache/tinkerpop/blob/3.6.0/CHANGELOG.asciidoc#release-3-6-0") and [upgrade
page](https://tinkerpop.apache.org/docs/current/upgrade/ "https://tinkerpop.apache.org/docs/current/upgrade/") for information about the changes in version 3.6 and things to consider
when upgrading.

If you are using `fold().coalesce(unfold(), <mutate>)`
for conditional inserts, we recommend that you migrate to the new `mergeV/E()`
syntax, described [here](https://tinkerpop.apache.org/docs/3.6.0/reference/#mergevertex-step "https://tinkerpop.apache.org/docs/3.6.0/reference/#mergevertex-step") and [here](https://tinkerpop.apache.org/docs/3.6.0/reference/#mergeedge-step "https://tinkerpop.apache.org/docs/3.6.0/reference/#mergeedge-step").
Neptune uses a narrower locking pattern for `Merge` than for `Coalesce`,
which can reduce concurrent modification exceptions (CMEs).

For more information about the new features available in this TinkerPop release,
see Stephen Mallette's blog,
[Exploring
new features of Apache TinkerPop 3.6.x in Amazon Neptune](https://aws.amazon.com/blogs/database/exploring-new-features-of-apache-tinkerpop-3-6-x-in-amazon-neptune/ "https://aws.amazon.com/blogs/database/exploring-new-features-of-apache-tinkerpop-3-6-x-in-amazon-neptune/").

- Added support for [R6i
  instance types](https://aws.amazon.com/ec2/instance-types/r6i/ "https://aws.amazon.com/ec2/instance-types/r6i/"), powered by 3rd-generation Intel Xeon Scalable processors.
  These are an ideal fit for memory-intensive workloads and offer up to 15% better
  compute/price performance and up to 20% higher memory bandwidth per vCPU than
  comparable R5 instance types.
- Added [graph summary API](neptune-graph-summary.md "neptune-graph-summary.md")
  endpoints for both property graphs and RDF graphs, that let you get a fast
  summary report about your graph.

For property (PG) graphs, the graph summary API provides a read-only
list of node and edge labels and property keys, along with counts of
nodes, edges, and properties. For RDF graphs, it provides a list of
classes and predicate keys, along with counts of quads, subjects, and
predicates.

The following changes went along with the new graph summary API:

    + Added a new [GetGraphSummary](iam-dp-actions.md#getgraphsummary "iam-dp-actions.md#getgraphsummary")
     dataplane action.
    + Added a new `rdf/statistics` endpoint to replace
     the `sparql/statistics` endpoint, which is now deprecated.
    + Changed the name of the `summary` field in
     the statistics status response to `signatureInfo`, so as not
     to confuse it with graph summary information. Previous engine versions
     continue to use `summary` in the JSON response.
    + Changed the precision of the `date` field in
     the statistics status response from minute to millisecond. The previous
     format was `2020-05-07T23:13Z` (minute precision), while
     the new format is `2023-01-24T00:47:43.319Z` (millisecond
     precision). Both are ISO 8601 compliant, but this change may break
     existing code, depending on how the date is being parsed.
    + Added a new [%statistics](notebooks-magics.md#notebooks-line-magics-statistics "notebooks-magics.md#notebooks-line-magics-statistics")
     line magic in the Workbench that lets you retrieve DFE engine statistics.
    + Added a new [%summary](notebooks-magics.md#notebooks-line-magics-summary "notebooks-magics.md#notebooks-line-magics-summary")
     line magic in the Workbench that lets you retrieve graph summary information.

- Added [slow-query logging](slow-query-logs.md "slow-query-logs.md") to log
  queries that take longer to execute than a specified threshold. You enable and control
  slow-query logging using the two new dynamic parameters, namely [neptune_enable_slow_query_log](parameters.md#parameters-db-cluster-parameters-neptune_enable_slow_query_log "parameters.md#parameters-db-cluster-parameters-neptune_enable_slow_query_log"), and [neptune_slow_query_log_threshold](parameters.md#parameters-db-cluster-parameters-neptune_slow_query_log_threshold "parameters.md#parameters-db-cluster-parameters-neptune_slow_query_log_threshold").
- Added support for two [dynamic
  parameters](parameter-groups.md "parameter-groups.md"), namely the new cluster parameters, [neptune_enable_slow_query_log](parameters.md#parameters-db-cluster-parameters-neptune_enable_slow_query_log "parameters.md#parameters-db-cluster-parameters-neptune_enable_slow_query_log"), and [neptune_slow_query_log_threshold](parameters.md#parameters-db-cluster-parameters-neptune_slow_query_log_threshold "parameters.md#parameters-db-cluster-parameters-neptune_slow_query_log_threshold").
  When you make a change to a dynamic parameter, it takes effect immediately,
  without requiring any instance reboot.
- Added a Neptune-specific openCypher [removeKeyFromMap()](access-graph-opencypher-extensions.md#opencypher-compliance-removeKeyFromMap-function "access-graph-opencypher-extensions.md#opencypher-compliance-removeKeyFromMap-function")
  function that removes a specified key from a map and returns the resulting new
  map.

## Improvements in This Engine Release

- Extended Gremlin DFE support to `limit` steps with local
  scope.
- Added `by()` modulation support for the Gremlin
  `DedupGlobalStep` in the DFE engine.
- Added DFE support for Gremlin `SelectStep` and
  `SelectOneStep`.
- Performance improvements and correctness fixes for various Gremlin
  operators, including `repeat`, `coalesce`, `store`,
  and `aggregate`.
- Improved performance of openCypher queries involving `MERGE`
  and `OPTIONAL MATCH`.
- Improved performance of openCypher queries involving `UNWIND`
  of a list of maps of literal values.
- Improved performance of openCypher queries that have an `IN`
  filter for `id`. For example:

```
MATCH (n) WHERE id(n) IN ['1', '2', '3'] RETURN n
```

- Added the ability to specify the base IRI for SPARQL queries using
  the BASE statement (see [Default base IRI for queries and updates](feature-sparql-compliance.md#opencypher-compliance-default-iri "feature-sparql-compliance.md#opencypher-compliance-default-iri")).
- Shortened the load processing wait time for Gremlin and openCypher
  edge-only bulk loads.
- Made bulk loads resume asynchronously when Neptune restarts to
  avoid a lengthy wait time caused by Amazon S3 connectivity issues before failing resume
  attempts.
- Improved handling of SPARQL DESCRIBE queries that have the
  [describeMode](sparql-query-hints-for-describe.md#sparql-query-hints-describeMode "sparql-query-hints-for-describe.md#sparql-query-hints-describeMode") query
  hint set to `"CBD"` (concise bounded description) and that involve
  a large number of blank nodes.

## Defects Fixed in This Engine Release

- Fixed an openCypher bug where queries returned the string, `"null"`,
  instead of a null value in Bolt and SPARQL-JSON.
- Fixed an openCypher bug in list comprehension that produced a null value
  rather than the values provided for the list elements.
- Fixed an openCypher bug where byte values were not correctly serialized.
- Fixed a Gremlin bug in `UnionStep` that occurred when
  an input was an edge traversing to a vertex inside a child traversal.
- Fixed a Gremlin bug that caused a step label associated with
  `UnionStep` not to propagate correctly to the last step of each
  child traversal.
- Fixed a Gremlin bug for the `dedup` step with labels
  following a `repeat` step, where the labels attached to the
  `dedup` step weren't available to use in query further.
- Fixed a Gremlin bug where translating the `repeat`
  step inside a `union` step failed with an internal error.
- Fixed Gremlin correctness issues for DFE queries with `limit`
  as a child traversal of non-union steps by falling back to Tinkerpop.
  Queries in a form like this are affected:

```
g.withSideEffect('Neptune#useDFE', true).V().as("a").select("a").by(out().limit(1))
```

- Fixed a SPARQL bug where `SPARQL GRAPH` patterns would
  not consider the dataset supplied by a `FROM NAMED` clause.
- Fixed a SPARQL bug where SPARQL `DESCRIBE` with some
  `FROM` and/or `FROM NAMED` clauses did not always correctly
  use data from the default graph and sometimes threw an exception. See [SPARQL DESCRIBE behavior with respect to the default graph](sparql-default-describe.md "sparql-default-describe.md").
- Fixed a SPARQL bug so that the correct exception message is returned
  when null characters are rejected.
- Fixed a SPARQL [explain](sparql-explain.md "sparql-explain.md") bug
  that affected plans containing a [PipelinedHashIndexJoin](sparql-explain-operators.md#sparql-explain-operator-pipeline-hash-index-join "sparql-explain-operators.md#sparql-explain-operator-pipeline-hash-index-join")
  operator.
- Fixed a bug that caused an internal error to be thrown when a query
  that returns a constant value was submitted.
- Fixed an issue with deadlock detector logic that occasionally made
  the engine unresponsive.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.2.1.0, make sure that your project is compatible
with these query-language versions:

- _Gremlin earliest version supported:_ `3.6.2`
- _Gremlin latest version supported:_ `3.6.2`
- _openCypher version:_ `Neptune-9.0.20190305-1.1`
- _SPARQL version:_ `1.1`

## Upgrade Paths to Engine Release 1.2.1.0

You can manually upgrade to this release from any previous Neptune
engine release greater than or equal to [1.1.0.0](engine-releases-1.1.0.md "engine-releases-1.1.0.md").

###### Note

Starting with [engine release 1.2.0.0](engine-releases-1.2.0.md "engine-releases-1.2.0.md"),
all custom parameter groups and custom cluster parameter groups that you were using
with engine versions earlier than `1.2.0.0` must now be re-created using
parameter group family `neptune1.2`. Previous releases used parameter group
family `neptune1`, and those parameter groups will not work with
releases from `1.2.0.0` onwards. See [Amazon Neptune parameter groups](parameter-groups.md "parameter-groups.md") for more information.

You will not be automatically upgraded to this major version release.

## Upgrading to This Release

Amazon Neptune 1.2.1.0 is now generally available.

If a DB cluster is running an engine version from which there is an upgrade path
to this release, it is eligible to be upgraded now. You can upgrade any eligible cluster
using the DB cluster operations on the console or by using the SDK. The following CLI
command will upgrade an eligible cluster immediately:

For Linux, OS X, or Unix:

```
aws neptune modify-db-cluster \
    --db-cluster-identifier `(your-neptune-cluster)` \
    --engine-version 1.2.1.0 \
    --apply-immediately
```

For Windows:

```
aws neptune modify-db-cluster ^
    --db-cluster-identifier `(your-neptune-cluster)` ^
    --engine-version 1.2.1.0 ^
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
