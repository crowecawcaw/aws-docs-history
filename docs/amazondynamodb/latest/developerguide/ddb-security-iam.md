# AWS managed policies for Amazon DynamoDB

DynamoDB uses AWS managed policies to define a set of permissions the service needs to perform specific actions.
DynamoDB maintains and updates its AWS managed policies. You can't change the permissions in AWS managed policies.
For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the IAM User Guide.

DynamoDB may occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects
all identities (users, groups, and roles) where the policy is attached. An AWS managed policy is most likely to be updated when a
new feature is launched or when new operations become available. DynamoDB will not remove permissions from an AWS managed policy,
so policy updates won't break your existing permissions. For a full list of AWS managed
policies, see [AWS
managed policies](../../../aws-managed-policy/latest/reference/policy-list.md "../../../aws-managed-policy/latest/reference/policy-list.md").

## AWS managed policy: DynamoDBReplicationServiceRolePolicy

You can’t attach the `DynamoDBReplicationServiceRolePolicy` policy to your IAM entities.
This policy is attached to a service-linked
role that allows DynamoDB to perform actions on your behalf. For more information, see
[Using IAM with global tables.](globaltables-security.md "globaltables-security.md")

This policy grants permissions that allow the service-linked role to perform data replication between global table replicas.
It also grants administrative permissions to manage global table replicas on your behalf.

**Permissions details**

This policy grants permissions to do the following:

- `dynamodb` – Perform data replication and manage table replicas.
- `application-autoscaling` – Retrieve and manage table Auto Scaling settings
- `account` – Retrieve region status for evaluating replica accessibility.
- `iam` – To create the service-linked role for application Auto Scaling in the event that the service-linked role does not already exist.

The definition of this managed policy can be found
[here](../../../aws-managed-policy/latest/reference/DynamoDBReplicationServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/DynamoDBReplicationServiceRolePolicy.md").

## AWS managed policy: AmazonDynamoDBFullAccess_v2

The scoped-down `AmazonDynamoDBFullAccess_v2` policy grants specific access privileges to users. You can attach the `AmazonDynamoDBFullAccess_v2` policy to your IAM identities. This policy grants administrative access to Amazon DynamoDB resources and grants an IAM identity (such as a user, group, or role) access to the AWS services that DynamoDB is integrated with to use all of DynamoDB features. Using this policy allows access to all of DynamoDB features that are available in the AWS Management Console.

**Permissions details**

This policy includes the following permissions:

- `Amazon DynamoDB`
- `DynamoDB Accelerator`
- `AWS KMS`
- `AWS Resource Groups Tagging`
- `Lambda`
- `Application Auto Scaling`
- `CloudWatch`
- `Amazon Kinesis`
- `Amazon EC2`
- `IAM`

To review the policy in `JSON` format, see [AmazonDynamoDBFullAccess_v2](../../../aws-managed-policy/latest/reference/AmazonDynamoDBFullAccess_v2.md "../../../aws-managed-policy/latest/reference/AmazonDynamoDBFullAccess_v2.md").

## AWS managed policy: AmazonDynamoDBReadOnlyAccess

You can attach the `AmazonDynamoDBReadOnlyAccess` policy to your IAM identities.

This policy grants read-only access to Amazon DynamoDB.

**Permissions details**

This policy includes the following permissions:

- `Amazon DynamoDB` – Provides read-only access to Amazon DynamoDB.
- `Amazon DynamoDB Accelerator (DAX)` – Provides read-only access to Amazon DynamoDB Accelerator (DAX).
- `Application Auto Scaling` – Allows principals to view configurations from Application Auto Scaling. This is required so that users can view automatic scaling policies that are attached to a table.
- `CloudWatch` – Allows principals to view metric data and alarms configured in CloudWatch. This is required so users can view the billable table size and CloudWatch alarms that have been configured for a table.
- `AWS Data Pipeline` – Allows principals to view AWS Data Pipeline and associated objects.
- `Amazon EC2` – Allows principals to view Amazon EC2 VPCs, subnets, and security groups.
- `IAM` – Allows principals to view IAM roles.
- `AWS KMS` – Allows principals to view keys configured in AWS KMS. This is required so users can view AWS KMS keys that they create and manage in their account.
- `Amazon SNS` – Allows principals to list Amazon SNS topics and subscriptions by topic.
- `AWS Resource Groups` – Allows principals to view resource groups and their queries.
- `AWS Resource Groups Tagging` – Allows principals to list all the tagged or previously tagged resources in a Region.
- `Kinesis` – Allows principals to view Kinesis data streams descriptions.
- `Amazon CloudWatch Contributor Insights` – Allow principals to view time series data collected by Contributor Insights rules.

To review the policy in `JSON` format, see [AmazonDynamoDBReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonDynamoDBReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonDynamoDBReadOnlyAccess.md").

## DynamoDB updates to AWS managed policies

This table shows updates to the AWS access management policies for DynamoDB.

| Change                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                  | Date Changed      |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `AmazonDynamoDBFullAccess` – Deprecated                                  | This policy has been replaced by a scoped-down policy named `AmazonDynamoDBFullAccess_v2`. After **April, 2025**, you can't attach the `AmazonDynamoDBFullAccess` policy to any new users, groups, or roles. For more information, see [AWS managed policy: AmazonDynamoDBFullAccess_v2](#ddb-security-iam.awsmanpol.fullaccesspolicy-v2 "#ddb-security-iam.awsmanpol.fullaccesspolicy-v2"). | April 28, 2025    |
| `AmazonDynamoDBReadOnlyAccess` update to an existing policy              | `AmazonDynamoDBReadOnlyAccess` added the permissions: `dynamodb:GetAbacStatus` and `dynamodb:UpdateAbacStatus`. These permissions allow you to view the ABAC status and enable ABAC for your AWS account in the current Region.                                                                                                                                                              | November 18, 2024 |
| `AmazonDynamoDBReadOnlyAccess` update to an existing policy              | `AmazonDynamoDBReadOnlyAccess` added the permission `dynamodb:GetResourcePolicy`. This permission provides access to read resource-based policies attached to DynamoDB resources.                                                                                                                                                                                                            | March 20, 2024    |
| `DynamoDBReplicationServiceRolePolicy` update to an existing policy      | `DynamoDBReplicationServiceRolePolicy` added the permission `dynamodb:GetResourcePolicy`. This permission allows the service-linked role to read resource-based policies attached to DynamoDB resources.                                                                                                                                                                                     | December 15, 2023 |
| `DynamoDBReplicationServiceRolePolicy` update to an existing policy      | `DynamoDBReplicationServiceRolePolicy` added the permission `account:ListRegions`. This permission allows the service-linked role to evaluate replica accessibility                                                                                                                                                                                                                          | May 10, 2023      |
| `DynamoDBReplicationServiceRolePolicy` added to list of managed policies | Added information about the managed policy `DynamoDBReplicationServiceRolePolicy`, which is used by the DynamoDB global tables service-linked role.                                                                                                                                                                                                                                          | May 10, 2023      |
| DynamoDB global tables started tracking changes                          | DynamoDB global tables started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                | May 10, 2023      |
