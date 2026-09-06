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

| Change                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                   | Date               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AWSTransformLandingZoneAgentPolicy](#security-iam-awsmanpol-AWSTransformLandingZoneAgentPolicy "#security-iam-awsmanpol-AWSTransformLandingZoneAgentPolicy") – New policy                                      | Added a new AWS managed policy that grants the permissions needed to set up AWS landing zones, including account provisioning, organizational governance, and AWS Control Tower configuration.                                                                                                                | September 3, 2026  |
| [AWSTransformNetworkMigrationAgentPolicy](#security-iam-awsmanpol-AWSTransformNetworkMigrationAgentPolicy "#security-iam-awsmanpol-AWSTransformNetworkMigrationAgentPolicy") – New policy                       | Added a new AWS managed policy that grants the permissions needed to deploy and configure network infrastructure, including VPCs, transit gateways, and route tables, for network migration.                                                                                                                  | September 3, 2026  |
| [AWSTransformServerMigrationAgentPolicy](#security-iam-awsmanpol-AWSTransformServerMigrationAgentPolicy "#security-iam-awsmanpol-AWSTransformServerMigrationAgentPolicy") – New policy                          | Added a new AWS managed policy that grants the permissions needed to perform server migration operations, including replication, testing, and cutover, using AWS Transform MGN.                                                                                                                               | September 3, 2026  |
| [AWSTransformInfrastructureExecutorAccessBatch](#security-iam-awsmanpol-AWSTransformInfrastructureExecutorAccessBatch "#security-iam-awsmanpol-AWSTransformInfrastructureExecutorAccessBatch") – Updated policy | Added Amazon SQS `SendMessage` permission to submit jobs to the `atx-dispatcher-queue`, and added CloudFormation visibility for the `AtxDispatcherStack`.                                                                                                                                                     | September 2, 2026  |
| [AWSTransformInfrastructureExecutorAccessEC2](#security-iam-awsmanpol-AWSTransformInfrastructureExecutorAccessEC2 "#security-iam-awsmanpol-AWSTransformInfrastructureExecutorAccessEC2") – Updated policy       | Added Amazon SQS `SendMessage` permission to submit jobs to the `atx-dispatcher-queue`, and added CloudFormation visibility for the `AtxDispatcherStack`.                                                                                                                                                     | September 2, 2026  |
| [AWSTransformInfrastructureExecutorAccessBatch](#security-iam-awsmanpol-AWSTransformInfrastructureExecutorAccessBatch "#security-iam-awsmanpol-AWSTransformInfrastructureExecutorAccessBatch") – Updated policy | Narrowed AWS Lambda permissions to an explicit function allowlist, added Amazon S3 write access for batch sidecar output, widened CloudFormation and Amazon EventBridge Scheduler resource scoping for multi-stack deployments, and added support for regional AWS Key Management Service key alias variants. | July 27, 2026      |
| [AWSTransformInfrastructureExecutorAccessEC2](#security-iam-awsmanpol-AWSTransformInfrastructureExecutorAccessEC2 "#security-iam-awsmanpol-AWSTransformInfrastructureExecutorAccessEC2") – Updated policy       | Widened CloudFormation, Amazon EventBridge Scheduler, and AWS Identity and Access Management PassRole resource scoping for multi-stack deployments, added Security Agent infrastructure visibility, and added support for regional AWS Key Management Service key alias variants.                             | July 27, 2026      |
| [AWSTransformSecurityAgentExecutorAccess](#security-iam-awsmanpol-AWSTransformSecurityAgentExecutorAccess "#security-iam-awsmanpol-AWSTransformSecurityAgentExecutorAccess") – Updated policy                   | Added CloudFormation permissions to discover and describe the Security Agent infrastructure stack, and migrated the Amazon S3 bucket prefix from `kct-security-agent-*` to `atx-security-agent-*`.                                                                                                            | July 27, 2026      |
| [AWSTransformInfrastructureExecutorAccessBatch](#security-iam-awsmanpol-AWSTransformInfrastructureExecutorAccessBatch "#security-iam-awsmanpol-AWSTransformInfrastructureExecutorAccessBatch") – New policy     | Added a new AWS managed policy that grants the permissions needed to execute AWS Transform Continuous Modernization assessments and transformations using AWS Batch, including uploading source code, retrieving results, monitoring Batch job status, reading logs, and managing transformation schedules.   | July 20, 2026      |
| [AWSTransformInfrastructureExecutorAccessEC2](#security-iam-awsmanpol-AWSTransformInfrastructureExecutorAccessEC2 "#security-iam-awsmanpol-AWSTransformInfrastructureExecutorAccessEC2") – New policy           | Added a new AWS managed policy that grants the permissions needed to execute AWS Transform Continuous Modernization assessments and transformations using Amazon EC2, including uploading source code, retrieving results, monitoring job status, and managing transformation schedules.                      | July 20, 2026      |
| [AWSTransformSecurityAgentExecutorAccess](#security-iam-awsmanpol-AWSTransformSecurityAgentExecutorAccess "#security-iam-awsmanpol-AWSTransformSecurityAgentExecutorAccess") – New policy                       | Added a new AWS managed policy that grants AWS Transform Continuous Modernization the permissions needed to invoke the AWS Security Agent service for automated code security reviews and remediation, including uploading scan artifacts and retrieving findings.                                            | June 30, 2026      |
| [AWSServiceRoleForAWSTransformCustom](#security-iam-awsmanpol-AWSServiceRoleForAWSTransformCustom "#security-iam-awsmanpol-AWSServiceRoleForAWSTransformCustom") – Updated policy                               | Added CloudWatch Logs permissions to allow AWS Transform custom to publish logs to the `/aws/TransformCustom` log group in your account.                                                                                                                                                                      | May 5, 2026        |
| [AWSTransformCustomExecuteTransformations](#security-iam-awsmanpol-AWSTransformCustomExecuteTransformations "#security-iam-awsmanpol-AWSTransformCustomExecuteTransformations") – Updated policy                | Added permission to create the AWS Transform custom service-linked role (`AWSServiceRoleForAWSTransformCustom`) to enable CloudWatch metrics emission to customer accounts.                                                                                                                                   | April 27, 2026     |
| [AWSTransformCustomManageTransformations](#security-iam-awsmanpol-AWSTransformCustomManageTransformations "#security-iam-awsmanpol-AWSTransformCustomManageTransformations") – Updated policy                   | Added permission to create the AWS Transform custom service-linked role (`AWSServiceRoleForAWSTransformCustom`) to enable CloudWatch metrics emission to customer accounts.                                                                                                                                   | April 27, 2026     |
| [AWSTransformCustomFullAccess](#security-iam-awsmanpol-AWSTransformCustomFullAccess "#security-iam-awsmanpol-AWSTransformCustomFullAccess") – Updated policy                                                    | Added permission to create the AWS Transform custom service-linked role (`AWSServiceRoleForAWSTransformCustom`) to enable CloudWatch metrics emission to customer accounts.                                                                                                                                   | April 7, 2026      |
| [AWSServiceRoleForAWSTransformCustom](#security-iam-awsmanpol-AWSServiceRoleForAWSTransformCustom "#security-iam-awsmanpol-AWSServiceRoleForAWSTransformCustom") – New policy                                   | Added a new AWS managed policy for the AWS Transform custom service-linked role. This policy allows AWS Transform custom to publish CloudWatch metrics to your account.                                                                                                                                       | March 23, 2026     |
| [DBModProvisioningAndMigration](#security-iam-awsmanpol-DBModProvisioningAndMigration "#security-iam-awsmanpol-DBModProvisioningAndMigration") – New policy                                                     | This policy grants database provisioning and migration capabilities.                                                                                                                                                                                                                                          | March 24, 2026     |
| [DBModDiscoveryAndAssessment](#security-iam-awsmanpol-DBModDiscoveryAndAssessment "#security-iam-awsmanpol-DBModDiscoveryAndAssessment") – New policy                                                           | Added a new AWS managed policy that provides comprehensive database modernization discovery and assessment capabilities.                                                                                                                                                                                      | March 24, 2026     |
| [AWSTransformCustomFullAccess](#security-iam-awsmanpol-AWSTransformCustomFullAccess "#security-iam-awsmanpol-AWSTransformCustomFullAccess") – New policy                                                        | Added a new AWS managed policy that provides full access to AWS Transform custom.                                                                                                                                                                                                                             | December 5, 2025   |
| [AWSTransformCustomExecuteTransformations](#security-iam-awsmanpol-AWSTransformCustomExecuteTransformations "#security-iam-awsmanpol-AWSTransformCustomExecuteTransformations") – New policy                    | Added a new AWS managed policy that provides access to execute transformations in AWS Transform custom.                                                                                                                                                                                                       | December 5, 2025   |
| [AWSTransformCustomManageTransformations](#security-iam-awsmanpol-AWSTransformCustomManageTransformations "#security-iam-awsmanpol-AWSTransformCustomManageTransformations") – New policy                       | Added a new AWS managed policy that provides access to create, update, read, and delete transformation resources in AWS Transform custom, as well as execute transformations.                                                                                                                                 | December 5, 2025   |
| [AWSServiceRoleForAWSTransform](#security-iam-awsmanpol-AWSServiceRoleForAWSTransform "#security-iam-awsmanpol-AWSServiceRoleForAWSTransform") – Updated policy                                                 | Added permissions to access the AWS Transform service-linked secret used to store the client secret for external identity providers.<br>Added permissions to create a premium support case from the AWS Transform web app.                                                                                    | December 1, 2025   |
| [AWSTransformApplicationECSDeploymentPolicy](#security-iam-awsmanpol-AWSTransformApplicationECSDeploymentPolicy "#security-iam-awsmanpol-AWSTransformApplicationECSDeploymentPolicy") – Updated policy          | Added IAM role inspection permissions, ECS service-linked role creation, and KMS permissions for ECR encryption support.                                                                                                                                                                                      | November 22, 2025  |
| [AWSTransformApplicationDeploymentPolicy](#security-iam-awsmanpol-AWSTransformApplicationDeploymentPolicy "#security-iam-awsmanpol-AWSTransformApplicationDeploymentPolicy") – Updated<br>policy                | Added EC2 networking permissions, IAM role inspection permissions, S3 bucket listing permissions, and KMS encryption support for enhanced deployment capabilities.                                                                                                                                            | November 22, 2025  |
| [AWSServiceRoleForAWSTransform](#security-iam-awsmanpol-AWSServiceRoleForAWSTransform "#security-iam-awsmanpol-AWSServiceRoleForAWSTransform") – Updated policy                                                 | Added support for customer managed keys in IAM Identity Center.                                                                                                                                                                                                                                               | September 17, 2025 |
| [AWSTransformApplicationDeploymentPolicy](#security-iam-awsmanpol-AWSTransformApplicationDeploymentPolicy "#security-iam-awsmanpol-AWSTransformApplicationDeploymentPolicy") – New<br>policy                    | Added a new AWS managed policy that enables AWS Transform to deploy transformed<br>.NET applications by creating and managing Amazon EC2 instances, CloudFormation stacks,<br>and associated resources.                                                                                                       | August 28, 2025    |
| [AWSServiceRoleForAWSTransform](#security-iam-awsmanpol-AWSServiceRoleForAWSTransform "#security-iam-awsmanpol-AWSServiceRoleForAWSTransform") – Updated policy                                                 | Added a new policy.                                                                                                                                                                                                                                                                                           | May 15, 2025       |

## AWS managed policy: AWSServiceRoleForAWSTransform

This policy is attached to the [AWSServiceRoleForAWSTransform](using-service-linked-roles.md "using-service-linked-roles.md") service-linked role (SLR).

**Permissions details**

To view the policy permission details see [AWSServiceRoleForAWSTransform](../../../aws-managed-policy/latest/reference/AWSServiceRoleForAWSTransform.md "../../../aws-managed-policy/latest/reference/AWSServiceRoleForAWSTransform.md") in the AWS Managed Policy Reference
Guide.

## AWS managed policy: AWSServiceRoleForAWSTransformCustom

This policy is attached to the [AWSServiceRoleForAWSTransformCustom](using-service-linked-roles.md#using-service-linked-roles-custom "using-service-linked-roles.md#using-service-linked-roles-custom") service-linked role (SLR). This role allows
AWS Transform custom to publish CloudWatch metrics and logs to your account on your behalf.

**Description**

This policy includes the following permissions:

- **Amazon CloudWatch** – Allows publishing metrics to CloudWatch under
  the `AWS/TransformCustom` namespace. This enables monitoring of transformation
  counts, latencies, and status codes in your CloudWatch dashboards.
- **Amazon CloudWatch Logs** – Allows creating log groups, log
  streams, setting retention policies, and publishing log events to the
  `/aws/TransformCustom` log group. This provides visibility into issues
  encountered during transformations.

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
- **AWS Identity and Access Management (IAM)** – Allows creating the AWS Transform custom
  [service-linked role](using-service-linked-roles.md#using-service-linked-roles-custom "using-service-linked-roles.md#using-service-linked-roles-custom")
  (`AWSServiceRoleForAWSTransformCustom`). This role is required for AWS Transform
  custom to emit CloudWatch metrics and logs to your account. The permission is scoped to only allow
  creating this specific service-linked role.

**Permissions details**

To view the policy permission details see [AWSTransformCustomFullAccess](../../../aws-managed-policy/latest/reference/AWSTransformCustomFullAccess.md "../../../aws-managed-policy/latest/reference/AWSTransformCustomFullAccess.md") in the AWS Managed Policy Reference
Guide.

## AWS managed policy: AWSTransformCustomExecuteTransformations

This policy provides access to execute transformations in AWS Transform custom.

**Description**

This policy includes the following permissions:

- **AWS Transform Custom** – Allows streaming conversations, executing transformations, and managing campaigns. Includes permissions to get campaign details, update campaign repository status, and update campaigns.
- **AWS Identity and Access Management (IAM)** – Allows creating the AWS Transform custom
  [service-linked role](using-service-linked-roles.md#using-service-linked-roles-custom "using-service-linked-roles.md#using-service-linked-roles-custom")
  (`AWSServiceRoleForAWSTransformCustom`). This role is required for AWS Transform
  custom to emit CloudWatch metrics and logs to your account. The permission is scoped to only allow
  creating this specific service-linked role.

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
- **AWS Identity and Access Management (IAM)** – Allows creating the AWS Transform custom
  [service-linked role](using-service-linked-roles.md#using-service-linked-roles-custom "using-service-linked-roles.md#using-service-linked-roles-custom")
  (`AWSServiceRoleForAWSTransformCustom`). This role is required for AWS Transform
  custom to emit CloudWatch metrics and logs to your account. The permission is scoped to only allow
  creating this specific service-linked role.

**Permissions details**

To view the policy permission details see [AWSTransformCustomManageTransformations](../../../aws-managed-policy/latest/reference/AWSTransformCustomManageTransformations.md "../../../aws-managed-policy/latest/reference/AWSTransformCustomManageTransformations.md") in the AWS Managed Policy Reference
Guide.

## AWS managed policy: AWSTransformInfrastructureExecutorAccessBatch

This policy grants the permissions needed to execute AWS Transform Continuous Modernization
assessments and transformations using AWS Batch. Attach this policy to an IAM
role in your account. The AWS Transform Continuous Modernization CLI and agent assume this
role to upload source code, retrieve results, monitor Batch job status, read logs,
and manage transformation schedules.

**Description**

This policy includes the following permissions:

- **AWS Lambda** – Allows invoking and retrieving the
  configuration of specific `atx`-prefixed Lambda functions that orchestrate
  the transformation workflow, including job triggering, status retrieval, and job
  listing functions.
- **Amazon S3** – Allows uploading source code to
  `atx-source-code-*` buckets, downloading transformation results from
  `atx-custom-output-*` and `atx-ct-output-*` buckets, and
  writing batch sidecar output to `atx-custom-output-*` buckets.
- **AWS Key Management Service (KMS)** – Allows encryption and
  decryption of data using the AWS Transform encryption key
  (`alias/atx-encryption-key`).
- **Amazon CloudWatch Logs** – Allows reading Batch job and Lambda
  execution log events for transformation monitoring and debugging.
- **Amazon CloudWatch** – Allows getting and listing the AWS Transform
  CLI dashboard for operational visibility.
- **AWS Batch** – Allows describing and listing
  compute environments, job queues, job definitions, and job status.
- **CloudFormation** – Allows describing and listing
  AWS Transform infrastructure stacks, including the Security Agent stack, to check
  deployment status.
- **Amazon SQS** – Allows sending messages to the
  `atx-dispatcher-queue` to enqueue transformation jobs through the
  dispatcher.
- **Resource Groups Tagging API** – Allows retrieving
  tagged resources to discover AWS Transform infrastructure in your account.
- **AWS Secrets Manager** – Allows retrieving and
  describing AWS Transform secrets stored under the `atx/` prefix.
- **Amazon EventBridge Scheduler** – Allows managing
  scheduled transformation jobs within the `atx-ct` schedule
  group.
- **Amazon EC2** – Allows describing VPC, subnet,
  security group, route table, and NAT gateway configuration for Batch compute
  environment networking.
- **AWS Identity and Access Management (IAM)** – Allows reading
  `ATX`-prefixed and `Atx`-prefixed role configurations to
  validate infrastructure setup, and passing the
  `AtxSchedulerInvocationRole` to Amazon EventBridge Scheduler so that it can
  invoke scheduled jobs.

The policy implements least-privilege access through resource-level permissions,
tag-based conditions, the `aws:ResourceAccount` condition, and service-scoped
`iam:PassedToService` conditions to ensure operations are limited to AWS Transform
resources within the same AWS account.

**Permissions details**

To view the policy permission details see [AWSTransformInfrastructureExecutorAccessBatch](../../../aws-managed-policy/latest/reference/AWSTransformInfrastructureExecutorAccessBatch.md "../../../aws-managed-policy/latest/reference/AWSTransformInfrastructureExecutorAccessBatch.md") in the AWS Managed Policy
Reference Guide.

## AWS managed policy: AWSTransformInfrastructureExecutorAccessEC2

This policy grants the permissions needed to execute AWS Transform Continuous Modernization
assessments and transformations using Amazon EC2. Attach this policy to an IAM role in
your account. The AWS Transform Continuous Modernization CLI and agent assume this role to
upload source code, retrieve results, monitor job status, and manage transformation
schedules.

**Description**

This policy includes the following permissions:

- **CloudFormation** – Allows describing AWS Transform
  infrastructure stacks (including the Security Agent stack), stack events, stack
  resources, and drift detection status, listing stacks, and validating CloudFormation
  templates before deployment.
- **Amazon SQS** – Allows sending messages to the
  `atx-dispatcher-queue` to enqueue transformation jobs through the
  dispatcher.
- **Amazon EC2** – Allows describing instances, AMIs,
  VPCs, subnets, security groups, key pairs, route tables, NAT gateways, and internet
  gateways. Permits starting and stopping EC2 instances tagged with
  `atx-remote-infra: true`.
- **Amazon EC2 Systems Manager (SSM)** – Allows monitoring command
  execution status, and running commands and sessions on AWS Transform-tagged instances,
  including running the `AWS-RunShellScript` document.
- **Amazon S3** – Allows managing source code and output
  artifacts in AWS Transform buckets, including getting, putting, and deleting objects and
  listing buckets.
- **AWS Key Management Service (KMS)** – Allows encryption and
  decryption of data using the AWS Transform encryption key
  (`alias/atx-encryption-key`).
- **AWS Secrets Manager** – Allows retrieving and
  describing transformation secrets, such as repository credentials, stored under the
  `atx/` prefix.
- **Amazon EventBridge Scheduler** – Allows managing
  scheduled transformation jobs within the `atx-ct` schedule
  group.
- **Resource Groups Tagging API** – Allows retrieving
  tagged resources to discover AWS Transform infrastructure in your account.
- **AWS Identity and Access Management (IAM)** – Allows passing the
  `atx-transform-role*` role to Amazon EC2 and the
  `AtxSchedulerInvocationRole` to Amazon EventBridge Scheduler, and reading
  role and instance profile configuration for EC2 instances.

The policy implements least-privilege access through resource-level permissions,
tag-based conditions, the `aws:ResourceAccount` condition, and service-scoped
`iam:PassedToService` conditions to ensure operations are limited to AWS Transform
resources within the same AWS account.

**Permissions details**

To view the policy permission details see [AWSTransformInfrastructureExecutorAccessEC2](../../../aws-managed-policy/latest/reference/AWSTransformInfrastructureExecutorAccessEC2.md "../../../aws-managed-policy/latest/reference/AWSTransformInfrastructureExecutorAccessEC2.md") in the AWS Managed Policy
Reference Guide.

## AWS managed policy: AWSTransformLandingZoneAgentPolicy

This policy grants the permissions needed to set up AWS landing zones, including
account provisioning, organizational governance, and AWS Control Tower configuration.
Attach this policy to the IAM role that AWS Transform assumes in your management account when it
builds a landing zone.

**Description**

This policy includes the following permissions:

- **AWS Control Tower** – Allows listing and
  describing landing zones, baselines, enabled baselines, enabled controls, and the
  status of baseline and control operations. Permits enabling controls and baselines and
  tagging Control Tower resources.
- **AWS Organizations** – Allows describing the
  organization, accounts, organizational units (OUs), and policies, and listing roots,
  parents, and the OU hierarchy. Permits creating accounts and OUs, moving accounts
  between OUs, and tagging organization resources. Creating, updating, and attaching
  service control policies is allowed only when the call is made through AWS Control
  Tower.
- **CloudFormation** – Allows creating, updating,
  tagging, and describing landing zone stacks with names that start with
  `AtxLz`, reading stack events and templates, and creating, describing,
  listing, and executing change sets. Deleting stacks is not permitted.
- **AWS Service Catalog** – Allows creating, updating,
  deleting, and listing provisioning artifacts for products in your account, which
  AWS Control Tower uses to provision accounts.
- **Amazon S3** – Allows creating and managing the
  `transform-vmware-landing-zone-*` bucket and its objects, including bucket
  policy, tagging, encryption configuration, and multipart uploads.

The policy implements least-privilege access through resource name prefixes
(`AtxLz*` and `transform-vmware-landing-zone-*`), tag-based conditions
on `CreatedBy: AWSTransform` and the workspace ID, the
`aws:ResourceAccount` condition, an `aws:RequestedRegion` condition
that restricts operations to your target AWS Region, and an `aws:CalledVia`
condition that limits service control policy changes to calls made by AWS Control
Tower.

**Permissions details**

To view the policy permission details see [AWSTransformLandingZoneAgentPolicy](../../../aws-managed-policy/latest/reference/AWSTransformLandingZoneAgentPolicy.md "../../../aws-managed-policy/latest/reference/AWSTransformLandingZoneAgentPolicy.md") in the AWS Managed Policy Reference
Guide.

## AWS managed policy: AWSTransformNetworkMigrationAgentPolicy

This policy grants the permissions needed to deploy and configure network infrastructure,
including VPCs, transit gateways, and route tables, for network migration. Attach this
policy to the IAM role that AWS Transform assumes in your target account when it migrates a network
topology.

**Description**

This policy includes the following permissions:

- **AWS Transform MGN (MGN)** – Allows creating, reading,
  updating, deleting, and tagging network migration definitions and their mapper
  segments. Permits starting and listing network mappings, analyses, code generations,
  deployments, and deployed stack deletions.
- **CloudFormation** – Allows creating, updating,
  deleting, and describing network stacks with names that start with `Nmd`,
  listing stacks, and managing termination protection.
- **Amazon EC2** – Allows describing network topology,
  including VPCs, subnets, security groups, route tables, network interfaces, NAT
  gateways, internet gateways, transit gateways and their attachments and route tables,
  VPN connections, and prefix lists. Permits creating VPCs, internet gateways, transit
  gateways, and Elastic IP addresses, and tagging them on creation. Through
  CloudFormation, permits creating, modifying, and deleting these and other network
  resources, including subnets, route tables and routes, NAT gateways, network
  interfaces, security groups and rules, and transit gateway attachments and route
  tables. Attachments to VPCs in other accounts are limited to accounts in your
  organization.
- **Reachability Analyzer** – Allows creating and
  tagging network insights paths, starting analyses, and reading results to validate
  connectivity between source and target networks. To place analysis probes, permits
  creating network interfaces and security groups, authorizing security group rules, and
  deleting those resources, paths, and analyses during cleanup. Includes read-only access
  to AWS Direct Connect, Elastic Load Balancing, AWS Global Accelerator, and AWS
  Network Firewall configuration used during path analysis.
- **AWS Resource Access Manager (RAM)** – Allows
  creating, updating, tagging, and deleting resource shares and their associations to
  share transit gateways and Systems Manager parameters with other accounts in your
  organization. Shares that allow external principals are not permitted.
- **AWS Lambda** – Allows creating, tagging, invoking,
  and deleting `network-migration*` functions that CloudFormation uses as
  custom resources for transit gateway modifications.
- **AWS Identity and Access Management (IAM)** – Allows creating, tagging,
  reading, and deleting the `Nmd*modifyTransitGateway*` Lambda execution role,
  attaching only the `AWSApplicationMigrationNetworkMigrationCustomResource` and
  `AWSLambdaBasicExecutionRole` policies to it, and passing it to AWS
  Lambda. Also allows creating the transit gateway service-linked role.
- **Amazon EC2 Systems Manager (SSM)** – Allows reading and writing
  `/network-migration/*` parameters and their resource policies for
  cross-account sharing.
- **Amazon CloudWatch Logs** – Allows creating log groups and log
  streams and publishing log events for `/aws/lambda/network-migration*`
  functions.
- **Amazon S3** – Allows creating and managing the
  `transform-vmware-target-*` bucket and the objects in it that store network
  migration artifacts.
- **AWS Key Management Service (KMS)** – Allows decrypting, describing,
  and generating data keys with your workspace encryption key, restricted to Amazon S3
  usage.
- **AWS Organizations** – Allows listing accounts to
  discover the accounts in your organization.
- **AWS STS** – Allows assuming the
  `AWSTransformNetworkMigrationAgentSharingRole_`management-or-delegated-admin-account-id``
  role in other accounts in your organization for multi-account deployments.

The policy implements least-privilege access through resource name prefixes
(`Nmd*`, `network-migration*`, and
`transform-vmware-target-*`), tag-based conditions on `CreatedBy` and
the workspace ID, the `aws:ResourceAccount` and `aws:ResourceOrgID`
conditions, an `aws:RequestedRegion` condition that restricts operations to your
target AWS Region, `aws:CalledVia` conditions that limit most network changes to
calls made by CloudFormation, and an external ID that includes your workspace ID for
cross-account role assumption.

**Permissions details**

To view the policy permission details see [AWSTransformNetworkMigrationAgentPolicy](../../../aws-managed-policy/latest/reference/AWSTransformNetworkMigrationAgentPolicy.md "../../../aws-managed-policy/latest/reference/AWSTransformNetworkMigrationAgentPolicy.md") in the AWS Managed Policy Reference
Guide.

## AWS managed policy: AWSTransformSecurityAgentExecutorAccess

This policy grants AWS Transform Continuous Modernization the permissions needed to invoke the
AWS Security Agent service for automated code security reviews and remediation. Attach
this policy to an IAM role in your account that the AWS Transform Continuous Modernization
CLI and agent assume to upload scan artifacts and retrieve findings.

**Description**

This policy includes the following permissions:

- **AWS Security Agent** – Allows listing agent spaces,
  creating code reviews, starting code review jobs, listing and retrieving findings, and
  starting code remediation. These actions are scoped to agent spaces in your
  account.
- **Amazon S3** – Allows downloading scan results and
  findings from the `atx-security-agent-*` bucket, and uploading source code
  for security scanning to the `security-scans/*` prefix within that
  bucket.
- **AWS Identity and Access Management (IAM)** – Allows passing the
  `security-agent-*` role to the AWS Security Agent service so that it can
  perform the scan.
- **CloudFormation** – Allows listing stacks in the
  account and describing the `AtxSecurityAgentStack-*` stack to discover and
  monitor the Security Agent infrastructure deployment status.

The policy implements least-privilege access through resource-level permissions, S3
bucket and key prefixes, the `aws:ResourceAccount` and
`s3:ResourceAccount` conditions, and a service-scoped
`iam:PassedToService` condition to ensure operations are limited to AWS
Security Agent resources within the same AWS account.

**Permissions details**

To view the policy permission details see [AWSTransformSecurityAgentExecutorAccess](../../../aws-managed-policy/latest/reference/AWSTransformSecurityAgentExecutorAccess.md "../../../aws-managed-policy/latest/reference/AWSTransformSecurityAgentExecutorAccess.md") in the AWS Managed Policy Reference
Guide.

## AWS managed policy: AWSTransformServerMigrationAgentPolicy

This policy grants the permissions needed to perform server migration operations,
including replication, testing, and cutover, using AWS Transform MGN. Attach this policy to the IAM
role that AWS Transform assumes in your target account when it migrates servers.

**Description**

This policy includes the following permissions:

- **AWS Transform MGN (MGN)** – Allows describing and managing
  source servers, applications, waves, jobs, connectors, and launch and replication
  configuration templates, including creating, updating, deleting, associating, and
  tagging them. Permits reading and updating account settings, registering agents,
  starting tests and cutovers, controlling replication (start, stop, pause, and resume),
  finalizing cutover, archiving source servers, terminating target instances, configuring
  source server and template post-launch actions, and importing and exporting server
  inventory.
- **Amazon EC2** – Allows describing instances, images,
  volumes, snapshots, VPCs, subnets, security groups, instance types, and launch
  templates. Permits creating launch template versions and modifying launch templates,
  restricted to launch templates that carry the
  `AWSApplicationMigrationServiceManaged` tag, and tagging launch templates and
  security groups on creation. Through MGN, permits running, starting, stopping, and
  terminating target instances, modifying instance attributes, creating volumes and
  snapshots, attaching, detaching, and deleting volumes, deleting launch template
  versions, and creating security groups and authorizing and revoking their egress rules.
  Instances can launch into VPCs in your account or into shared VPCs in other accounts in
  your organization.
- **Amazon FSx** – Allows describing file systems,
  storage virtual machines, volumes, and snapshots. Through MGN, permits creating
  volumes and snapshots, and deleting and tagging volumes, when you use FSx for ONTAP as
  target storage.
- **Amazon EC2 Systems Manager (SSM)** – Allows reading AWS-managed and
  account documents, sending commands to migrated instances, and starting and monitoring
  post-launch automation executions. Permits managing
  `ManagedByAWSApplicationMigrationService-*` parameters.
- **AWS Identity and Access Management (IAM)** – Allows passing the MGN service
  roles (`AWSApplicationMigrationConversionServerRole`,
  `AWSApplicationMigrationLaunchInstanceWithDrsRole`, and
  `AWSApplicationMigrationLaunchInstanceWithSsmRole`) to Amazon EC2.
- **Amazon S3** – Allows creating and managing the
  `transform-vmware-target-*` bucket and the objects in it that store
  migration artifacts, and reading the MGN source automation client signature
  file.
- **AWS Key Management Service (KMS)** – Allows decrypting, describing,
  and generating data keys with your workspace encryption key, restricted to Amazon S3
  usage.
- **Service Quotas** – Allows reading the VPC quota for
  security groups per network interface through MGN.
- **AWS Secrets Manager** – Allows listing secrets to discover the
  credentials used for source server discovery.
- **AWS Organizations** – Allows listing accounts to
  discover the accounts in your organization.
- **AWS STS** – Allows assuming the
  `AWSTransformRehostSharingRole_`management-or-delegated-admin-account-id``
  role in other accounts in your organization for multi-account migrations.

The policy implements least-privilege access through resource-level permissions,
tag-based conditions on `CreatedBy`,
`AWSApplicationMigrationServiceManaged`, and the workspace ID, the
`aws:ResourceAccount` and `aws:ResourceOrgID` conditions, an
`aws:RequestedRegion` condition that restricts operations to your target
AWS Region, `aws:CalledVia` conditions that limit most Amazon EC2, Amazon FSx, and
Systems Manager actions to calls made by MGN, and an external ID that includes your
workspace ID for cross-account role assumption.

**Permissions details**

To view the policy permission details see [AWSTransformServerMigrationAgentPolicy](../../../aws-managed-policy/latest/reference/AWSTransformServerMigrationAgentPolicy.md "../../../aws-managed-policy/latest/reference/AWSTransformServerMigrationAgentPolicy.md") in the AWS Managed Policy Reference
Guide.

## AWS managed policy: DBModDiscoveryAndAssessment

This policy provides comprehensive database modernization discovery and assessment capabilities for AWS Transform.

**Description**

This policy includes the following permissions:

- **Amazon EC2** – Allows describing infrastructure components including instances, VPCs, subnets, security groups, availability zones, VPC endpoints, and internet gateways.
- **Amazon RDS** – Allows describing database instances, clusters, and subnet groups. Allows modifying DB subnet groups within the same AWS account for migration preparation.
- **Amazon RDS Data API** – Allows enabling and disabling HTTP endpoints and executing SQL statements on database clusters tagged for the database modernization project.
- **AWS DMS** – Allows describing endpoints, replication instances, tasks, subnet groups, and orderable instances. Allows listing data providers, instance profiles, and migration projects. Allows describing table statistics, assessment runs, and metadata model operations. Detailed describe and metadata operations are restricted to resources tagged for the database modernization project.
- – Allows listing secrets for discovering database credentials.
- **AWS Identity and Access Management (IAM)** – Allows inspecting specific AWS DMS service roles and their attached policies. Includes access to read AWS-managed AWS DMS policies.
- **AWS Key Management Service (KMS)** – Allows listing key aliases and describing keys. Allows decryption of secrets through integration, restricted to the same AWS account.

The policy implements least-privilege access through resource-level permissions,
tag-based conditions, and account-level restrictions to ensure operations are limited to
database modernization project resources within the same AWS account.

**Permissions details**

To view the policy permission details see [DBModDiscoveryAndAssessment](../../../aws-managed-policy/latest/reference/DBModDiscoveryAndAssessment.md "../../../aws-managed-policy/latest/reference/DBModDiscoveryAndAssessment.md") in the AWS Managed Policy Reference
Guide.

## AWS managed policy: DBModProvisioningAndMigration

This policy provides database provisioning and migration capabilities for AWS Transform database modernization projects. It includes permissions to create and manage migration infrastructure, provision target databases, and store migration data.

**Description**

This policy includes the following permissions:

- **AWS DMS** – Allows creating and managing replication subnet groups, instance profiles, data providers, migration projects, endpoints, replication instances, and replication tasks. Includes schema conversion operations such as metadata model import, conversion, export, and assessment. Allows lifecycle management of replication instances (create, delete, modify, reboot) and replication tasks (delete, start, stop, assess). All write operations are restricted to resources tagged for the database modernization project.
- **Amazon RDS** – Allows creating database subnet groups, database clusters, and database instances. All resources must be tagged for the database modernization project.
- – Allows creating, updating, and tagging secrets with the database modernization naming prefix. Allows retrieving secret values and describing secrets for tagged resources.
- **Amazon S3** – Allows creating and managing S3 buckets and objects for migration data storage. Includes bucket tagging, versioning, and object lifecycle operations. Restricted to buckets with the database modernization naming prefix.
- **AWS Identity and Access Management (IAM)** – Allows passing specific AWS DMS service roles to AWS DMS and schema conversion services. Allows creating the Amazon RDS service-linked role required for database operations.

The policy implements least-privilege access through resource-level permissions,
tag-based conditions, and account-level restrictions to ensure operations are limited to
database modernization project resources within the same AWS account.

**Permissions details**

To view the policy permission details see [DBModProvisioningAndMigration](../../../aws-managed-policy/latest/reference/DBModProvisioningAndMigration.md "../../../aws-managed-policy/latest/reference/DBModProvisioningAndMigration.md") in the AWS Managed Policy Reference
Guide.
