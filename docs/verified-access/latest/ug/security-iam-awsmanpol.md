# AWS managed policies for Verified Access

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

## AWS managed policy:

AWSVPCVerifiedAccessServiceRolePolicy

This policy is attached to a service-linked role that allows Verified Access to perform actions on
your behalf. For more information, see [Use service-linked roles](using-service-linked-roles.md "using-service-linked-roles.md"). To view the permissions for this
policy, you can see [AWSVPCVerifiedAccessServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSVPCVerifiedAccessServiceRolePolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSVPCVerifiedAccessServiceRolePolicy") in the AWS Management Console, or you can view the
[AWSVPCVerifiedAccessServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSVPCVerifiedAccessServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSVPCVerifiedAccessServiceRolePolicy.md") policy in the _AWS Managed
Policy Reference Guide_.

## Verified Access updates to AWS managed policies

View details about updates to AWS managed policies for Verified Access since this service began
tracking these changes. For automatic alerts about changes to this page, subscribe to the
RSS feed on the Verified Access Document history page.

| Change                                                                                                                                    | Description                                                                                                                 | Date              |
| ----------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AWSVPCVerifiedAccessServiceRolePolicy](#AWSVPCVerifiedAccessServiceRolePolicy "#AWSVPCVerifiedAccessServiceRolePolicy") - Policy updated | Verified Access updated its managed policy to include descriptions of all actions under the "sid" field.                    | November 17, 2023 |
| [AWSVPCVerifiedAccessServiceRolePolicy](#AWSVPCVerifiedAccessServiceRolePolicy "#AWSVPCVerifiedAccessServiceRolePolicy") - Policy updated | Verified Access updated its managed policy to add security group resource to `ec2:CreateNetworkInterface` permission.       | May 31, 2023      |
| [AWSVPCVerifiedAccessServiceRolePolicy](#AWSVPCVerifiedAccessServiceRolePolicy "#AWSVPCVerifiedAccessServiceRolePolicy") - New policy     | Verified Access added a new policy to allow it to provision resources in your account that are required to use the service. | November 29, 2022 |
| Verified Access started tracking changes                                                                                                  | Verified Access started tracking changes for its AWS managed policies.                                                      | November 29, 2022 |
