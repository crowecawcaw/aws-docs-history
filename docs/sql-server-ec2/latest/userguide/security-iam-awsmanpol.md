

# AWS managed policies for Microsoft SQL Server on Amazon EC2
<a name="security-iam-awsmanpol"></a>

To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the **ReadOnlyAccess** AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

## AWS managed policy: AWSEC2SqlHaInstancePolicy
<a name="security-iam-awsmanpol-AWSEC2SqlHaInstancePolicy"></a>

You can attach this managed policy to the IAM role that's attached to your Amazon EC2 High Availability for SQL Server instance. The policy grants permissions to execute AWS owned Systems Manager command document **AWSEC2-DetectSqlHaState** to the instance, to retrieve the EC2 SQL HA instance metadata and decide whether it's in active or standby state.

To view the permissions for this policy, see [AWSEC2SqlHaInstancePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSEC2SqlHaInstancePolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSEC2SqlHaServiceRolePolicy
<a name="security-iam-awsmanpol-AWSEC2SqlHaServiceRolePolicy"></a>

This policy is attached to the service-linked role named [**AWSServiceRoleForEC2SqlHa**](slr-sql-ha.md) to allow Amazon EC2 High Availability for SQL Server on EC2 to detect whether an EC2 instance that's tagged with the EC2 SQL High Availability identifier (`SqlHaMonitored` set to `true`) is running in active or standby mode.

To view the permissions for this policy, see [AWSEC2SqlHaServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSEC2SqlHaServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSEC2VssRestorePolicy
<a name="security-iam-awsmanpol-AWSEC2VssRestorePolicy"></a>

You can attach this managed policy to the IAM role that's used to execute the `AWSEC2-RestoreSqlServerDatabaseWithVss` automation runbook. The policy grants permissions to create volumes from VSS snapshots, attach them to instances, and invoke AWS Systems Manager Run Command documents required for database restoration.

**Permissions details**  
This policy includes the following permissions:
+ **ec2** – Allows principals to create volumes from snapshots tagged with `AwsVssConfig`, attach volumes to instances, tag volumes during creation, and describe volumes, snapshots, and instance attributes.
+ **ssm** – Allows principals to describe SSM managed instances, retrieve SSM Run Command documents required for VSS restore operations, send commands to instances, and list command invocations and executions.

To view the permissions for this policy, see [AWSEC2VssRestorePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSEC2VssRestorePolicy.html) in the *AWS Managed Policy Reference*.

## SQL Server on EC2 updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for SQL Server on EC2 since this service began tracking these changes.


| Change | Description | Date | 
| --- | --- | --- | 
| [AWSEC2VssRestorePolicy](#security-iam-awsmanpol-AWSEC2VssRestorePolicy) – New policy | Added the AWSEC2VssRestorePolicy policy that can be attached to the IAM role assumed by the AWSEC2-RestoreSqlServerDatabaseWithVss automation runbook for restoring Microsoft SQL Server databases from VSS snapshots. | March 25, 2026 | 
| [AWSEC2SqlHaInstancePolicy](#security-iam-awsmanpol-AWSEC2SqlHaInstancePolicy) – New policy | Added the AWSEC2SqlHaInstancePolicy policy that can be attached to IAM role that's attached to the Windows and SQL HA instance to facilitate metadata collection for the purpose of keeping track of the current state of the database as it applies to active or passive mode. | November 17, 2025 | 
| [AWSEC2SqlHaServiceRolePolicy](#security-iam-awsmanpol-AWSEC2SqlHaServiceRolePolicy) – New policy | Added the policy that's attached to the AWSServiceRoleForEC2SqlHa service-linked role to detect whether an EC2 instance that's tagged with the EC2 SQL High Availability identifier is running in standby or passive mode. | November 17, 2025 | 
| SQL Server on EC2 started tracking changes | SQL Server on EC2 started tracking changes to its AWS managed policies | November 17, 2025 | 