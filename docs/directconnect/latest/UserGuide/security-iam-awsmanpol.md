# AWS managed policies for AWS Direct Connect

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

## AWS managed policy: AWSDirectConnectFullAccess

You can attach the `AWSDirectConnectFullAccess` policy to your IAM identities.
This policy grants permissions that allow full access to Direct Connect.

To view the permissions for this policy, see [AWSDirectConnectFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSDirectConnectFullAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSDirectConnectFullAccess") in the AWS Management Console.

## AWS managed policy: AWSDirectConnectReadOnlyAccess

You can attach the `AWSDirectConnectReadOnlyAccess` policy to your IAM identities.
This policy grants permissions that allow read-only access to Direct Connect.

To view the permissions for this policy, see [AWSDirectConnectReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSDirectConnectReadOnlyAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSDirectConnectReadOnlyAccess") in the AWS Management Console.

## AWS managed policy: AWSDirectConnectServiceRolePolicy

This policy is attached to the service-linked role named **AWSServiceRoleForDirectConnect** to allow Direct Connect to retrieve MAC Security
secrets on your behalf. For more information, see [Service-linked roles for Direct Connect](using-service-linked-roles.md "using-service-linked-roles.md").

To view the permissions for this policy, see [AWSDirectConnectServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSDirectConnectServiceRolePolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSDirectConnectServiceRolePolicy") in the AWS Management Console.

## Direct Connect updates to AWS managed policies

View details about updates to AWS managed policies for Direct Connect since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the Direct Connect Document history page.

| Change                                                                                                                                                                     | Description                                                                                       | Date           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------------- |
| [AWSDirectConnectServiceRolePolicy](#security-iam-awsmanpol-AWSDirectConnectServiceRolePolicy "#security-iam-awsmanpol-AWSDirectConnectServiceRolePolicy") -<br>New policy | To support MAC Security, the **AWSServiceRoleForDirectConnect**<br>service-linked role was added. | March 31, 2021 |
| Direct Connect started tracking changes                                                                                                                                    | Direct Connect started tracking changes to its AWS managed policies.                              | March 31, 2021 |
