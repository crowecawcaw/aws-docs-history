

# Amazon Neptune Engine version 1.4.1.0 (2024-11-21)
<a name="engine-releases-1.4.1.0"></a>

As of 2024-11-21, engine version 1.4.1.0 is being generally deployed. Please note that it takes several days for a new release to become available in every region.

**Warning**  
 The query plan cache is temporarily unsupported for the use case of executing parameterized queries involving numeric parameter values, due to a bug in handling duplicate usages of a numeric type parameter in the query. For example:   

```
MATCH (n:movie) WHERE n.runtime>=$minutes RETURN n 
      UNION 
      MATCH (n:show) WHERE n.duration>=$minutes RETURN n
      
      parameters={"minutes":130}
```
 Queries that do a lot of index searches on statements or dictionary indices could see a 5% performance regression. For example - getting a count of all vertices, or getting the `id` of all vertices would not be affected. Getting all properties of all vertices could see up to a 5% regression. 

## New features in this engine release
<a name="engine-releases-1.4.1.0-features"></a>
+  Added support for `CALL` subquery with a read-only subquery, allowing execution of operations within a defined scope. A `CALL` subquery is executed once for each incoming row and the variables returned in a subquery are available to the outer scope of the enclosing query. Variables from outer scope can be imported into a `CALL` subquery using an importing `WITH` clause. For more information, see [ CALL subquery support in Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-extensions.html#call-subquery-support). 

  ```
  MATCH (origin:airport {code:"AUS"})-[:route]->(stopover) 
  CALL { 
    WITH stopover 
    MATCH (stopover)-[r:route]->(destination) 
    RETURN destination 
    ORDER BY r.dist DESC LIMIT 2 
  } 
  RETURN stopover, destination
  ```
+  Added openCypher functions. We are introducing eight new functions to help with strings, collections operations and collection sorting. These include: `textIndexOf`, `collToSet`, `collSubtract`, `collIntersection`, `collSort`, `collSortMaps`, `collSortMulti`, and `collSortNodes`. See [ Neptune openCypher functions](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-extensions.html#opencypher-compliance-new-functions) for the description, input parameters, output and examples. 

## Improvements in this engine release
<a name="engine-releases-1.4.1.0-improvements"></a>

**Gremlin Improvements**
+  New lab mode parameter `AccurateQRCMemoryEstimation`. [Gremlin query result cache](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-results-cache.html), when enabled, allows caching of query results on the database. By default an approximate estimate is used to determine the size of the result cached. With this lab mode param `AccurateQRCMemoryEstimation` enabled, the size estimation for cached results will use an accurate size estimate instead of approximate. 
+  Fixed an issue with "not" filter optimization in Gremlin queries executing on default execution engine. This issue affected queries when edges are filtered using not() step combined with either of outV()/inV()/otherV() steps. Sample queries include: 
  +  `g.E().hasLabel("knows").not(outV().hasId("5"))` 
  +  `g.V().has('airport','code','SDF').outE().where(not(otherV().has(id, within('1','5','7')))).count()` 

**openCypher improvements**
+  Improved performance for queries which use large static lists or maps. Certain queries with UNWIND over a large list of nested maps used to insert / upsert a node with properties see significant performance improvements. 
+  Introduces a new openCypher query hint to instruct engine to assume consistent datatypes for values used in the query. See [AssumeConsistentDataTypes](https://docs.aws.amazon.com/neptune/latest/userguide/opencypher-query-hints-AssumeConsistentDataTypes.html) for details about the new openCypher query hint. 
+  Introduces a set of [ new openCypher functions](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-extensions.html#opencypher-compliance-new-functions) for handling text and collection values. 

## Defects fixed in this engine release
<a name="engine-releases-1.4.1.0-defects"></a>

**Gremlin fixes**
+  Fixed an issue in TinkerPop OSS code path to build a Bytecode representation of a traversal query when any of `withStrategies()/withoutStrategies()/with()` steps are used on `GraphTraversalSource` "g" object. The issue incorrectly appended new instructions to Bytecode instead of replacing existing instructions for the same strategy and caused a cache key mismatch during result cache invalidation to clear the stored results. 

**openCypher fixes**
+  Corrected behavior for ``~id`match` in CREATE/MERGE/MATCH clauses. When using an invalid ``~id`` value like null or non-string types, a correct exception is now thrown for CREATE/MERGE clauses and zero result is returned for a `MATCH` clause. 
+  Fixed IFE when user uses a value of unsupported type with aggregation functions (i.e. sum(<string>)). 
+  Fixed an issue where some low-latency mutation queries from a large workload of queries failed with an OutOfMemory error. 

**SPARQL fixes**
+  Fixed an audit log issue when handling SPARQL queries that contain the `'%'` character. 

## Query-Language Versions Supported in This Release
<a name="engine-releases-1.4.1.0-query-versions"></a>

Before upgrading a DB cluster to version 1.4.1.0, make sure that your project is compatible with these query-language versions:
+ *Gremlin earliest version supported:* `3.7.1`
+ *Gremlin latest version supported:* `3.7.1`
+ *openCypher version:* `Neptune-9.0.20190305-1.0`
+ *SPARQL version:* `1.1`

## Upgrade paths to engine release 1.4.1.0
<a name="engine-releases-1.4.1.0-upgrade-paths"></a>

You can upgrade to this release from [engine release 1.2.0.0](engine-releases-1.2.0.0.md) or above.

## Upgrading to This Release
<a name="engine-releases-1.4.1.0-upgrading"></a>

If a DB cluster is running an engine version from which there is an upgrade path to this release, it is eligible to be upgraded now. You can upgrade any eligible cluster using the DB cluster operations on the console or by using the SDK. The following CLI command will upgrade an eligible cluster immediately:

For Linux, OS X, or Unix:

```
1. aws neptune modify-db-cluster \
2.     --db-cluster-identifier {{(your-neptune-cluster)}} \
3.     --engine-version 1.4.1.0 \
4.     --allow-major-version-upgrade \
5.     --apply-immediately
```

For Windows:

```
1. aws neptune modify-db-cluster ^
2.     --db-cluster-identifier {{(your-neptune-cluster)}} ^
3.     --engine-version 1.4.1.0 ^
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
<a name="engine-1.4.1.0-test-before-upgrading"></a>

When a new major or minor Neptune engine version is released, always test your Neptune applications on it first before upgrading to it. Even a minor upgrade could introduce new features or behavior that would affect your code.

Start by comparing the release notes pages from your current version to those of the targeted version to see if there will be changes in query language versions or other breaking changes.

The best way to test a new version before upgrading your production DB cluster is to clone your production cluster so that the clone is running the new engine version. You can then run queries on the clone without affecting the production DB cluster.

### Always create a manual snapshot before you upgrade
<a name="engine-1.4.1.0-snapshot-before-upgrading"></a>

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