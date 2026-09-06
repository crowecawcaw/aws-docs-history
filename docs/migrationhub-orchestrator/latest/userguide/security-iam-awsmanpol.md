

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# AWS managed policies for Migration Hub Orchestrator
<a name="security-iam-awsmanpol"></a>

To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the **ReadOnlyAccess** AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

## AWS managed policy: AWSMigrationHubOrchestratorConsoleFullAccess
<a name="security-iam-awsmanpol-AWSMigrationHubOrchestratorConsoleFullAccess"></a>

Attach the `AWSMigrationHubOrchestratorConsoleFullAccess` policy to your IAM identities.

The `AWSMigrationHubOrchestratorConsoleFullAccess` policy grants an AWS account full access to the Migration Hub Orchestrator service through the AWS Management Console.

**Permissions details**

This policy includes the following permissions.
+ `account` – Grants permissions that allow listing AWS Regions.
+ `discovery` – Grants permissions that allow access to Application Discovery Service.
+ `ec2` – Grants permissions that allow describing EC2 instances and VPCs.
+ `iam` – Allows a service-linked role to be created for the AWS account, which is a requirement for using Migration Hub Orchestrator. This policy also grants permissions that allow listing instance profiles and IAM roles.
+ `kms` – Grants permissions that allow listing AWS KMS keys and aliases.
+ `migrationhub-orchestrator` – Grants full access to Migration Hub Orchestrator. 
+ `s3` – Grants permissions that allow creating and reading from the S3 buckets used by Migration Hub Orchestrator.
+ `secretsmanager` – Grants permissions that allow access to AWS Secrets Manager.

To view the permissions for this policy, see [AWSMigrationHubOrchestratorConsoleFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMigrationHubOrchestratorConsoleFullAccess.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSMigrationHubOrchestratorPlugin
<a name="security-iam-awsmanpol-AWSMigrationHubOrchestratorPlugin"></a>

Attach the `AWSMigrationHubOrchestratorPlugin` policy to your IAM identities.

The `AWSMigrationHubOrchestratorPlugin` policy grants an AWS account access to the Migration Hub Orchestrator service, read/write access to the S3 buckets that are related to the service, Amazon API Gateway access to upload logs and metrics to AWS, and AWS Secrets Manager access to fetch credentials.

**Permissions details**

This policy includes the following permissions.
+ `migrationhub-orchestrator` – Grants permissions that allow access to the Orchestrator plugin.
+ `s3` – Grants permissions that allow write access to the S3 buckets used by Migration Hub Orchestrator.
+ `secretsmanager` – Grants permissions that allow access to AWS Secrets Manager.

To view the permissions for this policy, see [AWSMigrationHubOrchestratorPlugin](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMigrationHubOrchestratorPlugin.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSMigrationHubOrchestratorInstanceRolePolicy
<a name="security-iam-awsmanpol-AWSMigrationHubOrchestratorInstanceRolePolicy"></a>

Attach the `AWSMigrationHubOrchestratorInstanceRolePolicy` policy to your IAM identities.

This policy grants an AWS account read/write access to Amazon S3 buckets that are related to the service and to AWS Secrets Manager to fetch credentials.

**Permissions details**

This policy includes the following permissions.
+ `migrationhub-orchestrator` – Grants permissions that allow access to Migration Hub Orchestrator.
+ `s3` – Grants permissions that allow read/write access to Amazon S3 buckets used by Migration Hub Orchestrator.
+ `secretsmanager` – Grants permissions that allow access to AWS Secrets Manager.

To view the permissions for this policy, see [AWSMigrationHubOrchestratorInstanceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMigrationHubOrchestratorInstanceRolePolicy.html) in the *AWS Managed Policy Reference Guide*.

## Migration Hub Orchestrator updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>



View details about updates to AWS managed policies for Migration Hub Orchestrator since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the Migration Hub Orchestrator Document history page.




| Change | Description | Date | 
| --- | --- | --- | 
| [AWSMigrationHubOrchestratorServiceRolePolicy](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/using-service-linked-roles.html) – Updated policy | launchwizard:ListDeployments and launchwizard:GetDeployment actions added to the policy. | March 4, 2024 | 
| [AWSMigrationHubOrchestratorConsoleFullAccess](#security-iam-awsmanpol-AWSMigrationHubOrchestratorConsoleFullAccess) – Updated policy | ec2:DescribeVpcs, kms:ListKeys, kms:ListAliases, iam:ListInstanceProfiles, iam:ListRoles, ecs:ListClusters, and account:ListRegions actions added to the policy. | December 5, 2023 | 
|  [AWSMigrationHubOrchestratorServiceRolePolicy](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/using-service-linked-roles.html) – Updated policy | `ec2:DescribeLaunchTemplates` action added to the policy. | February 24, 2023 | 
|  [AWSMigrationHubOrchestratorServiceRolePolicy](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/using-service-linked-roles.html) – Updated policy  | `ec2:DescribeImportImageTasks`, `s3:ListBucket`, and `events:RemoveTargets` actions added to the policy. | December 21, 2022 | 
| [AWSMigrationHubOrchestratorConsoleFullAccess](#security-iam-awsmanpol-AWSMigrationHubOrchestratorConsoleFullAccess) – New policy made available at launch | `AWSMigrationHubOrchestratorConsoleFullAccess` grants an AWS account full access to the Migration Hub Orchestrator service through the AWS Management Console. | April 20, 2022 | 
| [AWSMigrationHubOrchestratorPlugin](#security-iam-awsmanpol-AWSMigrationHubOrchestratorPlugin) – New policy made available at launch | `AWSMigrationHubOrchestratorPlugin` grants an AWS account access to the Migration Hub Orchestrator service and read/write access to Amazon S3 buckets that are related to the service. It also grants Amazon API Gateway access to upload logs and metrics to AWS, and AWS Secrets Manager access to fetch credentials. | April 20, 2022 | 
| [AWSMigrationHubOrchestratorServiceRolePolicy](using-service-linked-roles.md#slr-permissions) – New policy made available at launch | The `AWSMigrationHubOrchestratorServiceRolePolicy` service-linked role policy provides access to AWS Migration Hub and AWS Application Discovery Service. This policy also grants permissions for storing reports in Amazon Simple Storage Service (Amazon S3). | April 20, 2022 | 
| `AWSMigrationHubOrchestratorInstanceRolePolicy` – New policy | `AWSMigrationHubOrchestratorInstanceRolePolicy` grants an AWS account read/write access to Amazon S3 buckets that are related to the service and to AWS Secrets Manager to fetch credentials. | April 20, 2022 | 
| Migration Hub Orchestrator started tracking changes | Migration Hub Orchestrator started tracking changes for its AWS managed policies. | April 20, 2022 | 