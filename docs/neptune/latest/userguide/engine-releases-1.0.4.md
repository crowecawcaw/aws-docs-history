# Amazon Neptune Engine Version 1.0.4.1 (2020-12-08)

As of 2020-12-08, engine version 1.0.4.1 is being generally deployed. Please note
that it takes several days for a new release to become available in every region.

## Subsequent Patch Releases for This Release

- [Release: 1.0.4.1.R1.1 (2021-03-22)](engine-releases-1.0.4.1.R1.md "engine-releases-1.0.4.1.R1.md")
- [Release: 1.0.4.1.R2 (2021-02-24)](engine-releases-1.0.4.1.md "engine-releases-1.0.4.1.md")

###### Important

[Release: 1.0.4.0 (2020-10-12)](engine-releases-1.0.4.md "engine-releases-1.0.4.md")
made TLS 1.2 and HTTPS mandatory for all connections to Amazon Neptune. However, a bug in
that release has allowed HTTP connections and/or outdated TLS connections to continue
to work for customers who previously set a DB cluster parameter to prevent enforcement
of HTTPS connections.

That bug was fixed in patch releases [1.0.4.0.R2](engine-releases-1.0.4.0.md "engine-releases-1.0.4.0.md")
and [1.0.4.1.R2](engine-releases-1.0.4.1.md "engine-releases-1.0.4.1.md"), but the fix has caused unexpected
connection failures when the patches are automatically installed. For this reason, both patches
have been reverted, and can only be installed manually, to give you a chance to update your setup
for TLS 1.2.

Having to use SSL/TLS for all connections to Neptune affects your connections with
the Gremlin console, the Gremlin driver, Gremlin Python, .NET, nodeJs, REST APIs, and also
load-balancer connections. If you have been using HTTP or an older TLS version for any
or all of these up until now, you must update the relevant client and drivers and change
your code to use HTTPS exclusively before updating your system to the latest patches.

## New Features in This Engine Release

- Introduced the Neptune ML feature, which brings powerful machine learning
  capabilities to Amazon Neptune. See [Amazon Neptune ML for machine learning on graphs](machine-learning.md "machine-learning.md").
- Added a custom SPARQL `UNLOAD` operation for removing data
  retrieved from a remote source. See [SPARQL UPDATE UNLOAD](sparql-api-reference-unload.md "sparql-api-reference-unload.md").

## Improvements in This Engine Release

- Optimized some Gremlin conditional insert patterns to avoid
  concurrent-modification exceptions.

## Defects Fixed in This Engine Release

- Fixed a Gremlin bug that could cause missing results for a specific
  pattern of queries that used the `as()` step.
- Fixed a Gremlin bug that could cause errors when using the
  `project()` step nested inside another step such as
  `union()`.
- Fixed a Gremlin bug in the `project()` step.
- Fixed a Gremlin bug in string-based traversal where the
  `none()` step did not work.
- Fixed a Gremlin bug in string-based traversal where an
  empty map was not supported as an arguent to the `inject()` step.
- Fixed a Gremlin bug in string-based traversal execution in
  the DFE engine where a terminal method such as `toList()` did
  not work properly.
- Fixed a Gremlin bug that failed to close transactions which used the
  `iterate()` step in String queries.
- Fixed a Gremlin bug that could cause queries using the
  `is(P.gte(0))` pattern to throw an exception in some situations.
- Fixed a Gremlin bug that could cause queries using the
  `order().by(T.id)` pattern to throw an exception in some situations.
- Fixed a Gremlin bug that could cause queries using the
  `addV().aggregate()` pattern to give incorrect results in some situations.
- Fixed a Gremlin bug that could cause queries
  using the `path()` step followed by the `project()` step
  pattern to throw an exception in some situations.
- Fixed a SPARQL bug where the `SUBSTR` function signals
  an error instead of returning an empty string.
- Fixed a bug in the DFE engine that could cause join operations
  in non-blocking query plans to generate incorrect results in the presence of
  unbound variables.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.0.4.1, make sure that your project is compatible
with these query-language versions:

- _Gremlin version:_ `3.4.8`
- _SPARQL version:_ `1.1`

## Upgrade Paths to Engine Release 1.0.4.1

Your cluster will be upgraded to this patch release automatically during your next
maintenance window if you are running engine version `1.0.4.1`.

You can manually upgrade any previous Neptune engine release to this release.

## Upgrading to This Release

Amazon Neptune 1.0.4.1 is now generally available.

If a DB cluster is running an engine version from which there is an upgrade path
to this release, it is eligible to be upgraded now. You can upgrade any eligible cluster
using the DB cluster operations on the console or by using the SDK. The following CLI
command will upgrade an eligible cluster immediately:

For Linux, OS X, or Unix:

```
aws neptune modify-db-cluster \
    --db-cluster-identifier `(your-neptune-cluster)` \
    --engine-version 1.0.4.1 \
    --apply-immediately
```

For Windows:

```
aws neptune modify-db-cluster ^
    --db-cluster-identifier `(your-neptune-cluster)` ^
    --engine-version 1.0.4.1 ^
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
