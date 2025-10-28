# How ROSA works with AWS Marketplace

AWS Marketplace is a curated digital catalog that you can use to find, buy, deploy, and manage third-party software, data, and services that you need to build solutions and run your business.
AWS Marketplace simplifies software licensing and procurement with flexible pricing options and multiple deployment methods.

ROSA uses AWS Marketplace for service metering and billing.
ROSA classic is metered and billed through an AWS Marketplace Amazon Machine Image (AMI)-based product, whereas ROSA with hosted control planes (HCP) is metered and billed through an AWS Marketplace software as a service (SaaS)-based product.

This page explains how ROSA works with AWS Marketplace for payments, billing, subscriptions, and contract purchases.

## Terminology

This page uses the following terms when discussing ROSA’s integration with AWS Marketplace.

**Amazon Machine Image (AMI)**

An image of a server, including an operating system and additional software, that runs on AWS.

**AMI subscription**

In AWS Marketplace, AMI-based software products such as ROSA classic use an hourly with annual subscription pricing model.
Hourly pricing is the default pricing model, but you have the option to purchase a year’s worth of usage upfront for one Amazon EC2 instance type.

**SaaS subscription**

In AWS Marketplace, software-as-a-service (SaaS) products such as ROSA with HCP adopt a usage-based subscription model.
The software seller tracks your usage and you pay only for what you use.

**Public offer**

Public offers allow you to purchase AWS Marketplace software and services directly from the AWS Management Console.

**Private offer**

Private offers are a purchasing program that allow sellers and buyers to negotiate custom prices and end user licensing agreement (EULA) terms for purchases in AWS Marketplace.

**ROSA service fees**

Fees that ROSA charges for the OpenShift software and cluster management by Red Hat site reliability engineers (SREs).
ROSA service fees are metered through AWS Marketplace and appear on your AWS bill.

**AWS infrastructure fees**

Standard fees that AWS charges for the AWS services underlying ROSA clusters, including Amazon EC2, Amazon EBS, Amazon S3, and Elastic Load Balancing.
Fees are metered through the AWS service being used and appear on your AWS bill.

## ROSA payments and billing

ROSA integrates with AWS Marketplace to enable metering and billing of ROSA service fees.
ROSA service fees cover access to OpenShift software and cluster management by Red Hat site reliability engineers (SREs).
ROSA service fees are uniform across all supported AWS standard Regions.
ROSA with HCP service fees accrue on demand by default at a flat hourly rate based on the number of running clusters and worker node vCPUs running in those clusters.
ROSA classic service fees accrue on demand based on the number of worker node vCPUs.
ROSA classic does not charge service fees for the control plane or required infrastructure nodes.

