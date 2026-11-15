

# Gusto connection options
<a name="gusto-connection-options"></a>

The following are connection options for Gusto:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Gusto object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Gusto for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Gusto supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| company\_benefits | active | equals only | 
| contractors | onboarded | equals only | 
| employees | terminated, onboarded | equals only | 
| pay\_periods | pay\_period\_date | greater than or equal to and less than or equal to | 
| payrolls | pay\_period\_date | greater than or equal to and less than or equal to | 
| time\_off\_requests | request\_date | greater than or equal to and less than or equal to | 

AWS Glue applies filters on any other Gusto entity after it reads records, through the Spark DataFrame filters.