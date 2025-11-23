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

| Change                                                                                                                                                                                                 | Description                                                                                                                                                                                             | Date               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AWSTransformApplicationECSDeploymentPolicy](#security-iam-awsmanpol-AWSTransformApplicationECSDeploymentPolicy "#security-iam-awsmanpol-AWSTransformApplicationECSDeploymentPolicy") – Updated policy | Added IAM role inspection permissions, ECS service-linked role creation, and KMS permissions for ECR encryption support.                                                                                | November 22, 2025  |
| [AWSTransformApplicationDeploymentPolicy](#security-iam-awsmanpol-AWSTransformApplicationDeploymentPolicy "#security-iam-awsmanpol-AWSTransformApplicationDeploymentPolicy") – Updated<br>policy       | Added EC2 networking permissions, IAM role inspection permissions, S3 bucket listing permissions, and KMS encryption support for enhanced deployment capabilities.                                      | November 22, 2025  |
| [AWSServiceRoleForAWSTransform](#security-iam-awsmanpol-AWSServiceRoleForAWSTransform "#security-iam-awsmanpol-AWSServiceRoleForAWSTransform") – Updated policy                                        | Added support for customer managed keys in IAM Identity Center.                                                                                                                                         | September 17, 2025 |
| [AWSTransformApplicationDeploymentPolicy](#security-iam-awsmanpol-AWSTransformApplicationDeploymentPolicy "#security-iam-awsmanpol-AWSTransformApplicationDeploymentPolicy") – New<br>policy           | Added a new AWS managed policy that enables AWS Transform to deploy transformed<br>.NET applications by creating and managing Amazon EC2 instances, CloudFormation stacks,<br>and associated resources. | August 28, 2025    |
| [AWSServiceRoleForAWSTransform](#security-iam-awsmanpol-AWSServiceRoleForAWSTransform "#security-iam-awsmanpol-AWSServiceRoleForAWSTransform") – Updated policy                                        | Added a new policy.                                                                                                                                                                                     | May 15, 2025       |

## AWS managed

policy: AWSServiceRoleForAWSTransform

This policy is attached to the [AWSServiceRoleForAWSTransform](using-service-linked-roles.md "using-service-linked-roles.md") service-linked role (SLR).

**Permissions details**

To view the policy permission details see [AWSServiceRoleForAWSTransform](../../../aws-managed-policy/latest/reference/AWSServiceRoleForAWSTransform.md "../../../aws-managed-policy/latest/reference/AWSServiceRoleForAWSTransform.md") in the AWS Managed Policy Reference
Guide.

## AWS

managed policy: AWSTransformApplicationDeploymentPolicy

This policy enables AWS Transform to deploy transformed .NET applications by creating and
managing Amazon EC2 instances, CloudFormation stacks, and associated resources.

**Description**

This policy includes the following permissions:

- **CloudFormation** – Allows creating, updating,
  deleting, and describing CloudFormation stacks with names that start with
  AWSTransform. Stack operations are restricted to resources tagged
  with CreatedBy: AWSTransform and limited to the same AWS account.
- **Amazon EC2** – Allows describing VPCs, subnets,
  security groups, images, instances, route tables, and internet gateways. Permits running, starting, stopping,
  terminating, and modifying EC2 instances, but only when called through
  CloudFormation. Tag creation is restricted to specific allowed tag keys and only during CloudFormation operations.
- **AWS Identity and Access Management (IAM)** – Allows getting and passing
  specific IAM roles for AWSTransform deployment instances. Includes permissions to inspect role policies and attachments. Access is restricted to the same AWS account.
- **Amazon EC2 Systems Manager (SSM)** – Allows retrieving Amazon Linux
  AMI parameters from the AWS-managed parameter store and sending commands to AWSTransform-tagged instances.
- **Amazon S3** – Allows managing objects in AWSTransform deployment buckets, including listing buckets and getting bucket locations within the same AWS account.
- **AWS Key Management Service (KMS)** – Allows encryption and decryption operations using KMS keys tagged for AWSTransform, with restrictions to S3 and EC2 service usage.

The policy implements least-privilege access through resource-level permissions,
tag-based conditions, service control restrictions using `aws:CalledVia`,
account-level restrictions, and explicit deny statements to prevent unauthorized tag
modifications outside of CloudFormation operations.

**Permissions details**

To view the policy permission details see [AWSTransformApplicationDeploymentPolicy](../../../aws-managed-policy/latest/reference/AWSTransformApplicationDeploymentPolicy.md "../../../aws-managed-policy/latest/reference/AWSTransformApplicationDeploymentPolicy.md") in the AWS Managed Policy Reference
Guide.

## AWS

managed policy: AWSTransformApplicationECSDeploymentPolicy

This policy enables AWS Transform to deploy transformed applications to Amazon ECS by creating and
managing ECS clusters, services, tasks, and associated resources.

**Description**

This policy includes the following permissions:

- **CloudFormation** – Allows creating, updating,
  deleting, and describing CloudFormation stacks with names that start with
  AWSTransform. Stack operations are restricted to resources tagged with CreatedBy:
  AWSTransform and limited to the same AWS account.
- **Amazon ECS** – Allows creating, updating, and deleting
  ECS clusters, services, and task definitions. Permits running tasks, listing tasks,
  and describing task status. All operations are restricted to resources with names
  starting with AWSTransform and tagged with CreatedBy: AWSTransform.
- **AWS Identity and Access Management (IAM)** – Allows getting and passing
  specific IAM roles for ECS tasks (AWSTransform-Deploy-ECS-Task-Role and
  AWSTransform-Deploy-ECS-Execution-Role). Includes permissions to inspect role
  policies and create the ECS service-linked role when needed.
- **Amazon CloudWatch Logs** – Allows creating, deleting, and
  managing log groups with names starting with /aws/ecs/AWSTransform. Permits
  retrieving log events for troubleshooting deployed applications.
- **Amazon ECR** – Allows creating container repositories
  with names starting with awstransform for storing application container images.
- **AWS Key Management Service (KMS)** – Allows creating grants and
  generating data keys for ECR encryption when using customer-managed KMS keys.

The policy implements least-privilege access through resource-level permissions,
tag-based conditions, and account-level restrictions to ensure operations are limited to
AWSTransform-managed resources within the same AWS account.

**Permissions details**

To view the policy permission details see [AWSTransformApplicationECSDeploymentPolicy](../../../aws-managed-policy/latest/reference/AWSTransformApplicationECSDeploymentPolicy.md "../../../aws-managed-policy/latest/reference/AWSTransformApplicationECSDeploymentPolicy.md") in the AWS Managed Policy Reference
Guide.
