

# Amazon Neptune Engine Version 1.0.1.1 (2020-06-26)
<a name="engine-releases-1.0.1.1"></a>

## IMPORTANT: THIS ENGINE VERSION IS NOW DEPRECATED
<a name="engine-releases-1.0.1.1-deprecation"></a>

Starting from 2021-04-27, no new instances using this engine version will be created.

## Defects Fixed in This Engine Release
<a name="engine-releases-1.0.1.1-defects"></a>
+ Fixed a bug where commits were out of order when inserted concurrently.
+ Fixed a bug in load-status serialization.
+ Fixed a stochastic failure in server startup which delayed instance creation.
+ Fixed a memory leak.

## Query-Language Versions Supported in This Release
<a name="engine-releases-1.0.1.1-query-versions"></a>

Before upgrading a DB cluster to version 1.0.1.1, make sure that your project is compatible with these query-language versions:
+ *Gremlin version:* `3.3.2`
+ *SPARQL version:* `1.1`