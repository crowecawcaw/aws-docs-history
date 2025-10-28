# Integration prerequisites

The following topics list the prerequisites needed for using the AWS Partner CRM connector, and for a Partner Central API integration. For information about the prerequisites for a third-party
integration, contact your integration provider.

Expand each section to learn more.

To use the CRM connector or create a Partner Central API integration, you must have the following prerequisites.

- **An AWS account**. To use the Partner Central API, you must
  have an AWS account or an AWS Marketplace seller account for account linking. To
  integrate the CRM connector with AWS Marketplace, you must have a seller
  account.

To create an AWS account, navigate to [Sign up
for AWS](https://signin.aws.amazon.com/signup?request_type=register "https://signin.aws.amazon.com/signup?request_type=register"). For information about creating a seller account,
refer to [Registering as an AWS Marketplace seller](../../../marketplace/latest/userguide/seller-registration-process.md "../../../marketplace/latest/userguide/seller-registration-process.md") in the _AWS Marketplace Seller
Guide_.

- **An AWS Partner Central account**. For information about
  creating the account, refer to [Registering in AWS Partner Central](../getting-started/registering.md "../getting-started/registering.md") in the
  _AWS Partner Central Getting Started Guide_.
- **Linked Partner Central and AWS Marketplace seller accounts**.
  For information about linking the accounts, refer to [Linking your AWS Partner Central and AWS Marketplace accounts](link-pc-mkt-accounts.md "link-pc-mkt-accounts.md") later in this guide.
- **An IAM user in your AWS Marketplace seller account**. The user enables the connector to authenticate Salesforce on AWS. For more information, refer to
  [Creating the IAM user in your AWS Marketplace seller account](create-iam-user-seller-account.md "create-iam-user-seller-account.md") later in this guide.
- **[Amazon S3 permissions for the AWS Marketplace IAM user](s3-iam-perms.md "s3-iam-perms.md").**
  Setting up an integration requires people with the following roles:

- **Salesforce administrator**.
- **Partner alliance lead** – Has permission
  to initiate a new Integration request through Partner Central. The partner
  alliance lead oversees the progress of the Integration and monitors the status
  from the CRM Integration page in Partner Central.
- **Program manager** – Entrusted with
  driving the Integration process from the partner’s side. This person is able to
  define essential processes and necessary enablement post-integration.
- **Partner CRM administrator** – Helps map
  fields between AWS and the partner’s CRM. If partners choose an Integration
  through the AWS Partner CRM connector, the administrator is critical to its
  setup.
- **Developers** – For partners who choose
  the custom option, developers build and implement the custom Integration.
- **Partner cloud operations and IT team** –
  Configures authentication credentials, such as the IAM user or role. This
  involves creating an AWS account and an AWS user for secure access.
- **AWS Partner development manager (PDM)** – The
  partner’s AWS contact. You route all communication with the AWS team through
  the PDM. For more information, refer to [Integration FAQ](crm-integration-faq.md "crm-integration-faq.md")
  later in this guide.
- **AWS Partner solutions architect (PSA)** –
  Works closely with the PDM to assist with any technical questions from the
  partner.
- **AWS CRM Integration support** –
  Addresses technical support issues that partners raise through the Support
  Center in Partner Central.
  After you install the connector, you configure it to work with the following types of CRM integrations and services:

- An AWS Partner Central API integration.
- An earlier CRM with Amazon S3 integration, but only if you created the integration before 2024.
- AWS Marketplace.
  You must configure the connector for each type of integration. In turn, the
  configurations enable Salesforce to exchange data with the corresponding integration.

The following topics list and describe the prerequisites for each type of
configuration. Expand each section to learn more.

Complete the general prerequisites listed in [Integration prerequisites](crm-integration-setting-up.md "crm-integration-setting-up.md") earlier in this guide.

To use the CRM connector with AWS Marketplace, you must have must have the following
prerequisites:

- The [general prerequisites](crm-integration-setting-up.md#stage-1-prerequisites "crm-integration-setting-up.md#stage-1-prerequisites") listed earlier in this section.
- At least one product listed on AWS Marketplace. For information about listing products, refer to [Preparing your product for AWS Marketplace](../../../marketplace/latest/userguide/product-preparation.md "../../../marketplace/latest/userguide/product-preparation.md") in the _AWS Marketplace Seller Guide_.
- An Amazon S3 bucket for storing your custom end user license agreements. For
  more information about creating a bucket, refer to [Creating a
  bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon S3 User Guide_.
- A service-linked role for Resale Authorization. Independent software
  vendors and AWS Marketplace Channel Partners must create a service-linked role that
  provides resource-sharing permissions to AWS. Refer to [CPPO Prerequisites](../../../marketplace/latest/APIReference/work-with-cppos.md#cppo-prerequisites "../../../marketplace/latest/APIReference/work-with-cppos.md#cppo-prerequisites") in the _AWS Marketplace API
  Reference_, and [Using service-linked roles for Resale Authorization with AWS Marketplace](../../../marketplace/latest/userguide/using-roles-for-resale-authorization.md "../../../marketplace/latest/userguide/using-roles-for-resale-authorization.md")
  in the _AWS Marketplace Seller Guide_.
- Amazon EventBridge for real-time notifications. For information about setting up
  notifications, refer to [Setting up real-time notifications for AWS Partner Central and
  AWS Marketplace events](set-up-real-time-notifications.md "set-up-real-time-notifications.md") later in this
  section.
