

# Lemon Squeezy connection options
<a name="lemon-squeezy-connection-options"></a>

The following are connection options for Lemon Squeezy:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Lemon Squeezy object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate in Spark SQL format. AWS Glue pushes down predicates on the fields in the following filtering table to Lemon Squeezy.

Lemon Squeezy supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| checkouts | storeId, variantId | equals only | 
| customers | storeId | equals only | 
| discounts | storeId | equals only | 
| files | variantId | equals only | 
| license-keys | storeId, orderId, orderItemId, productId, userEmail, status | equals only | 
| order-items | orderId, productId, variantId | equals only | 
| orders | storeId, userEmail | equals only | 
| prices | variantId | equals only | 
| products | storeId | equals only | 
| subscription-invoices | storeId, subscriptionId, status | equals only | 
| subscription-items | subscriptionId, priceId | equals only | 
| subscriptions | storeId, orderId, orderItemId, productId, variantId, userEmail, status | equals only | 
| variants | productId | equals only | 

The filterable fields are filter-only. The connector sends them to Lemon Squeezy as filters, and they are not returned as columns. To filter on other values, or to filter the `stores` entity, apply the filter in your ETL job after the read.

Each record contains the JSON:API fields `id`, `type`, `attributes`, `relationships`, and `links`. The `attributes`, `relationships`, and `links` fields are nested structures that hold the resource's business fields and related-resource links.