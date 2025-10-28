# Amazon Neptune Engine Version 1.0.1.1 (2020-06-26)

## IMPORTANT: THIS ENGINE VERSION IS NOW DEPRECATED

Starting from 2021-04-27, no new instances using this engine version will be created.

## Defects Fixed in This Engine Release

- Fixed a bug where commits were out of order when inserted
  concurrently.
- Fixed a bug in load-status serialization.
- Fixed a stochastic failure in server startup which delayed instance creation.
- Fixed a memory leak.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.0.1.1, make sure that your project is compatible
with these query-language versions:

- _Gremlin version:_ `3.3.2`
- _SPARQL version:_ `1.1`
