

# Agreement Term data feed
<a name="data-feed-agreement-term"></a>

This data feed provides an overview about the agreement term associated with an agreement created by you as the seller of record.

The Agreement Term data feed is refreshed every 24 hours.

The following table lists and describes the items in the data feed.


| Column | Description | 
| --- | --- | 
| valid\_from | The first date that the value for the primary key is valid for in relation to values for other fields. | 
| insert\_date | The date a record was inserted into the data feed. | 
| update\_date | The date the record was last updated. | 
| delete\_date | The date the record was deleted. | 
| agreement\_id | The unique identifier of the agreement. | 
| term\_id | The unique identifier of the term. | 
| term\_type | The type of term associated with the agreement. Refer to https://docs.aws.amazon.com/marketplace/latest/APIReference/API\_Types\_AWS\_Marketplace\_Agreement\_Service.html for a complete list of available terms. | 
| term\_configuration | The additional parameters specified by the acceptor while accepting the term. This is applicable for ConfigurableUpfrontPricingTerms and RenewalTerms. | 

## Agreement Term data feed example
<a name="agreement-term-feed-example"></a>


| valid\_from | insert\_date | update\_date | delete\_date | agreement\_id | term\_id | term\_type | term\_configuration | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| 2024-12-24 11:31:47.0 | 2025-10-01 01:03:41.0 | 2025-10-01 01:03:41.0 | null | agmt-3kk39tbw3j6id2vakbp0XXXXX | term-3986e2c7f73768ed4ff7cd8a97b41ac0ae2aa02ada6b68deb9349c8604cXXXXX | ConfigurableUpfrontPricingTerm | {"selectorValue":"P36M","dimensions":[{"dimensionKey":"Applications","dimensionValue":1}]} | 