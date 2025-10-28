# AWS managed policies for AWS Certificate Manager

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWSCertificateManagerReadOnly

This policy provides read–only access to ACM certificates; it allows users to
describe, list, and retrieve ACM certificates.

To view this AWS managed policy in the console, go to [https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSCertificateManagerReadOnly](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSCertificateManagerReadOnly "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSCertificateManagerReadOnly").

For a JSON listing of the policy details, see [AWSCertificateManagerReadOnly](../../../aws-managed-policy/latest/reference/AWSCertificateManagerReadOnly.md "../../../aws-managed-policy/latest/reference/AWSCertificateManagerReadOnly.md").

## AWSCertificateManagerFullAccess

This policy provides full access to all ACM actions and resources.

To view this AWS managed policy in the console, go to [https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSCertificateManagerFullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSCertificateManagerFullAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSCertificateManagerFullAccess").

For a JSON listing of the policy details, see [AWSCertificateManagerFullAccess](../../../aws-managed-policy/latest/reference/AWSCertificateManagerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSCertificateManagerFullAccess.md").

## ACM updates to AWS managed

policies

View details about updates to AWS managed policies for ACM since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the ACM [Document history](dochistory.md "dochistory.md")
page.

| Change                                                                                                                                                | Description                                                                                                          | Date          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------- |
| Added `GetAccountConfiguration` support to the [AWSCertificateManagerReadOnly](#acm-read-only-managed-policy "#acm-read-only-managed-policy") policy. | The `AWSCertificateManagerReadOnly` policy now includes permission to call the `GetAccountConfiguration` API action. | March 3, 2021 |
| ACM starts tracking changes                                                                                                                           | ACM starts tracking changes for AWS managed policies.                                                                | March 3, 2021 |
