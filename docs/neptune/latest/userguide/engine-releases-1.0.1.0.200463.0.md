# Amazon Neptune Engine Updates 2019-10-15

**Version:** 1.0.1.0.200463.0

## IMPORTANT: THIS ENGINE VERSION IS NOW DEPRECATED

No new instances using this engine version will be created, beginning 2021-04-27.

## New Features in This Engine Release

- Added a Gremlin Explain/Profile feature (see [Analyzing Neptune query execution using Gremlin explain](gremlin-explain.md "gremlin-explain.md")).
- Added [Support for Gremlin script-based sessions](access-graph-gremlin-sessions.md "access-graph-gremlin-sessions.md") to enable executing
  multiple Gremlin traversals in a single transaction.
- Added support for the SPARQL Federated Query extension in Neptune (see [SPARQL 1.1 Federated Query](https://www.w3.org/TR/sparql11-federated-query/ "https://www.w3.org/TR/sparql11-federated-query/")
  and [SPARQL federated queries in Neptune using the SERVICE extension](sparql-service.md "sparql-service.md")).
- Added a feature letting you inject your own `queryId`
  into a Gremlin or SPARQL query, either through an HTTP URL parameter or through a SPARQL
  `queryId` query hint (see [Inject a Custom ID Into a Neptune Gremlin or SPARQL Query](features-query-id.md "features-query-id.md")).
- Added a [Lab Mode](features-lab-mode.md "features-lab-mode.md")
  feature to Neptune that can allow you to try out upcoming features which are not yet ready
  to be used in production.
- Added an upcoming [Neptune streams](streams.md "streams.md") feature
  that reliably logs every change made to your database into a stream that persists for
  a week. This feature is available only in Lab Mode.
- Updated the formal semantics for concurrent transactions (see
  [Transaction Semantics in Neptune](transactions.md "transactions.md")). This feature
  provides industry-standard guarantees around concurrency.

By default, these transaction semantics are enabled. In some scenarios, this
feature may change current load behavior and reduce load performance. You can use
the DB Cluster `neptune_lab_mode` parameter to revert to the previous
semantics by including `ReadWriteConflictDetection=disabled` in the
parameter value.

## Improvements in This Engine Release

- Improved the [Instance Status](access-graph-status.md "access-graph-status.md") API by reporting what
  version of TinkerPop and what version of SPARQL the engine is using.
- Improved Gremlin subgraph operator performance.
- Improved the performance of Gremlin response serialization.
- Improved the performance in the Gremlin Union step.
- Improved the latency of simple SPARQL queries.

## Defects Fixed in This Engine Release

- Fixed a Gremlin bug where timeout was incorrectly being returned as an
  internal failure.
- Fixed a SPARQL bug in which ORDER BY over a partial set of
  variables caused an Internal Server Error.
