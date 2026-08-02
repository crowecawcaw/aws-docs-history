# Attributed Revenue

The Attributed Revenue dashboard provides visibility into the AWS revenue impact of your solutions as measured by Partner Revenue Measurement (PRM). The dashboard displays aggregated monthly attributed revenue by Partner product, AWS service, and billing period.

For more information, review the Partner Revenue Measurement [Onboarding Guide](../../../PRM/latest/aws-prm-onboarding-guide/what-is-service.md "../../../PRM/latest/aws-prm-onboarding-guide/what-is-service.md") and [FAQs](../../../PRM/latest/aws-prm-onboarding-guide/prm-faqs.md "../../../PRM/latest/aws-prm-onboarding-guide/prm-faqs.md").

## Filters

The Attributed Revenue dashboard incorporates the following filtering capabilities for analyzing your attributed revenue data:

- **Time Frame:** Select a date range to view attributed revenue for specific billing periods.
- **Product Name:** Filter by one or more of your AWS Marketplace product listings to view revenue for specific products.
- **AWS Service:** Filter by specific AWS services (for example, Amazon EC2, Amazon S3, Amazon RDS) to understand which services your solutions drive consumption for.
- **AWS Account ID:** Filter by specific AWS account IDs to view revenue associated with an account.

## Key metrics

The dashboard displays three key metrics at the top of the page:

- **Products Measured:** The number of your AWS Marketplace products that have attributed revenue measured by Partner Revenue Measurement during the selected time frame.
- **AWS Services Measured:** The number of distinct AWS services where your products are driving consumption during the selected time frame.
- **Total Attributed Revenue:** The total aggregated revenue measured by Partner Revenue Measurement across all your products and AWS services during the selected time frame.

## Charts

**Attributed Revenue by Product**

This chart displays month-over-month attributed revenue for each of your AWS Marketplace products. Each product is represented as a separate series, allowing you to compare revenue trends across your product portfolio over time. Use this chart to identify which products are driving the most AWS consumption and monitor growth patterns.

**Attributed Revenue by AWS Service**

This chart displays attributed revenue by AWS service. Use this chart to understand which AWS services your solutions drive the most consumption for and how service-level revenue trends change over time.

## Tables

**Attributed Revenue**

This table shows attributed revenue measured by Partner Revenue Measurement capabilities aggregated by Partner product and AWS service. The table includes the following columns:

- **Product Name:** The name of your AWS Marketplace product.
- **AWS Service:** The AWS service where consumption was measured.
- **Billing Month:** The month for which revenue was measured.
- **Attributed Revenue:** The aggregated revenue amount for the product-service-month combination.

**Onboarding Status**

This table shows your products that are enabled with any of the Partner Revenue Measurement capabilities. Use this table to verify that your PRM implementation is active and to identify products that may need additional configuration. The table displays:

- **Product Name:** The name of your AWS Marketplace product.
- **PRM Capability:** The Partner Revenue Measurement capability enabled for the product — Resource Tagging, User Agent string, or AWS Marketplace Metering.
- **Status:** Whether the capability is actively measuring revenue for the product.

## Data availability and privacy

- Attributed revenue data is processed monthly and becomes available 17 days after the month ends for the previous month.
- Partners have visibility to aggregated attributed revenue data at the product and AWS service level.

For additional information regarding data sharing and privacy, please see the PRM [Frequently Asked Questions](https://partnercentral.awspartner.com/partnercentral2/s/article?category=Funding_Operations_and_Management&article=Partner-Revenue-Measurement-Overview "https://partnercentral.awspartner.com/partnercentral2/s/article?category=Funding_Operations_and_Management&article=Partner-Revenue-Measurement-Overview") in Partner Central (login required).

## Prerequisites

To access the Attributed Revenue dashboard, you must:

1. Migrate to AWS Partner Central in the Console; and
2. Implement at least one Partner Revenue Measurement capability — [Resource Tagging](../../../PRM/latest/aws-prm-onboarding-guide/resource-tagging.md "../../../PRM/latest/aws-prm-onboarding-guide/resource-tagging.md"), [User Agent string](../../../PRM/latest/aws-prm-onboarding-guide/user-agent-string.md "../../../PRM/latest/aws-prm-onboarding-guide/user-agent-string.md"), or have an AMI or ML product listed on AWS Marketplace (for automatic [Marketplace Metering](../../../PRM/latest/aws-prm-onboarding-guide/marketplace-metering-implementation.md "../../../PRM/latest/aws-prm-onboarding-guide/marketplace-metering-implementation.md")).

Partners with connected subsidiary accounts will see aggregated revenue across all connected accounts in a single view.

## Learn more

- [Partner Revenue Measurement Onboarding Guide](../../../PRM/latest/aws-prm-onboarding-guide/what-is-service.md "../../../PRM/latest/aws-prm-onboarding-guide/what-is-service.md")
- [Resource Tagging Implementation](../../../PRM/latest/aws-prm-onboarding-guide/resource-tagging.md "../../../PRM/latest/aws-prm-onboarding-guide/resource-tagging.md")
- [User Agent String Implementation](../../../PRM/latest/aws-prm-onboarding-guide/user-agent-string.md "../../../PRM/latest/aws-prm-onboarding-guide/user-agent-string.md")
- [AWS Marketplace Metering](../../../PRM/latest/aws-prm-onboarding-guide/marketplace-metering-implementation.md "../../../PRM/latest/aws-prm-onboarding-guide/marketplace-metering-implementation.md")
