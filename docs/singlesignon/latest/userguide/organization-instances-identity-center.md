# Organization instances of IAM Identity Center

When you enable IAM Identity Center in conjunction with AWS Organizations, you are creating an organization
instance of IAM Identity Center. Your organization instance must be enabled in your management account and
you can centrally manage the access of users and groups with a single organization instance.
You can have only one organization instance for each management account in AWS Organizations.

If you enabled IAM Identity Center before November 15, 2023, you have an organization instance of IAM Identity Center.

To enable an organization instance of IAM Identity Center, see [To enable an instance of IAM Identity Center](enable-identity-center.md#to-enable-identity-center-instance "enable-identity-center.md#to-enable-identity-center-instance").

## When to use an organization instance

An organization instance is the primary method of enabling IAM Identity Center and usually, an
organization instance is recommended. Organization instances offer the following
benefits:

- Support for all features of IAM Identity Center – Including
  managing permissions for multiple AWS accounts in your organization, assigning
  access to customer managed applications, and multi-Region replication.
- Reduction of the number of management points –
  An organization instance has a single management point, the management account. We
  recommend that you enable an organization instance, rather than an account instance, to
  reduce the number of management points.
- Central control of the creation of account instances
  – You can control whether account instances can be created by member accounts in
  your organization as long as you haven't deployed an instance of IAM Identity Center to your
  organization in an opt-in Region (AWS Region that is disabled by default).

For instructions on enabling an organization instance of IAM Identity Center, see [To enable an instance of IAM Identity Center](enable-identity-center.md#to-enable-identity-center-instance "enable-identity-center.md#to-enable-identity-center-instance").

## Instance configuration options

When you enable an organization instance in an [AWS Region that is enabled by default](../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-considerations "../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-considerations"),
you choose an instance configuration. In other Regions, your instance is created with
default settings.

###### Note

The **Multi-Region instance** and **Custom instance** (create new key) options create a customer managed KMS key
tagged with `CreatedBy: IAM Identity Center` and replicate it to the additional
Region on your behalf. Verify that your IAM principal has `kms:CreateKey`,
`kms:TagResource`, and `kms:ReplicateKey` permissions in addition
to the [permissions needed to enable
IAM Identity Center](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

### Single-Region instance

Your instance is created in the current Region.

- **Encryption at rest** – Your data is
  encrypted with an AWS owned key. You can switch to a customer managed key later
  from the Settings page.
- **Permission sets** – Enabled by default,
  allowing you to manage AWS account access for users and groups. This cannot be
  disabled once enabled.
- **Primary Region** – Your instance is
  created in the current Region. This cannot be changed after creation.
- **Additional Regions** – No additional
  Regions are configured. You can add Regions later from the Settings page.

### Multi-Region instance

Your instance is created in the current Region and replicated to an additional Region
for resilient AWS account and application access.

- **Encryption at rest** – Your data is
  encrypted with a customer managed multi-Region key that is created in your account
  with a key policy that supports replication. The key is tagged with
  `CreatedBy: IAM Identity Center` so you can easily identify it in your
  account. The key can be changed later. AWS KMS charges apply.
- **Permission sets** – Enabled by default,
  allowing you to manage AWS account access for users and groups. This cannot be
  disabled once enabled.
- **Primary Region** – Your instance is
  created in the current Region. This cannot be changed after creation.
- **Additional Regions** – Your instance is
  replicated to an additional Region for resilient AWS account and application
  access. You can change the Region or add more Regions later.

### Custom instance

Configure your instance settings individually.

Encryption at rest

Choose one of the following. A customer managed key is required to add
additional Regions.

- **Use AWS owned key** – Your data
  is encrypted with a key that AWS owns and manages. No additional charges
  apply.
- **Create a new customer managed key**
  – A multi-Region key is created in your account with a baseline key
  policy that supports replication. AWS KMS charges apply.
- **Choose an existing customer managed key**
  – Use a key already in your account. Ensure the key policy meets the
  requirements for your instance. AWS KMS charges apply.

Permission sets

You can choose to enable permission sets, allowing you to manage
AWS account access for users and groups. This cannot be disabled once
enabled.

Additional Regions

Add Regions for resilient AWS account and application access. The customer
managed AWS KMS key must also be available in the selected Region.

For instructions on enabling an organization instance, see [Enable IAM Identity Center](enable-identity-center.md "enable-identity-center.md"). For more
information about multi-Region support, see [Using IAM Identity Center across multiple AWS Regions](multi-region-iam-identity-center.md "multi-region-iam-identity-center.md").
