

# Collections and disbursement dashboard
<a name="collections-disbursement-dashboard"></a>

The collections and disbursements dashboard provides data about funds disbursed to your bank accounts. It also provides a list of all invoices where a disbursement has been sent for a partial payment, full payment, or where a failed disbursement has occurred. The list does not include invoices where a disbursement has not transpired. To review invoices not disbursed, use the **Billed revenue** dashboard.

Disbursements include customer payments, settled refunds for a subscription to your product, and some taxes collected or refunded to the customer. Refunds on the dashboard appear as negative amounts because the money is returned to your customer after you authorize a refund.

The collections and disbursements dashboard provides faster access to customer disbursements. Expect to save approximately four days compared to the legacy [disbursement report](https://docs.aws.amazon.com/marketplace/latest/userguide/monthly-disbursement-report.html), which is created five days after the disbursement is sent.

**Note**  
Customers have different payment terms with AWS, so some funds in the uncollected age categories might not be due from the customer.

The collections and disbursements dashboard provides information for operational and financial processes. The dashboard refreshes daily. For more information, see the following topics.

To open the dashboard, sign in to the [AWS Marketplace Management Portal](https://us-east-1.console.aws.amazon.com/partnercentral/home), choose **Insights**, **Finance operations**, and then choose the **Collections and disbursements** tab.

**Topics**
+ [Refresh frequency of the collections and disbursements dashboard](#publication-schedule)
+ [Section 1: Controls](#collections-disbursement-dashboard-controls)
+ [Section 2: Filters](#section-2-select-date-range)
+ [Section 3: Key metrics](#section-3-metrics-collections)
+ [Section 4: Trends](#section-4-trends-collections)
+ [Section 5: Breakdowns](#section-5-breakdowns)
+ [Section 6: Granular data](#section-6-granular-data)

## Refresh frequency of the collections and disbursements dashboard
<a name="publication-schedule"></a>

The collections and disbursements dashboard is updated on North American business days only. You can expect to see disbursed invoices within one day of receiving a deposit to your bank.

## Section 1: Controls
<a name="collections-disbursement-dashboard-controls"></a>

This section of the dashboard provides filters to refine your dashboard data. For example, you can select a filter on a field from the [notifications for AWS Marketplace events](https://docs.aws.amazon.com/marketplace/latest/userguide/notifications.html) to confirm disbursement for a specific customer account ID, subscriber company name, or offer ID. You can also filter by disbursement status to understand all invoices paid to you or invoices open and unpaid. You can add a filter to an analysis, such as the range of dates that you want to include in visuals. The filters selected within the controls update the data displayed in the metrics, trends, breakdowns, and granular data sections.

For more information about filtering, see [Filtering data on Quick](https://docs.aws.amazon.com/quicksight/latest/user/adding-a-filter.html) in the *Quick User Guide*.

### Control descriptions
<a name="control-descriptions-collections"></a>


| Control name | Description | 
| --- | --- | 
| Subscriber AWS account ID | The ID of the account that subscribed to the product. | 
| Subscriber company name  | The name of the account that subscribed to the product. | 
| Product title | The title of the product.  | 
| Offer ID | The identifier for the offer that the buyer signed. | 
| Offer visibility | Whether the offer is a public, private, or enterprise contract offer. | 
| Offer Set ID | The identifier for the offer set associated with the offer. | 
| Agreement ID | A unique agreement data feed reference for the agreement signed between a proposer and an accepter to start using a product. | 
| AWS seller of record | An identifier of the business entity that facilitated the transaction. Possible values include:+  AWS\_INC: The identifier for AWS, Inc. (based in the United States) <br />+  AWS\_EUROPE: The identifier for AWS EMEA SARL (based in Luxembourg) <br />+  AWS\_AUSTRALIA: The identifier for AWS Australia Pty Ltd (AWS Australia) <br />+  AWS\_JAPAN: The identifier for AWS Japan G.K. <br />+  AWS\_KOREA: The identifier for AWS Korea  | 
| Disbursement status | A status associated with an invoice to confirm that AWS has disbursed no funds, partial or all funds to your bank account. Possible statuses are: Disbursed, Partially disbursed, Failed, Not disbursed. | 
| Payer AWS account ID | The ID of the account that the charges are billed to. | 
| Payer company name | The business name of the account that the charges are billed to. | 
| Reseller company | The business name of the reseller account authorized to sell a software manufacturer's product. | 
| Reseller AWS account ID | The ID of the account that purchased a product or service at wholesale from an ISV to resell to a customer. | 
| Resale authorization ID | The unique identifier for a registered opportunity. | 
| Resale authorization name | The unique name for a registered opportunity. | 
| Subscriber country | The two-character country code associated with the account subscribed to the product. | 
| Subscriber state or region | The billing address state or region associated with the account subscribed to the product. | 
| Transaction reference ID | A unique identifier for the transaction that helps you correlate transactions across AWS Marketplace legacy reports. | 
| Disburse bank trace ID | For disbursements, the trace ID is assigned by the bank. The bank trace ID can correlate seller bank-provided deposit notifications and reports to invoices in AWS Marketplace reports. | 

## Section 2: Filters
<a name="section-2-select-date-range"></a>

This section of the dashboard provides filters to refine records based on the offer currency and two different date dimensions — whether the date field value is before or after a specified date or within a date range. The date dimensions are payment due date or last disbursement date. The disbursement date limits the results to invoices disbursed within the specified date range. The payment due date includes invoices with due dates within the specified range, regardless of disbursement date. The date category filter updates the data displayed in the metrics, trends, breakdowns, and granular data sections. The default date category is the last disbursement date and pulls data from the last six months.

## Section 3: Key metrics
<a name="section-3-metrics-collections"></a>

This section of the dashboard displays a key performance indicator (KPI) to visualize a comparison between disbursed and undisbursed revenue figures. A KPI is displayed for gross revenue, net revenue, wholesale cost (if applicable), amount disbursed, and amount undisbursed for the specified filter criteria.

## Section 4: Trends
<a name="section-4-trends-collections"></a>

This section of the dashboard provides a view of disbursement and past due trends for the specified date range. You can view the trends by a specified date aggregation, such as by day, month, quarter, or year, to gain insight into your AWS Marketplace collection health. Trend views include the following:
+ **Disbursement trends** – Provides a snapshot of the average number of days to disburse and associated net revenue. The trend measures the number of days between invoice date and disbursement date to report collection efficiency. You can select a date range from the date aggregation filter.
+ **Age of disbursed payments** – Provides a snapshot of net revenue and a count of disbursed invoices that is categorized by standard aging receivable buckets (such as not due, 1–30 days, and 31 to 60 days). The trend measures the days between payment due date and disbursement date to report if the disbursement was within the customer’s payment terms.
+ **Age of undisbursed payments** – Provides a snapshot of net revenue and count of open and unpaid invoices, organized by past due buckets (such as not due, 1–30 days, and 31 to 60 days). Undisbursed funds might include amounts that aren't due yet. The trend measures the days between today's date and the payment due date to display incoming receivables.

## Section 5: Breakdowns
<a name="section-5-breakdowns"></a>

This section of the dashboard provides you with a view of receivables by offer ID, product title, payer company name, subscriber company name, reseller name (if they participate in channel partner private offers), payer geography, and subscriber geography. Use the breakdowns to measure disbursed receivables against undisbursed receivables for each category.

## Section 6: Granular data
<a name="section-6-granular-data"></a>

This section of the dashboard shows all disbursements and uncollected funds by product, customer, and offer details.

**Note**  
Invoices created before April 1, 2021 might not have an associated agreement ID, offer ID, subscriber AWS account ID, or subscriber company name.

For information about how to export and download data from a Quick table, see [Exporting data from visuals](https://docs.aws.amazon.com/quicksight/latest/user/exporting-data.html) in the *Quick User Guide*.

### Granular data descriptions
<a name="collections-dashboard-granular-data"></a>


| Column | Description | 
| --- | --- | 
| Invoice date | The date the customer was billed for the product subscription. | 
| Payment due date | The payment due date in the format of YYYY-MM-DD. | 
| Payment terms | The customer's AWS invoice payment terms. | 
| Invoice ID | The AWS ID assigned to the AWS invoice where charges were billed.  | 
| Listing fee invoice ID | When an AWS Marketplace subscription is transacted through AWS EMEA SARL, Japan, or Australia legal entities (seller of record), the marketplace operator for the sale (for example, AWS EMEA SARL) is required to charge the seller a VAT on the seller listing fee. For applicable transactions, the invoice ID for the VAT assessed on the listing fee is different than the software or product subscription invoice ID. | 
| Wholesale invoice ID | The AWS ID assigned to the non-payable invoice that represents sale between ISV and Channel Partner in a Channel Partner Private offer (CPPO). For public offers and Marketplace Private offers (MPOs) this field will be 'Not applicable'. | 
| Seller issued invoice ID | An invoice issued by the Seller to AWS. | 
| Seller issued invoice variant | The kind of invoice that corresponds to the invoice\_id column. Possible values include:+  PURCHASE: An invoice from the seller of record to the end buyer. <br />+  RESALE: An invoice from the ISV to the channel partner to pay the wholesale amount. <br />+  LISTING\_FEE: An invoice from AWS to the ISV to pay the listing fee <br />+  TAX\_VAT: An invoice from the seller to AWS, to pay the Deemed VAT.  | 
| Subscriber company name | The name of the account that subscribed to the product. | 
| Subscriber AWS account ID | The ID of the account that subscribed to the product. | 
| Subscriber email domain | The email domain associated with the account that subscribed to the product. For example, if the email address is liu-jie@example.com, the entry is example.com. | 
| Subscriber city | The billing address city associated with the account that subscribed to the product. | 
| Subscriber state or region | The billing address state associated with the account subscribed to the product. | 
| Subscriber country | The billing address country associated with the account that subscribed to the product.  | 
| Subscriber postal code | The billing address postal code associated with the account that subscribed to the product. | 
| Product title | The title of the product. | 
| Offer name | The seller-defined name of the offer. | 
| Offer ID | The identifier for the offer that the buyer signed.  | 
| Offer visibility | Whether the offer is a public, private, or enterprise contract offer. | 
| Offer Set ID | The identifier for the offer set associated with the offer. | 
| Agreement ID | A unique agreement data feed reference for the agreement signed between a proposer and an accepter to start using a product.  | 
| Agreement start date | The date the customer's product subscription starts, formatted as MM-DD-YYYY. This date could be different than the acceptance date if this is a future dated agreement. | 
| Agreement end date | The date when the contract expires, formatted as MM-DD-YYYY. For metered/pay-as-you-go subscriptions, this date is set to JAN-1-9999. | 
|  |  | 
| Agreement acceptance date | The date when the customer subscribed to the product, formatted as MM-DD-YYYY. | 
| Usage period end date | The end date of the product usage period. | 
| Usage period start date | The start date of the product usage period. | 
| Disbursement status | A status associated with an invoice to confirm that AWS has collected and disbursed funds to your bank accounts since the previous disbursement. Disbursed funds for the associated invoice have been collected and disbursed. Not Disbursed funds for the associated invoice have not been collected and disbursed.  | 
| Disbursement date | The date AWS initiated disbursement to the seller’s bank. | 
| Disburse bank trace ID | For disbursements, the trace ID is assigned by the bank. The bank trace ID can be used to correlate seller bank-provided deposit notifications and reports to invoices in AWS Marketplace reports.  | 
| Gross revenue | The amount billed to the customer for the usage or monthly fees of the product. | 
| Gross refund | The total amount of the subscription cost refunded to customers if any refunds were processed during the data coverage period.  | 
| Listing fee | The AWS Marketplace fee amount to be deducted from the billed amount. | 
| Listing fee refund | The portion of the AWS Marketplace fee refunded if any refunds were processed during the data coverage period. | 
| Listing fee percentage | The AWS Marketplace fee percentage to be deducted from the billed amount. | 
| Seller tax share | The total amount of US sales and use tax billed for this transaction. | 
| Seller tax share refund | The total amount of US sales and use tax refunded for this transaction if a refund was processed. | 
| AWS tax share listing fee | Where AWS as a marketplace operator is required to charge and collect VAT in its own name on sales made by sellers. This amount will correspond with the amount of VAT charged to your AWS Marketplace Seller account. | 
| AWS tax share refund listing fee | Where AWS as a marketplace operator is required to refund VAT in its own name on sales made by sellers. This amount will correspond with the amount of VAT refunded to your AWS Marketplace Seller account.  | 
| Wholesale cost | For channel partner private offers only. The cost of goods to a reseller. For example, what a reseller pays a manufacturer when they sell a manufacturer's product. The wholesale cost is the list price multiplied by the discount percentage. | 
| Wholesale cost refund | For channel partner private offers only. The refunded cost of goods from a reseller. | 
| Wholesale seller tax share | The tax on the sale between ISV and Channel Partner in a Channel Partner Private offer (CPPO) where the seller is tax liable. For public offers and Marketplace Private offers (MPPOs) this field will be 'Not applicable'. | 
| Wholesale seller tax share refund | The refund on tax on the sale between ISV and Channel Partner in a Channel Partner Private offer (CPPO) where the seller is liable. For public offers and Marketplace Private offers (MPPOs) this field will be 'Not applicable'. | 
| Wholesale other seller tax share | The tax on the sale between ISV and Channel Partner in a Channel Partner Private offer (CPPO) where the seller is tax liable. This field is populated when the other seller involved in the transaction is liable. For public offers and Marketplace Private offers (MPPOs) this field will be 'Not applicable'. | 
| Wholesale other seller tax share refund | The refund on tax on the sale between ISV and Channel Partner in a Channel Partner Private offer (CPPO) where the seller is liable. This field is populated when the other seller involved in the transaction is liable. For public offers and Marketplace Private offers (MPPOs) this field will be 'Not applicable'.. | 
| Wholesale AWS tax share | The tax on the sale between ISV and Channel Partner in a Channel Partner Private offer (CPPO) where AWS is tax liable. For public offers and Marketplace Private offers (MPPOs) this field will be 'Not applicable'. | 
| Wholesale AWS tax share refund | The refund on tax on the sale between ISV and Channel Partner in a Channel Partner Private offer (CPPO) where AWS is tax liable. For public offers and Marketplace Private offers (MPPOs) this field will be 'Not applicable'. | 
| Seller net revenue | The total amount billed for the transaction, net of AWS Marketplace fees, refunds, and US sales and use tax. | 
| Currency | The currency of the transaction. For example, if the transaction is in US dollars, the entry is USD. | 
| Transaction reference ID | A unique identifier that represents the transaction, which you can use to correlate transactions across AWS Marketplace reports. | 
| AWS seller of record | An identifier of the business entity which facilitated the transaction. Possible values are as follows:+  AWS\_INC: The identifier for AWS, Inc. (based in the United States) <br />+  AWS\_EUROPE: The identifier for AWS EMEA SARL (based in Luxembourg) <br />+  AWS Australia Pty Ltd (AWS Australia) <br />+  AWS Japan G.K. <br />+  AWS\_KOREA  | 
| Resale authorization ID | The unique identifier for a registered opportunity. | 
| Resale authorization name | The unique name for a registered opportunity. | 
| Resale authorization description | The ISV-defined description for a registered opportunity. | 
| Reseller company name | The name of the account that purchased a product or service at wholesale cost from an ISV to resell to a customer. | 
| Reseller AWS account ID | The ID of the account that purchased a product or service at wholesale cost from an ISV to resell to a customer.  | 
| Payer company name | The name of the account that the charges are billed to. | 
| Payer AWS account ID | The ID of the account that the charges are billed to. | 
| Payer email domain | The email domain that is associated with the account that the charges are billed to. For example, if the email address is liu-jie@example.com, the entry is example.com. | 
| Payer city | The billing address city associated with the account that charges are billed to. | 
| Payer state or region | The billing address state associated with the account that the charges are billed to. | 
| Payer country | The two-character country code associated with the account that the charges are billed to. | 
| Payer postal code | The billing address postal code associated with the account that the charges are billed to. | 
| ISV account ID | The identifier of the product or service owner. | 
| ISV company name | The business name of the product or service owner. | 
| Product ID | The friendly unique identifier for the software product. | 
| Disbursement status | A status associated with an invoice to confirm that AWS has disbursed no funds, partial or all funds to your bank account. Possible statuses are: Disbursed, Partially disbursed, Failed, Not disbursed.  | 
| Disbursed net revenue | The total amount for the transaction disbursed to the seller. If the amount does not equal the "seller net revenue", then this is a partial payment. | 
| Undisbursed net revenue | The total amount for the transaction not disbursed to the seller. If the amount is anything other than zero, a remaining balance is owed by the customer. | 
| Disbursement period | The categories describing the receivables range in which the funds were collected (such as, not due, 1–30 days, and 31 to 60 days). | 