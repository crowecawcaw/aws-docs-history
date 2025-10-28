# Amazon Neptune Engine Version 1.0.3.0 (2020-08-03)

As of 2020-08-03, engine version 1.0.3.0 is being generally deployed. Please note
that it takes several days for a new release to become available in every region.

## Subsequent Patch Releases for This Release

- [Release: 1.0.3.0.R2 (2020-10-12)](engine-releases-1.0.3.0.md "engine-releases-1.0.3.0.md")
- [Release: 1.0.3.0.R3 (2021-02-19)](engine-releases-1.0.3.0.md "engine-releases-1.0.3.0.md")

## New Features in This Engine Release

- Neptune has introduced a new, alternative query engine (DFE)
  which can significantly speed up query execution. See [The Amazon Neptune alternative query engine (DFE)](neptune-dfe-engine.md "neptune-dfe-engine.md").
- The DFE relies on pre-generated statistics about your
  Neptune graph data that are managed through new statistics endpoints. See
  [DFE statistics](neptune-dfe-statistics.md "neptune-dfe-statistics.md").
- You can now exclude queued load jobs from the list of load IDs
  returned by the Loader Get-Status API by setting the new `includeQueuedLoads`
  parameter to FALSE. See [Neptune Loader Get-Status request parameters](load-api-reference-status-requests.md#load-api-reference-status-parameters "load-api-reference-status-requests.md#load-api-reference-status-parameters").
- Neptune now supports trailing headers for SPARQL query responses
  that can contain an error code and message if a request fails after it begins to
  return response chunks. See [Optional HTTP trailing headers for multi-part SPARQL responses](access-graph-sparql-http-trailing-headers.md "access-graph-sparql-http-trailing-headers.md").
- Neptune now also lets you enable chunked response encoding for
  Gremlin queries. As in the SPARQL case, the response chunks have trailing headers
  that can contain an error code and message if a failure occurs after the query has
  begun to return response chunks. See [Use optional HTTP
  trailing headers to enable multi-part Gremlin responses](access-graph-gremlin-rest-trailing-headers.md "access-graph-gremlin-rest-trailing-headers.md").

## Improvements in This Engine Release

- You can now provide the size of batch requests to ElasticSearch for full-
  text searches in Gremlin.
- Improved memory usage for SPARQL GROUP BY queries.
- Added a new Gremlin query optimizer to prune certain unbound filters.
- Increased the maximum time a WebSocket connection authenticated
  using IAM can stay open, from 36 hours to 10 days.

## Defects Fixed in This Engine Release

- Fixed a bug where if you sent an un-encoded URL parameter in a POST
  request, Neptune returned an HTTP status code of 500 and an `InternalServerErrorException`.
  Now Neptune returns an HTTP status code of 400 and a `BadRequestException`,
  with the message: `Failure to process the POST request parameters`.
- Fixed a Gremlin bug where a WebSocket connection failure was not
  correctly reported.
- Fixed a Gremlin bug involving disappearing sideEffects.
- Fixed a Gremlin bug where the full-text search `batchsize`
  parameter was not properly supported.
- Fixed a Gremlin bug to handle `toV` and `fromV`
  individually for each direction on `bothE`.
- Fixed a Gremlin bug involving `Edge pathType`
  in the `hasLabel` step.
- Fixed a SPARQL bug where join re-ordering with static bindings was
  not working correctly.
- Fixed a SPARQL UPDATE LOAD bug where an unavailable Amazon S3 bucket was not
  correctly reported.
- Fixed a SPARQL bug where an issue with a SERVICE node in a subquery was not
  correctly reported.
- Fixed a SPARQL bug in which queries containing nested FILTER EXISTS or
  FILTER NOT EXISTS conditions were not being properly evaluated.
- Fixed a SPARQL bug to correctly handle duplicate generated bindings
  when calling SPARQL Service endpoints through generate queries.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.0.3.0, make sure that your project is compatible
with these query-language versions:

- _Gremlin version:_ `3.4.3`
- _SPARQL version:_ `1.1`

## Upgrade Paths to Engine Release 1.0.3.0

You can manually upgrade any previous Neptune engine release to this release.

If your cluster has its `AutoMinorVersionUpgrade` parameter set to `True`,
your cluster will be upgraded to this engine release automatically two to three weeks after
the date of this release, during a maintenance window.

## Upgrading to This Release

Amazon Neptune 1.0.3.0 is now generally available.

If a DB cluster is running an engine version from which there is an upgrade path
to this release, it is eligible to be upgraded now. You can upgrade any eligible cluster
using the DB cluster operations on the console or by using the SDK. The following CLI
command will upgrade an eligible cluster immediately:

For Linux, OS X, or Unix:

```
aws neptune modify-db-cluster \
    --db-cluster-identifier `(your-neptune-cluster)` \
    --engine-version 1.0.3.0 \
    --apply-immediately
```

For Windows:

```
aws neptune modify-db-cluster ^
    --db-cluster-identifier `(your-neptune-cluster)` ^
    --engine-version 1.0.3.0 ^
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
