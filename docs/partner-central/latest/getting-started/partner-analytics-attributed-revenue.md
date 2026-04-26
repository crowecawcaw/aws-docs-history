# Attributed Revenue

The Attributed Revenue dashboard provides visibility into the AWS revenue impact of your solutions as measured by Partner Revenue Measurement (PRM). The dashboard displays aggregated revenue tracked by PRM capabilities across all customers at a monthly grain, broken down by product and AWS service.

For more information, review the Partner Revenue Measurement [Guide](../../../PRM/latest/aws-prm-onboarding-guide/what-is-service.md "../../../PRM/latest/aws-prm-onboarding-guide/what-is-service.md") and [FAQs](../../../PRM/latest/aws-prm-onboarding-guide/prm-faqs.md "../../../PRM/latest/aws-prm-onboarding-guide/prm-faqs.md").

## Filters

The Attributed Revenue dashboard incorporates the following filtering capabilities for analyzing your attributed revenue data:

- **Time Frame:** Select a date range to view attributed revenue for specific billing periods.
- **Product Name:** Filter by one or more of your AWS Marketplace product listings to view revenue for specific products.
- **AWS Service:** Filter by specific AWS services (for example, Amazon EC2, Amazon S3, Amazon RDS) to understand which services your solutions drive consumption for.
- **AWS Account ID:** Filter by specific AWS account IDs to view revenue associated with particular accounts.

## Key metrics

The dashboard displays three key metrics at the top of the page:

- **Products Measured:** The number of your AWS Marketplace products that have attributed revenue tracked by Partner Revenue Measurement during the selected time frame.
- **AWS Services Measured:** The number of distinct AWS services where your products are driving consumption during the selected time frame.
- **Total Attributed Revenue:** The total aggregated revenue measured by Partner Revenue Measurement across all your products, services, and customers during the selected time frame.

## Charts

**Attributed Revenue by Product**

This chart displays month-over-month attributed revenue for each of your AWS Marketplace products. Each product is represented as a separate series, allowing you to compare revenue trends across your product portfolio over time. Use this chart to identify which products are driving the most AWS consumption and track growth patterns.

**Attributed Revenue by AWS Service**

This chart displays attributed revenue broken down by AWS service. Use this chart to understand which AWS services your solutions drive the most consumption for and how service-level revenue trends change over time.

## Tables

**Attributed Revenue**

This table shows revenue tracked by Partner Revenue Measurement capabilities aggregated across all customers at a monthly grain. The table includes the following columns:

- **Product Name:** The name of your AWS Marketplace product.
- **AWS Service:** The AWS service where consumption was measured.
- **Billing Month:** The month for which revenue was measured.
- **Attributed Revenue:** The aggregated revenue amount for the product-service-month combination.

Revenue data is aggregated across all customers and is only displayed when a product is consumed by a minimum threshold of unique customer accounts per month. Individual customer revenue, names, or account IDs are not displayed.

**Onboarding Status**

This table shows your products that AWS can see enabled with any of the Partner Revenue Measurement capabilities. Use this table to verify that your PRM implementation is active and to identify products that may need additional configuration. The table displays:

- **Product Name:** The name of your AWS Marketplace product.
- **PRM Capability:** The Partner Revenue Measurement capability enabled for the product — Resource Tagging, User Agent string, or AWS Marketplace Metering.
- **Status:** Whether the capability is actively tracking revenue for the product.

## Data availability and privacy

- Revenue data is refreshed monthly and reflects the previous billing month's consumption.
- Revenue is only displayed when a product is consumed by a minimum threshold of unique customer accounts per month. If the customer count drops below the threshold for any month, no revenue data is displayed for that product for that month.
- Partners receive only aggregated revenue data at the product and service level. Individual customer revenue, names, or account IDs are never shared.
- Internal AWS accounts and accounts generating $0 in AWS revenue are excluded from threshold calculations.

## Prerequisites

To access the Attributed Revenue dashboard, you must:

1. Be on the new AWS Partner Central experience (PC 3.0).
2. Have implemented at least one Partner Revenue Measurement capability — [Resource Tagging](../../../PRM/latest/aws-prm-onboarding-guide/resource-tagging.md "../../../PRM/latest/aws-prm-onboarding-guide/resource-tagging.md"), [User Agent string](../../../PRM/latest/aws-prm-onboarding-guide/user-agent-string.md "../../../PRM/latest/aws-prm-onboarding-guide/user-agent-string.md"), or have an AMI or ML product listed on AWS Marketplace (for automatic [Marketplace Metering](../../../PRM/latest/aws-prm-onboarding-guide/marketplace-metering-implementation.md "../../../PRM/latest/aws-prm-onboarding-guide/marketplace-metering-implementation.md")).

Partners with subsidiary accounts connected via Partner Account Connections (PAC) will see aggregated revenue across all connected accounts in a single view.

## Learn more

- [Partner Revenue Measurement Onboarding Guide](../../../PRM/latest/aws-prm-onboarding-guide/what-is-service.md "../../../PRM/latest/aws-prm-onboarding-guide/what-is-service.md")
- [Resource Tagging Implementation](../../../PRM/latest/aws-prm-onboarding-guide/resource-tagging.md "../../../PRM/latest/aws-prm-onboarding-guide/resource-tagging.md")
- [User Agent String Implementation](../../../PRM/latest/aws-prm-onboarding-guide/user-agent-string.md "../../../PRM/latest/aws-prm-onboarding-guide/user-agent-string.md")
- [AWS Marketplace Metering](../../../PRM/latest/aws-prm-onboarding-guide/marketplace-metering-implementation.md "../../../PRM/latest/aws-prm-onboarding-guide/marketplace-metering-implementation.md")
