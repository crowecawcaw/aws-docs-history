# AWS managed policies for AWS Lambda

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

###### Topics

- [AWS managed policy: AWSLambda_FullAccess](#lambda-security-iam-awsmanpol-AWSLambda_FullAccess "#lambda-security-iam-awsmanpol-AWSLambda_FullAccess")
- [AWS managed policy: AWSLambda_ReadOnlyAccess](#lambda-security-iam-awsmanpol-AWSLambda_ReadOnlyAccess "#lambda-security-iam-awsmanpol-AWSLambda_ReadOnlyAccess")
- [AWS managed policy: AWSLambdaBasicExecutionRole](#lambda-security-iam-awsmanpol-AWSLambdaBasicExecutionRole "#lambda-security-iam-awsmanpol-AWSLambdaBasicExecutionRole")
- [AWS managed policy: AWSLambdaDynamoDBExecutionRole](#lambda-security-iam-awsmanpol-AWSLambdaDynamoDBExecutionRole "#lambda-security-iam-awsmanpol-AWSLambdaDynamoDBExecutionRole")
- [AWS managed policy: AWSLambdaENIManagementAccess](#lambda-security-iam-awsmanpol-AWSLambdaENIManagementAccess "#lambda-security-iam-awsmanpol-AWSLambdaENIManagementAccess")
- [AWS managed policy: AWSLambdaInvocation-DynamoDB](#lambda-security-iam-awsmanpol-AWSLambdaInvocation-DynamoDB "#lambda-security-iam-awsmanpol-AWSLambdaInvocation-DynamoDB")
- [AWS managed policy: AWSLambdaKinesisExecutionRole](#lambda-security-iam-awsmanpol-AWSLambdaKinesisExecutionRole "#lambda-security-iam-awsmanpol-AWSLambdaKinesisExecutionRole")
- [AWS managed policy: AWSLambdaMSKExecutionRole](#lambda-security-iam-awsmanpol-AWSLambdaMSKExecutionRole "#lambda-security-iam-awsmanpol-AWSLambdaMSKExecutionRole")
- [AWS managed policy: AWSLambdaRole](#lambda-security-iam-awsmanpol-AWSLambdaRole "#lambda-security-iam-awsmanpol-AWSLambdaRole")
- [AWS managed policy: AWSLambdaSQSQueueExecutionRole](#lambda-security-iam-awsmanpol-AWSLambdaSQSQueueExecutionRole "#lambda-security-iam-awsmanpol-AWSLambdaSQSQueueExecutionRole")
- [AWS managed policy: AWSLambdaVPCAccessExecutionRole](#lambda-security-iam-awsmanpol-AWSLambdaVPCAccessExecutionRole "#lambda-security-iam-awsmanpol-AWSLambdaVPCAccessExecutionRole")
- [Lambda updates to AWS managed
  policies](#lambda-security-iam-awsmanpol-updates "#lambda-security-iam-awsmanpol-updates")

## AWS managed policy: AWSLambda_FullAccess

This policy grants full access to Lambda actions. It also grants permissions to other AWS services that are used to develop and maintain Lambda resources.

You can attach the `AWSLambda_FullAccess` policy to your users, groups, and roles.

**Permissions details**

This policy includes the following permissions:

- `lambda` – Allows principals full access to Lambda.
- `cloudformation` – Allows principals to describe AWS CloudFormation stacks and list the resources in those stacks.
- `cloudwatch` – Allows principals to list Amazon CloudWatch metrics and get metric data.
- `ec2` – Allows principals to describe security groups, subnets, and VPCs.
- `iam` – Allows principals to get policies, policy versions, roles, role policies, attached role policies, and the list of roles. This policy also allows principals to pass roles to Lambda. The `PassRole` permission is used when you assign an execution role to a function.
- `kms` – Allows principals to list aliases.
- `logs` – Allows principals to describe log streams, get log events, filter log events, and to start and stop Live Tail sessions.
- `states` – Allows principals to describe and list AWS Step Functions state machines.
- `tag` – Allows principals to get resources based on their tags.
- `xray` – Allows principals to get AWS X-Ray trace summaries and retrieve a list of traces specified by ID.

For more information about this policy, including the JSON policy document and policy versions, see
[AWSLambda_FullAccess](../../../aws-managed-policy/latest/reference/AWSLambda_FullAccess.md "../../../aws-managed-policy/latest/reference/AWSLambda_FullAccess.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AWSLambda_ReadOnlyAccess

This policy grants read-only access to Lambda resources and to other AWS services that are used to develop and maintain Lambda resources.

You can attach the `AWSLambda_ReadOnlyAccess` policy to your users, groups, and roles.

**Permissions details**

This policy includes the following permissions:

- `lambda` – Allows principals to get and list all resources.
- `cloudformation` – Allows principals to describe and list AWS CloudFormation stacks and list the resources in those stacks.
- `cloudwatch` – Allows principals to list Amazon CloudWatch metrics and get metric data.
- `ec2` – Allows principals to describe security groups, subnets, and VPCs.
- `iam` – Allows principals to get policies, policy versions, roles, role policies, attached role policies, and the list of roles.
- `kms` – Allows principals to list aliases.
- `logs` – Allows principals to describe log streams, get log events, filter log events, and to start and stop Live Tail sessions.
- `states` – Allows principals to describe and list AWS Step Functions state machines.
- `tag` – Allows principals to get resources based on their tags.
- `xray` – Allows principals to get AWS X-Ray trace summaries and retrieve a list of traces specified by ID.

For more information about this policy, including the JSON policy document and policy versions, see
[AWSLambda_ReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSLambda_ReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSLambda_ReadOnlyAccess.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AWSLambdaBasicExecutionRole

This policy grants permissions to upload logs to CloudWatch Logs.

You can attach the `AWSLambdaBasicExecutionRole` policy to your users, groups, and roles.

For more information about this policy, including the JSON policy document and policy versions, see
[AWSLambdaBasicExecutionRole](../../../aws-managed-policy/latest/reference/AWSLambdaBasicExecutionRole.md "../../../aws-managed-policy/latest/reference/AWSLambdaBasicExecutionRole.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AWSLambdaDynamoDBExecutionRole

This policy grants permissions to read records from an Amazon DynamoDB stream and write to CloudWatch Logs.

You can attach the `AWSLambdaDynamoDBExecutionRole` policy to your users, groups, and roles.

For more information about this policy, including the JSON policy document and policy versions, see
[AWSLambdaDynamoDBExecutionRole](../../../aws-managed-policy/latest/reference/AWSLambdaDynamoDBExecutionRole.md "../../../aws-managed-policy/latest/reference/AWSLambdaDynamoDBExecutionRole.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AWSLambdaENIManagementAccess

This policy grants permissions to create, describe, and delete elastic network interfaces used by a VPC-enabled Lambda function.

You can attach the `AWSLambdaENIManagementAccess` policy to your users, groups, and roles.

For more information about this policy, including the JSON policy document and policy versions, see
[AWSLambdaENIManagementAccess](../../../aws-managed-policy/latest/reference/AWSLambdaENIManagementAccess.md "../../../aws-managed-policy/latest/reference/AWSLambdaENIManagementAccess.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AWSLambdaInvocation-DynamoDB

This policy grants read access to Amazon DynamoDB Streams.

You can attach the `AWSLambdaInvocation-DynamoDB` policy to your users, groups, and roles.

For more information about this policy, including the JSON policy document and policy versions, see
[AWSLambdaInvocation-DynamoDB](../../../aws-managed-policy/latest/reference/AWSLambdaInvocation-DynamoDB.md "../../../aws-managed-policy/latest/reference/AWSLambdaInvocation-DynamoDB.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AWSLambdaKinesisExecutionRole

This policy grants permissions to read events from an Amazon Kinesis data stream and write to CloudWatch Logs.

You can attach the `AWSLambdaKinesisExecutionRole` policy to your users, groups, and roles.

For more information about this policy, including the JSON policy document and policy versions, see
[AWSLambdaKinesisExecutionRole](../../../aws-managed-policy/latest/reference/AWSLambdaKinesisExecutionRole.md "../../../aws-managed-policy/latest/reference/AWSLambdaKinesisExecutionRole.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AWSLambdaMSKExecutionRole

This policy grants permissions to read and access records from an Amazon Managed Streaming for Apache Kafka cluster, manage elastic network interfaces, and write to CloudWatch Logs.

You can attach the `AWSLambdaMSKExecutionRole` policy to your users, groups, and roles.

For more information about this policy, including the JSON policy document and policy versions, see
[AWSLambdaMSKExecutionRole](../../../aws-managed-policy/latest/reference/AWSLambdaMSKExecutionRole.md "../../../aws-managed-policy/latest/reference/AWSLambdaMSKExecutionRole.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AWSLambdaRole

This policy grants permissions to invoke Lambda functions.

You can attach the `AWSLambdaRole` policy to your users, groups, and roles.

For more information about this policy, including the JSON policy document and policy versions, see
[AWSLambdaRole](../../../aws-managed-policy/latest/reference/AWSLambdaRole.md "../../../aws-managed-policy/latest/reference/AWSLambdaRole.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AWSLambdaSQSQueueExecutionRole

This policy grants permissions to read and delete messages from an Amazon Simple Queue Service queue, and grants write permissions to CloudWatch Logs.

You can attach the `AWSLambdaSQSQueueExecutionRole` policy to your users, groups, and roles.

For more information about this policy, including the JSON policy document and policy versions, see
[AWSLambdaSQSQueueExecutionRole](../../../aws-managed-policy/latest/reference/AWSLambdaSQSQueueExecutionRole.md "../../../aws-managed-policy/latest/reference/AWSLambdaSQSQueueExecutionRole.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AWSLambdaVPCAccessExecutionRole

This policy grants permissions to manage elastic network interfaces within an Amazon Virtual Private Cloud and write to CloudWatch Logs.

You can attach the `AWSLambdaVPCAccessExecutionRole` policy to your users, groups, and roles.

For more information about this policy, including the JSON policy document and policy versions, see
[AWSLambdaVPCAccessExecutionRole](../../../aws-managed-policy/latest/reference/AWSLambdaVPCAccessExecutionRole.md "../../../aws-managed-policy/latest/reference/AWSLambdaVPCAccessExecutionRole.md")
in the _AWS Managed Policy Reference Guide_.

## Lambda updates to AWS managed

policies

| Change                                                                                                                                                                                                                                                                                                                                                           | Description                                                                                                                                          | Date            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [AWSLambda_ReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSLambda_ReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSLambda_ReadOnlyAccess.md") and [AWSLambda_FullAccess](../../../aws-managed-policy/latest/reference/AWSLambda_FullAccess.md "../../../aws-managed-policy/latest/reference/AWSLambda_FullAccess.md") – Change | Lambda updated the `AWSLambda_ReadOnlyAccess` and `AWSLambda_FullAccess` policies to allow the `logs:StartLiveTail` and `logs:StopLiveTail` actions. | March 17, 2025  |
| [AWSLambdaVPCAccessExecutionRole](../../../aws-managed-policy/latest/reference/AWSLambdaVPCAccessExecutionRole.md "../../../aws-managed-policy/latest/reference/AWSLambdaVPCAccessExecutionRole.md") – Change                                                                                                                                                    | Lambda updated the `AWSLambdaVPCAccessExecutionRole` policy to allow the action `ec2:DescribeSubnets`.                                               | January 5, 2024 |
| [AWSLambda_ReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSLambda_ReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSLambda_ReadOnlyAccess.md") – Change                                                                                                                                                                         | Lambda updated the `AWSLambda_ReadOnlyAccess` policy to allow principals to list CloudFormation stacks.                                              | July 27, 2023   |
| AWS Lambda started tracking changes                                                                                                                                                                                                                                                                                                                              | AWS Lambda started tracking changes for its AWS managed policies.                                                                                    | July 27, 2023   |
