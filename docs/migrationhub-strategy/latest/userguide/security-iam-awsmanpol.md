AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# AWS managed policies for Migration Hub Strategy Recommendations

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

## AWS

managed policy: AWSMigrationHubStrategyConsoleFullAccess

You can attach the `AWSMigrationHubStrategyConsoleFullAccess` policy to
your IAM identities.

The `AWSMigrationHubStrategyConsoleFullAccess` policy grants a user full
access to the Strategy Recommendations service through the AWS Management Console.

**Permissions details**

This policy includes the following permissions.

- `discovery` – Grants the user access to get discovery
  summary in Application Discovery Service.
- `iam` – Allows a service-linked role to be created for the
  user, which is a requirement for using Strategy Recommendations.
- `migrationhub-strategy` – Grants the user full access to
  Strategy Recommendations.
- `s3` – Allows the user to create and read from the S3
  buckets used by Strategy Recommendations.
- `secretsmanager` – Allows the user to list secrets access in
  the Secrets Manager.

To view the permissions for this policy, see [AWSMigrationHubStrategyConsoleFullAccess](../../../aws-managed-policy/latest/reference/AWSMigrationHubStrategyConsoleFullAccess.md "../../../aws-managed-policy/latest/reference/AWSMigrationHubStrategyConsoleFullAccess.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed

policy: AWSMigrationHubStrategyCollector

You can attach the `AWSMigrationHubStrategyCollector` policy to your IAM
identities.

**Permissions details**

This policy includes the following permissions.

- `application-transformation` – Grants permissions to upload
  log and metric data for application transformation operations and work with
  porting compatibility assessments and recommendations.
- `execute-api` – Allows the user to access Amazon API Gateway
  to upload logs and metrics to AWS.
- `migrationhub-strategy` – Grants the user access to register
  messages, send messages, upload log data, and upload metric data to
  Strategy Recommendations.
- `s3` – Grants the user access to list buckets and their
  locations. Users are also granted access to write to, retrieve objects from, add
  objects to, return the access control list (ACL) of, create, access, configure
  encryption for, modify the `PublicAccessBlock` configuration for, set
  the versioning state for, and create or replace a lifecycle configuration for
  the S3 buckets used by Strategy Recommendations.
- `secretsmanager` – Allows the user to access secrets in the
  Secrets Manager that are used by Strategy Recommendations.

To view the permissions for this policy, see [AWSMigrationHubStrategyCollector](../../../aws-managed-policy/latest/reference/AWSMigrationHubStrategyCollector.md "../../../aws-managed-policy/latest/reference/AWSMigrationHubStrategyCollector.md")
in the _AWS Managed Policy Reference Guide_.

## Strategy Recommendations updates to AWS managed

policies

View details about updates to AWS managed policies for Strategy Recommendations since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the Strategy Recommendations Document history page.

| Change                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Date               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AWSMigrationHubStrategyCollector](#security-iam-awsmanpol-AWSMigrationHubStrategyCollector "#security-iam-awsmanpol-AWSMigrationHubStrategyCollector") – Update to an existing policy                                | This policy is updated to include the `PutLogData`, `StartPortingCompatibilityAssessment`, `GetPortingCompatibilityAssessment`, `StartPortingRecommendationAssessment` and `GetPortingRecommendationAssessment` application transformation actions to allow the application transformation service to send logs and metrics to the service. The `ListBucket` and `GetBucketLocation` were added for Amazon Simple Storage Service (Amazon S3) to support log and metric uploads. The `PutLogData` and `PutMetricData` were also added to allow the Strategy Recommendations collector to send logs and metrics to the service's endpoint. | April 1, 2024      |
| [AWSMigrationHubStrategyCollector](#security-iam-awsmanpol-AWSMigrationHubStrategyCollector "#security-iam-awsmanpol-AWSMigrationHubStrategyCollector") – Update to an existing policy                                | This policy is updated with the `PutMetricData` and `PutLogData` actions. These actions grant uploading log and metric data for application transformation operations. This update also adds conditions to ensure that the `aws:ResourceAccount` is equal to the `aws:PrincipalAccount` for permission to use the included Amazon Simple Storage Service and AWS Secrets Manager actions.                                                                                                                                                                                                                                                 | February 5, 2024   |
| [AWSMigrationHubStrategyCollector](#security-iam-awsmanpol-AWSMigrationHubStrategyCollector "#security-iam-awsmanpol-AWSMigrationHubStrategyCollector") – Update to an existing policy                                | This policy is updated with the following Amazon S3 APIs – `CreateBucket`, `PutEncryptionConfiguration`, `PutBucketPublicAccessBlock`, `PutBucketPolicy`, `PutBucketVersioning`, and `PutLifecycleConfiguration`.                                                                                                                                                                                                                                                                                                                                                                                                                         | September 15, 2023 |
| [AWSMigrationHubStrategyCollector](#security-iam-awsmanpol-AWSMigrationHubStrategyCollector "#security-iam-awsmanpol-AWSMigrationHubStrategyCollector") – Update to an existing policy                                | This policy update grants permissions that allow analysis of source code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | March 8, 2023      |
| [AWSMigrationHubStrategyConsoleFullAccess](#security-iam-awsmanpol-AWSMigrationHubStrategyConsoleFullAccess "#security-iam-awsmanpol-AWSMigrationHubStrategyConsoleFullAccess") – Update to an existing policy        | This policy is updated with three AWS Application Discovery Service APIs – `DescribeConfigurations`, `DescribeTags`, and `ListConfigurations`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | November 10, 2022  |
| [AWSMigrationHubStrategyCollector](#security-iam-awsmanpol-AWSMigrationHubStrategyCollector "#security-iam-awsmanpol-AWSMigrationHubStrategyCollector") – Update to an existing policy                                | This policy is updated with the `UpdateCollectorConfiguration` action. This action stores the configuration of your collector for easy retrieval.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | September 07, 2022 |
| [AWSMigrationHubStrategyConsoleFullAccess](#security-iam-awsmanpol-AWSMigrationHubStrategyConsoleFullAccess "#security-iam-awsmanpol-AWSMigrationHubStrategyConsoleFullAccess") – New policy made available at launch | `AWSMigrationHubStrategyConsoleFullAccess` grants a user full access to the Strategy Recommendations service through the AWS Management Console.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | October 25, 2021   |
| [AWSMigrationHubStrategyCollector](#security-iam-awsmanpol-AWSMigrationHubStrategyCollector "#security-iam-awsmanpol-AWSMigrationHubStrategyCollector") – New policy made available at launch                         | `AWSMigrationHubStrategyCollector` grants a user access to the Strategy Recommendations service and read/write access to the S3 buckets that are related to the service. It also grants Amazon API Gateway access to upload logs and metrics to AWS, and AWS Secrets Manager access to fetch credentials.                                                                                                                                                                                                                                                                                                                                 | October 25, 2021   |
| [AWSMigrationHubStrategyServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") – New policy made available at launch                                       | The `AWSMigrationHubStrategyServiceRolePolicy` service-linked role policy provides access to AWS Migration Hub and AWS Application Discovery Service. This policy also grants permissions for storing reports in Amazon Simple Storage Service (Amazon S3).                                                                                                                                                                                                                                                                                                                                                                               | October 25, 2021   |
| Strategy Recommendations started tracking changes                                                                                                                                                                     | Strategy Recommendations started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | October 25, 2021   |
