# Amazon Neptune Engine version 1.4.6.0 (2025-09-02)

As of 2025-09-02, engine version 1.4.6.0 is being generally deployed. Please note
that it takes several days for a new release to become available in every region.

###### Warning

The 1.4.6.0 engine version includes new network checks for clusters that are using non-RFC 1918 conforming private IP
ranges for database VPC without IAM authentication. If you have this VPC and IAM configuration, you will need to
update your database VPC to use RFC 1918 private IP ranges and/or enable IAM authentication to avoid errors with
queries after upgrading to 1.4.6.0.

## New features in this engine release

- Connect to Neptune using public endpoints. For more information see
  [Neptune public endpoints](neptune-public-endpoints.md "neptune-public-endpoints.md").

## Improvements in this engine release

###### General Improvements

- Improved SPARQL performance for update operations.
- Improved OpenCypher performance for `CREATE`, `MERGE`, and `SET` (mutations) operations.
- Improved OpenCypher performance for CALL Subquery operations.

## Defects fixed in this engine release

###### Gremlin fixes

- Connections to Gremlin sessions must occur on the same channel that created
  them, meaning that it is not possible to connect multiple client instances to the same session.
- Gremlin sessions have always closed when the client closes, but they will now
  also close for a server initiated close of the connection which prevents an unintended or unexpected re-connection.

###### openCypher fixes

- Fixed variable handling after a `CALL` subquery.

###### SPARQL fixes

- Fixed an error message for SPARQL `LOAD/UNLOAD` when the remote source is unavailable.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.4.6.0, make sure that your project is compatible
with these query-language versions:

- _Gremlin earliest version supported:_ `3.7.1`
- _Gremlin latest version supported:_ `3.7.1`
- _openCypher version:_ `Neptune-9.0.20190305-1.0`
- _SPARQL version:_ `1.1`

## Upgrade paths to engine release 1.4.6.0

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
    --engine-version 1.4.6.0 \
    --allow-major-version-upgrade \
    --apply-immediately
```

For Windows:

```
aws neptune modify-db-cluster ^
    --db-cluster-identifier `(your-neptune-cluster)` ^
    --engine-version 1.4.6.0 ^
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
