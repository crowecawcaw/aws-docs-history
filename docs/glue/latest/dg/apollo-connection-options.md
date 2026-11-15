

# Apollo connection options
<a name="apollo-connection-options"></a>

The following are connection options for Apollo:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Apollo object to read.
+ `API_VERSION` – (Required) Used for Read. The Apollo API version to use, for example `v1`.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate in Spark SQL format.

Apollo supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| organizations | name, primary\_domain, location, exclude\_location, keyword\_tag, employee\_count\_range, technology, revenue, total\_funding, latest\_funding | equals, greater than or equal to, and less than or equal to | 
| people | first\_name, title, seniority, person\_location, person\_title, employer\_location, employer\_domain, email\_status, employer\_size, employer\_revenue, include\_similar\_titles | equals, greater than or equal to, and less than or equal to | 

AWS Glue applies filters on any other Apollo entity after it reads records, through the Spark DataFrame filters.