

# Grafana connection options

The following are connection options for Grafana:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Grafana object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Grafana for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Grafana supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| dashboards | id, uid, isStarred, folderId, folderUid, isDeleted, query, tag | equals only | 
| provisioning-contact-points | name | equals only | 

For `dashboards`, `query` and `tag` are query-only fields and are not returned as columns. `query` is a Grafana dashboard search term, so it can return dashboards whose titles contain the value, not only exact matches. `tag` returns dashboards that have the specified tag.

AWS Glue applies filters on any other Grafana entity after it reads records, through the Spark DataFrame filters.