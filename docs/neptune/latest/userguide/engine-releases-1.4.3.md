# Amazon Neptune Engine version 1.4.3.0 (2025-01-21)

As of 2025-01-21, engine version 1.4.3.0 is being generally deployed. Please note
that it takes several days for a new release to become available in every region.

###### Warning

The query plan cache is temporarily unsupported for the use case of executing parameterized queries involving numeric
parameter values, due to a bug in handling duplicate usages of a numeric type parameter in the query. For example:

```
MATCH (n:movie) WHERE n.runtime>=$minutes RETURN n
      UNION
      MATCH (n:show) WHERE n.duration>=$minutes RETURN n

      parameters={"minutes":130}
```

Queries that do a lot of index searches on statements or dictionary indices could see a 5% performance regression. For
example - getting a count of all vertices, or getting the `id` of all vertices would not be affected. Getting
all properties of all vertices could see up to a 5% regression.

## New features in this engine release

- [Exporting Gremlin query results to Amazon S3](exporting-gremlin.md "exporting-gremlin.md"). Exporting Gremlin query results directly
  to Amazon S3. This feature allows you to handle large query results efficiently by exporting them to an Amazon S3
  bucket, instead of returning them as query response.

```
g.V().
    hasLabel('Comment').
    valueMap().
    call('neptune.query.exportToS3', [
    'destination': 's3://`your-bucket/path/`result.json',
    'format': 'GraphSONv3',
    'keyArn': '`optional-kms-key-arn`'
  ])
```

- **R7i instances**. R7i instance family, up to 48xlarge, are now available in the following
  regions:
  - ap-northeast-1 - Asia Pacific (Tokyo)
  - ap-northeast-2 - Asia Pacific (Seoul)
  - ap-south-1 - Asia Pacific (Mumbai)
  - ap-southeast-1 - Asia Pacific (Singapore)
  - ap-southeast-2 - Asia Pacific (Sydney)
  - ap-southeast-3 - Asia Pacific (Jakarta)
  - ca-central-1 - Canada (Central)
  - eu-central-1 - Europe (Frankfurt)
  - eu-north-1 - Europe (Stockholm)
  - eu-south-2 - Europe (Spain)
  - eu-west-1 - Europe (Ireland)
  - eu-west-2 - Europe (London)
  - eu-west-3 - Europe (Paris)
  - us-east-1 - US East (N. Virginia)
  - us-east-2 - US East (Ohio)
  - us-west-1 - US West (N. California)
  - us-west-2 - US West (Oregon)

## Improvements in this engine release

###### General Improvements

- Lab mode support for dictionary garbage collection (GC).

When enabled, the unused dictionary entries are cleaned up by a background job. It does not reduce
`VolumeBytesUsed`, it frees up space in the index for new inserts. The rate of growth in
`VolumeBytesUsed` is likely to be less when dictionary GC is enabled relative to when it is not.
This works for property graph data (inserted via Gremlin or openCypher) when the `neptune_streams`
parameter is not enabled. For more information, see [Neptune dictionary garbage collection](storage-gc.md "storage-gc.md")

## Defects fixed in this engine release

###### General fixes

- Fixed two memory leak issues affecting FreeableMemory when DFE engine used.

###### openCypher fixes

- Resolve issue with MERGE ON MATCH / ON CREATE for duplicate rows.

```
UNWIND [1, 1] AS id
MERGE (n:Person {id: id})
  ON CREATE SET n.p = 5
  ON MATCH SET n.p = 6
```

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.4.3.0, make sure that your project is compatible
with these query-language versions:

- _Gremlin earliest version supported:_ `3.7.1`
- _Gremlin latest version supported:_ `3.7.1`
- _openCypher version:_ `Neptune-9.0.20190305-1.0`
- _SPARQL version:_ `1.1`

## Upgrade paths to engine release 1.4.3.0

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
    --engine-version 1.4.3.0 \
    --allow-major-version-upgrade \
    --apply-immediately
```

For Windows:

```
aws neptune modify-db-cluster ^
    --db-cluster-identifier `(your-neptune-cluster)` ^
    --engine-version 1.4.3.0 ^
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
