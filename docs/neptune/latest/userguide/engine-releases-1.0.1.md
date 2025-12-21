# Amazon Neptune Engine Version 1.0.1.2 (2020-06-10)

## IMPORTANT: THIS ENGINE VERSION IS NOW DEPRECATED

Starting from 2021-04-27, no new instances using this engine version will be created.

## Improvements in This Engine Release

- Neptune now raises an `IllegalArgumentException` if you try to
  access a non-existent property, vertex, or edge. Previously, Neptune raised
  an `UnsupportedOperationException` in that situation.

For example, if you try to add an edge referencing a nonexistent vertex,
you will now raise an `IllegalArgumentException`.

## Defects Fixed in This Engine Release

- Fixed a bug where dictionary and user transaction commits were out of
  order when two `value->id` mappings were being inserted concurrently.
- Fixed a bug in load-status serialization.
- Fixed a stochastic failure in server startup which delayed instance creation.
- Fixed a cursor leak.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.0.1.2, make sure that your project is compatible
with these query-language versions:

- _Gremlin version:_ `3.4.1`
- _SPARQL version:_ `1.1`
