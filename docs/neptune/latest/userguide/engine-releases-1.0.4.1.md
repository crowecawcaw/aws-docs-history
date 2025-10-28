# Amazon Neptune Engine Version 1.0.4.1.R2 (2021-02-24)

As of 2021-02-24, engine version 1.0.4.1.R2 is being generally deployed. Please note
that it takes several days for a new release to become available in every region.

## Subsequent Patch Releases for This Release

- [Release: 1.0.4.1.R2.1 (2021-03-11)](engine-releases-1.0.4.1.R2.md "engine-releases-1.0.4.1.R2.md")

## New Features in This Engine Release

- Neptune now supports compression of single files in `bzip2`
  format for bulk loads. See [Load Data Formats](bulk-load-tutorial-format.md "bulk-load-tutorial-format.md").

## Defects Fixed in This Engine Release

- Fixed a bug in [Release: 1.0.4.0 (2020-10-12)](engine-releases-1.0.4.md "engine-releases-1.0.4.md") that allowed connections to Neptune
  using `HTTP` or earlier versions of TLS, rather than `HTTPS`
  and TLS 1.2.

###### Important

**Having to use SSL/TLS for all connections to
Neptune can be a breaking change.** It affects your connections with the Gremlin
console, the Gremlin driver, Gremlin Python, .NET, nodeJs, REST APIs, and also
load-balancer connections. If you have been using HTTP or an older TLS version
for any or all of these up until now, you must update the relevant client and drivers
before installing this patch, and change your code to use HTTPS exclusively.

- Fixed a Gremlin bug where `InternalFailureException`
  was set as the response code in certain circumstances when a
  `ConcurrentModificationException` occurred.
- Fixed a Gremlin bug where under certain conditions updating
  edges or vertices could cause a transient `InternalFailureException`.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.0.4.1.R2, make sure that your project is compatible
with these query-language versions:

- _Gremlin version:_ `3.4.8`
- _SPARQL version:_ `1.1`

## Upgrade Paths to Engine Release 1.0.4.1.R2

Your cluster will be upgraded to this patch release automatically during your next
maintenance window if you are running engine version `1.0.4.1`.

## Upgrading to This Release

Amazon Neptune 1.0.4.1.R2 is now generally available.

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
