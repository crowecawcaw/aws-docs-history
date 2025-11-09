Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Data protection in Amazon CodeCatalyst

Security and Compliance is a shared responsibility between Amazon CodeCatalyst and the customer, just
as the AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to your use of AWS resources used in a workflow. As described in this model, CodeCatalyst is
responsible for protecting the global infrastructure for the service. You are responsible for
maintaining control over your content that is hosted on this infrastructure. This shared
responsibility model applies to data protection in CodeCatalyst.

For data protection purposes, we recommend that you protect your account credentials, and
that you set up multi-factor authentication when signing in. For more information, see [Configure your AWS Builder ID to sign in with multi-factor authentication (MFA)](mfa.md "mfa.md").

Do not
enter
conﬁdential or sensitive information, such as your customers' email addresses,
in tags or free-form
ﬁelds such as a **Name** ﬁeld. This includes
resource
names and any other identifiers you enter in CodeCatalyst
in
addition to any connected AWS accounts.
For example, do not enter
confidential or sensistive information as part of space, project, or deployment fleet
names. Any data that you enter in tags, names, or free-form fields used for names might be used
for billing or diagnostic logs or could be included in URL paths. This applies
to using the console, API, AWS CLI,
the CodeCatalyst Action
Development Kit, or any AWS SDKs.

If you provide a URL to an external server, we strongly recommend that you
do not include any security
credentials information in the URL to validate your request to that
server.

CodeCatalyst source repositories are automatically encrypted at rest. No customer action is
required. CodeCatalyst also encrypts repository data in transit using the HTTPS protocol.

CodeCatalyst does not support encryption at rest using customer managed KMS keys for the identity
attributes retrieved from IAM Identity Center.

CodeCatalyst supports MFA. For more information, see [Configure your AWS Builder ID to sign in with multi-factor authentication (MFA)](mfa.md "mfa.md").

## Data encryption

CodeCatalyst securely stores and transfers data within the service. All data is encrypted in
transit and at rest. Any data created or stored by the service, including any metadata for the
service, is stored natively in the service and encrypted.

###### Note

While information about issues is stored securely within the service, information about
open issues is also stored in the local cache of the browser where you viewed issue boards,
backlogs, and individual issues. For optimal security, be sure to clear your browser cache
to remove this information.

If you use resources linked to CodeCatalyst, such as an account connection to an AWS account
or a linked repository in GitHub, data in transit from CodeCatalyst to that linked resource is
encrypted, but the data handling in that linked resource is managed by that linked service.
For more information, see the documentation for the linked service and [Best practices for workflow actions in Amazon CodeCatalyst](security-best-practices-for-actions.md "security-best-practices-for-actions.md").

### Key management

CodeCatalyst
uses
AWS-owned KMS keys. This means that the keys are managed by AWS and the customer doesn't
need to create or manage them directly. This simplifies key management for common encryption
scenarios within AWS.

## Inter-network traffic privacy

When you create a space in CodeCatalyst, you choose the AWS Region where the data and
resources will be stored for that space. Project data and metadata never leaves that
AWS Region. However, to support navigation within CodeCatalyst, a limited set of space,
project, and user metadata is replicated across all AWS Regions in the [partition](../../../whitepapers/latest/aws-fault-isolation-boundaries/partitions.md "../../../whitepapers/latest/aws-fault-isolation-boundaries/partitions.md"). It will not be replicated to AWS Regions outside of that partition.
For example, if you choose **US West (Oregon)** as the
AWS Region when you create your space, your data will not be replicated to Regions in
China Regions or AWS GovCloud (US). For more information, see [Managing AWS Regions](../../../general/latest/gr/rande-manage.md "../../../general/latest/gr/rande-manage.md"), [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure "https://aws.amazon.com/about-aws/global-infrastructure"),
and [AWS
service endpoints](../../../general/latest/gr/rande.md#region-names-codes "../../../general/latest/gr/rande.md#region-names-codes").

Data replicated across AWS Regions inside a partition includes:

- An encrypted hash value that represents the name of the space in order to ensure
  the uniqueness of space names. This value is not human-readable and does not expose
  the actual names of spaces
- The unique ID of the space
- Metadata for the space that assists in the navigation across spaces
- The AWS Region where the space is located
- The unique IDs of all projects in the space
- The role ID that indicates a user's role in a space or project
- When signing up for CodeCatalyst, data and metadata about the signup process,
  including:
  - The unique ID of the AWS Builder ID
  - The display name for the user in their AWS Builder ID
  - The alias of the user in their AWS Builder ID
  - The email address used when the user signed up for their AWS Builder ID
  - The progress of the sign up process
  - If creating a space as part of the sign up process, the AWS account ID that
    is used as the billing account for the space

Space names are unique across CodeCatalyst. Be sure not to include sensitive data in
the name of the space.

When working with linked resources and connected accounts such as a connection to an
AWS account or a GitHub repository, we recommend configuring your source and destination
locations with the highest level of security that each one supports. CodeCatalyst secures the
connection between AWS accounts, AWS Regions, and Availability Zones by using Transport
Layer Security (TLS) 1.2.
