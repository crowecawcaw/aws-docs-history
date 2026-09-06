

# Amazon Neptune Engine version 1.4.5.0 (2025-04-09)
<a name="engine-releases-1.4.5.0"></a>

As of 2025-04-09, engine version 1.4.5.0 is being generally deployed. Please note that it takes several days for a new release to become available in every region.

**Warning**  
 We have temporarily paused upgrades to 1.4.5.0 due to issues that can occur in certain Serverless configurations. We recommend upgrading to the 1.4.5.1 engine version. Upgrades to 1.4.5.0 have been temporarily disabled. 

## New features in this engine release
<a name="engine-releases-1.4.5.0-features"></a>
+  Added new Gremlin language steps into the DFE engine. 
  +  **Path and traversal steps: **asDate(), dateAdd(), dateDiff(), fail(), Inject(), label(), path(), project(), repeat(), sack(), select(), unfold(), disjunct(), drop(), identity(), intersect(), length(), loops(), barrier(), order(), range(), reverse(), sample(), cap(), split(), filter(), flatMap(), map(), sideEffect(), union(), index() 
  +  **Aggregate and collection steps: **aggregate(global), combine(), count(), dedup(global), fold(), group(), groupCount() 
  +  **Mathematical steps: **max(), mean(), min(), sum() 
  +  **Element steps: **otherV(), elementMap(), element(), V(), out(), in(), both(), outE(), inE(), bothE(), outV(), inV(), bothV(), otherV() 
  +  **Property steps: **properties(), key(), valueMap(), value() 
  +  **Filter steps: **and(), coalesce(), coin(), is(), local(), none(), not(), or(), where() 
  +  **String manipulation steps: **concat(), lTrim(), rTrim(), substring(), toLower(), toUpper(), trim() 
  + 

**Predicates:**
    +  Compare: eq, neq, lt, lte, gt, gte 
    +  Contains: within, without 
    +  TextP: endingWith, containing, notStartingWith, notEndingWith, notContaining 
    +  P: and, or, between, outside, inside 

 For details on all available Gremlin steps in DFE, refer to [Gremlin step coverage in DFE](gremlin-step-coverage-in-DFE.md). 

## Improvements in this engine release
<a name="engine-releases-1.4.5.0-improvements"></a>

**General Improvements**
+  Slow query log lock wait time improvement. Slow query logs now includes wait time metrics for shared and exclusive locks. They are stored as part of each transaction in case of lazy read-write promotion. These metrics appear in the storageCounters section of the slow query logs. 
+  Dropped support for the following cipher suites: 
  +  TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256 
  +  TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384 
  +  TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA256 
  +  TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384 

**Gremlin Improvements**
+  Added many new steps to the Gremlin language. For more information, see [Gremlin step coverage in DFE](gremlin-step-coverage-in-DFE.md). 

**openCypher improvements**
+  CREATE, MERGE, and SET (mutations) performance improvements. 
+  CALL Subquery performance improvements. 
+  Support for HTTP trailing header support for multi-part openCypher responses. For more information, see [ Optional HTTP trailing headers](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-queries.html#optional-http-trailing-headers). 
+  Added day, month, and year temporal function to openCypher. For more information, see [ Temporal functions](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-extensions.html#temporal-functions). 

  ```
  RETURN day(datetime('2021-06-03T01:48:14Z'))
  {
    "results": [{
        "day(datetime('2021-06-03T01:48:14Z'))": 3
      }]
  }
  ```

## Defects fixed in this engine release
<a name="engine-releases-1.4.5.0-defects"></a>

**General fixes**
+  Fixed issue that dropped the Audit/SlowQueryLog log files. 

**Gremlin fixes**
+  Fixed an issue with Gremlin queries running with Result Cache feature disabled. A query ending with iterate() was returning results instead of returning empty response. 
+  Fixed an issue with Gremlin Result Cache caused by concurrent queries with the same key. One of the concurrent running queries incorrectly returned results instead of returning empty results. 
+  Fixed an issue with Amazon S3 export queries that would cause a query to fail an Amazon S3 multi-part upload due to timeouts or cancellation, by increasing clean up time. 
+  Fixed a permission issue related to Gremlin Amazon S3 export. 

**SPARQL fixes**
+  Fixed an issue in the handling of SPARQL queries that declare multiple base IRIs that would cause only the initial declaration to be used. 
+  Fixed an issue in the handling of SPARQL `REPLACE` functions using invalid pattern strings that would cause an error to be returned. 
+  Fixed an issue in the handling of SPARQL `REPLACE` functions using the case-insensitivity (`"i"`) flag with unicode data. 
+  Fixed an issue in the parsing of SPARQL queries using invalid `\u` and `\U` codepoint escape sequences which could lead to no response being returned. 
+  Fixed an issue in the SPARQL `IRI` function that did not always correctly resolve relative IRIs against the current base IRI. 
+  Fixed an issue that caused `SPARQL INSERT DATA` and `DELETE DATA` updates using prefixed names to fail to correctly resolve relative IRIs against the current base IRI. 

## Query-Language Versions Supported in This Release
<a name="engine-releases-1.4.5.0-query-versions"></a>

Before upgrading a DB cluster to version 1.4.5.0, make sure that your project is compatible with these query-language versions:
+ *Gremlin earliest version supported:* `3.7.1`
+ *Gremlin latest version supported:* `3.7.1`
+ *openCypher version:* `Neptune-9.0.20190305-1.0`
+ *SPARQL version:* `1.1`

## Upgrade paths to engine release 1.4.5.0
<a name="engine-releases-1.4.5.0-upgrade-paths"></a>

You can upgrade to this release from [engine release 1.2.0.0](engine-releases-1.2.0.0.md) or above.

## Upgrading to This Release
<a name="engine-releases-1.4.5.0-upgrading"></a>

If a DB cluster is running an engine version from which there is an upgrade path to this release, it is eligible to be upgraded now. You can upgrade any eligible cluster using the DB cluster operations on the console or by using the SDK. The following CLI command will upgrade an eligible cluster immediately:

For Linux, OS X, or Unix:

```
1. aws neptune modify-db-cluster \
2.     --db-cluster-identifier {{(your-neptune-cluster)}} \
3.     --engine-version 1.4.5.0 \
4.     --allow-major-version-upgrade \
5.     --apply-immediately
```

For Windows:

```
1. aws neptune modify-db-cluster ^
2.     --db-cluster-identifier {{(your-neptune-cluster)}} ^
3.     --engine-version 1.4.5.0 ^
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
<a name="engine-1.4.5.0-test-before-upgrading"></a>

When a new major or minor Neptune engine version is released, always test your Neptune applications on it first before upgrading to it. Even a minor upgrade could introduce new features or behavior that would affect your code.

Start by comparing the release notes pages from your current version to those of the targeted version to see if there will be changes in query language versions or other breaking changes.

The best way to test a new version before upgrading your production DB cluster is to clone your production cluster so that the clone is running the new engine version. You can then run queries on the clone without affecting the production DB cluster.

### Always create a manual snapshot before you upgrade
<a name="engine-1.4.5.0-snapshot-before-upgrading"></a>

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