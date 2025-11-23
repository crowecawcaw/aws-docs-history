# AWS managed policies for SQL Server on EC2

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed policy: AWSEC2SqlHaInstancePolicy

You can attach this managed policy to the IAM role that's attached to your Amazon EC2 Windows
and SQL Server instance. The policy grants permissions to execute AWS owned Systems Manager
command document **AWSEC2-DetectSqlHaState** to the instance,
to retrieve the EC2 SQL Server instance metadata and decide whether it's in active or standby
state.

To view the permissions for this policy, see [AWSEC2SqlHaInstancePolicy](../../../aws-managed-policy/latest/reference/AWSEC2SqlHaInstancePolicy.md "../../../aws-managed-policy/latest/reference/AWSEC2SqlHaInstancePolicy.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AWSEC2SqlHaServiceRolePolicy

This policy is attached to the service-linked role named **AWSServiceRoleForEC2SqlHa**
to allow SQL Server on EC2 to detect whether an EC2 instance that's tagged with the EC2 SQL High Availability identifier
(`SqlHaMonitored` set to `true`) is running in active or standby mode.

To view the permissions for this policy, see [AWSEC2SqlHaServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSEC2SqlHaServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSEC2SqlHaServiceRolePolicy.md") in the _AWS Managed Policy Reference_.

## SQL Server on EC2 updates to AWS managed policies

View details about updates to AWS managed policies for SQL Server on EC2 since this service
began tracking these changes.

| Change                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                           | Date              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AWSEC2SqlHaInstancePolicy](#security-iam-awsmanpol-AWSEC2SqlHaInstancePolicy "#security-iam-awsmanpol-AWSEC2SqlHaInstancePolicy") –<br>New policy          | Added the \*_AWSEC2SqlHaInstancePolicy_<br>• policy that can be attached<br>to IAM role that's attached to the Windows and SQL Server instance to facilitate metadata collection for<br>the purpose of keeping track of the current state of the database as it applies to active or passive<br>mode. | November 17, 2025 |
| [AWSEC2SqlHaServiceRolePolicy](#security-iam-awsmanpol-AWSEC2SqlHaServiceRolePolicy "#security-iam-awsmanpol-AWSEC2SqlHaServiceRolePolicy") –<br>New policy | Added the policy that's attached to the **AWSServiceRoleForEC2SqlHa**<br>service-linked role to detect whether an EC2 instance that's tagged with the EC2 SQL High Availability<br>identifier is running in standby or passive mode.                                                                  | November 17, 2025 |
| SQL Server on EC2 started tracking changes                                                                                                                  | SQL Server on EC2 started tracking changes to its AWS managed policies                                                                                                                                                                                                                                | November 17, 2025 |
