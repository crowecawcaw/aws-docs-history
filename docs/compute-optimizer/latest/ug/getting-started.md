# Getting started with AWS Compute Optimizer

When you access the AWS Compute Optimizer console for the first time, you're asked to opt in using the
account that you’re signed in with. Before you can use the service, you must opt in or out. In
addition, you can also opt in or opt out using the Compute Optimizer API, AWS Command Line Interface (AWS CLI), or SDKs.

By opting in, you're authorizing Compute Optimizer to analyze the specifications and utilization metrics
of your AWS resources. Examples include EC2 instances and EC2 Amazon EC2 Auto Scaling groups.

###### Note

To improve the recommendation quality of Compute Optimizer, Amazon Web Services might use your CloudWatch metrics and
configuration data. This includes up to three months (93 days) of metrics analysis when you
activate the enhanced infrastructure metrics feature. Contact [AWS Support](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support") to request that AWS stop using your
CloudWatch metrics and configuration data to improve the recommendation quality of Compute Optimizer.

## Required permissions

You must have the appropriate permissions to opt in to Compute Optimizer, to view its recommendations,
and to opt out. For more information, see [Identity and Access Management for AWS Compute Optimizer](security-iam.md "security-iam.md").

When you opt in, Compute Optimizer automatically creates a Service-Linked Role in your account to
access its data. For more information, see [Using service-linked roles for AWS Compute Optimizer](using-service-linked-roles.md "using-service-linked-roles.md").

## Accounts supported by Compute Optimizer

The following AWS account types can opt in to Compute Optimizer:

- **Standalone AWS account**

A standalone AWS account that doesn't have AWS Organizations enabled. If you opt in to Compute Optimizer
while signed in to a standalone account, Compute Optimizer analyzes the resources in the account and
generates optimization recommendations for those resources.

- **Member account of an organization**

An AWS account that's a member of an organization. If you opt in to Compute Optimizer while
signed in to a member account of an organization, Compute Optimizer only analyzes the resources in the
member account and generates optimization recommendations for those resources.

- **Management account of an organization**

An AWS account that administers an organization. If you opt in to Compute Optimizer while signed
in to a management account of an organization, Compute Optimizer gives you the option to opt in the
management account only, or the management account and all member accounts of the
organization.

###### Important

To opt in all member accounts for an organization, make sure that the organization
has all features enabled. For more information, see [Enabling All Features in
Your Organization](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md") in the _AWS Organizations User Guide_.

When you opt in using your organization's management account and include all member
accounts within the organization, trusted access for Compute Optimizer is enabled in your
organization account. For more information, see [Trusted access for AWS Organizations](security-iam.md#trusted-service-access "security-iam.md#trusted-service-access").

## Next steps

For instructions on how to opt in your account, or the accounts within your organization,
to AWS Compute Optimizer, see [Opting in to AWS Compute Optimizer](account-opt-in.md "account-opt-in.md").

## Additional resources

- [Identity and Access Management for AWS Compute Optimizer](security-iam.md "security-iam.md")
- [AWS managed policies for AWS Compute Optimizer](managed-policies.md "managed-policies.md")
- [Using service-linked roles for AWS Compute Optimizer](using-service-linked-roles.md "using-service-linked-roles.md")
