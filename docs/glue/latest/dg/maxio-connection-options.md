

# Maxio connection options

The following are connection options for Maxio:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Maxio object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate in Spark SQL format.
+ `PARTITION_FIELD` – Used for Read. The field used to partition the query for parallel reads.
+ `LOWER_BOUND` – Used for Read. An inclusive lower bound for the partition field.
+ `UPPER_BOUND` – Used for Read. An exclusive upper bound for the partition field.
+ `NUM_PARTITIONS` – Default: 1. Used for Read. The number of partitions to split the read into.

Maxio supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| component | created\_at | greater than or equal to, less than, less than or equal to, and BETWEEN | 
| credit-note | issue\_date | greater than or equal to, less than, less than or equal to, and BETWEEN | 
| customer | created\_at | greater than or equal to, less than, less than or equal to, and BETWEEN | 
| invoice | subscription\_id, created\_at, status | equals, greater than or equal to, less than, less than or equal to, and BETWEEN | 
| product | created\_at | greater than or equal to, less than, less than or equal to, and BETWEEN | 
| product-family | created\_at | greater than or equal to, less than, less than or equal to, and BETWEEN | 
| subscription | customer\_id, state, coupon\_code, product\_price\_point\_id | equals only | 
| subscription-component-usage | created\_at | greater than or equal to, less than, less than or equal to, and BETWEEN | 

AWS Glue applies filters on any other Maxio entity after it reads records, through the Spark DataFrame filters.