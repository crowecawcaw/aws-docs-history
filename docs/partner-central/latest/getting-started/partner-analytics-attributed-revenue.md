

# Attributed Revenue

The Attributed Revenue dashboard provides visibility into the AWS revenue impact of your solutions as measured by AWS Revenue Measurement. The dashboard displays aggregated monthly attributed revenue by Partner product, AWS service, and billing period.

For more information, review the AWS Revenue Measurement [Onboarding Guide](https://docs.aws.amazon.com/PRM/latest/aws-prm-onboarding-guide/what-is-service.html) and [FAQs](https://docs.aws.amazon.com/PRM/latest/aws-prm-onboarding-guide/prm-faqs).

## Filters
<a name="attributed-revenue-filters"></a>

The Attributed Revenue dashboard incorporates the following filtering capabilities for analyzing your attributed revenue data:
+ **Time Frame:** Select a date range to view attributed revenue for specific billing periods.
+ **Product Name:** Filter by one or more of your AWS Marketplace product listings to view revenue for specific products. 
+ **AWS Service:** Filter by specific AWS services (for example, Amazon EC2, Amazon S3, Amazon RDS) to understand which services your solutions drive consumption for.
+ **AWS Account ID:** Filter by specific AWS account IDs to view revenue associated with an account. 

## Key metrics
<a name="attributed-revenue-key-metrics"></a>

The dashboard displays three key metrics at the top of the page:
+ **Products Measured:** The number of your AWS Marketplace products that have attributed revenue measured by AWS Revenue Measurement during the selected time frame.
+ **AWS Services Measured:** The number of distinct AWS services where your products are driving consumption during the selected time frame.
+ **Total Attributed Revenue:** The total aggregated revenue measured by AWS Revenue Measurement across all your products and AWS services during the selected time frame.

## Charts
<a name="attributed-revenue-charts"></a>

**Attributed Revenue by Product**

This chart displays month-over-month attributed revenue for each of your AWS Marketplace products. Each product is represented as a separate series, allowing you to compare revenue trends across your product portfolio over time. Use this chart to identify which products are driving the most AWS consumption and monitor growth patterns.

**Attributed Revenue by AWS Service**

This chart displays attributed revenue by AWS service. Use this chart to understand which AWS services your solutions drive the most consumption for and how service-level revenue trends change over time.

## Tables
<a name="attributed-revenue-tables"></a>

**Attributed Revenue**

This table shows attributed revenue measured by AWS Revenue Measurement capabilities aggregated by Partner product and AWS service. The table includes the following columns:
+ **Product Name:** The name of your AWS Marketplace product.
+ **AWS Service:** The AWS service where consumption was measured.
+ **Billing Month:** The month for which revenue was measured.
+ **Attributed Revenue:** The aggregated revenue amount for the product-service-month combination.

**Onboarding Status**

This table shows your products that are enabled with any of the AWS Revenue Measurement capabilities. Use this table to verify that your AWS Revenue Measurement implementation is active and to identify products that may need additional configuration. The table displays:
+ **Product Name:** The name of your AWS Marketplace product.
+ **AWS Revenue Measurement Capability:** The AWS Revenue Measurement capability enabled for the product — Resource Tagging, User Agent string, or AWS Marketplace Metering.
+ **Status:** Whether the capability is actively measuring revenue for the product. 

## Data availability and privacy
<a name="attributed-revenue-data-availability"></a>
+ Attributed revenue data is processed monthly and becomes available 17 days after the month ends for the previous month.
+ Partners have visibility to aggregated attributed revenue data at the product and AWS service level.

For additional information about data sharing and privacy, see the AWS Revenue Measurement [Frequently Asked Questions](https://us-east-1.console.aws.amazon.com/partnercentral/content/guidedetails/56a8de82-77d0-4337-bb9e-c24059ac5067) in Partner Central (login required).

## Prerequisites
<a name="attributed-revenue-prerequisites"></a>

To access the Attributed Revenue dashboard, you must:

1. Migrate to AWS Partner Central in the Console; and 

1. Implement at least one AWS Revenue Measurement capability — [Resource Tagging](https://docs.aws.amazon.com/PRM/latest/aws-prm-onboarding-guide/resource-tagging.html), [Identity Tagging](https://docs.aws.amazon.com/PRM/latest/aws-prm-onboarding-guide/identity-tagging.html), [Account Tagging for SaaS products](https://docs.aws.amazon.com/PRM/latest/aws-prm-onboarding-guide/account-tagging.html), [User Agent string](https://docs.aws.amazon.com/PRM/latest/aws-prm-onboarding-guide/user-agent-string.html), or have an AMI or ML product listed on AWS Marketplace (for automatic [Marketplace Metering](https://docs.aws.amazon.com/PRM/latest/aws-prm-onboarding-guide/marketplace-metering-implementation.html)).

Partners with connected subsidiary accounts will see aggregated revenue across all connected accounts in a single view.

## Learn more
<a name="attributed-revenue-learn-more"></a>
+ [AWS Revenue Measurement Onboarding Guide](https://docs.aws.amazon.com/PRM/latest/aws-prm-onboarding-guide/what-is-service.html)
+ [Resource Tagging Implementation](https://docs.aws.amazon.com/PRM/latest/aws-prm-onboarding-guide/resource-tagging.html)
+ [Identity Tagging Implementation](https://docs.aws.amazon.com/PRM/latest/aws-prm-onboarding-guide/identity-tagging.html)
+ [Account Tagging for SaaS Products](https://docs.aws.amazon.com/PRM/latest/aws-prm-onboarding-guide/account-tagging.html)
+ [User Agent String Implementation](https://docs.aws.amazon.com/PRM/latest/aws-prm-onboarding-guide/user-agent-string.html)
+ [AWS Marketplace Metering](https://docs.aws.amazon.com/PRM/latest/aws-prm-onboarding-guide/marketplace-metering-implementation.html)