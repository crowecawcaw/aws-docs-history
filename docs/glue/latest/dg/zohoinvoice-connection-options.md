

# Zoho Invoice connection options
<a name="zohoinvoice-connection-options"></a>

The following are connection options for Zoho Invoice:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Zoho Invoice object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Zoho Invoice for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Zoho Invoice supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| contacts | contact\_name, company\_name, first\_name, last\_name, email, phone | equals only | 
| creditnotes | creditnote\_number, status, reference\_number, date, total, customer\_id, customer\_name | equals only | 
| customerpayments | date, payment\_mode, amount | equals only | 
| expenses | date, account\_name, description, reference\_number, customer\_name, status | equals only | 
| invoices | customer\_name, customer\_id, status, invoice\_number, reference\_number, date, due\_date | equals only | 
| items | name, description, rate, tax\_id | equals only | 

AWS Glue applies filters on any other Zoho Invoice entity after it reads records, through the Spark DataFrame filters.