

# Implementation Methods

AWS Revenue Measurement supports the following implementation methods. Choose the method that best fits your product type and architecture.

## Methods Overview
<a name="methods-overview"></a>


| Method | Description | Best For | 
| --- | --- | --- | 
| [AWS Marketplace Metering](marketplace-metering.md) | Zero-touch revenue attribution through AWS Marketplace product metadata | Amazon Machine Image (AMI) and Machine Learning (ML) products listed on AWS Marketplace | 
| [Resource Tagging](resource-tagging.md) | Tag AWS resources with your product code using the tag key format aws-apn-id-{{partner-central-aws-account-id}} (e.g., aws-apn-id-012345678901). For how to construct your tag key, see [Constructing Your Tag Key and Value](manual-tagging.md#tag-key-construction) | SaaS, Professional Services, and any product type where you can tag AWS resources | 
| [User Agent String](user-agent-string.md) | Include a User Agent string in regular AWS API/CLI calls with your product code | Products with direct regular AWS API/CLI access; AMI/ML products seeking attribution beyond EC2/SageMaker | 
| [Identity Tagging](identity-tagging.md) | Tag the IAM role or user your organization operates with for revenue attribution based on API actions performed on billable AWS resources | MSPs, SIs, consulting partners, and GenAI/software partners operating in customer accounts via IAM roles or users; partners whose contribution is through identity-based engagement rather than resource ownership or SDK embedding | 
| [Account Tagging for SaaS products](account-tagging.md) | Tag the AWS account(s) that host your product (via AWS Organizations) using the tag key format aws-apn-id-{{partner-central-aws-account-id}}. All included AWS Revenue Measurement services usage in that account is attributed to your product | SaaS products on AWS Marketplace hosted in partner-owned accounts, with each account dedicated to a single product | 
| [Revenue Attribution IDs](revenue-attribution-id.md) | A unique identifier you create in AWS Partner Central, in the Console or through the AWS Revenue Measurement APIs, that links product-level AWS Revenue Measurement to specific AWS Marketplace offers and/or ACE opportunities. Use it on top of your existing product-level implementation method, or on its own as a resource tag value or User Agent string. For SaaS products hosted in a partner-owned account, the Marketplace Revenue Share lets you declare the share of a product's (or group of products') revenue that came through AWS Marketplace. AWS then calculates attributed revenue for each active offer, so you need a Revenue Attribution ID only to override an offer or attribute revenue to a co-sell opportunity. | Partners attributing revenue at the deal level, including multi-tenant SaaS products with shared infrastructure (automated through the Marketplace Revenue Share) and co-sell opportunities | 

**Note**  
You can implement multiple methods simultaneously. For example, an AMI product can benefit from AWS Marketplace Metering for EC2 attribution and User Agent String for attribution on additional AWS services used by the product.

## Choosing the Right Method
<a name="choosing-method"></a>

The following table provides guidance on choosing the right method based on your scenario:


| Scenario | Use Resource Tagging when... | Use User Agent String when... | Marketplace Metering | Use Identity Tagging when... | Use Account Tagging for SaaS products when... | Use Revenue Attribution IDs when... | 
| --- | --- | --- | --- | --- | --- | --- | 
| Marketplace AMI/ML | — | — | Automatic | — | — | — | 
| Partner Account (SaaS) | Static infrastructure, deploy once and runs long-term | Partner solution makes frequent regular AWS API/CLI calls | — | — | Each partner-owned account hosts a single SaaS product | Declare a Marketplace Revenue Share for automated offer-level attribution; use an RA ID to override offers or attribute ACE opportunities | 
| Customer Account (deploy/manage) | Deploy via IaC (CloudFormation, Terraform), customer allows tags | Partner solution makes ongoing regular AWS API/CLI calls, or customer has strict tag policies | — | Partner operates in customer account via IAM role (cross-account or same-account) to manage, deploy, or invoke AWS services | — | RA ID used as tag value or in User Agent string (Marketplace Revenue Share not applicable) | 
| Customer Account (read/access only) | Customer willing to tag their resources | Your solution makes read API calls | — | Partner performs read or operational API calls on billable resources via their own IAM role | — | RA ID as tag value or in User Agent string, or link your existing product-level implementation to an RA ID (no rework) | 
| Hybrid (Partner \+ Customer) | Taggable resources in either account | Partner solution makes regular AWS API/CLI calls in either account | — | Partner operates via tagged IAM roles in customer accounts; tag the role your organization assumes | Partner-hosted components, if each partner-owned account hosts a single product | Declare a Marketplace Revenue Share for partner-hosted components; use cost allocation % for overrides and opportunities | 

