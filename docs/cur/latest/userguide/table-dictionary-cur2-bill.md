

# Bill columns
<a name="table-dictionary-cur2-bill"></a>

Bill columns contain data about your bill for the billing period.



| Column name | Description | Data type | 
| --- | --- | --- | 
| bill\_bill\_type | The type of bill that this report covers. There are three bill types:+  **Anniversary:** Line items for services that you used during the month. <br />+  **Purchase:** Line items for upfront service fees. <br />+  **Refund:** Line items for refunds.  | string | 
| bill\_billing\_entity | Helps you identify whether your invoices or transactions are for AWS Marketplace or for purchases of other AWS services. | string | 
| bill\_billing\_period\_end\_date | The end date of the billing period that is covered by this report, in UTC. The format is `YYYY-MM-DDTHH:mm:ssZ`. | timestamp | 
| bill\_billing\_period\_start\_date | The start date of the billing period that is covered by this report, in UTC. The format is `YYYY-MM-DDTHH:mm:ssZ`. | timestamp | 
| bill\_invoice\_id | The ID associated with a specific line item. Until the report is final, the `InvoiceId` is blank. | string | 
| bill\_invoicing\_entity | The AWS entity that issues the invoice. | string | 
| bill\_payer\_account\_id | The account ID of the paying account. For an organization in AWS Organizations, this is the account ID of the management account. | string | 
| bill\_payer\_account\_name | The account name of the paying account. For an organization in AWS Organizations, this is the name of the management account. | string | 