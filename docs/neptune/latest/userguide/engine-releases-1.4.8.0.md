

# Amazon Neptune Engine version 1.4.8.0 (2026-07-27)
<a name="engine-releases-1.4.8.0"></a>

As of 2026-07-27, engine version 1.4.8.0 is being generally deployed. Please note that it takes several days for a new release to become available in every region.

## New Features in This Engine Release
<a name="engine-releases-1480-features"></a>
+ Native RDF export. You can now export RDF data from your Neptune cluster directly to Amazon Simple Storage Service (Amazon S3) using the export API. This feature also supports filtering exports by named graph URIs using the `exportFilter` parameter. See the [Native export for RDF data](neptune-native-export.md) documentation. 
+ Property graph schema. You can now retrieve the schema of your property graph data, including node labels, edge labels, and their associated properties. See the [Property graph schema](access-graph-pg-schema.md) documentation. 
+ [Dictionary garbage collection](features-lab-mode.md#features-lab-mode-features-gc) now works on clusters with Neptune Streams enabled.

## Improvements in This Engine Release
<a name="engine-releases-1480-improvements"></a>

Gremlin improvements:
+ Reduced the chance that a Gremlin query will encounter an out-of-memory condition when a serverless instance has scaled down to a low NCU value.

SPARQL improvements:
+ Improved performance of very large, multi-operation SPARQL Update requests.
+ Improved performance of SPARQL alternative property paths (for example, `?s <a>|<b> ?o`).

## Defects Fixed in This Engine Release
<a name="engine-releases-1480-defects"></a>

General fixes:
+ Fixed a rare condition that could prevent the engine from starting successfully under certain configurations.
+ Fixed an issue where rolled-back transactions could lead to gradual memory growth over time.
+ Various stability and correctness fixes for the DFE query engine.

## Query-Language Versions Supported in This Release
<a name="engine-releases-1.4.8.0-query-versions"></a>

Before upgrading a DB cluster to version 1.4.8.0, make sure that your project is compatible with these query-language versions:
+ *Gremlin earliest version supported:* `3.7.1`
+ *Gremlin latest version supported:* `3.7.1`
+ *openCypher version:* `Neptune-9.0.20190305-1.0`
+ *SPARQL version:* `1.1`

## Upgrade paths to engine release 1.4.8.0
<a name="engine-releases-1.4.8.0-upgrade-paths"></a>

You can upgrade to this release from [engine release 1.2.0.0](engine-releases-1.2.0.0.md) or above.

**Upgrading global database clusters to this release**  
Minor version upgrades to engine version 1.4.8.0 from versions prior to 1.4.7.0 are not supported for Neptune clusters that are part of a [global database](neptune-global-database.md). Non-global database clusters and major version upgrades are not affected.  
To minor version upgrade a global database cluster running a version prior to 1.4.7.0 to 1.4.8.0, you must first remove the secondary clusters from the global database (see [Removing a cluster](neptune-gdb-detaching.md)), upgrade the primary cluster to 1.4.8.0, and then create new secondary clusters in the global database.

## Upgrading to This Release
<a name="engine-releases-1.4.8.0-upgrading"></a>

If a DB cluster is running an engine version from which there is an upgrade path to this release, it is eligible to be upgraded now. You can upgrade any eligible cluster using the DB cluster operations on the console or by using the SDK. The following CLI command will upgrade an eligible cluster immediately:

For Linux, OS X, or Unix:

```
1. aws neptune modify-db-cluster \
2.     --db-cluster-identifier {{(your-neptune-cluster)}} \
3.     --engine-version 1.4.8.0 \
4.     --allow-major-version-upgrade \
5.     --apply-immediately
```

For Windows:

```
1. aws neptune modify-db-cluster ^
2.     --db-cluster-identifier {{(your-neptune-cluster)}} ^
3.     --engine-version 1.4.8.0 ^
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
<a name="engine-1.4.8.0-test-before-upgrading"></a>

When a new major or minor Neptune engine version is released, always test your Neptune applications on it first before upgrading to it. Even a minor upgrade could introduce new features or behavior that would affect your code.

Start by comparing the release notes pages from your current version to those of the targeted version to see if there will be changes in query language versions or other breaking changes.

The best way to test a new version before upgrading your production DB cluster is to clone your production cluster so that the clone is running the new engine version. You can then run queries on the clone without affecting the production DB cluster.

### Always create a manual snapshot before you upgrade
<a name="engine-1.4.8.0-snapshot-before-upgrading"></a>

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