## Decision Tree
<a name="decision-tree"></a>

The following decision tree helps you determine the right implementation method:



![AWS Revenue Measurement decision tree for choosing an implementation method across AWS Marketplace Metering, Resource Tagging, User Agent String, Identity Tagging, and SaaS Account Tagging](https://docs.aws.amazon.com/PRM/latest/aws-prm-onboarding-guide/images/PRM-decision-tree.png)




## Special Scenarios
<a name="special-scenarios"></a>


| Scenario | Use Resource Tagging when... | Use User Agent String when... | Marketplace Metering | Use Identity Tagging when... | Use Account Tagging for SaaS products when... | Use Revenue Attribution IDs when... | 
| --- | --- | --- | --- | --- | --- | --- | 
| Managed Services Provider (MSP) or Systems Integrator (SI/GSI) with limited access | Where write access allows. Provide IaC templates with tags embedded for customer to run | In management regular AWS API/CLI calls. Modify agents or installers to include UA strings | — | Tag the cross-account IAM role your organization assumes to manage customer workloads. Attribution is based on API actions performed on billable resources — no per-resource tagging or customer-side changes required | — | Use RA ID as tag value or in User Agent string | 
| Multi-partner on same AWS resource | Each partner can apply their own unique tag key (aws-apn-id-{{partner-central-aws-account-id}}). When more than one partner tags the same resource, each partner receives revenue attribution | Each partner uses own UA string in their respective regular AWS API/CLI calls, no conflicts | — | Each partner tags their own IAM role using their partner-scoped key (aws-apn-id-{{partner-central-aws-account-id}}). When multiple partners' tagged identities act on the same resource, revenue splits equally (1/N) across distinct partners | — | Each partner uses own RA ID; no conflicts | 
| Backfill existing resources | Bulk tag via Tag Editor or scripted bulk tagging for large-scale backfill. Revenue attribution will only be moving forward from the time tags are applied | Add UA to existing regular AWS API/CLI calls — often the lowest-effort path. Revenue attribution will only be moving forward from the time User Agent strings are implemented | — | Tag existing IAM roles your organization already operates with. Attribution begins the billing month after tag detection (5-day detection SLA); no historical backfill — all attribution is forward-looking from the month following implementation | Tag existing dedicated accounts; attribution is forward-looking only | Attribution applies to current and future months only | 

## Key Considerations
<a name="key-considerations"></a>
+ **Resource Tagging:** Tags are key-value pairs applied to a resource to hold metadata about that resource, in this case a partner identifier. The tag type is a user-defined tag, and can be managed (updated or removed), and counts against the 50-tag-per-resource limit. Attribution is continuous while the tag is present.
+ **User Agent String:** Ephemeral, specific to the regular AWS API/CLI operation carried out on a specific AWS resource, and is read-only. Allows multiple partners to independently use their identifier within their respective regular AWS API/CLI calls. Visible in CloudTrail, enabling customers to govern partner-solution interactions within their AWS resources. Requires at least one regular AWS API/CLI call per resource per month for attribution.
+ **Identity Tagging:** Tag is applied to the IAM principal (role or user) itself, not to individual workload resources. The tag counts against the 50-tag-per-principal limit. Attribution is based on API actions the tagged identity performs on billable AWS resources; account-level operations that do not reference a billable resource (e.g., sts:AssumeRole) do not generate attribution. Attribution begins the billing month after tag detection (5-day detection SLA); no historical backfill. When the tag is removed or the principal is deleted, attribution is retained for the current billing month and stops from the following month. Multiple partners can independently tag the same principal using partner-scoped keys. Not supported for federated users via AWS IAM Identity Center at launch.
+ **Multi-partner:** For multi-partner scenarios, both Resource Tagging and User Agent String are supported. With Resource Tagging, each partner applies their own partner-unique tag key (`aws-apn-id-{{partner-central-aws-account-id}}`), so up to 10 partners can tag the same resource and each receives independent attribution. When more than one partner tags the same resource, or uses the user agent string in an API call involving the same resource, each partner receives revenue attribution.
+ **Production only:** AWS Revenue Measurement is intended to measure production workloads. Dev/test/staging environments can be used for validating your implementation before rolling out to production.