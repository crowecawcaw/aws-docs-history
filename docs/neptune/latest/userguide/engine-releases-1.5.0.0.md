

# Amazon Neptune Engine version 1.5.0.0 (2026-10-13)
<a name="engine-releases-1.5.0.0"></a>

As of 2026-10-13, engine version 1.5.0.0 is being generally deployed. Please note that it takes several days for a new release to become available in every region.

## New Features in This Engine Release
<a name="engine-releases-1500-features"></a>
+ Fast bulk load (offline loader) for high-performance initial loads of large Gremlin CSV datasets into empty graphs. See the [Fast bulk load (offline loader)](bulk-load-offline.md) documentation. 
+ Storage management APIs: use the [Neptune storage usage breakdown](storage-info.md) to analyze storage usage, and the [Neptune online index rebuild](storage-index-rebuild.md) to defragment and reclaim index storage while your database remains fully operational. 
+ Gremlin upgrade to Apache TinkerPop 3.8.x. This includes updated Gremlin client minimum versions (Java 11\+, Python 3.10\+, Go 1.25\+, .NET 6.0\+), step behavior changes that improve consistency of the language, and new Gremlin features. Given the step behavior changes, it is important that you carefully review the [TinkerPop Upgrade Documentation](https://tinkerpop.apache.org/docs/3.8.0/upgrade/#_tinkerpop_3_8_0_2) to understand the semantics of Gremlin that have changed and how those changes will affect your existing queries. Given that these are semantic differences, the changes may not surface as errors, but rather change query results. You will need to decide if any of your queries are affected by these changes as part of your upgrade. 

## Improvements in This Engine Release
<a name="engine-releases-1500-improvements"></a>

**Gremlin improvements**
+ Expanded Gremlin step coverage on the DFE query engine offering significantly wider query pattern support aligned with TinkerPop 3.8.x semantics. See [Gremlin step coverage in DFE](gremlin-step-coverage-in-DFE.md).

**openCypher improvements**
+ Added native support for the `all()`, `any()`, `none()`, and `single()` predicate functions. These functions previously required list comprehension rewrites (see [Rewriting `None`, `All`, and `Any` predicate functions](migration-opencypher-rewrites.md#migration-opencypher-rewrites-none-all-any)).

**Gremlin and openCypher improvements**
+ Added DFE support for regex predicates in Gremlin and openCypher

**General improvements**
+ Improved query performance for openCypher and SPARQL queries that use variable assignments (such as `WITH` clauses or `BIND`) across join groups, by enabling the query optimizer to make better join ordering decisions based on variables produced in earlier query stages
+ Improved slow query logging for openCypher queries executed via Bolt protocol with explicit transactions
+ Improved memory efficiency for DFE queries that process large intermediate result sets
+ `pg_schema` computation that is interrupted by an engine restart or failover transitions to `Paused` (rather than `Stopped`)

## Defects Fixed in This Engine Release
<a name="engine-releases-1500-defects"></a>
+ openCypher `MERGE` clauses now reject null property values instead of silently ignoring them
+ Fixed query timeout being incorrectly reported as an internal failure error
+ Fixed a query cancellation issue that could reduce the available query-memory budget
+ Fixed an issue where Neptune Serverless instances may not scale down after running queries

## Query-Language Versions Supported in This Release
<a name="engine-releases-1.5.0.0-query-versions"></a>

Before upgrading a DB cluster to version 1.5.0.0, make sure that your project is compatible with these query-language versions:
+ *Gremlin earliest version supported:* `3.8.0`
+ *Gremlin latest version supported:* `3.8.1`
+ *openCypher version:* `Neptune-9.0.20190305-1.1`
+ *SPARQL version:* `1.1`

## Upgrade paths to engine release 1.5.0.0
<a name="engine-releases-1.5.0.0-upgrade-paths"></a>

You can upgrade to this release from [engine release 1.2.0.0](engine-releases-1.2.0.0.md) or above.

## Upgrading to This Release
<a name="engine-releases-1.5.0.0-upgrading"></a>

If a DB cluster is running an engine version from which there is an upgrade path to this release, it is eligible to be upgraded now. You can upgrade any eligible cluster using the DB cluster operations on the console or by using the SDK. The following CLI command will upgrade an eligible cluster immediately:

For Linux, OS X, or Unix:

```
1. aws neptune modify-db-cluster \
2.     --db-cluster-identifier {{(your-neptune-cluster)}} \
3.     --engine-version 1.5.0.0 \
4.     --allow-major-version-upgrade \
5.     --apply-immediately
```

For Windows:

```
1. aws neptune modify-db-cluster ^
2.     --db-cluster-identifier {{(your-neptune-cluster)}} ^
3.     --engine-version 1.5.0.0 ^
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
<a name="engine-1.5.0.0-test-before-upgrading"></a>

When a new major or minor Neptune engine version is released, always test your Neptune applications on it first before upgrading to it. Even a minor upgrade could introduce new features or behavior that would affect your code.

Start by comparing the release notes pages from your current version to those of the targeted version to see if there will be changes in query language versions or other breaking changes.

The best way to test a new version before upgrading your production DB cluster is to clone your production cluster so that the clone is running the new engine version. You can then run queries on the clone without affecting the production DB cluster.

### Always create a manual snapshot before you upgrade
<a name="engine-1.5.0.0-snapshot-before-upgrading"></a>

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