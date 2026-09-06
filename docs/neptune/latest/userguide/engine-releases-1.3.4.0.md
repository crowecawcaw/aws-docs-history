

# Amazon Neptune Engine version 1.3.4.0 (2024-10-01)
<a name="engine-releases-1.3.4.0"></a>

As of 2024-10-01, engine version 1.3.4.0 is being generally deployed. Please note that it takes several days for a new release to become available in every region.

**Note**  
[Engine release 1.3.0.0](engine-releases-1.3.0.0.md) introduced a new format for custom parameter groups and custom cluster parameter groups. As a result, if you are upgrading from an engine version earlier than 1.3.0.0 to engine version 1.3.0.0 or above, you must re-create all of your existing custom parameter groups and custom cluster parameter groups using parameter group family `neptune1.3`. Earlier releases used parameter group family `neptune1`, or `neptune1.2`. and those parameter groups won't work with release 1.3.0.0 and above. Similarly, you should use 1.4.0.0 cluster parameter groups for engine versions 1.4.0.0 and above. See [Amazon Neptune parameter groups](parameter-groups.md) for more information.

**Warning**  
 An issue was detected with SPARQL 1.1 update operations that may be present under certain conditions when update operators are used with action-based authorization policies. If you are using the SPARQL 1.1 update operations with action-based authorization policies, we recommend to upgrade to the latest Neptune minor engine version (at least 1.3.4.0) which includes a fix for this issue.   
 The query plan cache was temporarily disabled for parameterized queries involving numeric parameter values due to an issue in handling duplicate usages of a numeric type parameter as in the following query:   

```
MATCH (n:movie) WHERE n.runtime>=$minutes RETURN n 
UNION 
MATCH (n:show) WHERE n.duration>=$minutes RETURN n

parameters={"minutes":130}
```

## Improvements in this engine release
<a name="engine-releases-1.3.4.0-improvements"></a>
+  Added support for Gremlin limit() step execution in nested traversals for DFE engine. 
+  Added CloudWatch metrics related to Gremlin result cache as listed below, which can be useful in diagnosing and tuning result cache latency. See [ Neptune Metrics](https://docs.aws.amazon.com/neptune/latest/userguide/cw-metrics.html#cw-metrics-available) for details. 

  ```
  NumResultCacheHit
  NumResultCacheMiss
  ResultCacheSizeInBytes
  ResultCacheItemCount
  ResultCacheOldestItemTimestamp
  ResultCacheNewestItemTimestamp
  ```

## Defects fixed in this engine release
<a name="engine-releases-1.3.4.0-defects"></a>

**General improvements**
+ Fixed an issue where in rare cases, the engine crashes instead of returning a query error.

**Gremlin fixes**
+  We have improved request handling and error reporting when a client or a proxy sends a websocket upgrade request over an established/used HTTP connection (previous to that 400 responses with error "no gremlin script supplied, code MissingParameterException" were returned). 
+  Optimized the handling of `mergeV` steps with single cardinality property value updates. For example, the query below is now natively supported in Neptune. 

  ```
  g.mergeV([(T.id): 1234]). option(onMatch, ['age': single(20), 'name': single('alice'), 'city': set('miami')])
  ```
+  Fixed a Gremlin DFE query evaluation issue that caused queries to fail with an `InternalFailureException`. This error occurred with certain patterns of `select` as shown in the following example: 

  ```
  g.V("1").as("a").as("b").select("a","b").dedup()
  ```

**openCypher fixes**
+  Fixed an issue where running `collect(distinct())` with null values present caused an error to be returned. 
+  Fixed an issue where running a parameterized query containing range filter (</<=/>/>= against the parameter value) leads to duplicate/missing results. 
+  Fixed a bug where DFE engine produced more output than requested in limit queries, which could lead to out of memory errors. 

**SPARQL fixes**
+  Fixed an issue where running a federated SPARQL update query on IAM authentication-enabled clusters caused an error to be returned. 
+  Fixed action-based permissions for SPARQL 1.1 update operations. 

## Query-Language Versions Supported in This Release
<a name="engine-releases-1.3.4.0-query-versions"></a>

Before upgrading a DB cluster to version 1.3.4.0, make sure that your project is compatible with these query-language versions:
+ *Gremlin earliest version supported:* `3.7.1`
+ *Gremlin latest version supported:* `3.7.1`
+ *openCypher version:* `Neptune-9.0.20190305-1.0`
+ *SPARQL version:* `1.1`

## Upgrade paths to engine release 1.3.4.0
<a name="engine-releases-1.3.4.0-upgrade-paths"></a>

You can upgrade to this release from [engine release 1.2.0.0](engine-releases-1.2.0.0.md) or above.

## Upgrading to This Release
<a name="engine-releases-1.3.4.0-upgrading"></a>

If a DB cluster is running an engine version from which there is an upgrade path to this release, it is eligible to be upgraded now. You can upgrade any eligible cluster using the DB cluster operations on the console or by using the SDK. The following CLI command will upgrade an eligible cluster immediately:

For Linux, OS X, or Unix:

```
1. aws neptune modify-db-cluster \
2.     --db-cluster-identifier {{(your-neptune-cluster)}} \
3.     --engine-version 1.3.4.0 \
4.     --allow-major-version-upgrade \
5.     --apply-immediately
```

For Windows:

```
1. aws neptune modify-db-cluster ^
2.     --db-cluster-identifier {{(your-neptune-cluster)}} ^
3.     --engine-version 1.3.4.0 ^
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
<a name="engine-1.3.4.0-test-before-upgrading"></a>

When a new major or minor Neptune engine version is released, always test your Neptune applications on it first before upgrading to it. Even a minor upgrade could introduce new features or behavior that would affect your code.

Start by comparing the release notes pages from your current version to those of the targeted version to see if there will be changes in query language versions or other breaking changes.

The best way to test a new version before upgrading your production DB cluster is to clone your production cluster so that the clone is running the new engine version. You can then run queries on the clone without affecting the production DB cluster.

### Always create a manual snapshot before you upgrade
<a name="engine-1.3.4.0-snapshot-before-upgrading"></a>

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