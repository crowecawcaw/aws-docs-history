AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# AWS managed policies for Migration Hub Orchestrator

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

## AWS managed policy: AWSMigrationHubOrchestratorConsoleFullAccess

Attach the `AWSMigrationHubOrchestratorConsoleFullAccess` policy to your
IAM identities.

The `AWSMigrationHubOrchestratorConsoleFullAccess` policy grants an
AWS account full access to the Migration Hub Orchestrator service through the AWS Management Console.

**Permissions details**

This policy includes the following permissions.

- `account` – Grants permissions that allow listing
  AWS Regions.
- `discovery` – Grants permissions that allow access to
  Application Discovery Service.
- `ec2` – Grants permissions that allow describing EC2
  instances and VPCs.
- `iam` – Allows a service-linked role to be created for the
  AWS account, which is a requirement for using Migration Hub Orchestrator. This policy also
  grants permissions that allow listing instance profiles and IAM roles.
- `kms` – Grants permissions that allow listing AWS KMS keys and
  aliases.
- `migrationhub-orchestrator` – Grants full access to
  Migration Hub Orchestrator.
- `s3` – Grants permissions that allow creating and reading
  from the S3 buckets used by Migration Hub Orchestrator.
- `secretsmanager` – Grants permissions that allow access to
  AWS Secrets Manager.

To view the permissions for this policy, see [AWSMigrationHubOrchestratorConsoleFullAccess](../../../aws-managed-policy/latest/reference/AWSMigrationHubOrchestratorConsoleFullAccess.md "../../../aws-managed-policy/latest/reference/AWSMigrationHubOrchestratorConsoleFullAccess.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed

policy: AWSMigrationHubOrchestratorPlugin

Attach the `AWSMigrationHubOrchestratorPlugin` policy to your IAM
identities.

The `AWSMigrationHubOrchestratorPlugin` policy grants an AWS account
access to the Migration Hub Orchestrator service, read/write access to the S3 buckets that are related to
the service, Amazon API Gateway access to upload logs and metrics to AWS, and AWS
Secrets Manager access to fetch credentials.

**Permissions details**

This policy includes the following permissions.

- `migrationhub-orchestrator` – Grants permissions that allow
  access to the Orchestrator plugin.
- `s3` – Grants permissions that allow write access to the S3
  buckets used by Migration Hub Orchestrator.
- `secretsmanager` – Grants permissions that allow access to
  AWS Secrets Manager.

To view the permissions for this policy, see [AWSMigrationHubOrchestratorPlugin](../../../aws-managed-policy/latest/reference/AWSMigrationHubOrchestratorPlugin.md "../../../aws-managed-policy/latest/reference/AWSMigrationHubOrchestratorPlugin.md") in the
_AWS Managed Policy Reference Guide_.

## AWS managed policy: AWSMigrationHubOrchestratorInstanceRolePolicy

Attach the `AWSMigrationHubOrchestratorInstanceRolePolicy` policy to your
IAM identities.

This policy grants an AWS account read/write access to Amazon S3 buckets that are related
to the service and to AWS Secrets Manager to fetch credentials.

**Permissions details**

This policy includes the following permissions.

- `migrationhub-orchestrator` – Grants permissions that allow
  access to Migration Hub Orchestrator.
- `s3` – Grants permissions that allow read/write access to
  Amazon S3 buckets used by Migration Hub Orchestrator.
- `secretsmanager` – Grants permissions that allow access to
  AWS Secrets Manager.

To view the permissions for this policy, see [AWSMigrationHubOrchestratorInstanceRolePolicy](../../../aws-managed-policy/latest/reference/AWSMigrationHubOrchestratorInstanceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSMigrationHubOrchestratorInstanceRolePolicy.md") in the
_AWS Managed Policy Reference Guide_.

## Migration Hub Orchestrator updates to AWS managed

policies

View details about updates to AWS managed policies for Migration Hub Orchestrator since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the Migration Hub Orchestrator Document history page.

| Change                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                            | Date              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AWSMigrationHubOrchestratorServiceRolePolicy](using-service-linked-roles.md "using-service-linked-roles.md") –<br>Updated policy                                                                                                    | `launchwizard:ListDeployments` and<br>`launchwizard:GetDeployment` actions added to the<br>policy.                                                                                                                                                                                                                                     | March 4, 2024     |
| [AWSMigrationHubOrchestratorConsoleFullAccess](#security-iam-awsmanpol-AWSMigrationHubOrchestratorConsoleFullAccess "#security-iam-awsmanpol-AWSMigrationHubOrchestratorConsoleFullAccess") –<br>Updated policy                      | `ec2:DescribeVpcs`, `kms:ListKeys`,<br>`kms:ListAliases`, `iam:ListInstanceProfiles`,<br>`iam:ListRoles`, `ecs:ListClusters`, and<br>`account:ListRegions` actions added to the<br>policy.                                                                                                                                             | December 5, 2023  |
| [AWSMigrationHubOrchestratorServiceRolePolicy](using-service-linked-roles.md "using-service-linked-roles.md") –<br>Updated policy                                                                                                    | `ec2:DescribeLaunchTemplates` action added to the<br>policy.                                                                                                                                                                                                                                                                           | February 24, 2023 |
| [AWSMigrationHubOrchestratorServiceRolePolicy](using-service-linked-roles.md "using-service-linked-roles.md") –<br>Updated policy                                                                                                    | `ec2:DescribeImportImageTasks`,<br>`s3:ListBucket`, and<br>`events:RemoveTargets` actions added to the<br>policy.                                                                                                                                                                                                                      | December 21, 2022 |
| [AWSMigrationHubOrchestratorConsoleFullAccess](#security-iam-awsmanpol-AWSMigrationHubOrchestratorConsoleFullAccess "#security-iam-awsmanpol-AWSMigrationHubOrchestratorConsoleFullAccess") –<br>New policy made available at launch | `AWSMigrationHubOrchestratorConsoleFullAccess` grants<br>an AWS account full access to the Migration Hub Orchestrator service through the<br>AWS Management Console.                                                                                                                                                                   | April 20, 2022    |
| [AWSMigrationHubOrchestratorPlugin](#security-iam-awsmanpol-AWSMigrationHubOrchestratorPlugin "#security-iam-awsmanpol-AWSMigrationHubOrchestratorPlugin") – New policy<br>made available at launch                                  | `AWSMigrationHubOrchestratorPlugin` grants an<br>AWS account access to the Migration Hub Orchestrator service and read/write access<br>to Amazon S3 buckets that are related to the service. It also grants<br>Amazon API Gateway access to upload logs and metrics to<br>AWS, and AWS Secrets Manager access to fetch<br>credentials. | April 20, 2022    |
| [AWSMigrationHubOrchestratorServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") –<br>New policy made available at launch                                               | The `AWSMigrationHubOrchestratorServiceRolePolicy`<br>service-linked role policy provides access to AWS Migration Hub and<br>AWS Application Discovery Service. This policy also grants permissions for storing<br>reports in Amazon Simple Storage Service (Amazon S3).                                                               | April 20, 2022    |
| `AWSMigrationHubOrchestratorInstanceRolePolicy`<br>– New policy                                                                                                                                                                      | `AWSMigrationHubOrchestratorInstanceRolePolicy` grants<br>an AWS account read/write access to Amazon S3 buckets that are related<br>to the service and to AWS Secrets Manager to fetch<br>credentials.                                                                                                                                 | April 20, 2022    |
| Migration Hub Orchestrator started tracking<br>changes                                                                                                                                                                               | Migration Hub Orchestrator started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                                                                                   | April 20, 2022    |
