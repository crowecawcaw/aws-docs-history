# Customer agreements dashboard

The Customer agreements dashboard provides an overview of the agreements
and customers who subscribe to your products in AWS Marketplace. The dashboard provides
data on your new and active agreements, plus customer trends and profiles.

###### Note

- To unlock this dashboard, you must enroll the [AWS Marketplace Seller Prime](https://pages.awscloud.com/aws-marketplace-seller-prime.html "https://pages.awscloud.com/aws-marketplace-seller-prime.html") program.
- To open this dashboard, sign in to the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/"), choose **Insights**, **Marketing**,
  and then choose the **Customer agreements** tab.
  For more information about using the AWS Marketplace dashboards, see [Seller dashboards](dashboards.md "dashboards.md"), earlier in this section.

###### Topics

- [Section 1: Filters](#customer-agreements-filters "#customer-agreements-filters")
- [Section 2: Date filter deep dive](#customer-agreements-date-deep-dive "#customer-agreements-date-deep-dive")
- [Section 3:  Public and
  private offer agreements](#customer-agreements-public-private-agreements "#customer-agreements-public-private-agreements")
- [Section 4:  Customer metrics](#section-5-customer-metrics "#section-5-customer-metrics")

## Section 1: Filters

You can use the following filters to refine your agreements data.

| Control name          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Product title**     | The title of the product.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Date filter**       | Includes data for the past 30, 60, and 90 days, the trailing 12 months (TTM), and year to date (YTD).<br>Choose custom to define a specific start and end<br>date.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Customer industry** | The industry that AWS defines for a customer who<br>subscribed a seller product.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Customer segment**  | The segment that AWS defines for a customer who<br>subscribed a seller product. Customer segments include:<br>• **STRAT (Strategic)** – Represents the largest and most significant customers with the highest revenue potential for AWS. These are typically major corporations or organizations with extensive and complex cloud computing needs.<br>• **ENT (Enterprise)** – Represents large to medium-sized customers with substantial cloud computing requirements. While not as large as Strategic customers, they still represent significant business opportunities for AWS.<br>• **SMB (Small and Medium Business)** – Represents smaller businesses and organizations with more modest cloud computing needs. These customers may be at earlier stages of cloud adoption or have less complex requirements compared to Enterprise or Strategic customers.<br>• **ISV (Independent Software Vendor)** – Includes technology companies that develop, market, and sell software solutions designed for public sector customers (government, education, non-profit, healthcare, aerospace & defense). These companies often build their products on AWS infrastructure.<br>• **CSD (Consulting Services and Distribution)** – Encompasses companies such as System Integrators, Resellers, and Distributors that provide services enabling customers to leverage cloud technologies. These partners play a crucial role by facilitating cloud adoption and implementation.<br>• **SUP (Startup)** – Represents new and emerging companies, often with innovative business models and rapid growth potential. These customers typically have unique needs related to scalability and cost-efficiency.<br>• **INT (International)** – Refers to customers based outside of the primary market region. These customers may require specific considerations for data sovereignty, regional compliance, and localized support. |

For more information about filtering, see
[Filtering
data on Quick Suite](../../../quicksight/latest/user/adding-a-filter.md "../../../quicksight/latest/user/adding-a-filter.md") in the _Amazon
Quick Suite User Guide_.

## Section 2: Date filter deep dive

This date filter applies to all the metrics on the customer agreement dashboards. 

For example, when you use the default year-to-date filter value,
the follpwing metrics appear:

| Metric                                | Description                                                                                                                                                                                                                    |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Public offer agreement count**      | Number of agreements with public offer as offer visibility<br>that have at least 1 active day within YTD.                                                                                                                      |
| **Private offer agreement count**     | Number of agreements with private offer as offer<br>visibility that have at least 1 active day within YTD.                                                                                                                     |
| **New public offer agreement count**  | Number of agreements with public offer as offer visibility<br>that have acceptance date within YTD.                                                                                                                            |
| **New private offer agreement count** | Number of agreements with private offer as offer<br>visibility that have acceptance date within YTD.                                                                                                                           |
| **Active customers**                  | Number of unique customers, identified as subscriber AWS<br>account ID, that have at least 1 active agreement within<br>YTD. Active agreement is defined as an agreement with at<br>least 1 active day during the time period. |
| **New paying customers**              | Number of unique customers, identified as subscriber AWS<br>account ID, who have their first billing month within YTD.                                                                                                         |

## Section 3:  Public and

private offer agreements

This section of the dashboard displays an overview of your
agreements. Key performance indicators (KPIs) include the number of public offer agreements, the number of private offer
agreements, the number of new public offer agreements, and the number of new private offer
agreements. You can see the year-over-year or period-over-period changes in volume and
percentage. You can update the date range by updating the date filter in the filter section.

An _agreement_ is a contract signed between a proposer (the product or
service owner) and an accepter (the customer) to start using a product.

###### Note

New agreement metrics include active, expired, cancelled, and terminated
agreements.

The following table lists and describes the agreement statuses.

| Status         | Description                                                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Active**     | Some or all of the terms of the agreement are in-force.                                                                         |
| **Expired**    | The agreement ended on its pre-agreed end date.                                                                                 |
| **Canceled**   | The acceptor chooses to end the agreement prior to its end<br>date.                                                             |
| **Terminated** | The agreement ended before its pre-agreed end date due to<br>an  AWS-initiated termination event, such as a payment<br>failure. |
| **Renewed**    | The agreement was renewed into a new agreement using<br>functionality such as auto-renewal.                                     |
| **Replaced**   | The agreement was replaced using a replacement offer.                                                                           |

## Section 4:  Customer metrics

This section of the dashboard provides customer trends for a specified date range. KPIs
include the number of active customers and the number of new paying customers.

- **Monthly trend** – Provides the monthly view for the number of active
  customers and the number of new paying customers based on the filter within the chart.
- **Customer metrics** – Provides data on the
  number of active customers and the number of new paying customers, based on the chosen metric
  filter. You can select a customer segment or an industry to understand how each contributes to the total customer
  metric.

###### Note

Agreements have a given status. For information about the statuses, see the
[table in the previous section](#customer-agreements-public-private-agreements "#customer-agreements-public-private-agreements").

The following table lists and describes the metrics.

| Metrics                          | Description                                                                                                                                                                                                                                                             |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Public offer agreements**      | The number of agreements identified as agreement IDs with public offer<br>visibility; the length of the agreement has at least one day of overlap with the<br>selected date range; the length is identified between the agreement start date and<br>agreement end date. |
| **Private offer agreements**     | The number of agreements identified as agreement IDs with private offer<br>visibility; the length of the agreement has at least one day of overlap with the<br>selected date range; the length is identified between agreement start date and<br>agreement end date.    |
| **New public offer agreements**  | The number of agreements identified as agreement ID with<br>public offer visibility; the agreement acceptance date<br>falls within the selected date range.                                                                                                             |
| **New private offer agreements** | The number of agreements identified as agreement IDs with private offer<br>visibility; the agreement acceptance date falls within the selected date range.                                                                                                              |
| **Active customers**             | The number of customers identified as subscriber AWS account IDs with at least<br>1 active agreement; the length of agreement has at least one day overlap with the<br>selected date range                                                                              |
| **New paying customers**         | The number of customers identified as subscriber AWS account IDs that have<br>their first billing month within the selected date range.                                                                                                                                 |

For more information about agreements and revenue, see
[Agreements and renewals dashboard](agreements-renewals-dashboard.md "agreements-renewals-dashboard.md") and  
[Billed revenue dashboard](billed-revenue-dashboard.md "billed-revenue-dashboard.md"), both in this section.
