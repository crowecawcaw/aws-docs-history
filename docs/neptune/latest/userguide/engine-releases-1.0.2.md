# Amazon Neptune Engine Version 1.0.2.2 (2020-03-09)

As of 2020-03-09, engine version 1.0.2.2 is being generally deployed. Please note
that it takes several days for a new release to become available in every region.

## Subsequent Patch Releases for This Release

- [Release: 1.0.2.2.R2 (2020-04-02)](engine-releases-1.0.2.2.md "engine-releases-1.0.2.2.md")
- [Release: 1.0.2.2.R3 (2020-07-22)](engine-releases-1.0.2.2.md "engine-releases-1.0.2.2.md")
- [Release: 1.0.2.2.R4 (2020-07-23)](engine-releases-1.0.2.2.md "engine-releases-1.0.2.2.md")
- [Release: 1.0.2.2.R5 (2020-10-12)](engine-releases-1.0.2.2.md "engine-releases-1.0.2.2.md")
- [Release: 1.0.2.2.R6 (2021-02-19)](engine-releases-1.0.2.2.md "engine-releases-1.0.2.2.md")

## Improvements in This Engine Release

- Added information to the status API about transactions that are
  being rolled back. See [Instance Status](access-graph-status.md "access-graph-status.md").
- Upgraded the version of Apache TinkerPop to 3.4.3.

Version 3.4.3 is backwards compatible with the previous version
supported by Neptune (3.4.1). It does introduce one minor change in
behavior: Gremlin no longer returns an error when you try to close
a session that does not exist (see [Prevent error
when closing sessions that don't exist](https://issues.apache.org/jira/browse/TINKERPOP-2237 "https://issues.apache.org/jira/browse/TINKERPOP-2237")).

- Removed performance bottlenecks in execution of Gremlin full-text
  search steps.

## Defects Fixed in This Engine Release

- Fixed a SPARQL bug in the handling of empty graph patterns in queries.
- Fixed a SPARQL bug in the handling of unencoded semicolons in URL-encoded queries.
- Fixed a Gremlin bug in the handling of repeated vertices in the `Union` step.
- Fixed a Gremlin bug that caused some queries with a `.simplePath()` or
  `.cyclicPath()` inside a `.repeat()` to return incorrect results.
- Fixed a Gremlin bug that caused `.project()` to return incorrect results
  if its child traversal returned no solutions.
- Fixed a Gremlin bug where errors from read-write conflicts raised an
  `InternalFailureException` rather than a `ConcurrentModificationException`.
- Fixed a Gremlin bug that caused `.group().by(...).by(values("property"))`
  failures.
- Fixed Gremlin bugs in the profile output for full-text-search steps.
- Fixed a resource leak in Gremlin sessions.
- Fixed a bug that prevented the status API from reporting the correct orderable
  version in some cases.
- Fixed a bulk loader bug that allowed a URL to a location other than
  Amazon S3 to be used as the source in a bulk load request.
- Fixed a bulk loader bug in the detailed load status.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.0.2.2, make sure that your project is compatible
with these query-language versions:

- _Gremlin version:_ `3.4.3`
- _SPARQL version:_ `1.1`

## Upgrade Paths to Engine Release 1.0.2.2

You can manually upgrade any previous Neptune engine release to this release.

If your cluster has its `AutoMinorVersionUpgrade` parameter set to `True`,
your cluster will be upgraded to this engine release automatically two to three weeks after
the date of this release, during a maintenance window.

## Upgrading to This Release

Amazon Neptune 1.0.2.2 is now generally available.

If a DB cluster is running an engine version from which there is an upgrade path
to this release, it is eligible to be upgraded now. You can upgrade any eligible cluster
using the DB cluster operations on the console or by using the SDK. The following CLI
command will upgrade an eligible cluster immediately:

For Linux, OS X, or Unix:

```
aws neptune modify-db-cluster \
    --db-cluster-identifier `(your-neptune-cluster)` \
    --engine-version 1.0.2.2 \
    --apply-immediately
```

For Windows:

```
aws neptune modify-db-cluster ^
    --db-cluster-identifier `(your-neptune-cluster)` ^
    --engine-version 1.0.2.2 ^
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
