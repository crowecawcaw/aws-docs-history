

# Agreements data feed
<a name="data-feed-agreements"></a>

This data feed provides information about agreements, which is a contract signed between a proposer (seller of record) and an acceptor (AWS Buyer) to start using a product. This data feed provides information about the agreements for the product offers you have created as the seller of record.

The Agreement data feed is refreshed every 24 hours.

The following table lists and describes the items in the data feed.


| Column | Description | 
| --- | --- | 
| valid\_from | The first date that the value for the primary key is valid for in relation to values for other fields. | 
| insert\_date | The date a record was inserted into the data feed. | 
| update\_date | The date the record was last updated. | 
| delete\_date | This column is always blank. | 
| Status | The current status of the agreement. Supported statuses include:+ **Active** – Some or all of the terms of the agreement are in-force.<br />+ **Terminated** – The agreement ended before its pre-agreed end date due to an AWS-initiated termination event. Most commonly a payment failure.<br />+ **Cancelled** – The acceptor chooses to end the agreement before its end date.<br />+ **Expired** – The agreement ended on its pre-agreed end date.<br />+ **Replaced** – The agreement was replaced using a replacement offer.<br />+ **Renewed** – The agreement was renewed into a new agreement using functionality such as auto-renewal.<br />+ **Archived** – The agreement has ended; The exact reason for its ending, **Terminated**, **Canceled**, or **Expired**, is not specified. <br />+ **Rolled back** – The agreement revision has been rolled back because of an error. An earlier revision is now active. Only applicable to inactive agreement revisions.<br />+ **Superceded** – The agreement revision is no longer active and another agreement revision is now active. Only applicable to inactive agreement revisions.  | 
| estimated\_agreement\_value | The total known amount the customer is likely to pay across the lifecycle of the agreement. | 
| currency\_code | The currency of the total known amount the customer is likely to pay in across the lifecycle of the agreement. | 
| agreement\_id | The unique identifier of the agreement. | 
| license\_ids | The license identifiers associated with the agreement, represented as an array. | 
| proposer\_account\_id | The seller that proposed this PurchaseAgreement, represented by the globally unique identifier (GUID) of the seller's account. Can be used to join to the Account data feed. | 
| acceptor\_account\_id | The buyer that accepted this PurchaseAgreement, represented by the globally unique identifier (GUID) of the buyer's account. Can be used to join to the Account data feed. | 
| offer\_revision\_at\_acceptance | The friendly ID of the offer that corresponds to this agreement. Can be used to join to the Offer and Offer target data feeds. | 
| offer\_set\_id | The identifier for the offer set associated with the offer. | 
| start\_time | The date and time when the agreement starts. | 
| end\_time | The date and time when the agreement ends. The field is null for pay-as-you-go agreements, which don’t have end dates. | 
| acceptance\_time | The date and time the offer was accepted or the agreement was created.+ Can be back-dated for bring-your-own-license agreements<br />+ Can be different from the start\_date if the agreement was created with the Future-Dated Agreements feature | 
| intent | The buyer's intent when the agreement was last modified. | 
| preceding\_agreement\_id | The agreement ID of the previous agreement. | 
| status\_reason\_code | The reason for the agreement status change. | 
| recipient\_account\_id | The account of the seller that is receiving the data in the feeds. <br />Can be used to join to the `Account` data feed on the `account_id` field. | 

## Agreements data feed example
<a name="agreements-feed-example"></a>


| valid\_from | agreement\_id | proposer\_account\_id | acceptor\_account\_id | offer\_id | offer\_revision\_at\_acceptance | offer\_set\_id | start\_time | end\_time | acceptancet\_time | intent | preceding\_agreement\_id | status | status\_reason\_code | estimated\_agreement\_value | currency\_code | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| 2024-06-21 20:58:00.0 | agmt-34g544dfgsd5678adsrgwe5t | 88a3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx | 88a3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx | offer-krxxxxxxxxxxx | 1 | offerset-yricpu74oqox2 | 2024-06-21 20:58:00.0 | 2025-06-21 20:58:00.0 | 2024-06-21 20:58:00.0 | NEW |  | ACTIVE |  | 1,000 | USD | 