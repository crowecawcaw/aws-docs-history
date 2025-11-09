# AWS managed policies for AWS Transform

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

## AWS Transform updates for AWS managed policies

View details about updates to AWS managed policies for AWS Transform since March 1, 2021.

| Change                                                                                                                                                                                       | Description                                                                                                                                                                                                 | Date               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AWSServiceRoleForAWSTransform](#security-iam-awsmanpol-AWSServiceRoleForAWSTransform "#security-iam-awsmanpol-AWSServiceRoleForAWSTransform") – Updated policy                              | Added support for customer managed keys in IAM Identity Center.                                                                                                                                             | September 17, 2025 |
| [AWSTransformApplicationDeploymentPolicy](#security-iam-awsmanpol-AWSTransformApplicationDeploymentPolicy "#security-iam-awsmanpol-AWSTransformApplicationDeploymentPolicy") – New<br>policy | Added a new AWS managed policy that enables AWS Transform to deploy transformed<br>.NET applications by creating and managing Amazon EC2 instances, AWS CloudFormation stacks,<br>and associated resources. | August 28, 2025    |
| [AWSServiceRoleForAWSTransform](#security-iam-awsmanpol-AWSServiceRoleForAWSTransform "#security-iam-awsmanpol-AWSServiceRoleForAWSTransform") – Updated policy                              | Added a new policy.                                                                                                                                                                                         | May 15, 2025       |

## AWS managed

policy: AWSServiceRoleForAWSTransform

This policy is attached to the [AWSServiceRoleForAWSTransform](using-service-linked-roles.md "using-service-linked-roles.md") service-linked role (SLR).

**Permissions details**

To view the policy permission details see [AWSServiceRoleForAWSTransform](../../../aws-managed-policy/latest/reference/AWSServiceRoleForAWSTransform.md "../../../aws-managed-policy/latest/reference/AWSServiceRoleForAWSTransform.md") in the AWS Managed Policy Reference
Guide.

## AWS

managed policy: AWSTransformApplicationDeploymentPolicy

This policy enables AWS Transform to deploy transformed .NET applications by creating and
managing Amazon EC2 instances, AWS CloudFormation stacks, and associated resources.

**Description**

This policy includes the following permissions:

- **CloudFormation** – Allows creating, updating,
  deleting, and describing CloudFormation stacks with names that start with
  AWSTransform-Deploy-Infra-stack. Stack operations are restricted to resources tagged
  with CreatedBy: AWSTransform and limited to the same AWS account.
- **Amazon EC2** – Allows describing VPCs, subnets,
  security groups, images, and instances. Permits running, starting, stopping,
  terminating, and modifying EC2 instances, but only when called through
  CloudFormation. Tag creation is restricted to specific allowed tag keys (Name,
  CreatedBy, CreatedFor, Environment) and only during instance launch.
- **AWS Identity and Access Management (IAM)** – Allows getting and passing the
  specific IAM role AWSTransform-Deploy-EC2-Instance-Role and accessing the instance
  profile AWSTransform-Deploy-EC2-Instance-Profile. Access is restricted to resources
  tagged with CreatedFor: AWSTransform.
- **Amazon EC2 Systems Manager (SSM)** – Allows retrieving Amazon Linux
  AMI parameters from the AWS-managed parameter store.

The policy implements least-privilege access through resource-level permissions,
tag-based conditions, service control restrictions using `aws:CalledVia`,
account-level restrictions, and explicit deny statements to prevent unauthorized tag
modifications outside of CloudFormation operations.

**Permissions details**

To view the policy permission details see [AWSTransformApplicationDeploymentPolicy](../../../aws-managed-policy/latest/reference/AWSTransformApplicationDeploymentPolicy.md "../../../aws-managed-policy/latest/reference/AWSTransformApplicationDeploymentPolicy.md") in the AWS Managed Policy Reference
Guide.
