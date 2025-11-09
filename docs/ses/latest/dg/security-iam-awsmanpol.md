# AWS managed policies for Amazon Simple Email Service

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To
get started quickly, you can use our AWS managed policies. These policies cover common use
cases and are available in your AWS account. For more information about AWS managed
policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to
an AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update
an AWS managed policy when a new feature is launched or when new operations become
available. Services do not remove permissions from an AWS managed policy, so policy
updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service
launches a new feature, AWS adds read-only permissions for new operations and resources.
For a list and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed policy:

AmazonSESFullAccess

You can attach the `AmazonSESFullAccess` policy to your IAM identities.
Provides full access to Amazon SES.

To view the permissions for this policy, see [AmazonSESFullAccess](../../../aws-managed-policy/latest/reference/AmazonSESFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSESFullAccess.md") in the _AWS Managed
Policy Reference_.

## AWS managed policy:

AmazonSESReadOnlyAccess

You can attach the `AmazonSESReadOnlyAccess` policy to your IAM
identities. Provides read only access to Amazon SES.

To view the permissions for this policy, see [AmazonSESReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonSESReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonSESReadOnlyAccess.md") in the _AWS Managed
Policy Reference_.

## AWS managed

policy: AmazonSESServiceRolePolicy

You can't attach the `AmazonSESServiceRolePolicy` policy to your IAM
entities. This policy is attached to a service-linked role that allows Amazon SES to perform
actions on your behalf. For more information, see [Service-linked role permissions for
Amazon SES](using-service-linked-roles.md#service-linked-role-permissions "using-service-linked-roles.md#service-linked-role-permissions").

To view the permissions for this policy, see [AmazonSESServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonSESServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonSESServiceRolePolicy.md") in the _AWS
Managed Policy Reference_.

## Amazon Simple Email Service updates to AWS managed

policies

View details and about updates to AWS managed policies for Amazon Simple Email Service since this
service began tracking these changes.

| Change                                                     | Description                                                                                                                                                                                                                                                               | Date          |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| Amazon Simple Email Service added a new managed policy     | Amazon Simple Email Service added `AmazonSESServiceRolePolicy` to the<br>service-linked role `AWSServiceRoleForAmazonSES` that allows<br>SES to perform actions on your behalf                                                                                            | May 13, 2024  |
| Amazon Simple Email Service updated a policy definition    | \*Amazon Simple Email Service clarified the previous entry in this table (row<br>below) to be:<br>• Amazon Simple Email Service added<br>`ses:BatchGetMetricData` to AmazonSESReadOnlyAccess<br>managed policy—this will give access to the SES API<br>BatchGetMetricData | Apr 30, 2024  |
| Amazon Simple Email Service updated a policy definition    | Amazon Simple Email Service added `ses:BatchGet*` to AmazonSESReadOnlyAccess<br>managed policy—this will give access to the SES API<br>BatchGetMetricData                                                                                                                 | Feb 16, 2024  |
| Amazon Simple Email Service changed two policy definitions | Amazon Simple Email Service removed "via the AWS Management Console" from the end of<br>the AmazonSESFullAccess and AmazonSESReadOnlyAccess definitions                                                                                                                   | May 3, 2023   |
| Amazon Simple Email Service started tracking changes       | Amazon Simple Email Service started tracking changes to its AWS managed<br>policies                                                                                                                                                                                       | April 5, 2023 |
