

# Marketplace Usage dataset

The Marketplace Usage dataset provides usage records for SaaS and server usage-based products, by dimension key, Region, and product. Revenue is estimated until billing is finalized at the end of the month. AWS Marketplace delivers this dataset to the `marketplace_daily_usage_report` folder in your bucket.

The following table lists the columns in the dataset.

Every row includes a `row_type` value of `INSERT`, `UPDATE`, or `DELETE`, and a `row_modified_date` timestamp. Apply rows to your copy of the data by key column, in order of `row_modified_date`.


**Marketplace Usage columns**  

| Column name | Type | Description | 
| --- | --- | --- | 
| internal\_usage\_line\_item\_id (key column) | string | The unique identifier of the usage line item. | 
| partner\_aws\_account\_id | string | The AWS account ID of the partner (seller) account. | 
| end\_user\_aws\_account\_id | string | The ID of the account that used the product. | 
| end\_user\_address\_id | string | The address reference for the end user. | 
| end\_user\_company\_name | string | The name of the account that used the product. | 
| end\_user\_email\_domain | string | The email domain associated with the account that used the product. For example, if the email address is abc@example.com, the entry is example.com. | 
| end\_user\_city | string | The city associated with the account that used the product. | 
| end\_user\_state\_or\_region | string | The state or region associated with the account that used the product. | 
| end\_user\_country | string | The two-character country code associated with the account that used the product. | 
| end\_user\_postal\_code | string | The billing address postal code associated with the account that used the product. | 
| payer\_aws\_account\_id | string | The ID of the account that paid for the product. | 
| payer\_address\_id | string | The address reference for the payer. | 
| payer\_company\_name | string | The name of the account that paid for the product. | 
| payer\_email\_domain | string | The email domain associated with the account that paid for the product. For example, if the email address is abc@example.com, the entry is example.com. | 
| payer\_city | string | The billing address city associated with the account that paid for the product. | 
| payer\_state\_or\_region | string | The billing address state associated with the account that paid for the product. | 
| payer\_country | string | The billing address country associated with the account that paid for the product. | 
| payer\_postal\_code | string | The billing address postal code associated with the account that paid for the product. | 
| subscriber\_aws\_account\_id | string | The ID of the account that subscribed to the product. | 
| subscriber\_address\_id | string | The address reference for the subscriber. | 
| subscriber\_company\_name | string | The name of the account that subscribed to the product. | 
| subscriber\_email\_domain | string | The email domain associated with the account that subscribed to the product. For example, if the email address is abc@example.com, the entry is example.com. | 
| subscriber\_city | string | The billing address city associated with the account that subscribed to the product. | 
| subscriber\_state\_or\_region | string | The billing address state associated with the account subscribed to the product. | 
| subscriber\_country | string | The billing address country associated with the account that subscribed to the product. | 
| subscriber\_postal\_code | string | The billing address postal code associated with the account that subscribed to the product. | 
| usage\_date | string | The date of the customer's product consumption. | 
| dimension\_key | string | The resource type associated with the product usage. Dimension keys apply to SaaS and server usage-based products. | 
| region | string | The Region where the buyer deployed Amazon Elastic Compute Cloud (Amazon EC2) instances. | 
| usage\_unit\_types | string | The unit type for which the usage is recorded. For Agentic Commerce products, the quantity for the agentic\_commerce\_default dimension is in dollars: one unit equals USD 1.00 of quoted charges. | 
| currency | string | The currency of the transaction. For example, if the transaction is in U.S. dollars, the entry is USD. | 
| estimated\_usage\_units | decimal(38,2) | The quantity of the usage recorded for the product. | 
| estimated\_revenue | decimal(38,2) | The revenue from the product usage. Revenue should be considered estimated until billing is finalized at the end of the month. | 
| product\_id | string | The friendly unique identifier for the product. | 
| legacy\_product\_id | string | The legacy unique identifier for the product. | 
| product\_title | string | The title of the product. | 
| product\_code | string | The existing entitlement product code used to meter the product. This value is also used to join data with a report, or to reference what's provided in AWS Marketplace Metering Service. | 
| agreement\_id | string | A unique agreement data feed reference for the agreement signed between a proposer and an accepter to start using a product. | 
| agreement\_revision | string | The revision number of the agreement. | 
| agreement\_start\_date | string | The date timestamp in UTC when the customer's product subscription starts. This date can be different than the acceptance date if this is a future-dated agreement. | 
| agreement\_end\_date | string | The date in UTC when the contract expires. For metered or pay-as-you-go subscriptions, this date is set to January 1, 9999, 12:00 AM UTC. | 
| agreement\_acceptance\_date | string | The date timestamp in UTC when the customer subscribed to the product. | 
| offer\_id | string | The identifier for the offer that the buyer signed. | 
| offer\_visibility | string | Whether the offer is a public, private, or an enterprise contract offer. | 
| offer\_name | string | The seller-defined name of the offer. | 
| cppo\_flag | string | A yes/no flag indicating whether an agreement was made using a channel partner private offer. If yes, the seller of record is the channel partner. If no, the seller of record is the product manufacturer (ISV). | 
| resale\_authorization\_id | string | The unique identifier for a registered resale opportunity. | 
| resale\_authorization\_name | string | The unique name for a registered resale opportunity. | 
| resale\_authorization\_description | string | The description for a registered resale opportunity. | 
| resale\_aws\_account\_id | string | The ID of the account that purchased a product or service at wholesale cost from an ISV to resell to a customer. | 
| resale\_company\_name | string | The name of the account that purchased a product or service at wholesale cost from an ISV to resell to a customer. | 
| isv\_aws\_account\_id | string | The identifier of the product or service owner. | 
| isv\_company\_name | string | The name of the product or service owner. | 
| usage\_reported\_date | string | The date the customer's product consumption is reported. | 
| end\_user\_encrypted\_account\_id | string | The encrypted identifier of the end user's account. | 
| payer\_encrypted\_account\_id | string | The encrypted identifier of the payer's account. | 
| subscriber\_encrypted\_account\_id | string | The encrypted identifier of the subscriber's account. | 
| accepted\_term\_types | string | The types of terms associated with and accepted by the acceptor during agreement creation. | 
| catalog | string | The catalog associated with the record. | 
| offer\_set\_id | string | The identifier for the offer set associated with the offer. | 
| usage\_rate\_per\_unit | decimal(38,6) | The usage rate per unit. | 
| charge\_item\_description | string | The description of the charge. | 
| recipient\_aws\_account\_id (key column) | string | The AWS account ID of the recipient of the data. | 
| row\_type | varchar(30) | The change that this delivery records for the row. INSERT adds a new row, UPDATE replaces a changed row, and DELETE marks a row removed from the source. | 
| row\_modified\_date | timestamp | The UTC time of the last recorded change to the row. This is not the business date of the event. | 