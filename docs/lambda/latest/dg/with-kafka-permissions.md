# Configuring Lambda execution role permissions

In addition to [accessing your self-managed Kafka cluster](kafka-cluster-auth.md "kafka-cluster-auth.md"), your Lambda function needs permissions to perform
various API actions. You add these permissions to the function's [execution role](lambda-intro-execution-role.md "lambda-intro-execution-role.md"). If your users need access to any API actions, add the required permissions to the
identity policy for the AWS Identity and Access Management (IAM) user or role.

###### Topics

- [Required Lambda function permissions](#smaa-api-actions-required "#smaa-api-actions-required")
- [Optional Lambda function permissions](#smaa-api-actions-optional "#smaa-api-actions-optional")
- [Adding permissions to your execution role](#smaa-permissions-add-policy "#smaa-permissions-add-policy")
- [Granting users access with an IAM policy](#smaa-permissions-add-users "#smaa-permissions-add-users")

## Required Lambda function permissions

To create and store logs in a log group in Amazon CloudWatch Logs, your Lambda function must have the following
permissions in its execution role:

- [logs:CreateLogGroup](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md")
- [logs:CreateLogStream](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md")
- [logs:PutLogEvents](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md")

## Optional Lambda function permissions

Your Lambda function might also need permissions to:

- Describe your Secrets Manager secret.
- Access your AWS Key Management Service (AWS KMS) customer managed key.
- Access your Amazon VPC.
- Send records of failed invocations to a destination.

### Secrets Manager and AWS KMS permissions

Depending on the type of access control that you're configuring for your Kafka brokers, your Lambda function
might need permission to access your Secrets Manager secret or to decrypt your AWS KMS customer managed key. To access these
resources, your function's execution role must have the following permissions:

- [secretsmanager:GetSecretValue](../../../secretsmanager/latest/apireference/API_GetSecretValue.md "../../../secretsmanager/latest/apireference/API_GetSecretValue.md")
- [kms:Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md")

### VPC permissions

If only users within a VPC can access your self-managed Apache Kafka cluster, your Lambda function must have permission to
access your Amazon VPC resources. These resources include your VPC, subnets, security groups, and network
interfaces. To access these resources, your function's execution role must have the following
permissions:

- [ec2:CreateNetworkInterface](../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md "../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md")
- [ec2:DescribeNetworkInterfaces](../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md "../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md")
- [ec2:DescribeVpcs](../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md "../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md")
- [ec2:DeleteNetworkInterface](../../../AWSEC2/latest/APIReference/API_DeleteNetworkInterface.md "../../../AWSEC2/latest/APIReference/API_DeleteNetworkInterface.md")
- [ec2:DescribeSubnets](../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md "../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md")
- [ec2:DescribeSecurityGroups](../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md "../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md")

## Adding permissions to your execution role

To access other AWS services that your self-managed Apache Kafka cluster uses, Lambda uses the permissions policies that you
define in your Lambda function's [execution role](lambda-intro-execution-role.md "lambda-intro-execution-role.md").

By default, Lambda is not permitted to perform the required or optional actions for a self-managed Apache Kafka cluster. You
must create and define these actions in an [IAM trust policy](../../../IAM/latest/UserGuide/id_roles_update-role-trust-policy.md "../../../IAM/latest/UserGuide/id_roles_update-role-trust-policy.md") for your execution role. This example shows how you might create a policy that allows
Lambda to access your Amazon VPC resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "ec2:CreateNetworkInterface",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeVpcs",
 "ec2:DeleteNetworkInterface",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups"
 ],
 "Resource":"*"
 }
 ]
 }`

```

## Granting users access with an IAM policy

By default, users and roles don't have permission to perform [event source API operations](invocation-eventsourcemapping.md#event-source-mapping-api "invocation-eventsourcemapping.md#event-source-mapping-api"). To grant access to users in your
organization or account, you create or update an identity-based policy. For more information, see [Controlling access to AWS resources
using policies](../../../IAM/latest/UserGuide/access_controlling.md "../../../IAM/latest/UserGuide/access_controlling.md") in the _IAM User Guide_.

For troubleshooting authentication and authorization errors, see [Troubleshooting Kafka event source mapping errors](with-kafka-troubleshoot.md "with-kafka-troubleshoot.md").
