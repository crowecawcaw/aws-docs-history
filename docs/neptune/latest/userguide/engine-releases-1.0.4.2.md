# Amazon Neptune Engine Version 1.0.4.2.R4 (2021-07-23)

As of 2021-07-23, engine version 1.0.4.2.R4 is being generally deployed. Please note
that it takes several days for a new release to become available in every region.

## Improvements in This Engine Release

- Improved the behavior of the lookup cache to avoid redundant cache
  clearing after running fast reset on a replica.
- Improved handling of streaming change logs when `AFTER_SEQUENCE_NUMBER`
  streams are requested with the last event ID on the server, when that event ID has
  already expired. The server no longer throws an expired event ID error if the requested
  event ID is the most recently purged event ID on the server.

## Defects Fixed in This Engine Release

- Fixed a bug introduced in 1.0.4.0.R1 where queries would not return
  the entirety of string values larger than 760 characters. The terms affected by this
  bug were RDF literals and URIs, or Gremlin IDs, keys, and string values.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.0.4.2.R4, make sure that your project is compatible
with these query-language versions:

- _Gremlin version:_ `3.4.10`
- _SPARQL version:_ `1.1`

## Upgrade Paths to Engine Release 1.0.4.2.R4

Your cluster will be upgraded to this patch release automatically during your next
maintenance window if you are running engine version `1.0.4.2`.

You can manually upgrade any previous Neptune engine release to this release.
