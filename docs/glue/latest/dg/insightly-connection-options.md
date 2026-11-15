

# Insightly connection options
<a name="insightly-connection-options"></a>

The following are connection options for Insightly:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Insightly object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Insightly for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Insightly supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| Contacts | DATE\_UPDATED\_UTC | greater than or equal to | 
| Events | DATE\_UPDATED\_UTC | greater than or equal to | 
| Milestones | DATE\_UPDATED\_UTC | greater than or equal to | 
| Notes | DATE\_UPDATED\_UTC | greater than or equal to | 
| Tasks | DATE\_UPDATED\_UTC | greater than or equal to | 

AWS Glue applies filters on any other Insightly entity after it reads records, through the Spark DataFrame filters.