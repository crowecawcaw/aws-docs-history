

# Xero connection options
<a name="xero-connection-options"></a>

The following are connection options for Xero:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Xero object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Xero for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Xero supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| accounts | Status, Type | equals only | 
| currencies | Code | equals only | 
| items | IsSold, IsPurchased | equals only | 
| tax-rates | TaxType, Status | equals only | 
| tracking-categories | Name, Status | equals only | 
| users | IsSubscriber | equals only | 

AWS Glue applies filters on any other Xero entity after it reads records, through the Spark DataFrame filters.