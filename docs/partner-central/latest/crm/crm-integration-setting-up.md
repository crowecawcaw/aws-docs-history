

# Integration prerequisites
<a name="crm-integration-setting-up"></a>

The following topics list the prerequisites needed for using the AWS Partner CRM connector, and for a Partner Central API integration. For information about the prerequisites for a third-party integration, contact your integration provider.

Expand each section to learn more.

## General prerequisites
<a name="stage-1-prerequisites"></a>

To use the CRM connector or create a Partner Central API integration, you must have the following prerequisites.
+ **An AWS account**. To use the Partner Central API, you must have an AWS account or an AWS Marketplace seller account for account linking. To integrate the CRM connector with AWS Marketplace, you must have a seller account.

  To create an AWS account, navigate to [Sign up for AWS](https://signin.aws.amazon.com/signup?request_type=register). For information about creating a seller account, refer to [ Registering as an AWS Marketplace seller](https://docs.aws.amazon.com/marketplace/latest/userguide/seller-registration-process.html) in the *AWS Marketplace Seller Guide*.
+ **An AWS Partner Central account**. For information about creating the account, refer to [Registering in AWS Partner Central](https://docs.aws.amazon.com/partner-central/latest/getting-started/registering.html) in the *AWS Partner Central Getting Started Guide*. 
+ **Linked Partner Central and AWS Marketplace seller accounts**. For information about linking the accounts, refer to [Linking your AWS Partner Central and AWS Marketplace accounts](link-pc-mkt-accounts.md) later in this guide.
+ **An IAM user in your AWS Marketplace seller account**. The user enables the connector to authenticate Salesforce on AWS. For more information, refer to [Creating the IAM user in your AWS Marketplace seller account](create-iam-user-seller-account.md) later in this guide.
+ **[Amazon S3 permissions for the AWS Marketplace IAM user](s3-iam-perms.md).**

## Required user roles for integration
<a name="whos-involved-in-setting-up-the-integration"></a>

Setting up an integration requires people with the following roles:
+ **Salesforce administrator**.
+ **Partner alliance lead** – Has permission to initiate a new Integration request through Partner Central. The partner alliance lead oversees the progress of the Integration and monitors the status from the CRM Integration page in Partner Central.
+ **Program manager** – Entrusted with driving the Integration process from the partner’s side. This person is able to define essential processes and necessary enablement post-integration.
+ **Partner CRM administrator** – Helps map fields between AWS and the partner’s CRM. If partners choose an Integration through the AWS Partner CRM connector, the administrator is critical to its setup.
+ **Developers** – For partners who choose the custom option, developers build and implement the custom Integration.
+ **Partner cloud operations and IT team** – Configures authentication credentials, such as the IAM user or role. This involves creating an AWS account and an AWS user for secure access.
+ **AWS Partner development manager (PDM)** – The partner’s AWS contact. You route all communication with the AWS team through the PDM. For more information, refer to [Integration FAQ](crm-integration-faq.md) later in this guide. 
+ **AWS Partner solutions architect (PSA)** – Works closely with the PDM to assist with any technical questions from the partner.
+ **AWS CRM Integration support** – Addresses technical support issues that partners raise through the Support Center in Partner Central.