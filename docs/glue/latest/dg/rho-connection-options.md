

# Rho connection options
<a name="rho-connection-options"></a>

The following are connection options for Rho:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Rho object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Rho for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Rho supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| cards | type, status | equals only | 
| invoicing-invoices | status | equals only | 
| reimbursements | user\_id, approval\_status | equals only | 
| statements | statement\_type | equals only | 
| transactions | account\_id, account\_type, transaction\_type, status, user\_id, card\_id | equals only | 
| users | email, membership\_status, role\_name | equals only | 

AWS Glue applies filters on any other Rho entity after it reads records, through the Spark DataFrame filters.