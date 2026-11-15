

# Zoho Books connection options
<a name="zohobooks-connection-options"></a>

The following are connection options for Zoho Books:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Zoho Books object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Zoho Books for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Zoho Books supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| bills | vendor\_id, vendor\_name, status, bill\_number, reference\_number, date, due\_date, total, last\_modified\_time, created\_date, description, project\_id, item\_name, item\_description, item\_id, customer\_id | equals only | 
| chart-of-accounts | account\_id, account\_name, account\_code, account\_type, last\_modified\_time | equals only | 
| contacts | contact\_name, company\_name, contact\_type, status, first\_name, last\_name, phone | equals only | 
| customer-payments | date, payment\_mode, amount, customer\_id, customer\_name, reference\_number | equals only | 
| estimates | customer\_name, customer\_id, status, estimate\_number, reference\_number, date, total, last\_modified\_time, expiry\_date, item\_id, item\_name, item\_description | equals, greater than or equal to, and less than or equal to | 
| expenses | date, account\_name, description, reference\_number, customer\_id, customer\_name, vendor\_id, vendor\_name, status, amount, project\_id | equals only | 
| invoices | customer\_name, customer\_id, status, invoice\_number, reference\_number, date, due\_date, total, balance, last\_modified\_time, item\_name, item\_id, item\_description, created\_date | equals, greater than or equal to, and less than or equal to | 
| items | name, status, description, rate, tax\_id, tax\_name, is\_taxable, account\_id | equals, greater than, greater than or equal to, less than, and less than or equal to | 

AWS Glue applies filters on any other Zoho Books entity after it reads records, through the Spark DataFrame filters.