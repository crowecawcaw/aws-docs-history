# Amazon Neptune Engine version 1.3.2.0 (2024-06-10)

As of 2024-06-10, engine version 1.3.2.0 is being generally deployed. Please note
that it takes several days for a new release to become available in every region.

###### Note

[Engine release 1.3.0.0](engine-releases-1.3.0.md "engine-releases-1.3.0.md") introduced
a new format for custom parameter groups and custom cluster parameter
groups. As a result, if you are upgrading from an engine version earlier than 1.3.0.0
to engine version 1.3.0.0 or above, you must re-create all of your existing custom
parameter groups and custom cluster parameter groups using parameter group family
`neptune1.3`. Earlier releases used parameter group family `neptune1`,
or `neptune1.2`. and those parameter groups won't work with release
1.3.0.0 and above. Similarly, you should use 1.4.0.0 cluster parameter groups for engine versions 1.4.0.0 and above.
See [Amazon Neptune parameter groups](parameter-groups.md "parameter-groups.md") for more
information.

###### Warning

Engine release 1.3.2.0 introduced some potential issues that you should be aware of. See the section below on
[Mitigating issues in release 1.3.2.0](#1.3.2.0-mitigation "#1.3.2.0-mitigation") for more information.

## Improvements in this engine release

###### General improvements

- Support for TLS version 1.3 including cipher suites TLS_AES_128_GCM_SHA256 and TLS_AES_256_GCM_SHA384.
  TLS 1.3 is an option - TLS 1.2 is still the minimum.

###### Gremlin improvements

- TinkerPop 3.7.x upgrade
  - Provides a large expansion of the Gremlin language.
    - New steps for processing strings, lists and dates.
    - New syntax for specifying cardinality withing the `mergeV()` step.
    - `union()` can now be used as a start step.
    - To learn more about the changes in 3.7.x, see the [TinkerPop upgrade documentation](https://tinkerpop.apache.org/docs/3.7.1/upgrade/#_tinkerpop_3_7_1 "https://tinkerpop.apache.org/docs/3.7.1/upgrade/#_tinkerpop_3_7_1").

  - When upgrading client Gremlin language drivers for Java, note that the serializer classes have ungone some
    [renaming](https://tinkerpop.apache.org/docs/3.7.1/upgrade/#_serializer_renaming "https://tinkerpop.apache.org/docs/3.7.1/upgrade/#_serializer_renaming"). You will
    need to update package and class naming in your configuration files and in code, if specified.

- `StrictTimeoutValidation` (only when enabled via labmode `StrictTimeoutValidation` by including
  `StrictTimeoutValidation=enabled`): When the
  `StrictTimeoutValidation` parameter has a value of `enabled`, a per-query timeout value
  specified as a request option or a query hint cannot exceed the value set globally in the parameter group.
  In such a case, Neptune will throw a `InvalidParameterException`. This setting can be confirmed in
  a response on the `/status` endpoint when the value is `disabled`, and in Neptune version
  1.3.2.0 the default value of this parameter is `Disabled`.

###### openCypher improvements

- Amazon Neptune engine version 1.3.2.0 delivers up to 9x faster and 10x higher throughput for openCypher query
  performance vs. previous engine releases.
- Low latency queries and throughput performance improvement: Overall performance improvements for low latency
  openCypher queries. The new version also improves the throughput for such queries. The improvements are more
  significant when parameterized queries are used.
- Support for Query Plan Cache: When a query is submitted to Neptune, the query string is parsed, optimized, and
  transformed into a query plan, which then gets executed by the engine. Applications are often backed by common
  query patterns that are instantiated with different values. Query plan cache can reduce the overall latency by
  caching the query plans and thereby avoiding parsing and optimization for such repeated patterns.
- Performance Improvement for DISTINCT aggregation queries.
- Performance improvement for joins involving nullable variables.
- Performance improvement for queries involving not equals to id(node/relationship) predicate.
- Extended support for datetime functionality (Only enabled via lab mode `DatetimeMillisecond` by including
  `DatetimeMillisecond=enabled`. For more information, see [Temporal support in the Neptune openCypher implementation
  (Neptune Analytics and Neptune Database 1.3.2.0 and above)](feature-opencypher-compliance.md#opencypher-compliance-time-na "feature-opencypher-compliance.md#opencypher-compliance-time-na").

## Defects fixed in this engine release

###### General improvements

- Updated the NeptuneML error message when validating access to Graphlytics buckets.

###### Gremlin fixes

- Fixed missing label information in DFE query translation, for scenarios where non-path contributing steps
  contain labels. For example:

```
g.withSideEffect('Neptune#useDFE', true).
  V().
  has('name', 'marko').
  has("name", TextP.regex("mark.*")).as("p1").
  not(out().has("name", P.within("peter"))).
  out().as('p2').
  dedup('p1', 'p2')
```

- Fixed a `NullPointerException` bug in the DFE query translation, which occurs when a query is executed
  in two DFE fragments, and the first fragment is optimized to an unsatisfiable node. For example:

```
g.withSideEffect('Neptune#useDFE', true).
  V().
  has('name', 'doesNotExists').
  has("name", TextP.regex("mark.*")).
  inject(1).
  V().
  out().
  has('name', 'vadas')
```

- Fixed a bug where Neptune could throw an `InternalFailureException` when a query contains
  ValueTraversal inside by() modulator and its input is Map. For example:

```
g.V().
  hasLabel("person").
  project("age", "name").by("age").by("name").
  order().by("age")
```

###### openCypher fixes

- Improved UNWIND operations (e.g. expand a list of values into individual values) to help prevent out of memory
  (OOM) situations. For example:

```
MATCH (n)-->(m)
WITH collect(m) AS list
UNWIND list AS m
RETURN m, list
```

- Fixed custom id optimization in case of multiple MERGE operations where id is injected via UNWIND. For example:

```
UNWIND [{nid: 'nid1', mid: 'mid1'}, {nid: 'nid2', mid: 'mid2'}] as ids
MERGE (n:N {`~id`: ids.nid})
MERGE (m:M {`~id`: ids.mid})
```

- Fixed memory explosion while planning for complex queries with property access and multiple hops with bi-directional
  relationships. For example:

```
MATCH (person1:person)-[:likes]->(res)-[:partOf]->(group)-[:knows]-(:entity {name: 'foo'}),
       (person1)-[:knows]->(person2)-[:likes]-(res2), (comment)-[:presentIn]->(:Group {name: 'barGroup'}),
       (person1)-[:commented]->(comment2:comment)-[:partOf]->(post:Post), (comment2)-[:presentIn]->(:Group {name: 'fooGroup'}),
       (comment)-[:contains]->(info:Details)-[:CommentType]->(:CommentType {name: 'Positive'}),
       (comment2)-[:contains]->(info2:Details)-[:CommentType]->(:CommentType {name: 'Positive'})
WHERE datetime('2020-01-01T00:00') <= person1.addedAfter <= datetime('2023-01-01T23:59') AND comment.approvedBy = comment2.approvedBy
MATCH (comment)-[:contains]->(info3:Details)-[:CommentType]->(:CommentType {name: 'Neutral'})
RETURN person1, group.name, info1.value,  post.ranking, info3.value
```

- Fixed aggregation queries with null as group by variables. For example:

```
MATCH (n)
RETURN null AS group, sum(n.num) AS result
```

###### SPARQL fixes

- Fixed the SPARQL parser to improve parsing time for large queries like INSERT DATA containing many triples and
  large tokens.

## Mitigating issues in release 1.3.2.0

- For version 1.3.2.0, we have detected an issue in query plan cache when `skip`
  or `limit` is used in an inner `WITH` clause and are parameterized. For example:

```
MATCH (n:Person)
WHERE n.age > $age
WITH n skip $skip LIMIT $limit
RETURN n.name, n.age

parameters={"age": 21, "skip": 2, "limit": 3}
```

In this case, the parameter values for skip and limit from the first plan will be applied to subsequent queries, too, leading to unexpected results.

**Mitigation**

To prevent this issue, add the query hint `QUERY:PLANCACHE "disabled"` when submitting a query that includes a parameterized skip and/or limit sub-clause. Alternatively, you can hard-code the values into the query.

**Option 1:** Using the Query Hint to disable plan cache:

```
Using QUERY:PLANCACHE "disabled"
MATCH (n:Person) WHERE n.age > $age
WITH n skip $skip LIMIT $limit
RETURN n.name, n.age

parameters={"age": 21, "skip": 2, "limit": 3}
```

**Option 2:** Using hard-coded values for skip and limit:

```
MATCH (n:Person)
WHERE n.age > $age
WITH n skip 2 LIMIT 3
RETURN n.name, n.age

parameters={"age": 21}
```

- Queries using numerical filter values can return incorrect results when using the query plan cache. To avoid the issue, use
  the query hint `QUERY:PLANCACHE "disabled"` to skip the query plan cache. For example, use:

```
USING QUERY:PLANCACHE "disabled"
MATCH (n:person)
WHERE n.yearOfBirth > $year
RETURN n

parameters={"year":1950}
```

- Queries using the same parameter name multiple times can fail with the error `Parameter name should not be a number 
and/or contain _internal_ or _modified_user_ string within it. These are reserved for planCache. Otherwise, rerun with 
HTTP parameter planCache=disabled`. Either skip the query plan cache like above in such cases, or duplicate the
  parameters as in this example:

```
MATCH (n:movie) WHERE n.runtime>=$minutes RETURN n
UNION
MATCH (n:show) WHERE n.duration>=$minutes RETURN n

parameters={"minutes":130}
```

Use the hint `QUERY:PLANCACHE "disabled"` or modify the parameters:

```
MATCH (n:movie) WHERE n.runtime>=$rt_min RETURN n
UNION
MATCH (n:show) WHERE n.duration>=$dur_min RETURN n

parameters={"rt_min":130, "dur_min":130}
```

- Queries executed with the Bolt protocol can produce incorrect results if the query is a UNION or UNION ALL query.
  To avoid the issue, consider executing the particular query with the HTTP endpoint. Alternatively, execute each part
  of the union separately when using the Bolt protocol.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.3.2.0, make sure that your project is compatible
with these query-language versions:

- _Gremlin earliest version supported:_ `3.7.1`
- _Gremlin latest version supported:_ `3.7.1`
- _openCypher version:_ `Neptune-9.0.20190305-1.0`
- _SPARQL version:_ `1.1`

## Upgrade paths to engine release 1.3.2.0

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
    --engine-version 1.3.2.0 \
    --allow-major-version-upgrade \
    --apply-immediately
```

For Windows:

```
aws neptune modify-db-cluster ^
    --db-cluster-identifier `(your-neptune-cluster)` ^
    --engine-version 1.3.2.0 ^
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
