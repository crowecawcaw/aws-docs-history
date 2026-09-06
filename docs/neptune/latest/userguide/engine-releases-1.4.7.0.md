

# Amazon Neptune Engine version 1.4.7.0 (2026-03-03)
<a name="engine-releases-1.4.7.0"></a>

As of 2026-03-03, engine version 1.4.7.0 is being generally deployed. Please note that it takes several days for a new release to become available in every region.

## New Features in This Engine Release
<a name="engine-releases-1470-features"></a>
+ openCypher read from S3 support for Parquet and CSV files via OC. See the [neptune.read()](access-graph-opencypher-21-extensions-s3-read.md) documentation. 
+ openCypher geospatial query functions. This release includes 12 Spatial Types functions based on the ISO/IEC 13249-3:2016 standard, a new Geometry property type for POINT stored in a new geopetric index for fast retrival, and support for Well-Known Text (WKT) format. See the [Spatial Data](access-graph-opencypher-22-spatial-data.md) and the [Spatial Functions](access-graph-opencypher-22-spatial-functions.md) documentation. 

## Improvements in This Engine Release
<a name="engine-releases-1470-improvements"></a>
+ Improved query performance for SPARQL subqueries that return small result sets, including those with small LIMIT values
+ Improved query performance in cases where variables are constrained by a very large number of constant values (for example, by a SPARQL VALUES clause, or an OpenCypher UNWIND clause)
+ Improvements for low latency insert queries via some optimizations to dictionary inserts
+ Added new Gremlin language steps into the DFE engine (see [Gremlin step coverage in DFE](gremlin-step-coverage-in-DFE.md)).
  + Path and traversal steps: `order(local)`
  + Aggregate and collection steps: `dedup(local)`
+ Performance improvement for OpenCypher queries including `COLLECT(DISTINCT ...)`. The rewrite described in [Rewriting COLLECT(DISTINCT ...) queries](best-practices-content-11.md) is no longer needed when using engine version 1.4.7.0 or later.

## Defects Fixed in This Engine Release
<a name="engine-releases-1470-defects"></a>

General fixes:
+ Fix for bulk load becoming unresponsive when loading a large number of edge files
+ Fix a global database cluster patching issue that affected secondary cluster updates from releases 1.4.0.0, 1.4.1.0, and 1.4.2.0.

## Query-Language Versions Supported in This Release
<a name="engine-releases-1.4.7.0-query-versions"></a>

Before upgrading a DB cluster to version 1.4.7.0, make sure that your project is compatible with these query-language versions:
+ *Gremlin earliest version supported:* `3.7.1`
+ *Gremlin latest version supported:* `3.7.1`
+ *openCypher version:* `Neptune-9.0.20190305-1.0`
+ *SPARQL version:* `1.1`

## Upgrade paths to engine release 1.4.7.0
<a name="engine-releases-1.4.7.0-upgrade-paths"></a>

You can upgrade to this release from [engine release 1.2.0.0](engine-releases-1.2.0.0.md) or above.

**Upgrading global database clusters to this release**  
Minor version upgrades to engine version 1.4.7.0 are not supported for Neptune clusters that are part of a [global database](neptune-global-database.md). Non-global database clusters and major version upgrades are not affected.  
To minor version upgrade a global database cluster to 1.4.7.0, you must first remove the secondary clusters from the global database (see [Removing a cluster](neptune-gdb-detaching.md)), upgrade the primary cluster to 1.4.7.0, and then create new secondary clusters in the global database.

## Upgrading to This Release
<a name="engine-releases-1.4.7.0-upgrading"></a>

If a DB cluster is running an engine version from which there is an upgrade path to this release, it is eligible to be upgraded now. You can upgrade any eligible cluster using the DB cluster operations on the console or by using the SDK. The following CLI command will upgrade an eligible cluster immediately:

For Linux, OS X, or Unix:

```
1. aws neptune modify-db-cluster \
2.     --db-cluster-identifier {{(your-neptune-cluster)}} \
3.     --engine-version 1.4.7.0 \
4.     --allow-major-version-upgrade \
5.     --apply-immediately
```

For Windows:

```
1. aws neptune modify-db-cluster ^
2.     --db-cluster-identifier {{(your-neptune-cluster)}} ^
3.     --engine-version 1.4.7.0 ^
4.     --allow-major-version-upgrade ^
5.     --apply-immediately
```

Instead of `--apply-immediately`, you can specify `--no-apply-immediately`. To perform a major version upgrade, the allow-major-version-upgrade parameter is required. Also, be sure to include the engine version or your engine may be upgraded to a different version.

If your cluster uses a custom cluster parameter group, be sure to include this paramater to specify it:

```
    --db-cluster-parameter-group-name {{(name of the custom DB cluster parameter group)}}
```

Similarly, if any instances in the cluster use a custom DB parameter group, be sure to include this parameter to specify it:

```
    --db-instance-parameter-group-name {{(name of the custom instance parameter group)}}
```

### Always test before you upgrade
<a name="engine-1.4.7.0-test-before-upgrading"></a>

When a new major or minor Neptune engine version is released, always test your Neptune applications on it first before upgrading to it. Even a minor upgrade could introduce new features or behavior that would affect your code.

Start by comparing the release notes pages from your current version to those of the targeted version to see if there will be changes in query language versions or other breaking changes.

The best way to test a new version before upgrading your production DB cluster is to clone your production cluster so that the clone is running the new engine version. You can then run queries on the clone without affecting the production DB cluster.

### Always create a manual snapshot before you upgrade
<a name="engine-1.4.7.0-snapshot-before-upgrading"></a>

Before performing an upgrade, we strongly recommend that you always create a manual snapshot of your DB cluster. Having an automatic snapshot only offers short-term protection, whereas a manual snapshot remains available until you explicitly delete it.

In certain cases Neptune creates a manual snapshot for you as a part of the upgrade process, but you should not rely on this, and should create your own manual snapshot in any case.

When you are certain that you won't need to revert your DB cluster to its pre-upgrade state, you can explicitly delete the manual snapshot that you created yourself, as well as the manual snapshot that Neptune might have created. If Neptune creates a manual snapshot, it will have a name that begins with `preupgrade`, followed by the name of your DB cluster, the source engine version, the target engine version, and the date.

**Note**  
If you are trying to upgrade while [a pending action is in process](manage-console-maintaining), you may encounter an error such as the following:  

```
   We're sorry, your request to modify DB cluster (cluster identifier) has failed.
   Cannot modify engine version because instance (instance identifier) is
   running on an old configuration. Apply any pending maintenance actions on the instance before
   proceeding with the upgrade.
```
If you encounter this error, wait for the pending action to finish, or trigger a maintenance window immediately to let the previous upgrade complete.

For more information about upgrading your engine version, see [Maintaining your Amazon Neptune DB Cluster](cluster-maintenance.md). If you have any questions or concerns, the AWS Support team is available on the community forums and through [AWS Premium Support](http://aws.amazon.com/support).