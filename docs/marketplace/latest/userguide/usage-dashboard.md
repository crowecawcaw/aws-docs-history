# Usage dashboard

The Usage dashboard provides visualizations and fine-grained data for customers using SaaS
and server usage-based products. AWS Marketplace sellers can use this dashboard to track customer
consumption across usage-based products to make decisions on product support, pricing,
conversion from public to private offers, and product discontinuation. The dashboard provides data from the last 6 months, which is a rolling
window.

To open the dashboard, sign in to the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/"),
choose **Insights**, choose **Sales operations**, then choose the **Usage** tab.

###### Note

This dashboard displays usage for all the dimension keys specified at the time of the
offer creation. For example, for Amazon Machine Image (AMI) products, dimension keys are
instance types, and all instance types specified in the offer appear in this dashboard,
even when priced at $0. To see product usage for a dimension that wasn't specified at
the time of offer creation, consider republishing the product to include the dimension you
need.

###### Topics

- [Refresh frequency of the usage
  dashboard](#usage-publication-schedule "#usage-publication-schedule")
- [Section 1: Controls](#usage-dashboard-controls "#usage-dashboard-controls")
- [Section 2: Filters](#section-2-invoice-date-range "#section-2-invoice-date-range")
- [Section 3: Metrics](#section-3-metrics "#section-3-metrics")
- [Section 4: Trends](#section-3-metrics "#section-3-metrics")
- [Section 5: Breakdowns](#section-4-breakdowns "#section-4-breakdowns")
- [Section 6: Granular data](#section-5-new-product-subscribers "#section-5-new-product-subscribers")

## Refresh frequency of the usage

dashboard

Dashboards are updated daily at 4 PM PST (midnight UTC). Note that the usage data is
received from upstream data sources and may encounter delays, you can refer to the usage date
and the usage reported date for clarity on when the usage occurred compared to when it was
reported on the dashboard.

## Section 1: Controls

This section of the dashboard provides filters to refine your usage data. For example, you
can select from the following filters.

###### Note

For more information about filtering, see [Filtering data in Quick Suite](../../../quicksight/latest/user/adding-a-filter.md "../../../quicksight/latest/user/adding-a-filter.md") in the
_Quick Suite User Guide_.

### Control descriptions

| Control name              | Description                                                                                                                                                                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| End user company name     | The name of the account that used the product.                                                                                                                                                                                                  |
| End user AWS account ID   | The ID of the account that used the product.                                                                                                                                                                                                    |
| End user country          | The two-character country code associated with the account that used the<br>product.                                                                                                                                                            |
| Product title             | The title of the product.                                                                                                                                                                                                                       |
| Product code              | The existing entitlement product code used to meter the product. This value is also<br>used to join data with a report, or to reference what's provided in the AWS Marketplace<br>Metering Service.                                             |
| Offer ID                  | The identifier for the offer that the buyer signed.                                                                                                                                                                                             |
| Offer visibility          | Whether the offer is a public, private, or enterprise contract offer.                                                                                                                                                                           |
| Offer Set ID              | The identifier for the offer set associated with the offer.                                                                                                                                                                                     |
| Agreement ID              | A unique agreement data feed reference for the agreement signed between a proposer<br>and an accepter to start using a product.                                                                                                                 |
| Dimension key             | The resource type associated with the product usage. Dimension keys apply to SaaS<br>and server usage-based products.                                                                                                                           |
| Subscriber company name   | The name of the account that subscribed to the product.                                                                                                                                                                                         |
| Subscriber AWS account ID | The ID of the account that subscribed to the product.                                                                                                                                                                                           |
| Subscriber country        | The two-character country code associated with the account subscribed to the<br>product.                                                                                                                                                        |
| Reseller company name     | The name of the reseller account authorized to sell a product manufacturer's<br>product.                                                                                                                                                        |
| Reseller AWS account ID   | The ID of the account that purchased a product or service at wholesale from an ISV<br>to resell to a customer.                                                                                                                                  |
| Resale authorization ID   | The ID of the account that purchased a product or service at wholesale from an ISV<br>to resell to a customer.                                                                                                                                  |
| CPPO flag                 | A yes/no flag indicating whether an agreement was made using a channel partner<br>private offer. If yes, the seller of record is the channel partner. If no, the seller of<br>record is the product manufacturer (independent software vendor). |

## Section 2: Filters

This section of the dashboard provides filters to refine records based on the usage date.
The values selected in these filters update the data displayed in the metrics, trends,
breakdowns, and granular data sections. The default selection is to pull data for last 6
months usage.

## Section 3: Metrics

This section of the dashboard displays a key performance indicator (KPI) to visualize
metrics related to consumption: estimated usage units, customers with usage, and products with
usage. You can update the date range by updating the usage date criteria in the filters
section. Note that the key metrics display data for all unit types.

## Section 4: Trends

This section of the dashboard provides usage trends for a specified date range. You can
view the trends by a specified date aggregation, such as daily, month-over-month,
quarter-over-quarter, or year-over-year to gain insight into usage. You can also select a
usage unit type to view its usage trends graphically.

## Section 5: Breakdowns

This section of the dashboard provides you with estimated usage metrics for your business
across company names, product titles, dimension key and offer IDs for the unit type selected.
You may also select the number of entries to view.

## Section 6: Granular data

This section of the dashboard shows granular data for usage, offers, product, subscriber,
payer, end user, resale authorizations, resellers, and independent software vendors (ISVs).
Note that the granular data table displays data for all unit types.

Revenue should be considered estimated until billing is finalized at the end of the month.
Usage-based invoices are presented to buyers on the second or third day of the following month
for the previous month's usage (for example, customers metered for usage between 11/1 and
11/30 will be presented an invoice for the usage on 12/2 or 12/3). Metered usage may arrive to
this dashboard several days after the actual usage date, so the usage date and usage reported
dates may be different. This means you may need to visit the dashboard daily throughout the
month for up-to-date tracking in the current month. For authoritative customer billing
information, see the [Billed revenue
dashboard](billed-revenue-dashboard.md "billed-revenue-dashboard.md") in the **Financial operations** tab.

###### Note

For more information about filtering, see [Exporting data from visuals](../../../quicksight/latest/user/exporting-data.md "../../../quicksight/latest/user/exporting-data.md") in
the _Quick Suite User Guide_.

### Granular data descriptions

| Column                           | Description                                                                                                                                                                                                                                                        |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Usage date                       | The date of the customer's product consumption.                                                                                                                                                                                                                    |
| Usage reported date              | The date the customer's product consumption is surfaced in the insights<br>dashboard.                                                                                                                                                                              |
| End user company name            | The name of the account that used the product.                                                                                                                                                                                                                     |
| End user AWS account ID          | The ID of the account that used the product.                                                                                                                                                                                                                       |
| End user email domain            | The email domain associated with the account that used the product. For example,<br>if the email address is abc@example.com, the entry is example.com.                                                                                                             |
| End user city                    | The city associated with the account that used the product.                                                                                                                                                                                                        |
| End user state or region         | The state or region associated with the account that used the product.                                                                                                                                                                                             |
| End user country                 | The two-character country code associated with the account that used the<br>product.                                                                                                                                                                               |
| End user postal code             | The billing address postal code associated with the account that used the<br>product.                                                                                                                                                                              |
| Product title                    | The title of the product.                                                                                                                                                                                                                                          |
| Legacy product ID                | The legacy unique identifier for the product.                                                                                                                                                                                                                      |
| Product ID                       | The friendly unique identifier for the product.                                                                                                                                                                                                                    |
| Product code                     | The existing entitlement product code used to meter the product. This value is<br>also used to join data with a report, or to reference what's provided in<br>AWS Marketplace Metering Service.                                                                    |
| Offer ID                         | The identifier for the offer that the buyer signed.                                                                                                                                                                                                                |
| Offer name                       | The seller-defined name of the offer.                                                                                                                                                                                                                              |
| Offer visibility                 | Whether the offer is a public, private, or an enterprise contract offer.                                                                                                                                                                                           |
| Offer Set ID                     | The identifier for the offer set associated with the offer.                                                                                                                                                                                                        |
| Agreement ID                     | A unique agreement data feed reference for the agreement signed between a<br>proposer and an accepter to start using a product.                                                                                                                                    |
| Agreement acceptance date        | The date time stamp in UTC when the customer subscribed to the product.                                                                                                                                                                                            |
| Agreement start date             | The date timestamps in UTC when the customer's product subscription starts. This<br>date could be different than acceptance date if this is a future dated<br>agreement.                                                                                           |
| Agreement end date               | The date in UTC when the contract expires. For metered/pay-as-you-go<br>subscriptions, this date is set to Jan 1, 9999 12:00 AM.                                                                                                                                   |
| Agreement Term Types             | The types of terms associated with and accepted by the acceptor during agreement creation.                                                                                                                                                                         |
| Dimension key                    | The resource type associated with the product usage. Dimension keys apply for<br>SaaS and server usage-based products.                                                                                                                                             |
| Region                           | The region where the buyer deployed Amazon EC2 instances.                                                                                                                                                                                                          |
| Estimated usage                  | The quantity of the usage recorded for the product.                                                                                                                                                                                                                |
| Usage unit types                 | The unit type for which the usage is recorded.                                                                                                                                                                                                                     |
| Usage rate per unit              | The usage rate per unit.                                                                                                                                                                                                                                           |
| Charge item description          | The description of the charge.                                                                                                                                                                                                                                     |
| Estimated revenue                | The revenue from the product usage. Revenue should be considered estimated until<br>billing is finalized at the end of the month. Usage-based invoices are presented to<br>buyers on the second or third of the following month for the previous month's<br>usage. |
| Currency                         | The currency of the transaction. For example, if the transaction is in U.S.<br>dollars, the entry is USD.                                                                                                                                                          |
| Subscriber company name          | The name of the account that subscribed to the product.                                                                                                                                                                                                            |
| Subscriber AWS account ID        | The ID of the account that subscribed to the product.                                                                                                                                                                                                              |
| Subscriber email domain          | The email domain associated with the account that subscribed to the product. For<br>example, if the email address is abc@example.com, the entry is example.com.                                                                                                    |
| Subscriber city                  | The billing address city associated with the account that subscribed to the<br>product.                                                                                                                                                                            |
| Subscriber state or region       | The billing address state associated with the account subscribed to the<br>product.                                                                                                                                                                                |
| Subscriber country               | The billing address country associated with the account that subscribed to the<br>product.                                                                                                                                                                         |
| Subscriber postal code           | The billing address postal code associated with the account that subscribed to<br>the product.                                                                                                                                                                     |
| Payer company name               | The name of the account that paid for the product.                                                                                                                                                                                                                 |
| Payer AWS account ID             | The ID of the account that paid for the product.                                                                                                                                                                                                                   |
| Payer email domain               | The email domain associated with the account that paid for the product. For<br>example, if the email address is abc@example.com, the entry is example.com.                                                                                                         |
| Payer city                       | The billing address city associated with the account that paid for the<br>product.                                                                                                                                                                                 |
| Payer state or region            | The billing address state associated with the account that paid for the<br>product.                                                                                                                                                                                |
| Payer country                    | The billing address country associated with the account that paid for the<br>product.                                                                                                                                                                              |
| Payer postal code                | The billing address postal code associated with the account that paid for the<br>product.                                                                                                                                                                          |
| Reseller company name            | The name of the account that purchased a product or service at wholesale cost<br>from an ISV to resell to a customer.                                                                                                                                              |
| Reseller AWS account ID          | The ID of the account that purchased a product or service at wholesale cost from<br>an ISV to resell to a customer.                                                                                                                                                |
| Resale authorization ID          | The unique identifier for a registered resale opportunity.                                                                                                                                                                                                         |
| Resale authorization name        | The unique name for a registered resale opportunity.                                                                                                                                                                                                               |
| Resale authorization description | The description for a registered resale opportunity.                                                                                                                                                                                                               |
| CPPO flag                        | A yes/no flag indicating whether an agreement was made using a channel partner<br>private offer. If yes, the seller of record is the channel partner. If no, the seller<br>of record is the product manufacturer (ISV).                                            |
| ISV company name                 | The name of the product or service owner.                                                                                                                                                                                                                          |
| ISV AWS account ID               | The identifier of the product or service owner.                                                                                                                                                                                                                    |
