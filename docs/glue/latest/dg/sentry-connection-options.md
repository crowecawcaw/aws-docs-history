

# Sentry connection options
<a name="sentry-connection-options"></a>

The following are connection options for Sentry:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Sentry object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Sentry for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Sentry supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| organizations-dashboards | query, filter | equals only | 
| organizations-detectors | projectId, type, enabled, query | equals only | 
| organizations-environments | visibility | equals only | 
| organizations-issues | query, environment, project, statsPeriod, start, end | equals only | 
| organizations-members | query | equals only | 
| organizations-monitors | project, environment, owner | equals only | 
| organizations-releases | query, project, environment | equals only | 
| organizations-tags | project, statsPeriod, start, end | equals only | 
| projects | query | equals only | 
| teams | query, detailed | equals only | 

The `query` field accepts Sentry search syntax, such as `is:unresolved`, instead of an exact value. The `statsPeriod` field takes a relative period such as `24h` or `14d` and overrides `start` and `end`. The `visibility` field accepts `all` (the default), `visible`, or `hidden`. Except for `projectId`, `type`, and `enabled` on `organizations-detectors`, these fields are used only for filtering and are not returned as columns.

AWS Glue applies filters on any other Sentry entity after it reads records, through the Spark DataFrame filters.