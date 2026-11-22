

# Avalara connection options

The following are connection options for Avalara:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Avalara object to read. Four entities take a parent value that AWS Glue discovers for you. For these, use the entity path, for example `transactions/{{company-code}}`, `companies-nexus-bytaxtypegroup/{{company-id}}/{{tax-type-group}}`, `definitions-countries-ratetypes/{{country-code}}`, or `definitions-countries-regions/{{country-code}}`.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate in Spark SQL format.

Avalara supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| transactions | code, date, status, modifiedDate, taxDate | equals, greater than, greater than or equal to, less than, less than or equal to, and BETWEEN | 

AWS Glue applies filters on any other Avalara entity after it reads records, through the Spark DataFrame filters.