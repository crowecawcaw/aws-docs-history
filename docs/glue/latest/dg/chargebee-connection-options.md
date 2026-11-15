

# Chargebee connection options
<a name="chargebee-connection-options"></a>

The following are connection options for Chargebee:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Chargebee object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Chargebee for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Chargebee supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| coupons | id, status, created\_at\_after, created\_at\_before, updated\_at\_after, updated\_at\_before | equals only | 
| credit\_notes | id, customer\_id, subscription\_id, type, status, date\_after, date\_before, updated\_at\_after, updated\_at\_before | equals only | 
| customers | id, email, auto\_collection, created\_at\_after, created\_at\_before, updated\_at\_after, updated\_at\_before | equals only | 
| events | id, occurred\_at\_after, occurred\_at\_before, event\_type | equals only | 
| invoices | id, customer\_id, subscription\_id, status, date\_after, date\_before, updated\_at\_after, updated\_at\_before | equals only | 
| item\_families | id, updated\_at\_after, updated\_at\_before | equals only | 
| item\_prices | id, item\_family\_id, item\_id, status, updated\_at\_after, updated\_at\_before, created\_at\_after, created\_at\_before | equals only | 
| items | id, status, updated\_at\_after, updated\_at\_before, item\_family\_id, type | equals only | 
| payment\_sources | id, updated\_at\_after, updated\_at\_before, customer\_id, type, status, created\_at\_after, created\_at\_before | equals only | 
| subscriptions | id, customer\_id, status, created\_at\_after, created\_at\_before, updated\_at\_after, updated\_at\_before | equals only | 
| transactions | id, customer\_id, subscription\_id, type, date\_after, date\_before, status, updated\_at\_after, updated\_at\_before | equals only | 

AWS Glue applies filters on any other Chargebee entity after it reads records, through the Spark DataFrame filters.