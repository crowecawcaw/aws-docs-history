# Amazon Neptune Engine Updates 2019-08-13

## IMPORTANT: THIS ENGINE VERSION IS NOW DEPRECATED

Starting from 2021-04-27, no new instances using this engine version will be created.

## New Features in This Engine Release

- Added an `OVERSUBSCRIBE` option to the `parallelism`
  parameter of the [Neptune Loader Command](load-api-reference-load.md "load-api-reference-load.md"),
  which causes the Neptune bulk loader to use all available threads and resources.

## Improvements in This Engine Release

- Improved performance of SPARQL filters containing simple logical OR
  expressions.
- Improved Gremlin performance in handling conjunctive predicates.

## Defects Fixed in This Engine Release

- Fixed a SPARQL bug preventing subtraction of an `xsd:duration`
  from an `xsd:date`.
- Fixed a SPARQL bug causing incomplete results from static inlining in the
  presence of a `UNION`.
- Fixed a SPARQL bug in query cancellation.
- Fixed a Gremlin bug causing overflow during type promotion.
- Fixed a Gremlin bug in the handling of vertex elements in
  `addE().from().to()` steps.
- Fixed a Gremlin bug (released 2019-07-26 in [Engine version
  1.0.1.0.200366.0](engine-releases-1.0.1.0.200366.md "engine-releases-1.0.1.0.200366.md")) involving the handling of NaN doubles and floats
  in single-cardinality inserts.
- Fixed a bug in generating query plans involving property based
  searches.
