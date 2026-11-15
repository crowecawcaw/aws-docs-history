

# GoCardless connection options
<a name="gocardless-connection-options"></a>

The following are connection options for GoCardless:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the GoCardless object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to GoCardless for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

GoCardless supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| block | block\_type, reason\_type | equals only | 
| creditor-bank-account | enabled, creditor | equals only | 
| customer | currency, action\_required | equals only | 
| customer-bank-account | enabled, customer | equals only | 
| event | resource\_type, action, billing\_request, creditor, export, instalment\_schedule, mandate, outbound\_payment, payer\_authorisation, payment, payment\_account\_transaction, payout, refund, subscription, scheme\_identifier, parent\_event | equals only | 
| instalment-schedule | status, mandate, customer | equals only | 
| institution | country\_code, branch\_code | equals only | 
| mandate | reference, status, scheme, mandate\_type, customer, creditor, customer\_bank\_account | equals only | 
| payment | status, customer, creditor, subscription, mandate | equals only | 
| payout | currency, reference, status, payout\_type, creditor, creditor\_bank\_account | equals only | 
| refund | payment, mandate, refund\_type | equals only | 
| scheme-identifier | creditor | equals only | 
| subscription | status, mandate, customer | equals only | 
| tax-rate | jurisdiction | equals only | 

AWS Glue applies filters on any other GoCardless entity after it reads records, through the Spark DataFrame filters.