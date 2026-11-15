

# TestRail connection options
<a name="testrail-connection-options"></a>

The following are connection options for TestRail:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the TestRail object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to TestRail for the fields listed in the filtering support table below. Supply it as an AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

TestRail supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| cases | priority\_id | equals only | 

AWS Glue applies filters on any other TestRail entity after it reads records, through the Spark DataFrame filters.