# AWS managed policies for Amazon RDS

To add permissions to permission sets and roles, it's easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To
get started quickly, you can use our AWS managed policies. These policies cover common use
cases and are available in your AWS account. For more information about AWS managed
policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to
an AWS managed policy to support new features. This type of update affects all identities
(permission sets and roles) where the policy is attached. Services are most likely to update
an AWS managed policy when a new feature is launched or when new operations become
available. Services don't remove permissions from an AWS managed policy, so policy updates
don't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the `ReadOnlyAccess` AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

###### Topics

- [AWS managed policy: AmazonRDSReadOnlyAccess](#rds-security-iam-awsmanpol-AmazonRDSReadOnlyAccess "#rds-security-iam-awsmanpol-AmazonRDSReadOnlyAccess")
- [AWS managed policy: AmazonRDSFullAccess](#rds-security-iam-awsmanpol-AmazonRDSFullAccess "#rds-security-iam-awsmanpol-AmazonRDSFullAccess")
- [AWS managed policy: AmazonRDSDataFullAccess](#rds-security-iam-awsmanpol-AmazonRDSDataFullAccess "#rds-security-iam-awsmanpol-AmazonRDSDataFullAccess")
- [AWS managed policy: AmazonRDSEnhancedMonitoringRole](#rds-security-iam-awsmanpol-AmazonRDSEnhancedMonitoringRole "#rds-security-iam-awsmanpol-AmazonRDSEnhancedMonitoringRole")
- [AWS managed policy: AmazonRDSPerformanceInsightsReadOnly](#rds-security-iam-awsmanpol-AmazonRDSPerformanceInsightsReadOnly "#rds-security-iam-awsmanpol-AmazonRDSPerformanceInsightsReadOnly")
- [AWS managed policy: AmazonRDSPerformanceInsightsFullAccess](#rds-security-iam-awsmanpol-AmazonRDSPerformanceInsightsFullAccess "#rds-security-iam-awsmanpol-AmazonRDSPerformanceInsightsFullAccess")
- [AWS managed policy: AmazonRDSDirectoryServiceAccess](#rds-security-iam-awsmanpol-AmazonRDSDirectoryServiceAccess "#rds-security-iam-awsmanpol-AmazonRDSDirectoryServiceAccess")
- [AWS managed policy: AmazonRDSServiceRolePolicy](#rds-security-iam-awsmanpol-AmazonRDSServiceRolePolicy "#rds-security-iam-awsmanpol-AmazonRDSServiceRolePolicy")
- [AWS managed policy: AmazonRDSCustomServiceRolePolicy](#rds-security-iam-awsmanpol-AmazonRDSCustomServiceRolePolicy "#rds-security-iam-awsmanpol-AmazonRDSCustomServiceRolePolicy")
- [AWS managed policy:
  AmazonRDSCustomInstanceProfileRolePolicy](#rds-security-iam-awsmanpol-AmazonRDSCustomInstanceProfileRolePolicy "#rds-security-iam-awsmanpol-AmazonRDSCustomInstanceProfileRolePolicy")
- [AWS managed policy: AmazonRDSPreviewServiceRolePolicy](#rds-security-iam-awsmanpol-AmazonRDSPreviewServiceRolePolicy "#rds-security-iam-awsmanpol-AmazonRDSPreviewServiceRolePolicy")
- [AWS managed policy: AmazonRDSBetaServiceRolePolicy](#rds-security-iam-awsmanpol-AmazonRDSBetaServiceRolePolicy "#rds-security-iam-awsmanpol-AmazonRDSBetaServiceRolePolicy")

## AWS managed policy: AmazonRDSReadOnlyAccess

This policy allows read-only access to Amazon RDS through the AWS Management Console.

**Permissions details**

This policy includes the following permissions:

- `rds` – Allows principals to describe Amazon RDS resources and list the tags for Amazon RDS resources.
- `cloudwatch` – Allows principals to get Amazon CloudWatch metric statistics.
- `ec2` – Allows principals to describe Availability Zones and networking resources.
- `logs` – Allows principals to describe CloudWatch Logs log streams of log groups, and get CloudWatch Logs log events.
- `devops-guru` – Allows principals to describe resources that
  have Amazon DevOps Guru coverage, which is specified either by CloudFormation stack names or
  resource tags.

For more information about this policy, including the JSON policy document, see
[AmazonRDSReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonRDSReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonRDSReadOnlyAccess.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AmazonRDSFullAccess

This policy provides full access to Amazon RDS through the AWS Management Console.

**Permissions details**

This policy includes the following permissions:

- `rds` – Allows principals full access to Amazon RDS.
- `application-autoscaling` – Allows principals describe and manage Application Auto Scaling
  scaling targets and policies.
- `cloudwatch` – Allows principals get CloudWatch metric statics and manage
  CloudWatch alarms.
- `ec2` – Allows principals to describe Availability Zones and networking resources.
- `logs` – Allows principals to describe CloudWatch Logs log streams of log groups, and get CloudWatch Logs log events.
- `outposts` – Allows principals to get AWS Outposts instance types.
- `pi` – Allows principals to get Performance Insights metrics.
- `sns` – Allows principals to Amazon Simple Notification Service (Amazon SNS) subscriptions and topics,
  and to publish Amazon SNS messages.
- `devops-guru` – Allows principals to describe resources that
  have Amazon DevOps Guru coverage, which is specified either by CloudFormation stack names or
  resource tags.

For more information about this policy, including the JSON policy document, see
[AmazonRDSFullAccess](../../../aws-managed-policy/latest/reference/AmazonRDSFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonRDSFullAccess.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AmazonRDSDataFullAccess

This policy allows full access to use the Data API and the query editor on
Aurora Serverless clusters in a specific AWS account. This policy allows the
AWS account to get the value of a secret from AWS Secrets Manager.

You can attach the `AmazonRDSDataFullAccess` policy to your IAM identities.

**Permissions details**

This policy includes the following permissions:

- `dbqms` – Allows principals to access, create, delete, describe, and update queries.
  The Database Query Metadata Service (`dbqms`) is an internal-only service. It provides your recent and
  saved queries for the query editor on the AWS Management Console for multiple AWS services, including Amazon RDS.
- `rds-data` – Allows principals to run SQL statements on Aurora Serverless databases.
- `secretsmanager` – Allows principals to get the value of a secret from AWS Secrets Manager.

For more information about this policy, including the JSON policy document, see
[AmazonRDSDataFullAccess](../../../aws-managed-policy/latest/reference/AmazonRDSDataFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonRDSDataFullAccess.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AmazonRDSEnhancedMonitoringRole

This policy provides access to Amazon CloudWatch Logs for Amazon RDS Enhanced Monitoring.

**Permissions details**

This policy includes the following permissions:

- `logs` – Allows principals to create CloudWatch Logs log groups and
  retention policies, and to create and describe CloudWatch Logs log streams of log groups.
  It also allows principals to put and get CloudWatch Logs log events.

For more information about this policy, including the JSON policy document, see
[AmazonRDSEnhancedMonitoringRole](../../../aws-managed-policy/latest/reference/AmazonRDSEnhancedMonitoringRole.md "../../../aws-managed-policy/latest/reference/AmazonRDSEnhancedMonitoringRole.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AmazonRDSPerformanceInsightsReadOnly

This policy provides read-only access to Amazon RDS Performance Insights for Amazon RDS DB instances and Amazon Aurora DB clusters.

This policy now includes `Sid`
(statement ID) as an identifier for the policy statement.

**Permissions details**

This policy includes the following permissions:

- `rds` – Allows principals to describe Amazon RDS DB instances and Amazon Aurora DB clusters.
- `pi` – Allows principals make calls to the Amazon RDS Performance Insights API and access Performance Insights metrics.

For more information about this policy, including the JSON policy document, see
[AmazonRDSPerformanceInsightsReadOnly](../../../aws-managed-policy/latest/reference/AmazonRDSPerformanceInsightsReadOnly.md "../../../aws-managed-policy/latest/reference/AmazonRDSPerformanceInsightsReadOnly.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AmazonRDSPerformanceInsightsFullAccess

This policy provides full access to Amazon RDS Performance Insights for Amazon RDS DB instances
and Amazon Aurora DB clusters.

This policy now includes `Sid`
(statement ID) as an identifier for the policy statement.

**Permissions details**

This policy includes the following permissions:

- `rds` – Allows principals to describe Amazon RDS DB instances and Amazon Aurora DB clusters.
- `pi` – Allows principals make calls to the Amazon RDS Performance Insights API, and create, view, and delete performance analysis reports.
- `cloudwatch` – Allows principals to list all the Amazon CloudWatch metrics, and get metric data and statistics.

For more information about this policy, including the JSON policy document, see
[AmazonRDSPerformanceInsightsFullAccess](../../../aws-managed-policy/latest/reference/AmazonRDSPerformanceInsightsFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonRDSPerformanceInsightsFullAccess.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AmazonRDSDirectoryServiceAccess

This policy allows Amazon RDS to make calls to the AWS Directory Service.

**Permissions details**

This policy includes the following permission:

- `ds` – Allows principals to describe AWS Directory Service directories and control authorization to AWS Directory Service directories.

For more information about this policy, including the JSON policy document, see
[AmazonRDSDirectoryServiceAccess](../../../aws-managed-policy/latest/reference/AmazonRDSDirectoryServiceAccess.md "../../../aws-managed-policy/latest/reference/AmazonRDSDirectoryServiceAccess.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AmazonRDSServiceRolePolicy

You can't attach the `AmazonRDSServiceRolePolicy` policy to your IAM
entities. This policy is attached to a service-linked role that allows Amazon RDS to perform
actions on your behalf. For more information, see [Service-linked role permissions for
Amazon RDS](UsingWithRDS.IAM.md#service-linked-role-permissions "UsingWithRDS.IAM.md#service-linked-role-permissions").

## AWS managed policy: AmazonRDSCustomServiceRolePolicy

You can't attach the `AmazonRDSCustomServiceRolePolicy` policy to your
IAM entities. This policy is attached to a service-linked role that allows Amazon RDS to
call AWS services on behalf of your RDS DB resources.

This policy includes the following permissions:

- `ec2` ‐ Allows RDS Custom to perform backup
  operations on the DB instance that provides point-in-time restore
  capabilities.
- `secretsmanager` ‐ Allows RDS Custom to manage DB instance specific
  secrets created by RDS Custom.
- `cloudwatch` ‐ Allows RDS Custom to upload
  DB instance metrics and logs to CloudWatch through CloudWatch agent.
- `events`, `sqs` ‐ Allows RDS Custom to send and receive
  status information about the DB instance.
- `cloudtrail` ‐ Allows RDS Custom to recieve change events about the DB instance
- `servicequotas` ‐ Allows RDS Custom to read service quotas related to the DB instance
- `ssm` ‐ Allows RDS Custom to manage the DB instance's underlying EC2 instance.
- `rds` ‐ Allows RDS Custom to manage RDS resources for your DB instance
- `iam` ‐ Allows RDS Custom to validate and attach the instance profile to a DB instance's underlying EC2 instance.

For more information about this policy, including the JSON policy document, see
[AmazonRDSCustomServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonRDSCustomServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonRDSCustomServiceRolePolicy.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy:

AmazonRDSCustomInstanceProfileRolePolicy

You shouldn't attach
`AmazonRDSCustomInstanceProfileRolePolicy` to your IAM
entities. It should only be attached to an instance profile role that is used to grant
permissions to your Amazon RDS Custom DB instance to perform various automation actions and
database management tasks. Pass the instance profile as
`custom-iam-instance-profile` parameter during the RDS Custom instance
creation and RDS Custom associates this instance profile to your DB instance.

**Permissions details**

This policy includes the following permissions:

- `ssm`, `ssmmessages`, `ec2messages` ‐
  Allows RDS Custom to communicate, execute automation and maintain agents on the
  DB instance through Systems Manager.
- `ec2`, `s3` ‐ Allows RDS Custom to perform backup
  operations on the DB instance that provides point-in-time restore
  capabilities.
- `secretsmanager` ‐ Allows RDS Custom to manage DB instance specific
  secrets created by RDS Custom.
- `cloudwatch`, `logs` ‐ Allows RDS Custom to upload
  DB instance metrics and logs to CloudWatch through CloudWatch agent.
- `events`, `sqs` ‐ Allows RDS Custom to send and receive
  status information about the DB instance.
- `kms` ‐ Allows RDS Custom to use an instance-specific KMS key to
  perform encryption of secrets and S3 objects that RDS Custom manages.

For more information about this policy, including the JSON policy document, see [AmazonRDSCustomInstanceProfileRolePolicy](../../../aws-managed-policy/latest/reference/AmazonRDSCustomInstanceProfileRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonRDSCustomInstanceProfileRolePolicy.md") in the
_AWS Managed Policy Reference Guide_.

## AWS managed policy: AmazonRDSPreviewServiceRolePolicy

You shouldn't attach
`AmazonRDSPreviewServiceRolePolicy` to your IAM
entities. This policy is attached to a service-linked role that allows Amazon RDS to
call AWS services on behalf of your RDS DB resources. For more information, see
[Service-linked role for Amazon RDS Preview](UsingWithRDS.IAM.md#slr-permissions-rdspreview "UsingWithRDS.IAM.md#slr-permissions-rdspreview").

**Permissions details**

This policy includes the following permissions:

- `ec2` ‐ Allows principals to describe Availability Zones and networking resources.
- `secretsmanager` – Allows principals to get the value of a secret from AWS Secrets Manager.
- `cloudwatch`, `logs` ‐ Allows Amazon RDS to upload
  DB instance metrics and logs to CloudWatch through CloudWatch agent.

For more information about this policy, including the JSON policy document, see
[AmazonRDSPreviewServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonRDSPreviewServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonRDSPreviewServiceRolePolicy.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AmazonRDSBetaServiceRolePolicy

You shouldn't attach `AmazonRDSBetaServiceRolePolicy` to your IAM
entities. This policy is attached to a service-linked role that allows Amazon RDS to
call AWS services on behalf of your RDS DB resources. For more information, see
[Service-linked role permissions for Amazon RDS Beta](UsingWithRDS.IAM.md#slr-permissions-rdsbeta "UsingWithRDS.IAM.md#slr-permissions-rdsbeta").

**Permissions details**

This policy includes the following permissions:

- `ec2` ‐ Allows Amazon RDS to perform backup
  operations on the DB instance that provides point-in-time restore
  capabilities.
- `secretsmanager` ‐ Allows Amazon RDS to manage DB instance specific
  secrets created by Amazon RDS.
- `cloudwatch`, `logs` ‐ Allows Amazon RDS to upload
  DB instance metrics and logs to CloudWatch through CloudWatch agent.

For more information about this policy, including the JSON policy document, see [AmazonRDSBetaServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonRDSBetaServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonRDSBetaServiceRolePolicy.md") in the _AWS Managed Policy Reference Guide_.
