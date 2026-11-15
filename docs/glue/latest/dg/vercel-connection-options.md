

# Vercel connection options
<a name="vercel-connection-options"></a>

The following are connection options for Vercel:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Vercel object to read. For a project-scoped or team-scoped entity, append a forward slash and the parent identifier, as described in [Reading from Vercel entities](vercel-reading-from-entities.md).
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Vercel for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Vercel supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| aliases | projectId | equals only | 
| deployments | isRollbackCandidate, name, projectId, state, target | equals only | 
| domains | createdAt | greater than | 
| events | principalId, type | equals only | 
| projects-checks | blocks | equals only | 
| projects-domains | verified | equals only | 
| teams | createdAt | greater than | 
| teams-members | role | equals only | 

The `createdAt` filter for `domains` and `teams` takes a Unix timestamp in milliseconds, for example `createdAt > 1704067200000`.

AWS Glue applies filters on any other Vercel entity after it reads records, through the Spark DataFrame filters.