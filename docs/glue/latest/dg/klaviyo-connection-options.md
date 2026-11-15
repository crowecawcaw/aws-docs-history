

# Klaviyo connection options
<a name="klaviyo-connection-options"></a>

The following are connection options for Klaviyo:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Klaviyo object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate in Spark SQL format.
+ `PARTITION_FIELD` – Used for Read. The field used to partition the query for parallel reads.
+ `LOWER_BOUND` – Used for Read. An inclusive lower bound for the partition field.
+ `UPPER_BOUND` – Used for Read. An exclusive upper bound for the partition field.
+ `NUM_PARTITIONS` – Default: 1. Used for Read. The number of partitions to split the read into.

Klaviyo supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| events | datetime | BETWEEN (a bounded range using greater than or equal to and less than or equal to). A single open-ended operator on the timestamp is not supported. | 

AWS Glue applies filters on any other Klaviyo entity after it reads records, through the Spark DataFrame filters.