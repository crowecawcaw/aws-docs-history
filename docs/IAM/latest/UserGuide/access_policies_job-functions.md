# AWS managed policies for job functions

We recommend using policies that [grant least
privilege](best-practices.md#grant-least-privilege "best-practices.md#grant-least-privilege"), or granting only the permissions required to perform a task. The most secure
way to grant least privilege is to write a custom policy with only the permissions needed by
your team. You must create a process to allow your team to request more permissions when
necessary. It takes time and expertise to [create
IAM customer managed policies](access_policies_create-console.md "access_policies_create-console.md") that provide your team with only the permissions they
need.

To get started adding permissions to your IAM identities (users, groups of users, and
roles), you can use [AWS managed policies](access_policies_managed-vs-inline.md#aws-managed-policies "access_policies_managed-vs-inline.md#aws-managed-policies").
AWS managed policies cover common use cases and are available in your AWS account. AWS
managed policies don't grant least privilege permissions. You must consider the security risk of
granting your principals more permissions than they need to do their job.

You can attach AWS managed policies, including job functions, to any IAM identity. To
switch to least privilege permissions, you can run AWS Identity and Access Management and Access Analyzer to monitor principals with
AWS managed policies. After learning which permissions they are using, then you can write a
custom policy or generate a policy with only the required permissions for your team. This is
less secure, but provides more flexibility as you learn how your team is using AWS.

AWS managed policies for job functions are designed to closely align to common job
functions in the IT industry. You can use these policies to grant the permissions needed to
carry out the tasks expected of someone in a specific job function. These policies consolidate
permissions for many services into a single policy that's easier to work with than having
permissions scattered across many policies.

###### Use Roles to Combine Services

Some of the policies use IAM service roles to help you take advantage of features found
in other AWS services. These policies grant access to `iam:passrole`, which
allows a user with the policy to pass a role to an AWS service. This role delegates IAM
permissions to the AWS service to carry out actions on your behalf.

You must create the roles according to your needs. For example, the Network Administrator
policy allows a user with the policy to pass a role named "flow-logs-vpc" to the Amazon CloudWatch
service. CloudWatch uses that role to log and capture IP traffic for VPCs created by the user.

To follow security best practices, the policies for job functions include filters that limit
the names of valid roles that can be passed. This helps avoid granting unnecessary permissions.
If your users do require the optional service roles, you must create a role that follows the
naming convention specified in the policy. You then grant permissions to the role. Once that is
done, the user can configure the service to use the role, granting it whatever permissions the
role provides.

In the following sections, each policy's name is a link to the policy details page in the
AWS Management Console. There you can see the policy document and review the permissions it grants.

## Administrator job function

**AWS managed policy name:**
[AdministratorAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AdministratorAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AdministratorAccess")

**Use case:** This user has full access and can delegate
permissions to every service and resource in AWS.

**Policy updates:** AWS maintains and updates this policy.
For a history of changes for this policy, view the policy in the IAM console and then choose
the **Policy versions** tab. For more information about job function policy
updates, see [Updates to AWS managed policies
for job functions](#security-iam-awsmanpol-jobfunction-updates "#security-iam-awsmanpol-jobfunction-updates").

**Policy description:** This policy grants all actions for
all AWS services and for all resources in the account. For more information about the
managed policy, see [AdministratorAccess](../../../aws-managed-policy/latest/reference/AdministratorAccess.md "../../../aws-managed-policy/latest/reference/AdministratorAccess.md") in _AWS Managed Policy Reference
Guide_.

###### Note

Before an IAM user or role can access the AWS Billing and Cost Management console with the permissions in
this policy, you must first activate IAM user and role access. To do this, follow the
instructions in [Grant access to the billing
console](getting-started-account-iam.md "getting-started-account-iam.md") to delegate access to the billing console.

## Billing job function

**AWS managed policy name:**
[Billing](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/job-function/Billing "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/job-function/Billing")

**Use case:** This user needs to view billing information,
set up payments, and authorize payments. The user can monitor the costs accumulated for the
entire AWS service.

**Policy updates:** AWS maintains and updates this policy.
For a history of changes for this policy, view the policy in the IAM console and then choose
the **Policy versions** tab. For more information about job function policy
updates, see [Updates to AWS managed policies
for job functions](#security-iam-awsmanpol-jobfunction-updates "#security-iam-awsmanpol-jobfunction-updates").

**Policy description:** This policy grants full permissions
for managing billing, costs, payment methods, budgets, and reports. For additional cost
management policy examples, see [AWS Billing policy
examples](../../../awsaccountbilling/latest/aboutv2/billing-example-policies.md "../../../awsaccountbilling/latest/aboutv2/billing-example-policies.md") in the _AWS Billing and Cost Management User Guide_. For more information about
the managed policy, see [Billing](../../../aws-managed-policy/latest/reference/Billing.md "../../../aws-managed-policy/latest/reference/Billing.md") in _AWS
Managed Policy Reference Guide_.

###### Note

Before an IAM user or role can access the AWS Billing and Cost Management console with the permissions in
this policy, you must first activate IAM user and role access. To do this, follow the
instructions in [Grant access to the billing
console](getting-started-account-iam.md "getting-started-account-iam.md") to delegate access to the billing console.

## Database administrator job function

**AWS managed policy name:**
[DatabaseAdministrator](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/job-function/DatabaseAdministrator "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/job-function/DatabaseAdministrator")

**Use case:** This user sets up, configures, and maintains
databases in the AWS Cloud.

**Policy updates:** AWS maintains and updates this policy.
For a history of changes for this policy, view the policy in the IAM console and then choose
the **Policy versions** tab. For more information about job function policy
updates, see [Updates to AWS managed policies
for job functions](#security-iam-awsmanpol-jobfunction-updates "#security-iam-awsmanpol-jobfunction-updates").

**Policy description:** This policy grants permissions to
create, configure, and maintain databases. It includes access to AWS database services, such
as Amazon DynamoDB, Amazon Relational Database Service (RDS), and Amazon Redshift. View the policy for the full list of database
services that this policy supports. For more information about the managed policy, see [DatabaseAdministrator](../../../aws-managed-policy/latest/reference/DatabaseAdministrator.md "../../../aws-managed-policy/latest/reference/DatabaseAdministrator.md") in _AWS Managed Policy Reference
Guide_.

This job function policy supports the ability to pass roles to AWS services. The policy
allows the `iam:PassRole` action for only those roles named in the following table.
For more information, see [Creating roles and attaching
policies (console)](access_policies_job-functions_create-policies.md "access_policies_job-functions_create-policies.md") later in this topic.

| Use case                                                                                | Role name (\<br>• is a wildcard)                                                                                                                                                                                                                           | Service role type to select                                                                                                                                                                                        | Select this AWS managed policy                                                                                                                                                                                                                                                      |
| --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Allow the user to monitor RDS databases                                                 | [rds-monitoring-role](../../../AmazonRDS/latest/UserGuide/USER_Monitoring.md "../../../AmazonRDS/latest/UserGuide/USER_Monitoring.md")                                                                                                                     | Amazon RDS Role for Enhanced Monitoring                                                                                                                                                                            | [AmazonRDSEnhancedMonitoringRole](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonRDSEnhancedMonitoringRole "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonRDSEnhancedMonitoringRole")    |
| Allow AWS Lambda to monitor your database and access external databases                 | [rdbms-lambda-access](https://aws.amazon.com/blogs/big-data/from-sql-to-microservices-integrating-aws-lambda-with-relational-databases "https://aws.amazon.com/blogs/big-data/from-sql-to-microservices-integrating-aws-lambda-with-relational-databases") | Amazon EC2                                                                                                                                                                                                         | [AWSLambda_FullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSLambda_FullAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSLambda_FullAccess")                                                               |
| Allow Lambda to upload files to Amazon S3 and to Amazon Redshift clusters with DynamoDB | [lambda_exec_role](https://aws.amazon.com/blogs/big-data/a-zero-administration-amazon-redshift-database-loader "https://aws.amazon.com/blogs/big-data/a-zero-administration-amazon-redshift-database-loader")                                              | AWS Lambda                                                                                                                                                                                                         | Create a new managed policy as defined in the [AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/a-zero-administration-amazon-redshift-database-loader "https://aws.amazon.com/blogs/big-data/a-zero-administration-amazon-redshift-database-loader")                        |
| Allow Lambda functions to act as triggers for your DynamoDB tables                      | [lambda-dynamodb-\*](../../../lambda/latest/dg/with-ddb.md "../../../lambda/latest/dg/with-ddb.md")                                                                                                                                                        | AWS Lambda                                                                                                                                                                                                         | [AWSLambdaDynamoDBExecutionRole](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AWSLambdaDynamoDBExecutionRole "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AWSLambdaDynamoDBExecutionRole")       |
| Allow Lambda functions to access Amazon RDS in a VPC                                    | [lambda-vpc-execution-role](../../../lambda/latest/dg/vpc-rds.md "../../../lambda/latest/dg/vpc-rds.md")                                                                                                                                                   | Create a role with a trust policy as defined in the [AWS Lambda Developer Guide](../../../lambda/latest/dg/vpc-rds.md "../../../lambda/latest/dg/vpc-rds.md")                                                      | [AWSLambdaVPCAccessExecutionRole](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole")    |
| Allow AWS Data Pipeline to access your AWS resources                                    | [DataPipelineDefaultRole](../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md "../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md")                                                                                                       | Create a role with a trust policy as defined in the [AWS Data Pipeline Developer Guide](../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md "../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md") | The AWS Data Pipeline documentation lists the required permissions for this use case. See<br>[IAM roles for AWS Data Pipeline](../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md "../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md")                           |
| Allow your applications running on Amazon EC2 instances to access your AWS<br>resources | [DataPipelineDefaultResourceRole](../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md "../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md")                                                                                               | Create a role with a trust policy as defined in the [AWS Data Pipeline Developer Guide](../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md "../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md") | [AmazonEC2RoleforDataPipelineRole](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforDataPipelineRole "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforDataPipelineRole") |

## Data scientist job function

**AWS managed policy name:**
[DataScientist](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/job-function/DataScientist "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/job-function/DataScientist")

**Use case:** This user runs Hadoop jobs and queries. The
user also accesses and analyzes information for data analytics and business
intelligence.

**Policy updates:** AWS maintains and updates this policy.
For a history of changes for this policy, view the policy in the IAM console and then choose
the **Policy versions** tab. For more information about job function policy
updates, see [Updates to AWS managed policies
for job functions](#security-iam-awsmanpol-jobfunction-updates "#security-iam-awsmanpol-jobfunction-updates").

**Policy description:** This policy grants permissions to
create, manage, and run queries on an Amazon EMR cluster and perform data analytics with tools such
as Amazon QuickSight. The policy includes access to additional data scientist services, such
as AWS Data Pipeline, Amazon EC2, Amazon Kinesis, Amazon Machine Learning, and SageMaker AI. View the policy for the full list of data
scientist services that this policy supports. For more information about the managed policy,
see [DataScientist](../../../aws-managed-policy/latest/reference/DataScientist.md "../../../aws-managed-policy/latest/reference/DataScientist.md") in _AWS Managed Policy Reference Guide_.

This job function policy supports the ability to pass roles to AWS services. One
statement allows passing any role to SageMaker AI. Another statement allows the
`iam:PassRole` action for only those roles named in the following table. For more
information, see [Creating roles and attaching
policies (console)](access_policies_job-functions_create-policies.md "access_policies_job-functions_create-policies.md") later in this topic.

| Use case                                                                                | Role name (\<br>• is a wildcard)                                                                                                                                                                        | Service role type to select                                                                                                                                                                                                                                         | AWS managed policy to select                                                                                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Allow Amazon EC2 instances access to services and resources suitable for<br>clusters    | [EMR-EC2_DefaultRole](../../../emr/latest/DeveloperGuide/emr-iam-roles-defaultroles.md "../../../emr/latest/DeveloperGuide/emr-iam-roles-defaultroles.md")                                              | Amazon EMR for EC2                                                                                                                                                                                                                                                  | [AmazonElasticMapReduceforEC2Role](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role")        |
| Allow Amazon EMR access to access the Amazon EC2 service and resources for clusters     | [EMR_DefaultRole](../../../emr/latest/DeveloperGuide/emr-iam-roles-defaultroles.md "../../../emr/latest/DeveloperGuide/emr-iam-roles-defaultroles.md")                                                  | Amazon EMR                                                                                                                                                                                                                                                          | [AmazonEMRServicePolicy_v2](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonEMRServicePolicy_v2 "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonEMRServicePolicy_v2")                             |
| Allow Kinesis Managed Service for Apache Flink to access streaming data sources         | [kinesis-\*](https://aws.amazon.com/blogs/big-data/a-zero-administration-amazon-redshift-database-loader "https://aws.amazon.com/blogs/big-data/a-zero-administration-amazon-redshift-database-loader") | Create a role with a trust policy as defined in the [AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/a-zero-administration-amazon-redshift-database-loader "https://aws.amazon.com/blogs/big-data/a-zero-administration-amazon-redshift-database-loader"). | See the [AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/a-zero-administration-amazon-redshift-database-loader "https://aws.amazon.com/blogs/big-data/a-zero-administration-amazon-redshift-database-loader"), which outlines four possible options depending on your<br>use case |
| Allow AWS Data Pipeline to access your AWS resources                                    | [DataPipelineDefaultRole](../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md "../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md")                                                    | Create a role with a trust policy as defined in the [AWS Data Pipeline Developer Guide](../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md "../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md")                                                  | The AWS Data Pipeline documentation lists the required permissions for this use case. See<br>[IAM roles for AWS Data Pipeline](../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md "../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md")                                  |
| Allow your applications running on Amazon EC2 instances to access your AWS<br>resources | [DataPipelineDefaultResourceRole](../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md "../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md")                                            | Create a role with a trust policy as defined in the [AWS Data Pipeline Developer Guide](../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md "../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md")                                                  | [AmazonEC2RoleforDataPipelineRole](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforDataPipelineRole "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforDataPipelineRole")        |

## Developer power user job function

**AWS managed policy name:**
[PowerUserAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/PowerUserAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/PowerUserAccess")

**Use case:** This user performs application development
tasks and can create and configure resources and services that support AWS aware application
development.

**Policy updates:** AWS maintains and updates this policy.
For a history of changes for this policy, view the policy in the IAM console and then choose
the **Policy versions** tab. For more information about job function policy
updates, see [Updates to AWS managed policies
for job functions](#security-iam-awsmanpol-jobfunction-updates "#security-iam-awsmanpol-jobfunction-updates").

**Policy description:** The first statement of this policy
uses the [NotAction](reference_policies_elements_notaction.md "reference_policies_elements_notaction.md")
element to allow all actions for all AWS services and for all resources except AWS Identity and Access Management,
AWS Organizations, and AWS Account Management. The second statement grants IAM permissions to create a
service-linked role. This is required by some services that must access resources in another
service, such as an Amazon S3 bucket. It also grants AWS Organizations permissions to view information about
the user's organization, including the management account email and organization limitations.
Although this policy limits IAM, AWS Organizations, it allows the user to perform all IAM Identity Center actions
if IAM Identity Center is enabled. It also grants Account Management permissions to view which AWS Regions are enabled
or disabled for the account.

## Network administrator job function

**AWS managed policy name:**
[NetworkAdministrator](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/job-function/NetworkAdministrator "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/job-function/NetworkAdministrator")

**Use case:** This user is tasked with setting up and
maintaining AWS network resources.

**Policy updates:** AWS maintains and updates this policy.
For a history of changes for this policy, view the policy in the IAM console and then choose
the **Policy versions** tab. For more information about job function policy
updates, see [Updates to AWS managed policies
for job functions](#security-iam-awsmanpol-jobfunction-updates "#security-iam-awsmanpol-jobfunction-updates").

**Policy description:** This policy grants permissions to
create and maintain network resources in Amazon EC2 Auto Scaling, Amazon EC2, AWS Direct Connect, Route 53, Amazon CloudFront,
Elastic Load Balancing, AWS Elastic Beanstalk, Amazon SNS, CloudWatch, CloudWatch Logs, Amazon S3, IAM, and Amazon Virtual Private Cloud. For more information
about the managed policy, see [NetworkAdministrator](../../../aws-managed-policy/latest/reference/NetworkAdministrator.md "../../../aws-managed-policy/latest/reference/NetworkAdministrator.md") in _AWS Managed Policy Reference
Guide_.

This job function requires the ability to pass roles to AWS services. The policy grants
`iam:GetRole` and `iam:PassRole` for only those roles named in the
following table. For more information, see [Creating roles and attaching
policies (console)](access_policies_job-functions_create-policies.md "access_policies_job-functions_create-policies.md") later in this topic.

| Use case                                                                                                                                  | Role name (\<br>• is a wildcard)                                                                                                    | Service role type to select                                                                                                                                                                      | AWS managed policy to select                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Allows Amazon VPC to create and manage logs in CloudWatch Logs on the user's behalf to monitor<br>IP traffic going in and out of your VPC | [flow-logs-\*](../../../vpc/latest/userguide/flow-logs.md#flow-logs-iam "../../../vpc/latest/userguide/flow-logs.md#flow-logs-iam") | Create a role with a trust policy as defined in the [Amazon VPC User Guide](../../../vpc/latest/userguide/flow-logs.md#flow-logs-iam "../../../vpc/latest/userguide/flow-logs.md#flow-logs-iam") | This use case does not have an existing AWS managed policy, but the<br>documentation lists the required permissions. See [Amazon VPC User Guide](../../../vpc/latest/userguide/flow-logs.md#flow-logs-iam "../../../vpc/latest/userguide/flow-logs.md#flow-logs-iam"). |

## Read-only access

**AWS managed policy name:**
[ReadOnlyAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/ReadOnlyAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/ReadOnlyAccess")

**Use case:** This user requires read-only access to every
resource in an AWS account.

###### Important

This user will also have access to read data in storage services like Amazon S3 buckets and
Amazon DynamoDB tables.

**Policy updates:** AWS maintains and updates this policy.
For a history of changes for this policy, view the policy in the IAM console and then choose
the **Policy versions** tab. For more information about job function policy
updates, see [Updates to AWS managed policies
for job functions](#security-iam-awsmanpol-jobfunction-updates "#security-iam-awsmanpol-jobfunction-updates").

**Policy description:** This policy grants permissions to
list, get, describe, and otherwise view resources and their attributes. It does not include
mutating functions like create or delete. This policy does include read-only access to
security-related AWS services, such as AWS Identity and Access Management and AWS Billing and Cost Management. View the policy for the full
list of services and actions that this policy supports. For more information about the managed
policy, see [ReadOnlyAccess](../../../aws-managed-policy/latest/reference/ReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/ReadOnlyAccess.md") in
_AWS Managed Policy Reference Guide_. If you need a similar policy that
does not grant access to read data in storage services, see [View-only user job function](#jf_view-only-user "#jf_view-only-user").

## MCP service actions full access

**AWS managed policy name:**
[AWSMcpServiceActionsFullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSMcpServiceActionsFullAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSMcpServiceActionsFullAccess")

**Use case:** This user requires access to AWS services
using AWS MCP servers. This policy does not grant access to actions taken by an MCP service
to other AWS services.

**Policy updates:** AWS maintains and updates this policy.
For a history of changes for this policy, view the policy in the IAM console and then choose
the **Policy versions** tab. For more information about job function policy
updates, see [Updates to AWS managed policies
for job functions](#security-iam-awsmanpol-jobfunction-updates "#security-iam-awsmanpol-jobfunction-updates").

**Policy description:** This policy grants permissions to
call any AWS MCP service action. You can use when you do not need to specify permissions
per AWS MCP service. It does not grant permissions to actions taken by the MCP service to
other AWS services, those permissions must always be granted separately and in addition to
MCP service actions. For more information about the managed policy, see [AWSMcpServiceActionsFullAccess](../../../aws-managed-policy/latest/reference/AWSMcpServiceActionsFullAccess.md "../../../aws-managed-policy/latest/reference/AWSMcpServiceActionsFullAccess.md") in _AWS Managed Policy Reference
Guide_.

## Security auditor job function

**AWS managed policy name:**
[SecurityAudit](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/SecurityAudit "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/SecurityAudit")

**Use case:** This user monitors accounts for compliance with
security requirements. This user can access logs and events to investigate potential security
breaches or potential malicious activity.

**Policy updates:** AWS maintains and updates this policy.
For a history of changes for this policy, view the policy in the IAM console and then choose
the **Policy versions** tab. For more information about job function policy
updates, see [Updates to AWS managed policies
for job functions](#security-iam-awsmanpol-jobfunction-updates "#security-iam-awsmanpol-jobfunction-updates").

**Policy description:** This policy grants permissions to
view configuration data for many AWS services and to review their logs. For more information
about the managed policy, see [SecurityAudit](../../../aws-managed-policy/latest/reference/SecurityAudit.md "../../../aws-managed-policy/latest/reference/SecurityAudit.md") in
_AWS Managed Policy Reference Guide_.

## Support user job function

**AWS managed policy name:**
[AWSSupportAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSSupportAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSSupportAccess")

**Use case:** This user contacts AWS Support, creates
support cases, and views the status of existing cases.

**Policy updates:** AWS maintains and updates this policy.
For a history of changes for this policy, view the policy in the IAM console and then choose
the **Policy versions** tab. For more information about job function policy
updates, see [Updates to AWS managed policies
for job functions](#security-iam-awsmanpol-jobfunction-updates "#security-iam-awsmanpol-jobfunction-updates").

**Policy description:** This policy grants permissions to
create and update Support cases. For more information about the managed policy, see [AWSSupportAccess](../../../aws-managed-policy/latest/reference/AWSSupportAccess.md "../../../aws-managed-policy/latest/reference/AWSSupportAccess.md") in _AWS Managed Policy Reference
Guide_.

## System administrator job function

**AWS managed policy name:**
[SystemAdministrator](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/job-function/SystemAdministrator "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/job-function/SystemAdministrator")

**Use case:** This user sets up and maintains resources for
development operations.

**Policy updates:** AWS maintains and updates this policy.
For a history of changes for this policy, view the policy in the IAM console and then choose
the **Policy versions** tab. For more information about job function policy
updates, see [Updates to AWS managed policies
for job functions](#security-iam-awsmanpol-jobfunction-updates "#security-iam-awsmanpol-jobfunction-updates").

**Policy description:** This policy grants permissions to
create and maintain resources across a large variety of AWS services, including AWS CloudTrail,
Amazon CloudWatch, AWS CodeCommit, AWS CodeDeploy, AWS Config, AWS Directory Service, Amazon EC2, AWS Identity and Access Management, AWS Key Management Service, AWS Lambda,
Amazon RDS, Route 53, Amazon S3, Amazon SES, Amazon SQS, AWS Trusted Advisor, and Amazon VPC. For more information about the
managed policy, see [SystemAdministrator](../../../aws-managed-policy/latest/reference/SystemAdministrator.md "../../../aws-managed-policy/latest/reference/SystemAdministrator.md") in _AWS Managed Policy Reference
Guide_.

This job function requires the ability to pass roles to AWS services. The policy grants
`iam:GetRole` and `iam:PassRole` for only those roles named in the
following table. For more information, see [Creating roles and attaching
policies (console)](access_policies_job-functions_create-policies.md "access_policies_job-functions_create-policies.md") later in this topic. For
more information about job function policy updates, see [Updates to AWS managed policies
for job functions](#security-iam-awsmanpol-jobfunction-updates "#security-iam-awsmanpol-jobfunction-updates").

| Use case                                                                          | Role name (\<br>• is a wildcard)                                                                                                                 | Service role type to select               | AWS managed policy to select                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Allow apps running in EC2 instances in an Amazon ECS cluster to access Amazon ECS | [ecr-sysadmin-\*](../../../AmazonECS/latest/developerguide/instance_IAM_role.md "../../../AmazonECS/latest/developerguide/instance_IAM_role.md") | Amazon EC2 Role for EC2 Container Service | [AmazonEC2ContainerServiceforEC2Role](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role") |
| Allow a user to monitor databases                                                 | [rds-monitoring-role](../../../AmazonRDS/latest/UserGuide/USER_Monitoring.md "../../../AmazonRDS/latest/UserGuide/USER_Monitoring.md")           | Amazon RDS Role for Enhanced Monitoring   | [AmazonRDSEnhancedMonitoringRole](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonRDSEnhancedMonitoringRole "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonRDSEnhancedMonitoringRole")             |
| Allow apps running in EC2 instances to access AWS resources.                      | [ec2-sysadmin-\*](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md")   | Amazon EC2                                | Sample policy for role that grants access to an S3 bucket as shown in the [Amazon EC2 User Guide](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md");<br>customize as needed                                       |
| Allow Lambda to read DynamoDB streams and write to CloudWatch Logs                | [lambda-sysadmin-\*](../../../lambda/latest/dg/with-ddb.md "../../../lambda/latest/dg/with-ddb.md")                                              | AWS Lambda                                | [AWSLambdaDynamoDBExecutionRole](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AWSLambdaDynamoDBExecutionRole "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AWSLambdaDynamoDBExecutionRole")                |

## View-only user job function

**AWS managed policy name:**
[ViewOnlyAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/job-function/ViewOnlyAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/job-function/ViewOnlyAccess")

**Use case:** This user can view a list of AWS resources
and basic metadata in the account across services. The user cannot read resource content or
metadata that goes beyond the quota and list information for resources.

**Policy updates:** AWS maintains and updates this policy.
For a history of changes for this policy, view the policy in the IAM console and then choose
the **Policy versions** tab. For more information about job function policy
updates, see [Updates to AWS managed policies
for job functions](#security-iam-awsmanpol-jobfunction-updates "#security-iam-awsmanpol-jobfunction-updates").

**Policy description:** This policy grants
`List*`, `Describe*`, `Get*`, `View*`, and
`Lookup*` access to resources for AWS services. To see what actions this policy
includes for each service, see [ViewOnlyAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/job-function/ViewOnlyAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/job-function/ViewOnlyAccess"). For more information about the managed policy, see [ViewOnlyAccess](../../../aws-managed-policy/latest/reference/ViewOnlyAccess.md "../../../aws-managed-policy/latest/reference/ViewOnlyAccess.md") in _AWS Managed Policy Reference Guide_.

## Updates to AWS managed policies

for job functions

These policies are all maintained by AWS and are kept up to date to include support for
new services and new capabilities as they are added by AWS services. These policies cannot
be modified by customers. You can make a copy of the policy and then modify the copy, but that
copy is not automatically updated as AWS introduces new services and API operations.

For a job function policy, you can view the version history and the time and date of each
update in the IAM console. To do this, use the links on this page to view the policy
details. Then choose the **Policy versions** tab to view the versions. This
page shows the last 25 versions of a policy. To view all of the versions for a policy, call
the [get-policy-version](../../../cli/latest/reference/iam/get-policy-version.md "../../../cli/latest/reference/iam/get-policy-version.md") AWS CLI command or the [GetPolicyVersion](../APIReference/API_GetPolicyVersion.md "../APIReference/API_GetPolicyVersion.md") API operation.

###### Note

You can have up to five versions of a customer managed policy, but AWS retains the
full version history of AWS managed policies.
