

# Square connection options

The following are connection options for Square:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Square object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Square for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Square supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| bank-accounts | location\_id | equals only | 
| catalog-list | type | equals only | 
| devices | location\_id | equals only | 
| gift-cards | type, state, customer\_id | equals only | 
| gift-cards-activities | type, location\_id, gift\_card\_id, begin\_time, end\_time | equals only | 
| locations-transactions | begin\_time, end\_time | equals only | 
| payments | location\_id, begin\_time, end\_time, total, card\_brand, last\_4 | equals only | 
| refunds | status, location\_id, begin\_time, end\_time, source\_type | equals only | 
| team-member-wages | team\_member\_id | equals only | 

The `begin_time` and `end_time` fields set the start and end of a time range instead of matching an exact value. On `gift-cards-activities`, filter on both fields together. On `locations-transactions`, include `begin_time` whenever you filter on `end_time`. The `begin_time`, `end_time`, `total`, `card_brand`, `last_4`, `source_type`, and `customer_id` fields, and `location_id` on `devices`, are used only for filtering and are not returned as columns.

AWS Glue applies filters on any other Square entity after it reads records, through the Spark DataFrame filters.