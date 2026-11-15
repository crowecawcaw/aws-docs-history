

# Webex connection options
<a name="webex-connection-options"></a>

The following are connection options for Webex:
+ `ENTITY_NAME` – (Required) Used for Read. The entity path of the Webex object to read. Use the nested forms described in [Reading from Webex entities](webex-reading-from-entities.md) for `messages` and `team-memberships`.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Webex for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Webex supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| memberships | roomId, personId, personEmail | equals only | 
| messages | parentId | equals only | 
| rooms | type, teamId, orgPublicSpaces | equals only | 

For `rooms`, `orgPublicSpaces` is filter-only. The connector doesn't return it as a column. Webex doesn't accept `orgPublicSpaces` together with `type` or `teamId`.

For `memberships`, Webex requires a `roomId` filter when you filter on `personId` or `personEmail`, unless the access token belongs to a compliance officer.

AWS Glue applies filters on any other Webex entity or field after it reads records, through the Spark DataFrame filters.