# AWS managed policies for AWS Parallel Computing Service

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

## AWS managed policy: AWSPCSComputeNodePolicy

You can attach AWSPCSComputeNodePolicy to your IAM entities. You can
attach this policy to an AWS PCS compute node IAM role that you specify to allow nodes that
use that role to connect to an AWS PCS cluster.

AWS PCS attaches this policy to a compute node group role when
you use the console to create a compute node group.

**Permissions details**

This policy includes the following permissions.

- `pcs:RegisterComputeNodeGroupInstance` – Allow an AWS PCS compute
  node (EC2 instance) to register with an AWS PCS cluster.

To view the permissions for this policy, see [AWSPCSComputeNodePolicy](../../../aws-managed-policy/latest/reference/AWSPCSComputeNodePolicy.md "../../../aws-managed-policy/latest/reference/AWSPCSComputeNodePolicy.md")
in the _AWS Managed Policy Reference_.

## AWS managed policy: AWSPCSServiceRolePolicy

You can't attach AWSPCSServiceRolePolicy to your IAM entities. This policy is attached to a
service-linked role that allows AWS PCS to perform actions on your behalf. For more
information, see [Service-linked roles for
AWS PCS](service-linked-roles.md "service-linked-roles.md").

**Permissions details**

This policy includes the following permissions.

- `ec2` – Allows AWS PCS to create and manage Amazon EC2 resources.
- `iam` – Allows AWS PCS
  to create a service-linked role for the Amazon EC2 fleet and to pass the role
  to Amazon EC2.
- `cloudwatch` – Allows AWS PCS to publish service metrics to Amazon CloudWatch.
- `secretsmanager` – Allows AWS PCS to manage secrets for AWS PCS cluster resources.

To view the permissions for this policy, see [AWSPCSServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSPCSServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSPCSServiceRolePolicy.md")
in the _AWS Managed Policy Reference_.

## AWS PCS updates to AWS managed

policies

View details about updates to AWS managed policies for AWS PCS since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the AWS PCS Document history page.

| Change                                                                                                                                              | Description                                                                                                                                                                                                                               | Date               |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AWSPCSServiceRolePolicy](#security-iam-awsmanpol-service-role-policy "#security-iam-awsmanpol-service-role-policy") – Update to an existing policy | AWS PCS added new permissions to support Capacity Blocks for predictable compute capacity. Added `ec2:DescribeCapacityReservations` permission to enable AWS PCS to discover and use Capacity Block reservations for compute node groups. | September 11, 2025 |
| [AWSPCSComputeNodePolicy](#security-iam-awsmanpol-AWSPCSComputeNodePolicy "#security-iam-awsmanpol-AWSPCSComputeNodePolicy") – New policy           | AWS PCS added a new policy to grant permission to AWS PCS compute nodes to connect to AWS PCS clusters. AWS PCS attaches this policy to an IAM role when you create a compute node group in the AWS PCS console.                          | June 23, 2025      |
| Updated the JSON in this document                                                                                                                   | Corrected the JSON in this document to include `"arn:aws:ec2:*:*:spot-instances-request/*"`.                                                                                                                                              | September 5, 2024  |
| AWS PCS started tracking changes                                                                                                                    | AWS PCS started tracking changes for its AWS managed policies.                                                                                                                                                                            | August 28, 2024    |
