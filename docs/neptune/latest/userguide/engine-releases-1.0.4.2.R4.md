

# Amazon Neptune Engine Version 1.0.4.2.R4 (2021-07-23)
<a name="engine-releases-1.0.4.2.R4"></a>

As of 2021-07-23, engine version 1.0.4.2.R4 is being generally deployed. Please note that it takes several days for a new release to become available in every region.

## Improvements in This Engine Release
<a name="engine-releases-1.0.4.2.R4-improvements"></a>
+ Improved the behavior of the lookup cache to avoid redundant cache clearing after running fast reset on a replica.
+ Improved handling of streaming change logs when `AFTER_SEQUENCE_NUMBER` streams are requested with the last event ID on the server, when that event ID has already expired. The server no longer throws an expired event ID error if the requested event ID is the most recently purged event ID on the server.

## Defects Fixed in This Engine Release
<a name="engine-releases-1.0.4.2.R4-defects"></a>
+ Fixed a bug introduced in 1.0.4.0.R1 where queries would not return the entirety of string values larger than 760 characters. The terms affected by this bug were RDF literals and URIs, or Gremlin IDs, keys, and string values.

## Query-Language Versions Supported in This Release
<a name="engine-releases-1.0.4.2.R4-query-versions"></a>

Before upgrading a DB cluster to version 1.0.4.2.R4, make sure that your project is compatible with these query-language versions:
+ *Gremlin version:* `3.4.10`
+ *SPARQL version:* `1.1`

## Upgrade Paths to Engine Release 1.0.4.2.R4
<a name="engine-releases-1.0.4.2.R4-upgrade-paths"></a>

Your cluster will be upgraded to this patch release automatically during your next maintenance window if you are running engine version `1.0.4.2`.

You can manually upgrade any previous Neptune engine release to this release.