ROSA customers also pay standard AWS infrastructure fees for the AWS services underlying ROSA clusters, including Amazon EC2, Amazon EBS, Amazon S3, and Elastic Load Balancing.
AWS infrastructure fees are a separate billing item from the ROSA service fees that are metered through AWS Marketplace.
AWS infrastructure fees vary by AWS Region and are based on hourly usage by default.
For additional AWS infrastructure cost savings, you can purchase Amazon EC2 savings plans or reserved instances.
For more information, see [Compute Savings Plans](https://aws.amazon.com/savingsplans/compute-pricing/ "https://aws.amazon.com/savingsplans/compute-pricing/") and [Reserved Instances](../../../AWSEC2/latest/UserGuide/ec2-reserved-instances.md "../../../AWSEC2/latest/UserGuide/ec2-reserved-instances.md") in the _Amazon EC2 User Guide_.

ROSA does not charge fees until you create a ROSA cluster, or purchase a ROSA contract.
For more information, see [Red Hat OpenShift Service on AWS pricing](https://aws.amazon.com/rosa/pricing "https://aws.amazon.com/rosa/pricing").

You can view ROSA service fees and AWS infrastructure fees and manage payments in the [AWS Billing console](https://console.aws.amazon.com/billing "https://console.aws.amazon.com/billing").
You can also view your costs and monitor usage using the AWS Cost Explorer Service interface free of charge.
For more information, see [Viewing your bill](../../../awsaccountbilling/latest/aboutv2/getting-viewing-bill.md "../../../awsaccountbilling/latest/aboutv2/getting-viewing-bill.md") in the _AWS Billing and Cost Management User Guide_ and [Analyzing your costs with AWS Cost Explorer Service](../../../cost-management/latest/userguide/ce-what-is.md "../../../cost-management/latest/userguide/ce-what-is.md") in the _AWS Cost Management User Guide_.

## Subscribing to ROSA Marketplace listings through the console

When you enable ROSA in the [ROSA console](https://console.aws.amazon.com/rosa "https://console.aws.amazon.com/rosa"), your AWS account is subscribed to the ROSA classic and ROSA with HCP listings on AWS Marketplace.
There is no fee for enabling ROSA subscriptions.

For AWS Organizations users, ROSA allows you to share ROSA classic subscriptions with other accounts in your organization.
For more information, see [Sharing subscriptions in an organization](../../../marketplace/latest/buyerguide/organizations-sharing.md "../../../marketplace/latest/buyerguide/organizations-sharing.md") in the _AWS Marketplace Buyer Guide_.

## Purchasing a ROSA contract

ROSA uses AWS Marketplace to provide optional contracts for ROSA with HCP and ROSA classic. Contracts provide savings on ROSA worker node service fees. ROSA contracts do not impact the fees charged for AWS infrastructure.

### 12-month contracts

You can purchase 12-month public offer contracts for ROSA classic and ROSA with HCP from the ROSA console.

###### Note

ROSA classic must be enabled on your account before you can purchase 12-month contracts from the console.

###### Note

12-month contracts cannot be transferred to a private offer.

#### Purchasing a ROSA classic 12-month contract

When you purchase a ROSA classic 12-month contract, you make a upfront payment for an annual term and pay no hourly service fee for the next 12 months for the covered instances.
Contract cost is based on the Amazon EC2 instance type and number of instances that you select.
The contract does not cover the AWS infrastructure fees that ROSA charges for the underlying AWS services that are used.
For more information, see [Red Hat OpenShift Service on AWS Pricing](https://aws.amazon.com/rosa/pricing "https://aws.amazon.com/rosa/pricing").

The contract covers only the instance types that you specify during contract creation (m5.xlarge for example).
You can purchase additional 12-month contracts for cost savings on more than one Amazon EC2 instance type.
Usage outside of your 12-month contract incurs ROSA service fees at the on-demand rate.

###### Note

ROSA classic 12-month contracts do not auto renew.

**To purchase a 12-month contract for ROSA classic**

###### Note

If you are using the ROSA console in a Region that does not yet support ROSA with HCP, this workflow is not yet available.
For a list of Regions that support ROSA with HCP, see [Comparing ROSA with HCP and ROSA classic](rosa-architecture-models.md#rosa-architecture-differences "rosa-architecture-models.md#rosa-architecture-differences").

To purchase ROSA classic contracts in Regions without ROSA with HCP support, go to the [ROSA console](https://console.aws.amazon.com/rosa "https://console.aws.amazon.com/rosa") and choose **Purchase a software contract and view existing contracts**.

1. Go to the [ROSA console](https://console.aws.amazon.com/rosa "https://console.aws.amazon.com/rosa").
2. On the left navigation pane, choose **Contracts**.
3. Choose **Contracts for ROSA classic**.
4. Choose **Purchase contract**.
5. Select the EC2 instance type and number of instances that you need.
6. Choose **Review contract**.
7. Review the contract details and choose **Purchase contract**.

###### Note

ROSA 12-month contracts cannot be downgraded or cancelled after creation using the console.
If you need to downgrade or cancel the contract during the active contract duration, go to [Support Center](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support") and open a support case.

#### Purchasing a ROSA with HCP 12-month contract

When you enable ROSA with HCP in the console, a no-cost 12-month ROSA with HCP contract is initially created on your account to facilitate on-demand billing.
If you choose to purchase a ROSA with HCP contract to save on worker node service fees, the initial contract is modified to cover usage costs for the worker node vCPUs and control planes that you specify.

When you purchase a ROSA with HCP 12-month contract, you make an upfront payment for an annual term and pay no hourly usage fee for the next 12 months for the covered worker node vCPUs and control planes.
Contract cost is based on the number of worker node vCPUs and control planes that you select.
The contract covers only the worker node vCPUs and control planes that you specify during contract creation.
The contract does not cover the AWS infrastructure fees that ROSA charges for the underlying AWS services that are used.
For more information, see [Red Hat OpenShift Service on AWS Pricing](https://aws.amazon.com/rosa/pricing "https://aws.amazon.com/rosa/pricing").

##### Monthly usage quota

Upon purchase, your prepaid vCPUs and control planes are converted to a monthly usage quota.
Hourly on-demand usage rates apply for vCPU and control plane usage that exceeds the monthly quota.
ROSA with HCP uses the following formulas to calculate the monthly quota associated with the contract:

- **Worker node vCPUs:** number of vCPUs x 24 hours x 365 days / 12 months
- **Control planes:** number of control planes x 24 hours x 365 days / 12 months

For example, a purchase of 4,000 worker node vCPUs and 8 control planes would convert to a monthly quota of 2,920,000 worker node vCPU hours and 5,840 control plane hours consumable per month.

**To purchase a ROSA with HCP 12-month contract**

###### Note

If you are using the Red Hat OpenShift Service on AWS console in a Region that doesn’t yet support ROSA with hosted control planes, this workflow is not yet available.
For a list of Regions that support ROSA with HCP, see [Comparing ROSA with HCP and ROSA classic](rosa-architecture-models.md#rosa-architecture-differences "rosa-architecture-models.md#rosa-architecture-differences").

1. Go to the [ROSA console](https://console.aws.amazon.com/rosa "https://console.aws.amazon.com/rosa").
2. On the left navigation pane, choose **Contracts**.
3. Choose **Contracts for ROSA with HCP**.
4. Choose **Purchase contract**.
5. Enter the number of vCPUs to purchase. Specify in multiples of 4.
6. Enter the number of control planes to purchase.
7. Choose **Review contract**.
8. Review the contract details and choose **Purchase contract**.

###### Note

ROSA 12-month contracts cannot be downgraded or cancelled after creation using the console.
If you need to downgrade or cancel the contract during the active contract duration, go to [Support Center](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support") and open a support case.

##### Upgrading a ROSA with HCP 12-month contract

You can upgrade your active ROSA with HCP 12-month contract at any time with additional worker node vCPUs and control planes.
When you upgrade your ROSA with HCP 12-month contract, you make an upfront prorated payment for the added resources.
Prorated amounts are calculated based on the number of days remaining on the contract.
The contract covers only the worker node vCPUs and control planes that you specify during contract creation.
Contract upgrades do not impact the fees charged for AWS infrastructure.

Upon upgrade, the added vCPUs and control planes are converted to a monthly usage quota using the same formulas as the original contract purchase.
Hourly on-demand usage rates apply for vCPU and control plane usage that exceeds the monthly quota.
For more information, see [Monthly usage quota](#purchase-rosa-classic-public-contract-monthly-quota "#purchase-rosa-classic-public-contract-monthly-quota").

**To upgrade a ROSA with HCP 12-month contract**

1. Go to the [ROSA console](https://console.aws.amazon.com/rosa "https://console.aws.amazon.com/rosa").
2. On the left navigation pane, choose **Contracts**.
3. Choose **Contracts for ROSA with HCP**.
4. Choose **Upgrade**.
5. Enter the number of vCPUs to add. Specify in multiples of 4.
6. Enter the number of control planes to add to the contract.
7. Choose **Review upgrade**.
8. Review the contract details and choose **Purchase upgrade**.

###### Note

ROSA classic 12-month contracts cannot be upgraded.
Additional 12-month ROSA classic contracts can be purchased at any time using the ROSA console.

### Obtaining a private offer

You can request an AWS Marketplace private offer for ROSA with HCP or ROSA classic to receive product pricing and end user licensing agreement (EULA) terms negotiated with Red Hat.
For more information, see [Private offers](../../../marketplace/latest/buyerguide/buyer-private-offers.md "../../../marketplace/latest/buyerguide/buyer-private-offers.md") in the _AWS Marketplace Buyer Guide_.

**To obtain a ROSA private offer**

###### Note

If you are an AWS Organizations user and received a private offer that was issued to your payer and member accounts, follow the procedure below to subscribe to ROSA directly on each account in your organization.

If you receive a ROSA classic private offer that was only issued to the AWS Organizations payer account, you will need to share the subscription with members accounts in your organization.
For more information, see [Sharing subscriptions in an organization](../../../marketplace/latest/buyerguide/organizations-sharing.md "../../../marketplace/latest/buyerguide/organizations-sharing.md") in the _AWS Marketplace Buyer Guide_.

1. Once a private offer has been issued, sign in to the [AWS Marketplace console](https://console.aws.amazon.com/marketplace "https://console.aws.amazon.com/marketplace").
2. Open the email with a ROSA private offer link.
3. Follow the link to directly access the private offer.

###### Note

Following this link before logging in to the correct account will result in a **Page note found** (404) error. 4. Review the terms and conditions. 5. Choose **Accept terms**.

###### Note

If an AWS Marketplace private offer is not accepted, the ROSA service fees from AWS Marketplace will continue to be billed at the public hourly rate. 6. To verify the offer details, select **Show details** in the product listing. 7. To get started using ROSA, choose **Continue to configuration**. You will be redirected to the ROSA console.

## Private Marketplace

Private Marketplace enables administrators to build customized digital catalogs of approved products from AWS Marketplace.
Administrators can create unique sets of vetted software available in AWS Marketplace for AWS organizational units or different AWS accounts within their organization to purchase.

If your organization uses a private marketplace, an administrator must add the AWS Marketplace listings for ROSA to the private marketplace before users can enable the service.
For more information, see [Getting started with private marketplace](../../../marketplace/latest/buyerguide/private-catalog-administration.md "../../../marketplace/latest/buyerguide/private-catalog-administration.md") in the _AWS Marketplace Buyer Guide_.
