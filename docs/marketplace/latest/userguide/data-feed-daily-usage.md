

# Daily Usage data feed
<a name="data-feed-daily-usage"></a>

This data feed provides detailed daily usage information for your products, including customer usage metrics, estimated revenue, and pricing details. The data helps you track how customers are using your products and calculate estimated revenue based on usage patterns.

The Daily Usage data feed is refreshed every 24 hours.

The following table lists and describes the items in the data feed.


| Column | Description | 
| --- | --- | 
| valid\_from | The first date that the value for the primary key is valid for in relation to values for other fields. | 
| insert\_date | The date a record was inserted into the data feed. | 
| update\_date | The date the record was last updated. | 
| delete\_date | The date the record was soft deleted. | 
| usage\_feed\_id | The unique identifier of the usage record. This is a per-seller salted hash that ensures data privacy while maintaining record uniqueness. | 
| usage\_date | The customer usage date, without the time component. The time is omitted because usage is aggregated for each day. | 
| product\_id | The friendly ID of the product. Can be used to join to the `product_id` fields of the Account, Billing\_Event, and Offer\_Product data feeds. | 
| agreement\_id | The unique identifier of the agreement. If present, this always starts with `agmnt-`. This field may occasionally be null or not match corresponding invoice line items. | 
| end\_user\_account\_id | The account that actually used the product, represented by the globally unique identifier (GUID) of the end user's account. Can be used to join to the Account data feed. This is a per-seller salted hash, not the raw AWS account ID. | 
| payer\_account\_id | The account that is expected to pay for usage of the product, represented by the globally unique identifier (GUID) of the payer's account. Can be used to join to the Account data feed. This is a per-seller salted hash, not the raw AWS account ID. | 
| region | The AWS region where the buyer usage occurred. | 
| dimension\_key | The dimension key configured by the seller when publishing the offer. | 
| usage\_unit | A classification for the usage units, describing the type of usage measurement. | 
| usage\_quantity | The usage value for the AWS service or usage type associated with the billing record. The value is provided with up to 2 decimal places. | 
| pricing\_currency | The currency of estimated revenue. | 
| estimated\_revenue\_in\_pricing\_currency | The estimated revenue calculated using the `usage_rate_per_unit` and `usage_quantity`. The value is provided with up to 2 decimal places. For ISV views of usage from reseller offers, this needs to be multiplied by the revenue share percentage. | 
| recipient\_account\_id | The account of the seller that is receiving the data in the feeds. | 
| offer\_id | The friendly ID of the offer. This will match the offer\_id of the purchase agreement when available. Can be used to join to the Offer and Offer target data feeds. For consistency, this field is always non-null. | 
| usage\_rate\_per\_unit\_in\_pricing\_currency | The usage rate per unit that can be multiplied by the `usage_quantity` to verify the `estimated_revenue_in_pricing_currency`. The value is provided with up to 6 decimal places. | 
| charge\_item\_description | The complete charge item description, typically formatted as offer\_term\_description\|region\|dimension\_description for usage-based charges. | 

## Daily Usage data feed example
<a name="daily-usage-feed-example"></a>

The following shows an example of the Daily Usage data feed with key columns. For readability, some columns are not shown.


| usage\_date | product\_id | agreement\_id | region | dimension\_key | usage\_unit | usage\_quantity | pricing\_currency | estimated\_revenue\_in\_pricing\_currency | offer\_id | usage\_rate\_per\_unit\_in\_pricing\_currency | charge\_item\_description | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| 2025-01-15 | prod-abcd1234efgh5678 | agmnt-wxyz9876abcd5432 | us-east-1 | USE1\_InputTokenCount | units | 24.00 | USD | 12.00 | offer-mnop5432qrst7890 | 0.500000 | AWS Marketplace software usage\|us-east-1\|Million Input Tokens | 
| 2025-01-15 | prod-ijkl9876mnop1234 | agmnt-stuv5432wxyz9876 | us-west-2 | USE1\_InputTokenCount | units | 1000.00 | USD | 5.50 | offer-abcd9876efgh5432 | 0.005500 | AWS Marketplace software usage\|us-west-2\|API Calls | 