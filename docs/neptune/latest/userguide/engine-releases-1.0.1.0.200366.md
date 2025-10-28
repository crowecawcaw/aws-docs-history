# Amazon Neptune Engine Updates 2019-07-26

**Version:** 1.0.1.0.200366.0

## IMPORTANT: THIS ENGINE VERSION IS NOW DEPRECATED

No new instances using this engine version will be created, beginning 2021-04-27.

## New Features in This Engine Release

- Upgraded to TinkerPop 3.4.1 (see [TinkerPop Upgrade
  Information](http://tinkerpop.apache.org/docs/3.4.1/upgrade/ "http://tinkerpop.apache.org/docs/3.4.1/upgrade/"), and [TinkerPop
  3.4.1 Change Log](https://github.com/apache/tinkerpop/blob/3.4.1/CHANGELOG.asciidoc#release-3-4-1 "https://github.com/apache/tinkerpop/blob/3.4.1/CHANGELOG.asciidoc#release-3-4-1")).

For Neptune customers, these changes provide new functionality and improvements, such as:

    + `GraphBinary` is now available as a serialization format.
    + A keep-alive bug that caused memory leaks in the TinkerPop Java driver has
     been fixed, so a work-around is no longer necessary.

However, in a few cases, they may affect existing Gremlin code in Neptune. For example:

    + `valueMap()` now returns a `Map<Object,Object>`
     instead of a `Map<String,Object>`.
    + Inconsistent behavior of the `within()` step was fixed so it would
     work consistently with other steps. Previously, types had to match for comparisons to work.
     Now, numbers of different types can be accurately compared. For example, `33`
     now compares as equal to `33L`, which it did not before.
    + A bug in `ReducingBarrierStep` was fixed, so it now returns no value if
     no elements are available for output.
    + The order of `select()` scopes changed (the order is now `maps`,
     `side-effects`, `paths`). This changes the results of the rare queries that
     combine `side-effects` and `select` with the same key name for
     `side-effects` as for `select`.
    + `bulkSet()` is now part of the GraphSON protocol. Queries that
     end with `toBulkSet()` won't work with older clients.
    + One parameterization of the `Submit()` step was removed from
     the 3.4 client.

Many other changes introduced in TinkerPop 3.4 do not affect current Neptune behavior.
For example, Gremlin `io()` was added as a step to `Traversal`
and is now deprecated in `Graph`, but was never enabled in Neptune.

- Added support for single cardinality vertex properties
  to the [bulk
  loader for Gremlin](bulk-load-tutorial-format-gremlin.md#bulk-load-tutorial-format-gremlin-propheaders "bulk-load-tutorial-format-gremlin.md#bulk-load-tutorial-format-gremlin-propheaders"), for loading property graph data.
- Added an option to overwrite the existing values for a
  single-cardinality property in the bulk loader.
- Added the ability to [retrieve the status
  of a Gremlin query](gremlin-api-status.md "gremlin-api-status.md"), and to [cancel a Gremlin
  query](gremlin-api-status-cancel.md "gremlin-api-status-cancel.md").
- Added a [query
  hint for SPARQL query timeouts](sparql-query-hints-queryTimeout.md "sparql-query-hints-queryTimeout.md").
- Added the ability to see the instance role in the status API (see [Instance Status](access-graph-status.md "access-graph-status.md")).
- Added support for database cloning (see [Database Cloning in Neptune](manage-console-cloning.md "manage-console-cloning.md")).

## Improvements in This Engine Release

- Improved the SPARQL Query Explanation to show graph variables
  from FROM clauses.
- Improved performance for SPARQL in filters, equal filters, VALUES
  clauses, and range counts.
- Improved performance for Gremlin step ordering.
- Improved performance for Gremlin `.repeat.dedup`
  traversals.
- Improved the performance of Gremlin `valueMap()` and
  `path().by()` traversals.

## Defects Fixed in This Engine Release

- Fixed multiple issues with SPARQL property paths
  including operation with named graphs.
- Fixed an issue with SPARQL CONSTRUCT queries
  causing memory issues.
- Fixed an issue with the RDF Turtle parser and
  local names.
- Fixed an issue to correct error messages
  displayed to users.
- Fixed an issue with Gremlin `repeat()...drop()`
  traversals.
- Fixed an issue with the Gremlin `drop()` step.
- Fixed an issue with Gremlin label filters.
- Fixed an issue with Gremlin query timeouts.
