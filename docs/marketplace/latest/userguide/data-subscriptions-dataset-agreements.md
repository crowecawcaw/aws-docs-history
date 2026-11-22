

# Marketplace Agreements and Renewals dataset

The Marketplace Agreements and Renewals dataset lists active, expired, renewed, and cancelled agreements within 24 hours of signing, with offer details and subscriber, reseller, and ISV relationships. AWS Marketplace delivers this dataset to the `marketplace_agreements_and_renewals` folder in your bucket.

The following table lists the columns in the dataset.

Every row includes a `row_type` value of `INSERT`, `UPDATE`, or `DELETE`, and a `row_modified_date` timestamp. Apply rows to your copy of the data by key column, in order of `row_modified_date`.


**Marketplace Agreements and Renewals columns**  

| Column name | Type | Description | 
| --- | --- | --- | 
| partner\_aws\_account\_id (key column) | string | The AWS account ID of the partner (seller) account. | 
| product\_title | string | The title of the product. | 
| product\_id | string | The friendly unique identifier for the product. | 
| product\_type | string | The type of the product. | 
| legacy\_product\_id | string | The legacy unique identifier for the product. | 
| offer\_name | string | The seller-defined name of the offer. | 
| offer\_id | string | The identifier for the offer that the buyer signed. | 
| offer\_visibility | string | Whether the offer is a public, private, or an enterprise contract offer. | 
| agreement\_id (key column) | string | A unique agreement data feed reference for the agreement signed between a proposer and an accepter to start using a product. | 
| agreement\_start\_date | string | The date timestamp in UTC when the customer's product subscription starts. This date can be different than the acceptance date if this is a future-dated agreement. | 
| agreement\_end\_date | string | The date in UTC when the contract expires. For metered or pay-as-you-go subscriptions, this date is set to January 1, 9999, 12:00 AM UTC. | 
| agreement\_acceptance\_date | string | The date timestamp in UTC when the customer subscribed to the product. | 
| agreement\_type | string | The type of the agreement. | 
| agreement\_intent | string | The intent of the agreement. | 
| previous\_agreement\_id | string | The identifier of the previous agreement, for a renewed or replaced agreement. | 
| next\_agreement\_id | string | The identifier of the next agreement, for a renewed or replaced agreement. | 
| previous\_offer\_id | string | The identifier of the previous offer, for a renewed or replaced agreement. | 
| next\_offer\_id | string | The identifier of the next offer, for a renewed or replaced agreement. | 
| next\_agreement\_id\_acceptance\_dates | string | The acceptance dates of the next agreement, for a renewed or replaced agreement. | 
| proposer\_aws\_account\_id | string | The AWS account ID of the party that proposed the agreement. | 
| proposer\_company\_name | string | The company name of the party that proposed the agreement. | 
| subscriber\_aws\_account\_id | string | The ID of the account that subscribed to the product. | 
| subscriber\_company\_name | string | The name of the account that subscribed to the product. | 
| subscriber\_email\_domain | string | The email domain associated with the account that subscribed to the product. For example, if the email address is abc@example.com, the entry is example.com. | 
| subscriber\_city | string | The billing address city associated with the account that subscribed to the product. | 
| subscriber\_state\_or\_region | string | The billing address state associated with the account that subscribed to the product. | 
| subscriber\_country | string | The billing address country associated with the account that subscribed to the product. | 
| subscriber\_postal\_code | string | The billing address postal code associated with the account that subscribed to the product. | 
| resale\_authorization\_id | string | The unique identifier for a registered resale opportunity. | 
| resale\_authorization\_name | string | The unique name for a registered resale opportunity. | 
| resale\_authorization\_description | string | The description for a registered resale opportunity. | 
| resale\_company\_name | string | The name of the account that purchased a product or service at wholesale cost from an ISV to resell to a customer. | 
| resale\_aws\_account\_id | string | The ID of the account that purchased a product or service at wholesale cost from an ISV to resell to a customer. | 
| isv\_company\_name | string | The name of the product or service owner. | 
| isv\_aws\_account\_id | string | The identifier of the product or service owner. | 
| estimated\_agreement\_value | decimal(38,2) | The estimated monetary value of the agreement. | 
| subscriber\_encrypted\_account\_id | string | The encrypted identifier of the subscriber's account. | 
| currency\_code | string | The currency of the transaction. For example, if the transaction is in U.S. dollars, the entry is USD. | 
| status | string | The current status of the agreement. | 
| accepted\_term\_types | string | The types of terms associated with and accepted by the acceptor during agreement creation. | 
| catalog | string | The catalog associated with the record. | 
| license\_ids | string | The identifiers of the licenses associated with the agreement. | 
| offer\_set\_id | string | The identifier for the offer set associated with the offer. | 
| recipient\_aws\_account\_id (key column) | string | The AWS account ID of the recipient of the data. | 
| row\_type | varchar(30) | The change that this delivery records for the row. INSERT adds a new row, UPDATE replaces a changed row, and DELETE marks a row removed from the source. | 
| row\_modified\_date | timestamp | The UTC time of the last recorded change to the row. This is not the business date of the event. | 