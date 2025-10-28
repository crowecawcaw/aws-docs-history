# Seller dashboards

AWS Marketplace provides dashboards powered by [Amazon Quick Suite](../../../quicksight/latest/user/welcome.md "../../../quicksight/latest/user/welcome.md") with charts, graphs, and insights
that help you access and analyze financial, sales, and marketing data. The seller dashboards include:

###### [Dashboards for finance operations](finance-operations.md "finance-operations.md")

- [Billed revenue dashboard](billed-revenue-dashboard.md "billed-revenue-dashboard.md") – Provides information about billed
  revenue for accounting and other financial reporting purposes.
- [Collections and disbursement
  dashboard](collections-disbursement-dashboard.md "collections-disbursement-dashboard.md") – Provides information about
  funds that AWS collected and disbursed to your bank accounts since the previous
  disbursement.
- [Taxation dashboard](taxation-dashboard.md "taxation-dashboard.md") – Provides information about taxes for
  seller transactions.

###### [Dashboards for sales operations](sales-operations.md "sales-operations.md")

- [Agreements and renewals dashboard](agreements-renewals-dashboard.md "agreements-renewals-dashboard.md") – Provides information about
  agreements and renewals within 24 hours of signing an agreement in AWS Marketplace.
- [Usage dashboard](usage-dashboard.md "usage-dashboard.md") – Provides visualizations and fine-grained data
  for customers using SaaS and server usage-based products.
- [Dashboards for marketing](marketing-dashboards.md "marketing-dashboards.md") – Provides multiple dashboards to help you track your marketing data.

###### [Dashboards for marketing](marketing-dashboards.md "marketing-dashboards.md")

- [Customer agreements dashboard](customer-agreements-dashboard.md "customer-agreements-dashboard.md") – Provides data about the agreements and customers who subscribe to your products.
- [Listing performance dashboard](listing-performance-dashboard.md "listing-performance-dashboard.md") – Provides data about the traffic and user behavior in your AWS Marketplace listings.
- [Search performance dashboard](search-performance-dashboard.md "search-performance-dashboard.md") – Provides data about the keywords applied to AWS Marketplace listings.
  Dashboards are available to AWS Marketplace sellers who have the appropriate permissions.

## Accessing dashboards

By default, AWS Marketplace system administrators for seller accounts have access to all dashboards
on the Insights tab in the AWS Marketplace Management Portal. System administrators can create an AWS Identity and Access Management (IAM)
policy to provide access for specific dashboards to other users in the seller company.

###### Note

In September 2023, we will no longer support access to seller dashboards enabled by
legacy IAM permissions. Update your IAM permissions using the new Amazon Resource Name (ARN)
format in the code examples below.

For information about creating policies, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md").

### Dashboard policy

Use one of the following policies to provide access to some or all of the dashboards.

The following example provides access to current and future AWS Marketplace resources, including dashboards and
reports. It uses all current and future data feeds:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "aws-marketplace:GetSellerDashboard"
 ],
 "Resource": [
 "arn:aws:aws-marketplace::`111122223333`:AWSMarketplace/*"
 ]
 }
 ]
}`

```

You can also provide access to one or more dashboards by including their ARNs. The following example shows how to provide access to all the dashboards:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "aws-marketplace:GetSellerDashboard"
 ],
 "Resource": [
 "arn:aws:aws-marketplace::`111122223333`:AWSMarketplace/ReportingData/BillingEvent_V1/Dashboard/BilledRevenue_V1",
 "arn:aws:aws-marketplace::`111122223333`:AWSMarketplace/ReportingData/BillingEvent_V1/Dashboard/CollectionsAndDisbursements_V1",
 "arn:aws:aws-marketplace::`111122223333`:AWSMarketplace/ReportingData/Agreement_V1/Dashboard/AgreementsAndRenewals_V1",
 "arn:aws:aws-marketplace::`111122223333`:AWSMarketplace/ReportingData/Usage_V1/Dashboard/Usage_V1",
 "arn:aws:aws-marketplace::`111122223333`:AWSMarketplace/ReportingData/TaxItem_V1/Dashboard/Tax_V1",
 "arn:aws:aws-marketplace::`111122223333`:AWSMarketplace/ReportingData/Marketing_V1/Dashboard/CustomerAgreements_V1",
 "arn:aws:aws-marketplace::`111122223333`:AWSMarketplace/ReportingData/Marketing_V1/Dashboard/ListingPerformance_V1",
 "arn:aws:aws-marketplace::`111122223333`:AWSMarketplace/ReportingData/Marketing_V1/Dashboard/SearchPerformance_V1"
 ]
 }
 ]
}`

```

To remove access to a dashboard, delete it from the `Resource` section of the policy.

###### Note

For information about creating AWS Identity and Access Management (IAM) policies, see [Creating IAM
policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _AWS Identity and Access Management User Guide_.
