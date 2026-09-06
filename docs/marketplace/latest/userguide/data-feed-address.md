

# Address data feed
<a name="data-feed-address"></a>

**Important**  
AWS Marketplace will discontinue the PIIFeed, which is delivered using the [seller delivery data feeds service](https://docs.aws.amazon.com/marketplace/latest/userguide/data-feed-service.html), in December 2023. Use the AddressFeed\_V1 data feed for your address data needs. If you have questions or require support, contact the [AWS Marketplace Seller Operations](https://aws.amazon.com/marketplace/management/contact-us/) team.

This data feed provides contact information for all the accounts you interact with: your own, any channel partners you work with, buyers, payers, and all taxed accounts. Each time a new transaction occurs, the customer address for the transaction is scanned, and if it's not in your data feed, a new entry is added to your data feed file.

Address data is immutable. 

The address data feed is refreshed every 24 hours, so new data is available daily.

The following table explains the names and descriptions of the data feed's columns. 


| Column name  | Description  | 
| --- | --- | 
| address\_id  | The unique key of the address. Can be used to join from the `Billing_Event` data feed on the `billing_address_id` field, or from the `Account` data feed on the `mailing_address_id` or `tax_address_id` fields. | 
| email\_domain  | The domain for the email address on file for this account.  | 
| company\_name  | The company name on file for this account.  | 
| country\_code | The ISO 3166 alpha-2 country code on file for this address.  | 
| state\_or\_region  | The state or region on file for this address.  | 
| city  | The city on file for this address.  | 
| postal\_code  | The postal code on file for this address.  | 
| address\_line\_1  | The first line of the address on file for this address.  | 
| address\_line\_2  | The second line of the address on file for this address.  | 
| address\_line\_3  | The third line of the address on file for this address.  | 

## Example of address data feed
<a name="data-feed-address-sample-data"></a>

The following shows an example of the address data feed. In the data feed, this information is presented in a single table. For readability, the data is shown in two tables here, and the data history columns aren't shown. For information about data history fields, see [Historization of the data](data-feed-details.md#data-feed-historization). 


| address\_id  | email\_domain  | company\_name  | country\_code  | state\_or\_region  | city  | postal\_code  | 
| --- | --- | --- | --- | --- | --- | --- | 
| V5NhBYBiYogwy0WMhndGU4AfMggmuoTC2j7Pm8ZKKNNyT | a.com | Mateo Jackson's Company | DE |  | Hamburg | 67568 | 
| G68xdbkZQDVVHzfBGw6yf5yos0A6NiSVWHmH5ViLjf | b.com | Mary Major's Company | US | OH | Dayton | 57684 | 
| NLUc5UeiMlGFTrDWCoftDPhDUF1oaSd8xgl5QM8Db7 | c.com | Our Seller | US | NY | New York | 89475 | 




| address\_line\_1  | address\_line\_2  | address\_line\_3  | 
| --- | --- | --- | 
|   |   |  | 
|  |   |  | 
|  | 19th Floor |  | 

