# Amazon Neptune Engine Version 1.0.2.0.R3 (2020-05-05)

## IMPORTANT: THIS ENGINE VERSION IS NOW DEPRECATED

Starting from 2020-05-19, no new instances using this engine version will be created.

This engine version is now superseded by [version
1.0.2.1](engine-releases-1.0.2.md "engine-releases-1.0.2.md"), which contains all the bug fixes in this version as well as
additional features such as full-text search integration, OSGP index support,
and database snapshot cluster copy across AWS Regions.

Starting June 1, 2020, Neptune will automatically upgrade any cluster running
this engine version to [the latest patch
of version 1.0.2.1](engine-releases-1.0.2.1.md "engine-releases-1.0.2.1.md") during the next maintenance window. You can upgrade manually
before then, as described [here](engine-releases-1.0.2.md "engine-releases-1.0.2.md").

If you have any issues with the upgrade, please contact us through [AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support") or the [AWS Developer Forums](https://forums.aws.amazon.com/forum.jspa?forumID=253 "https://forums.aws.amazon.com/forum.jspa?forumID=253").

## Defects Fixed in This Engine Release

- Fixed a bug where `ConcurrentModificationConflictException`
  and `TransactionException` were reported as generic
  `InternalFailureException`s.
- Fixed bugs in health checks that caused frequent restarts of
  the server during start up.
- Fixed a bug where data was not visible on replicas because commits
  were out of order under certain conditions.
- Fixed a bug in load-status serialization where a load failed
  from a lack of Amazon S3 access permissions.
- Fixed a resource leak in Gremlin sessions.
- Fixed a bug in health check that hid the unhealthy status on
  start-up of components managing IAM authentication.
- Fixed a bug where Neptune failed to send a WebSocket close frame
  before closing the channel.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.0.2.0.R3, make sure that your project is compatible
with these query-language versions:

- _Gremlin version:_ `3.4.1`
- _SPARQL version:_ `1.1`

## Upgrade Paths to Engine Release 1.0.2.0.R3

Your cluster will be upgraded to this patch release automatically during your next
maintenance window if you are running engine version `1.0.2.0`.

You can manually upgrade any earlier Neptune engine release to this release.

## Upgrading to This Release

Amazon Neptune 1.0.2.0.R3 is now generally available.

If a DB cluster is running an engine version from which there is an upgrade path
to this release, it is eligible to be upgraded now. You can upgrade any eligible cluster
using the DB cluster operations on the console or by using the SDK. The following CLI
command will upgrade an eligible cluster immediately:

For Linux, OS X, or Unix:

```
aws neptune modify-db-cluster \
    --db-cluster-identifier `(your-neptune-cluster)` \
    --engine-version 1.0.2.0 \
    --apply-immediately
```

For Windows:

```
aws neptune modify-db-cluster ^
    --db-cluster-identifier `(your-neptune-cluster)` ^
    --engine-version 1.0.2.0 ^
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
