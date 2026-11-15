

# Close CRM connection options
<a name="close-connection-options"></a>

The following are connection options for Close CRM:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Close CRM object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Close CRM for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Close CRM supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| activity | \_type, lead\_id, activity\_at, date\_created | equals, greater than, greater than or equal to, less than, and less than or equal to | 
| opportunity | lead\_id, user\_id, status\_id, status\_label, status\_type, value\_period, date\_won, date\_created, date\_updated | equals, greater than, greater than or equal to, less than, and less than or equal to | 
| task | \_type, is\_complete, lead\_id, assigned\_to, date, date\_created, date\_updated | equals, greater than, greater than or equal to, less than, and less than or equal to | 

AWS Glue applies filters on any other Close CRM entity after it reads records, through the Spark DataFrame filters.