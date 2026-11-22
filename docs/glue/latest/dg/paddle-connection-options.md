

# Paddle connection options

The following are connection options for Paddle:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Paddle object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate in Spark SQL format.
+ `PARTITION_FIELD` – Used for Read. The field used to partition the query for parallel reads.
+ `LOWER_BOUND` – Used for Read. An inclusive lower bound for the partition field.
+ `UPPER_BOUND` – Used for Read. An exclusive upper bound for the partition field.
+ `NUM_PARTITIONS` – Default: 1. Used for Read. The number of partitions to split the read into.

Paddle supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| addresses | id | equals only | 
| adjustments | id, action, transaction\_id, subscription\_id, customer\_id | equals only | 
| businesses | id | equals only | 
| checkout\_domains | domain | equals only | 
| credit\_balances | currency\_code | equals only | 
| customer\_payment\_methods | address\_id | equals only | 
| customers | id, email | equals only | 
| discount\_groups | id | equals only | 
| discounts | id, code, mode, discount\_group\_id | equals only | 
| events | event\_type | equals only | 
| notification\_settings | active, traffic\_source | equals only | 
| notifications | occurred\_at, notification\_setting\_id | equals, greater than or equal to, and less than | 
| prices | id, product\_id, type | equals only | 
| products | id, type, tax\_category | equals only | 
| simulation\_run\_events | id | equals only | 
| subscription\_history | occurred\_at | greater than or equal to and less than or equal to | 
| subscriptions | id, customer\_id, address\_id, collection\_mode | equals only | 
| transactions | id, customer\_id, origin, subscription\_id, invoice\_number, collection\_mode, created\_at, updated\_at, billed\_at | equals, greater than, greater than or equal to, less than, and less than or equal to | 

AWS Glue applies filters on any other Paddle entity after it reads records, through the Spark DataFrame filters.