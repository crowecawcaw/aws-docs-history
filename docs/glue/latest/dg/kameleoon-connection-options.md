

# Kameleoon connection options

The following are connection options for Kameleoon:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Kameleoon object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.

Kameleoon supports server-side (pushed-down) filtering as an inclusive date range only, on the following entities and fields, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| goals | dateModified | inclusive date range only (greater than or equal to and less than or equal to, as a pair) | 
| key-moments | dateModified | inclusive date range only (greater than or equal to and less than or equal to, as a pair) | 
| segments | dateModified | inclusive date range only (greater than or equal to and less than or equal to, as a pair) | 
| sites | dateCreated, dateModified | inclusive date range only (greater than or equal to and less than or equal to, as a pair) | 
| studio-recommender-blocks | dateModified | inclusive date range only (greater than or equal to and less than or equal to, as a pair) | 

A single-sided operator (equals, greater than, greater than or equal to, less than, or less than or equal to on its own) is not supported and is rejected. AWS Glue applies filters on any other Kameleoon entity or field after it reads records, through the Spark DataFrame filters.