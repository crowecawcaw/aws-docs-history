

# Agreement Charge data feed
<a name="data-feed-agreement-charge"></a>

This data feed provides an overview about the charge associated with an agreement created by you as the seller of record. This data feed currently provides only charge information for agreements associated with a Payment Schedule term.

The Agreement Charge data feed is refreshed every 24 hours.

The following table lists and describes the items in the data feed.


| Column | Description | 
| --- | --- | 
| valid\_from | The first date that the value for the primary key is valid for in relation to values for other fields. | 
| insert\_date | The date a record was inserted into the data feed. | 
| update\_date | The date the record was last updated. | 
| delete\_date | This column is always blank. | 
| amount | The amount to be charged. | 
| currency\_code | The pricing currency of the payment. | 
| time | The scheduled charge date for the planned installment. | 
| agreement\_id | The unique identifier of the agreement. | 
| term\_id | The unique identifier of the term. | 

## Agreement Charge data feed example
<a name="agreement-charge-feed-example"></a>


| valid\_from | insert\_date | update\_date | delete\_date | amount | currency\_code | time | agreement\_id | term\_id | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| 2024-12-24 11:31:47.0 | 2025-10-01 01:03:41.0 | 2025-10-01 01:03:41.0 | null | 28440.00 | USD | 2025-11-06 00:00:00.000000 | agmt-3kk39tbw3j6id2vakbp0XXXXX | term-3986e2c7f73768ed4ff7cd8a97b41ac0ae2aa02ada6b68deb9349c8604cXXXXX | 