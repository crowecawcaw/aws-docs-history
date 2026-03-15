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

| Change                                                                                                                                                                                                 | Description                                                                                                                                                                                                                | Date               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [DBModProvisioningAndMigration](#security-iam-awsmanpol-DBModProvisioningAndMigration "#security-iam-awsmanpol-DBModProvisioningAndMigration") – New policy                                            | This policy grants database provisioning and migration capabilities.                                                                                                                                                       | February 26, 2026  |
| [DBModDiscoveryAndAssessment](#security-iam-awsmanpol-DBModDiscoveryAndAssessment "#security-iam-awsmanpol-DBModDiscoveryAndAssessment") – New policy                                                  | Added a new AWS managed policy that provides comprehensive database modernization discovery and assessment capabilities.                                                                                                   | February 26, 2026  |
| [AWSTransformCustomFullAccess](#security-iam-awsmanpol-AWSTransformCustomFullAccess "#security-iam-awsmanpol-AWSTransformCustomFullAccess") – New policy                                               | Added a new AWS managed policy that provides full access to AWS Transform custom.                                                                                                                                          | December 5, 2025   |
| [AWSTransformCustomExecuteTransformations](#security-iam-awsmanpol-AWSTransformCustomExecuteTransformations "#security-iam-awsmanpol-AWSTransformCustomExecuteTransformations") – New policy           | Added a new AWS managed policy that provides access to execute transformations in AWS Transform custom.                                                                                                                    | December 5, 2025   |
| [AWSTransformCustomManageTransformations](#security-iam-awsmanpol-AWSTransformCustomManageTransformations "#security-iam-awsmanpol-AWSTransformCustomManageTransformations") – New policy              | Added a new AWS managed policy that provides access to create, update, read, and delete transformation resources in AWS Transform custom, as well as execute transformations.                                              | December 5, 2025   |
| [AWSServiceRoleForAWSTransform](#security-iam-awsmanpol-AWSServiceRoleForAWSTransform "#security-iam-awsmanpol-AWSServiceRoleForAWSTransform") – Updated policy                                        | Added permissions to access the AWS Transform service-linked secret used to store the client secret for external identity providers.<br>Added permissions to create a premium support case from the AWS Transform web app. | December 1, 2025   |
| [AWSTransformApplicationECSDeploymentPolicy](#security-iam-awsmanpol-AWSTransformApplicationECSDeploymentPolicy "#security-iam-awsmanpol-AWSTransformApplicationECSDeploymentPolicy") – Updated policy | Added IAM role inspection permissions, ECS service-linked role creation, and KMS permissions for ECR encryption support.                                                                                                   | November 22, 2025  |
| [AWSTransformApplicationDeploymentPolicy](#security-iam-awsmanpol-AWSTransformApplicationDeploymentPolicy "#security-iam-awsmanpol-AWSTransformApplicationDeploymentPolicy") – Updated<br>policy       | Added EC2 networking permissions, IAM role inspection permissions, S3 bucket listing permissions, and KMS encryption support for enhanced deployment capabilities.                                                         | November 22, 2025  |
| [AWSServiceRoleForAWSTransform](#security-iam-awsmanpol-AWSServiceRoleForAWSTransform "#security-iam-awsmanpol-AWSServiceRoleForAWSTransform") – Updated policy                                        | Added support for customer managed keys in IAM Identity Center.                                                                                                                                                            | September 17, 2025 |
| [AWSTransformApplicationDeploymentPolicy](#security-iam-awsmanpol-AWSTransformApplicationDeploymentPolicy "#security-iam-awsmanpol-AWSTransformApplicationDeploymentPolicy") – New<br>policy           | Added a new AWS managed policy that enables AWS Transform to deploy transformed<br>.NET applications by creating and managing Amazon EC2 instances, CloudFormation stacks,<br>and associated resources.                    | August 28, 2025    |
| [AWSServiceRoleForAWSTransform](#security-iam-awsmanpol-AWSServiceRoleForAWSTransform "#security-iam-awsmanpol-AWSServiceRoleForAWSTransform") – Updated policy                                        | Added a new policy.                                                                                                                                                                                                        | May 15, 2025       |

## AWS managed policy: AWSServiceRoleForAWSTransform

This policy is attached to the [AWSServiceRoleForAWSTransform](using-service-linked-roles.md "using-service-linked-roles.md") service-linked role (SLR).

**Permissions details**

To view the policy permission details see [AWSServiceRoleForAWSTransform](../../../aws-managed-policy/latest/reference/AWSServiceRoleForAWSTransform.md "../../../aws-managed-policy/latest/reference/AWSServiceRoleForAWSTransform.md") in the AWS Managed Policy Reference
Guide.

## AWS managed policy: AWSTransformApplicationDeploymentPolicy

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

## AWS managed policy: AWSTransformApplicationECSDeploymentPolicy

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

## AWS managed policy: AWSTransformCustomFullAccess

This policy provides full access to AWS Transform custom.

**Description**

This policy includes the following permissions:

- **AWS Transform Custom** – Allows all actions on all AWS Transform custom resources. This provides complete administrative access to the service.

**Permissions details**

To view the policy permission details see [AWSTransformCustomFullAccess](../../../aws-managed-policy/latest/reference/AWSTransformCustomFullAccess.md "../../../aws-managed-policy/latest/reference/AWSTransformCustomFullAccess.md") in the AWS Managed Policy Reference
Guide.

## AWS managed policy: AWSTransformCustomExecuteTransformations

This policy provides access to execute transformations in AWS Transform custom.

**Description**

This policy includes the following permissions:

- **AWS Transform Custom** – Allows streaming conversations, executing transformations, and managing campaigns. Includes permissions to get campaign details, update campaign repository status, and update campaigns.

**Permissions details**

To view the policy permission details see [AWSTransformCustomExecuteTransformations](../../../aws-managed-policy/latest/reference/AWSTransformCustomExecuteTransformations.md "../../../aws-managed-policy/latest/reference/AWSTransformCustomExecuteTransformations.md") in the AWS Managed Policy Reference
Guide.

## AWS managed policy: AWSTransformCustomManageTransformations

This policy provides access to create, update, read, and delete transformation resources in AWS Transform custom, as well as execute transformations.

**Description**

This policy includes the following permissions:

- **AWS Transform Custom** – Allows comprehensive management of transformation resources including streaming conversations, executing transformations, and managing transformation packages. Permits creating, getting, and deleting transformation package URLs and completing package uploads.
- **Knowledge Management** – Allows listing, getting, deleting, and updating knowledge items and their configurations and status.
- **Campaign Management** – Allows getting campaign details, updating campaign repository status, and updating campaigns.
- **Resource Tagging** – Allows listing, adding, and removing tags for AWS Transform custom resources.

**Permissions details**

To view the policy permission details see [AWSTransformCustomManageTransformations](../../../aws-managed-policy/latest/reference/AWSTransformCustomManageTransformations.md "../../../aws-managed-policy/latest/reference/AWSTransformCustomManageTransformations.md") in the AWS Managed Policy Reference
Guide.

## AWS managed policy: DBModDiscoveryAndAssessment

This policy grants you comprehensive database modernization discovery and assessment capabilities to streamline your database migration projects.

**Description**

This policy grants the following permissions:

- **Amazon EC2** – Read-only access to discover infrastructure components including instances, VPCs, subnets, security groups, and connectivity.
- **Amazon RDS** – Access to discover database instances, clusters, and subnet groups, and to modify subnet groups for migration preparation.
- **Amazon RDS Data API** – Access to execute SQL statements for schema analysis and assessment.
- **AWS DMS** – Comprehensive access to manage migration projects, schema conversion, metadata model operations, and replication resources. Write operations are restricted to resources tagged for the database modernization project.
- – Access to discover and retrieve database credentials. Write access is restricted to resources tagged for the database modernization project.
- **AWS Identity and Access Management (IAM)** – Read-only access to verify IAM policies and specific DMS service role configurations.
- **AWS Key Management Service (KMS)** – Access to discover encryption keys and decrypt secrets specifically through integration.

**Permissions details**

To view the policy permission details see [DBModDiscoveryAndAssessment](../../../aws-managed-policy/latest/reference/DBModDiscoveryAndAssessment.md "../../../aws-managed-policy/latest/reference/DBModDiscoveryAndAssessment.md") in the AWS Managed Policy Reference
Guide.

## AWS managed policy: DBModProvisioningAndMigration

This policy grants you database provisioning and migration capabilities for database modernization projects. It provides permissions to create and manage migration infrastructure, provision target databases, and store migration data.

**Description**

This policy grants the following permissions:

- **AWS DMS** – Access to create and manage replication instances, tasks, endpoints, and migration projects. Includes lifecycle operations such as starting, stopping, and assessing replication tasks. All resources must be tagged for the database modernization project.
- **Amazon RDS** – Access to provision database instances, clusters, and subnet groups. Includes HTTP endpoint management for serverless databases. All resources must be tagged for the database modernization project.
- – Access to create and update secrets for database credentials. Restricted to secrets with the database modernization naming prefix and project tags.
- **Amazon S3** – Access to create and manage S3 buckets and objects for migration data storage. Restricted to buckets with the database modernization naming prefix.
- **AWS Identity and Access Management (IAM)** – Access to pass specific DMS service roles and create the Amazon RDS service-linked role required for database operations.

**Permissions details**

To view the policy permission details see [DBModProvisioningAndMigration](../../../aws-managed-policy/latest/reference/DBModProvisioningAndMigration.md "../../../aws-managed-policy/latest/reference/DBModProvisioningAndMigration.md") in the AWS Managed Policy Reference
Guide.
