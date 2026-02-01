# Resource Tagging Prerequisites

Before implementing Resource Tagging, you must have:

1. **AWS Partner Central and AWS account linking**

Before linking accounts, AWS Partners must understand that this linked AWS account will become the primary account for managing all APN activities in Partner Central. This account will:

    * Determine Partner Revenue Measurement compliance for APN funding benefits eligibility
    * Serve as the primary account for the migration to the new Partner Central experience and all Partner Central users will need to be provisioned access
    * Be billed for the annual APN membership fee

When determining which AWS account to link, consider these options:

**Option A. Partners with one AWS Marketplace account**

Evaluate your existing AWS Marketplace account against the [account selection guidance criteria](https://partnercentral.awspartner.com/partnercentral2/s/article?category=Introductory_resources&article=AWS-Partner-Central-and-AWS-account-linking-How-to-Get-Started "https://partnercentral.awspartner.com/partnercentral2/s/article?category=Introductory_resources&article=AWS-Partner-Central-and-AWS-account-linking-How-to-Get-Started") (Partner Central login required). Link your AWS Marketplace account if you're comfortable with:

    * Provisioning Partner Central user access to this account
    * Using this account as your primary account for APN engagements
    * Being billed the APN membership fee on this account

If you prefer not to designate your AWS Marketplace account as your primary account, create a new AWS account or link an existing non-AWS Marketplace account that meets the above criteria.

**Option B. Partners with multiple AWS Marketplace accounts**

Evaluate your AWS Marketplace accounts against the [account selection guidance criteria](https://partnercentral.awspartner.com/partnercentral2/s/article?category=Introductory_resources&article=AWS-Partner-Central-and-AWS-account-linking-How-to-Get-Started "https://partnercentral.awspartner.com/partnercentral2/s/article?category=Introductory_resources&article=AWS-Partner-Central-and-AWS-account-linking-How-to-Get-Started") (Partner Central login required).

###### Note

AWS recommends creating and linking a new AWS account to represent your global business, then connecting all individual AWS Marketplace accounts to your primary account using Subsidiary Account Connections (accessible only after migrating to the new Partner Central experience).

Complete these three steps:

    1. [Create and link](https://partnercentral.awspartner.com/partnercentral2/s/article?category=Introductory_resources&article=AWS-Partner-Central-and-AWS-account-linking-How-to-Get-Started "https://partnercentral.awspartner.com/partnercentral2/s/article?category=Introductory_resources&article=AWS-Partner-Central-and-AWS-account-linking-How-to-Get-Started") an AWS account (which will become your primary account) to your Partner Central account
    2. [Migrate](https://partnercentral.awspartner.com/partnercentral2/s/article?category=Introductory_resources&article=AWS-Partner-Central-and-AWS-account-linking-How-to-Get-Started "https://partnercentral.awspartner.com/partnercentral2/s/article?category=Introductory_resources&article=AWS-Partner-Central-and-AWS-account-linking-How-to-Get-Started") to the new Partner Central experience (Partner Central login required)
    3. Link all AWS Marketplace accounts to your primary AWS account through [Subsidiary Account Connections](../../../partner-central/latest/getting-started/manage-subsidiary.md "../../../partner-central/latest/getting-started/manage-subsidiary.md") (Partner Central login required)

2. **Product listing on AWS Marketplace (Public or Limited)**

See the [AWS Marketplace Seller Guide](../../../marketplace/latest/userguide/user-guide-for-sellers.md "../../../marketplace/latest/userguide/user-guide-for-sellers.md") for general information. For product-specific listing guide instructions:

| Product Type          | Listing Guide                                                                                                                                                                                            |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SaaS                  | [SaaS Product Listing Guide](../../../marketplace/latest/userguide/saas-create-product.md "../../../marketplace/latest/userguide/saas-create-product.md")                                                |
| Professional Services | [Professional Services Listing Guide](../../../marketplace/latest/userguide/proserv-getting-started.md#proserv-create "../../../marketplace/latest/userguide/proserv-getting-started.md#proserv-create") |

3. **Product that uses one or more of the [supported AWS services](included-aws-services.md "included-aws-services.md")**
4. **Ability to tag AWS resources in your own account or in customer's account**
5. **Ensure that Cost Explorer is enabled**

To learn how to enable Cost Explorer, see [Enabling Cost Explorer](../../../cost-management/latest/userguide/ce-enable.md "../../../cost-management/latest/userguide/ce-enable.md").
