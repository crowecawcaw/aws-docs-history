

# AWS managed policies for AWS Lambda
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

**Topics**
+ [AWS managed policy: AWSLambda\_FullAccess](#lambda-security-iam-awsmanpol-AWSLambda_FullAccess)
+ [AWS managed policy: AWSLambda\_ReadOnlyAccess](#lambda-security-iam-awsmanpol-AWSLambda_ReadOnlyAccess)
+ [AWS managed policy: AWSLambdaBasicExecutionRole](#lambda-security-iam-awsmanpol-AWSLambdaBasicExecutionRole)
+ [AWS managed policy: AWSLambdaBasicDurableExecutionRolePolicy](#lambda-security-iam-awsmanpol-AWSLambdaBasicDurableExecutionRolePolicy)
+ [AWS managed policy: AWSLambdaDynamoDBExecutionRole](#lambda-security-iam-awsmanpol-AWSLambdaDynamoDBExecutionRole)
+ [AWS managed policy: AWSLambdaENIManagementAccess](#lambda-security-iam-awsmanpol-AWSLambdaENIManagementAccess)
+ [AWS managed policy: AWSLambdaInvocation-DynamoDB](#lambda-security-iam-awsmanpol-AWSLambdaInvocation-DynamoDB)
+ [AWS managed policy: AWSLambdaKinesisExecutionRole](#lambda-security-iam-awsmanpol-AWSLambdaKinesisExecutionRole)
+ [AWS managed policy: AWSLambdaMSKExecutionRole](#lambda-security-iam-awsmanpol-AWSLambdaMSKExecutionRole)
+ [AWS managed policy: AWSLambdaRole](#lambda-security-iam-awsmanpol-AWSLambdaRole)
+ [AWS managed policy: AWSLambdaSQSQueueExecutionRole](#lambda-security-iam-awsmanpol-AWSLambdaSQSQueueExecutionRole)
+ [AWS managed policy: AWSLambdaVPCAccessExecutionRole](#lambda-security-iam-awsmanpol-AWSLambdaVPCAccessExecutionRole)
+ [AWS managed policy: AWSLambdaManagedEC2ResourceOperator](#lambda-security-iam-awsmanpol-AWSLambdaManagedEC2ResourceOperator)
+ [AWS managed policy: AWSLambdaServiceRolePolicy](#lambda-security-iam-awsmanpol-AWSLambdaServiceRolePolicy)
+ [AWS managed policy: AWSLambdaNetworkConnectorOperatorPolicy](#lambda-security-iam-awsmanpol-AWSLambdaNetworkConnectorOperatorPolicy)
+ [AWS managed policy: AWSLambdaInvokeWebFunctionEndpointAccess](#lambda-security-iam-awsmanpol-AWSLambdaInvokeWebFunctionEndpointAccess)
+ [Lambda updates to AWS managed policies](#lambda-security-iam-awsmanpol-updates)

## AWS managed policy: AWSLambda\_FullAccess
<a name="lambda-security-iam-awsmanpol-AWSLambda_FullAccess"></a>

This policy grants full access to Lambda actions. It also grants permissions to other AWS services that are used to develop and maintain Lambda resources.

You can attach the `AWSLambda_FullAccess` policy to your users, groups, and roles.

**Permissions details**

This policy includes the following permissions:
+ `lambda` – Allows principals full access to Lambda.
+ `cloudformation` – Allows principals to describe AWS CloudFormation stacks and list the resources in those stacks.
+ `cloudwatch` – Allows principals to list Amazon CloudWatch metrics and get metric data.
+ `ec2` – Allows principals to describe security groups, subnets, and VPCs.
+ `iam` – Allows principals to get policies, policy versions, roles, role policies, attached role policies, and the list of roles. This policy also allows principals to pass roles to Lambda. The `PassRole` permission is used when you assign an execution role to a function. The `CreateServiceLinkedRole` permission is used when creating a service-linked role.
+ `kms` – Allows principals to list aliases and describe key for volume encryption.
+ `logs` – Allows principals to describe log streams, get log events, filter log events, and to start and stop Live Tail sessions.
+ `states` – Allows principals to describe and list AWS Step Functions state machines.
+ `tag` – Allows principals to get resources based on their tags.
+ `xray` – Allows principals to get AWS X-Ray trace summaries and retrieve a list of traces specified by ID.

For more information about this policy, including the JSON policy document and policy versions, see [AWSLambda\_FullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambda_FullAccess.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSLambda\_ReadOnlyAccess
<a name="lambda-security-iam-awsmanpol-AWSLambda_ReadOnlyAccess"></a>

This policy grants read-only access to Lambda resources and to other AWS services that are used to develop and maintain Lambda resources.

You can attach the `AWSLambda_ReadOnlyAccess` policy to your users, groups, and roles.

**Permissions details**

This policy includes the following permissions:
+ `lambda` – Allows principals to get and list all resources.
+ `cloudformation` – Allows principals to describe and list AWS CloudFormation stacks and list the resources in those stacks.
+ `cloudwatch` – Allows principals to list Amazon CloudWatch metrics and get metric data.
+ `ec2` – Allows principals to describe security groups, subnets, and VPCs.
+ `iam` – Allows principals to get policies, policy versions, roles, role policies, attached role policies, and the list of roles.
+ `kms` – Allows principals to list aliases.
+ `logs` – Allows principals to describe log streams, get log events, filter log events, and to start and stop Live Tail sessions.
+ `states` – Allows principals to describe and list AWS Step Functions state machines.
+ `tag` – Allows principals to get resources based on their tags.
+ `xray` – Allows principals to get AWS X-Ray trace summaries and retrieve a list of traces specified by ID.

For more information about this policy, including the JSON policy document and policy versions, see [AWSLambda\_ReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambda_ReadOnlyAccess.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSLambdaBasicExecutionRole
<a name="lambda-security-iam-awsmanpol-AWSLambdaBasicExecutionRole"></a>

This policy grants permissions to upload logs to CloudWatch Logs.

You can attach the `AWSLambdaBasicExecutionRole` policy to your users, groups, and roles.

For more information about this policy, including the JSON policy document and policy versions, see [AWSLambdaBasicExecutionRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaBasicExecutionRole.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSLambdaBasicDurableExecutionRolePolicy
<a name="lambda-security-iam-awsmanpol-AWSLambdaBasicDurableExecutionRolePolicy"></a>

This policy provides write permissions to CloudWatch Logs and read/write permissions to durable execution APIs used by Lambda durable functions. This policy provides the essential permissions required for Lambda durable functions, which use durable execution APIs to persist progress and maintain state across function invocations.

You can attach the `AWSLambdaBasicDurableExecutionRolePolicy` policy to your users, groups, and roles.

**Permissions details**

This policy includes the following permissions:
+ `logs` – Allows principals to create log groups and log streams, and write log events to CloudWatch Logs.
+ `lambda` – Allows principals to checkpoint durable execution state and retrieve durable execution state for Lambda durable functions.

To view more details about the policy, including the latest version of the JSON policy document, see [AWSLambdaBasicDurableExecutionRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaBasicDurableExecutionRolePolicy.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSLambdaDynamoDBExecutionRole
<a name="lambda-security-iam-awsmanpol-AWSLambdaDynamoDBExecutionRole"></a>

This policy grants permissions to read records from an Amazon DynamoDB stream and write to CloudWatch Logs.

You can attach the `AWSLambdaDynamoDBExecutionRole` policy to your users, groups, and roles.

For more information about this policy, including the JSON policy document and policy versions, see [AWSLambdaDynamoDBExecutionRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaDynamoDBExecutionRole.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSLambdaENIManagementAccess
<a name="lambda-security-iam-awsmanpol-AWSLambdaENIManagementAccess"></a>

This policy grants permissions to create, describe, and delete elastic network interfaces used by a VPC-enabled Lambda function.

You can attach the `AWSLambdaENIManagementAccess` policy to your users, groups, and roles.

For more information about this policy, including the JSON policy document and policy versions, see [AWSLambdaENIManagementAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaENIManagementAccess.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSLambdaInvocation-DynamoDB
<a name="lambda-security-iam-awsmanpol-AWSLambdaInvocation-DynamoDB"></a>

This policy grants read access to Amazon DynamoDB Streams.

You can attach the `AWSLambdaInvocation-DynamoDB` policy to your users, groups, and roles.

For more information about this policy, including the JSON policy document and policy versions, see [AWSLambdaInvocation-DynamoDB](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaInvocation-DynamoDB.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSLambdaKinesisExecutionRole
<a name="lambda-security-iam-awsmanpol-AWSLambdaKinesisExecutionRole"></a>

This policy grants permissions to read events from an Amazon Kinesis data stream and write to CloudWatch Logs.

You can attach the `AWSLambdaKinesisExecutionRole` policy to your users, groups, and roles.

For more information about this policy, including the JSON policy document and policy versions, see [AWSLambdaKinesisExecutionRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaKinesisExecutionRole.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSLambdaMSKExecutionRole
<a name="lambda-security-iam-awsmanpol-AWSLambdaMSKExecutionRole"></a>

This policy grants permissions to read and access records from an Amazon Managed Streaming for Apache Kafka cluster, manage elastic network interfaces, and write to CloudWatch Logs.

You can attach the `AWSLambdaMSKExecutionRole` policy to your users, groups, and roles.

For more information about this policy, including the JSON policy document and policy versions, see [AWSLambdaMSKExecutionRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaMSKExecutionRole.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSLambdaRole
<a name="lambda-security-iam-awsmanpol-AWSLambdaRole"></a>

This policy grants permissions to invoke Lambda functions.

You can attach the `AWSLambdaRole` policy to your users, groups, and roles.

For more information about this policy, including the JSON policy document and policy versions, see [AWSLambdaRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaRole.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSLambdaSQSQueueExecutionRole
<a name="lambda-security-iam-awsmanpol-AWSLambdaSQSQueueExecutionRole"></a>

This policy grants permissions to read and delete messages from an Amazon Simple Queue Service queue, and grants write permissions to CloudWatch Logs.

You can attach the `AWSLambdaSQSQueueExecutionRole` policy to your users, groups, and roles.

For more information about this policy, including the JSON policy document and policy versions, see [AWSLambdaSQSQueueExecutionRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaSQSQueueExecutionRole.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSLambdaVPCAccessExecutionRole
<a name="lambda-security-iam-awsmanpol-AWSLambdaVPCAccessExecutionRole"></a>

This policy grants permissions to manage elastic network interfaces within an Amazon Virtual Private Cloud and write to CloudWatch Logs.

You can attach the `AWSLambdaVPCAccessExecutionRole` policy to your users, groups, and roles.

For more information about this policy, including the JSON policy document and policy versions, see [AWSLambdaVPCAccessExecutionRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaVPCAccessExecutionRole.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSLambdaManagedEC2ResourceOperator
<a name="lambda-security-iam-awsmanpol-AWSLambdaManagedEC2ResourceOperator"></a>

This policy enables automated Amazon Elastic Compute Cloud instance management and Amazon CloudWatch logging for Lambda capacity providers. It grants permissions to Lambda to perform instance lifecycle operations and write logs on your behalf.

You can attach the `AWSLambdaManagedEC2ResourceOperator` policy to your users, groups, and roles.

**Permissions details**

This policy includes the following permissions:
+ `ec2:RunInstances` – Allows Lambda to launch new Amazon EC2 instances with the condition that ec2:ManagedResourceOperator equals scaler.lambda.amazonaws.com and restricts AMI usage to Amazon-owned images only.
+ `ec2:DescribeInstances` and `ec2:DescribeInstanceStatus` – Allows Lambda to monitor instance status and retrieve instance information.
+ `ec2:CreateTags` – Allows Lambda to tag Amazon EC2 resources for management and identification purposes.
+ `ec2:DescribeAvailabilityZones` – Allows Lambda to view available zones for instance placement decisions.
+ `ec2:DescribeCapacityReservations` – Allows Lambda to check capacity reservations for optimal instance placement.
+ `ec2:DescribeInstanceTypes` and `ec2:DescribeInstanceTypeOfferings` – Allows Lambda to review available instance types and their offerings.
+ `ec2:DescribeSubnets` – Allows Lambda to examine subnet configurations for network planning.
+ `ec2:DescribeVpcEncryptionControls` – Allows Lambda to examine VPC encryption control settings for instance configuration.
+ `ec2:DescribeSecurityGroups` – Allows Lambda to retrieve security group information for network interface configuration.
+ `ec2:CreateNetworkInterface` – Allows Lambda to create network interfaces and manage subnet and security group associations.
+ `ec2:AttachNetworkInterface` – Allows Lambda to attach network interfaces to Amazon EC2 instances with the condition that `ec2:ManagedResourceOperator` equals [scaler.lambda.amazonaws.com](http://scaler.lambda.amazonaws.com/).
+ `logs:CreateLogGroup` – Allows Lambda to create CloudWatch Logs log groups.
+ `logs:CreateLogStream` and `logs:PutLogEvents` – Allows Lambda to create log streams and write log events to CloudWatch Logs.

For more information about this policy, including the JSON policy document and policy versions, see [AWSLambdaManagedEC2ResourceOperator](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaManagedEC2ResourceOperator.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSLambdaServiceRolePolicy
<a name="lambda-security-iam-awsmanpol-AWSLambdaServiceRolePolicy"></a>

This policy is attached to the service-linked role named AWSServiceRoleForLambda to allow Lambda to 1) terminate instances managed as part of Lambda capacity providers and 2) delete Elastic Network Interfaces (ENIs) managed as part of Lambda network connectors.

**Permissions details**

This policy includes the following permissions:
+ `ec2:TerminateInstances` – Allows Lambda to terminate EC2 instances with the condition that ec2:ManagedResourceOperator equals scaler.lambda.amazonaws.com.
+ `ec2:DescribeInstanceStatus` and `ec2:DescribeInstances` – Allows Lambda to describe EC2 instances.
+ `ec2:DescribeNetworkInterfaces`, `ec2:DescribeSubnets`, and `ec2:DescribeSecurityGroups` – Allows Lambda to describe network interfaces, subnets, and security groups.
+ `ec2:DeleteNetworkInterface` – Allows Lambda to delete ENIs with the condition that ec2:ManagedResourceOperator equals network-connectors.lambda.amazonaws.com.

For more information about this policy, see [Using service-linked roles for Lambda](using-service-linked-roles.md).

## AWS managed policy: AWSLambdaNetworkConnectorOperatorPolicy
<a name="lambda-security-iam-awsmanpol-AWSLambdaNetworkConnectorOperatorPolicy"></a>

This policy grants permissions to create and administer elastic network interface (ENI) resources managed by the Lambda Network Connector.

You can attach the `AWSLambdaNetworkConnectorOperatorPolicy` policy to your users, groups, and roles.

### Permissions details
<a name="w2aac27c23c48c47b7"></a>

This policy includes the following permissions:
+ `ec2:CreateNetworkInterface` – Grants permission to create network interfaces in any subnet with associated security groups. For network interface resources, only tags with the keys `aws:lambda:networkConnectorName` and `aws:lambda:networkConnectorId` are permitted.
+ `ec2:CreateTags` – Grants permission to tag network interfaces at creation time. This permission applies only when the create action is `CreateNetworkInterface` and the managed resource operator is `network-connectors.lambda.amazonaws.com`.

For more information about this policy, including the JSON policy document and policy versions, see [AWSLambdaNetworkConnectorOperatorPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaNetworkConnectorOperatorPolicy.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSLambdaInvokeWebFunctionEndpointAccess
<a name="lambda-security-iam-awsmanpol-AWSLambdaInvokeWebFunctionEndpointAccess"></a>

This policy grants permissions to invoke Lambda web function endpoints.

You can attach the `AWSLambdaInvokeWebFunctionEndpointAccess` policy to your users, groups, and roles.

For more information about this policy, including the JSON policy document and policy versions, see [AWSLambdaInvokeWebFunctionEndpointAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaInvokeWebFunctionEndpointAccess.html) in the *AWS Managed Policy Reference Guide*.

## Lambda updates to AWS managed policies
<a name="lambda-security-iam-awsmanpol-updates"></a>


| Change | Description | Date | 
| --- | --- | --- | 
| [AWSLambdaInvokeWebFunctionEndpointAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaInvokeWebFunctionEndpointAccess.html) – New policy | Lambda added a new managed policy to grant permissions to invoke Lambda web function endpoints. | October 1, 2026 | 
| [AWSLambdaNetworkConnectorOperatorPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaNetworkConnectorOperatorPolicy.html) – New policy | Lambda added a new managed policy to grant permissions to create and administer ENI resources managed by the Lambda Network Connector. | June 19, 2026 | 
| [AWSLambdaManagedEC2ResourceOperator](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaManagedEC2ResourceOperator.html) – Change | Lambda updated the `AWSLambdaManagedEC2ResourceOperator` policy to allow the `logs:CreateLogGroup`, `logs:CreateLogStream`, and `logs:PutLogEvents` actions. These permissions enable Lambda to write logs to CloudWatch Logs. | June 10, 2026 | 
| [AWSLambdaManagedEC2ResourceOperator](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaManagedEC2ResourceOperator.html) – Change | Lambda updated the `AWSLambdaManagedEC2ResourceOperator` policy to allow the `ec2:DescribeVpcEncryptionControls` action. This permission enables Lambda to examine VPC encryption control settings for instance configuration. | April 23, 2026 | 
| [AWSLambdaManagedEC2ResourceOperator](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaManagedEC2ResourceOperator.html) – New policy | Lambda added a new managed policy to enable automated Amazon EC2 instance management for Lambda capacity providers, allowing the scaler service to perform instance lifecycle operations. | November 30, 2025 | 
| [AWSLambdaServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaServiceRolePolicy.html) – New policy | Lambda added a new managed policy for the service-linked role to allow Lambda to terminate instances managed as part of Lambda capacity providers. | November 30, 2025 | 
| [AWSLambda\_FullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambda_FullAccess.html) – Change | Lambda updated the `AWSLambda_FullAccess` policy to allow the `kms:DescribeKey` and `iam:CreateServiceLinkedRole` actions. | November 30, 2025 | 
| [AWSLambdaBasicDurableExecutionRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaBasicDurableExecutionRolePolicy.html) – New managed policy | Lambda released a new managed policy `AWSLambdaBasicDurableExecutionRolePolicy` that provides write permissions to CloudWatch Logs and read/write permissions to durable execution APIs used by Lambda durable functions. | December 1, 2025 | 
| [AWSLambda\_ReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambda_ReadOnlyAccess.html) and [AWSLambda\_FullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambda_FullAccess.html) – Change | Lambda updated the `AWSLambda_ReadOnlyAccess` and `AWSLambda_FullAccess` policies to allow the `logs:StartLiveTail` and `logs:StopLiveTail` actions. | March 17, 2025 | 
| [AWSLambdaVPCAccessExecutionRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaVPCAccessExecutionRole.html) – Change | Lambda updated the `AWSLambdaVPCAccessExecutionRole` policy to allow the action `ec2:DescribeSubnets`. | January 5, 2024 | 
| [AWSLambda\_ReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambda_ReadOnlyAccess.html) – Change | Lambda updated the `AWSLambda_ReadOnlyAccess` policy to allow principals to list CloudFormation stacks. | July 27, 2023 | 
| AWS Lambda started tracking changes | AWS Lambda started tracking changes for its AWS managed policies. | July 27, 2023 | 