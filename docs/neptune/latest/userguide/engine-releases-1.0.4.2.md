# Amazon Neptune Engine Version 1.0.4.2.R2 (2021-06-01)

As of 2021-06-01, engine version 1.0.4.2.R2 is being generally deployed. Please note
that it takes several days for a new release to become available in every region.

## Subsequent Patch Releases for This Release

- [Release: 1.0.4.2.R3 (2021-06-28)](engine-releases-1.0.4.2.md "engine-releases-1.0.4.2.md")

## Known issues in this engine release

**Issue:**

A SPARQL bug that fails to honor media type in an `Accept` header if
there are spaces present.

For example, a query with `-H "Accept: text/csv; q=1.0, */*; q=0.1"`
returns JSON output rather than CSV output.

**Workaround:**

If you remove the spaces in the `Accept` clause in the header, the engine
returns output in the correct requested format. In other words, instead of
`-H "Accept: text/csv; q=1.0, */*; q=0.1"` , use:

```
  -H "Accept: text/csv;q=1.0,*/*;q=0.1"
```

## New Features in This Engine Release

- Added the new R5d instance type, which includes a lookup cache
  for speeding up reads in use cases involving a high volume of property value
  or RDF literal lookups. See [The Neptune lookup cache can accelerate read queries](feature-overview-lookup-cache.md "feature-overview-lookup-cache.md").
- Added a new lab-mode parameter that lets the experimental DFE engine be
  invoked only on a per-query basis with the `useDFE` query hint.

## Improvements in This Engine Release

- Added support for TinkerPop 3.4.10.
- Added support for using the `withStrategies( )` configuration
  step when sending Gremlin script requests. Specifically, the `SubgraphStrategy`,
  `PartitionStrategy`, `ReadOnlyStrategy`, `EdgeLabelVerificationStrategy`,
  and `ReservedKeysVerificationStrategy` are all supported.
- Added optimization for `V()` traversals in the middle of a
  query. Previously, such traversals were not optimized in Neptune.
- Added support for [RFC
  2141 URNs](https://tools.ietf.org/html/rfc2141 "https://tools.ietf.org/html/rfc2141") to be used as the `baseUri` and `namedGraphUri`
  parameters for a bulk load.

## Defects Fixed in This Engine Release

- Fixed a Gremlin bug in the parser where incorrect queries were treated
  as valid.
- Fixed a Gremlin bug where unfolding an `aggregate()` side-effect
  with `cap().unfold()` to a `valueMap()` would raise an exception.
- Fixed a Gremlin bug where some `property()` steps after an
  `addV()` step fail with a "cannot cast to String" error.
- Fixed a Gremlin bug to prevent some conditional insert patterns
  from raising concurrent-modification exceptions.
- Fixed a Gremlin bug so that the query request timeout now cannot exceed
  the session timeout.
- Fixed a SPARQL bug where updates using LOAD or UNLOAD could fail with
  an HTTP code 500 instead of HTTP code 400 when the remote server is unavailable.
- Fixed a bug where stream API calls were failing when `commitNum`
  or `opNum` values larger than the 32-bit signed integer limit (2,147,483,647)
  were used.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.0.4.2.R2, make sure that your project is compatible
with these query-language versions:

- _Gremlin version:_ `3.4.10`
- _SPARQL version:_ `1.1`

## Upgrade Paths to Engine Release 1.0.4.2.R2

You can manually upgrade any previous Neptune engine release to this release.

You will not automatically upgrade to this release.

## Upgrading to This Release

Amazon Neptune 1.0.4.2.R2 is now generally available.

If a DB cluster is running an engine version from which there is an upgrade path
to this release, it is eligible to be upgraded now. You can upgrade any eligible cluster
using the DB cluster operations on the console or by using the SDK. The following CLI
command will upgrade an eligible cluster immediately:

For Linux, OS X, or Unix:

```
aws neptune modify-db-cluster \
    --db-cluster-identifier `(your-neptune-cluster)` \
    --engine-version 1.0.4.2 \
    --apply-immediately
```

For Windows:

```
aws neptune modify-db-cluster ^
    --db-cluster-identifier `(your-neptune-cluster)` ^
    --engine-version 1.0.4.2 ^
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
