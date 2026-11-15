

# DevRev connection options
<a name="devrev-connection-options"></a>

The following are connection options for DevRev:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the DevRev object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to DevRev for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

DevRev supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| commands | namespace, status | equals only | 
| conversations | is\_frozen, source\_channel | equals only | 
| conversations | modified\_date | greater than or equal to, less than or equal to, and between | 
| dev-users | email, state, timezone | equals only | 
| groups | name, is\_default, member\_type | equals only | 
| metric-definitions | type, status, applies\_to\_type | equals only | 
| parts | type, name | equals only | 
| rev-orgs | display\_name, external\_ref | equals only | 
| rev-orgs | created\_date, modified\_date | greater than or equal to, less than or equal to, and between | 
| stock-schema-fragments | leaf\_type | equals only | 
| vistas | type, flavor, object\_type, state, members | equals only | 
| works | type | equals only | 

On `metric-definitions`, `type`, `status`, and `applies_to_type` are query-only fields. On `vistas`, `object_type`, `state`, and `members` are query-only fields. The connector sends these fields to DevRev as filters and doesn't return them as columns.

AWS Glue applies filters on any other DevRev entity or field after it reads records, through the Spark DataFrame filters.