

# Anthropic connection options
<a name="anthropic-connection-options"></a>

The following are connection options for Anthropic:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Anthropic object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Anthropic for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Anthropic supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| api\_keys | workspace\_id, status, created\_by\_user\_id | equals only | 
| cost\_report | starting\_at, ending\_at, group\_by | equals only | 
| invites | email, role, status | equals only | 
| models | lifecycle | equals only | 
| skills | source | equals only | 
| usage\_report | starting\_at, ending\_at, api\_key\_id, workspace\_id, model, account\_id, service\_account\_id, service\_tier, context\_window, inference\_geo, speed, group\_by | equals only | 
| users | email, role | equals only | 

AWS Glue applies filters on any other Anthropic entity after it reads records, through the Spark DataFrame filters.