# Amazon Neptune Engine Updates 2019-10-31

**Version:** 1.0.1.0.200502.0

## IMPORTANT: THIS ENGINE VERSION IS NOW DEPRECATED

No new instances using this engine version will be created, beginning 2021-04-27.

## Defects Fixed in This Engine Release

- Fixed a Gremlin bug in the serialization of the `tree()` step's
  response when clients connect to Neptune using `traversal().withRemote(...)`
  (in other words, using GLV bytecode).

This release addresses an issue in which clients who connected to Neptune using
`traversal().withRemote(...)` received an invalid response to Gremlin
queries that contained a `tree()` step.

- Fixed a SPARQL bug in `DELETE WHERE LIMIT` queries, in which
  the query termination process would hang because of a race condition, causing
  the query to time out.
