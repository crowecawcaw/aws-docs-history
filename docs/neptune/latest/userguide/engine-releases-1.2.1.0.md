# Amazon Neptune Engine Version 1.2.1.0.R2 (2023-05-02)

As of 2023-05-02, engine version 1.2.1.0.R2 is being generally deployed. Please note
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

## Improvements in This Engine Release

- Added an `enableInterContainerTrafficEncryption`
  parameter to all [Neptune
  ML APIs](machine-learning-api-reference.md "machine-learning-api-reference.md"), that you can use to enable and disable inter-container traffic
  encryption in training or hyper-parameter tuning jobs.
- Added multi-label support for Gremlin `mergeV()` and
  `mergeE()`.

## Defects Fixed in This Engine Release

- Fixed an openCypher bug where update and return queries did not handle
  `orderBy`, `limit`, or `skip` properly.
- Fixed an openCypher bug that allowed parameters contained in one request
  to be overridden by parameters contained in another simultaneous request.
- Fixed an openCypher bug where slow query logs did not contain correct
  query times.
- Fixed a Gremlin bug where a transaction leak could occur when a query
  containing `GroupCountStep` was submitted as a string.
- Fixed a Gremlin bug where WebSocket queries were failing when
  slow query logs were enabled.
- Fixed a Gremlin bug where storage-counter debug logs were missing
  in the slow query logs for WebSocket requests.
- Fixed several Gremlin bugs involving `mergeV()`
  and `mergeE()`.
- Fixed a SPARQL bug where named graph query costs were mis-estimated,
  leading to sub-optimal query plans and out-of-memory errors.
- Fixed a bug that affected authorization for Gremlin
  and openCypher queries on an IAM-enabled cluster.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.2.1.0.R2, make sure that your project is compatible
with these query-language versions:

- _Gremlin earliest version supported:_ `3.6.2`
- _Gremlin latest version supported:_ `3.6.2`
- _openCypher version:_ `Neptune-9.0.20190305-1.0`
- _SPARQL version:_ `1.1`

## Upgrade Paths to Engine Release 1.2.1.0.R2

## Upgrading to This Release

Amazon Neptune 1.2.1.0.R2 is now generally available.

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
