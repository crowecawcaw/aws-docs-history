# Event source permissions for Amazon EventBridge Pipes

When settings up a pipe, you can use an existing execution role, or have EventBridge create one
for you with the needed permissions. The permissions EventBridge Pipes requires vary based on the source type, and are listed below. If you’re setting up your own
execution role, you must add these permissions yourself.

###### Note

If you’re unsure of the exact well-scoped permissions required to access the source, use the EventBridge Pipes console to create a new role,
then inspect the actions listed in the policy.

###### Topics

- [DynamoDB execution role permissions](#pipes-perms-ddb "#pipes-perms-ddb")
- [Kinesis execution role permissions](#pipes-perms-ak "#pipes-perms-ak")
- [Amazon MQ execution role permissions](#pipes-perms-mq "#pipes-perms-mq")
- [Amazon MSK execution role permissions](#pipes-perms-msk "#pipes-perms-msk")
- [Self managed Apache Kafka execution role permissions](#pipes-perms-kafka "#pipes-perms-kafka")
- [Amazon SQS execution role permissions](#pipes-perms-sqs "#pipes-perms-sqs")
- [Enrichment and target permissions](#pipes-perms-enhance-target "#pipes-perms-enhance-target")

## DynamoDB execution role permissions

For DynamoDB Streams, EventBridge Pipes requires the following permissions
to manage resources that are related to your DynamoDB data stream.

- [`dynamodb:DescribeStream`](../../../amazondynamodb/latest/APIReference/API_streams_DescribeStream.md "../../../amazondynamodb/latest/APIReference/API_streams_DescribeStream.md")
- [`dynamodb:GetRecords`](../../../amazondynamodb/latest/APIReference/API_streams_GetRecords.md "../../../amazondynamodb/latest/APIReference/API_streams_GetRecords.md")
- [`dynamodb:GetShardIterator`](../../../amazondynamodb/latest/APIReference/API_streams_GetShardIterator.md "../../../amazondynamodb/latest/APIReference/API_streams_GetShardIterator.md")
- [`dynamodb:ListStreams`](../../../amazondynamodb/latest/APIReference/API_streams_ListStreams.md "../../../amazondynamodb/latest/APIReference/API_streams_ListStreams.md")

To send records of failed batches to the pipe dead-letter queue, your pipe execution role needs the following permission:

- [`sqs:SendMessage`](../../../AWSSimpleQueueService/latest/APIReference/API_SendMessage.md "../../../AWSSimpleQueueService/latest/APIReference/API_SendMessage.md")

## Kinesis execution role permissions

For Kinesis, EventBridge Pipes requires the following permissions
to manage resources that are related to your Kinesis data stream.

- [`kinesis:DescribeStream`](../../../kinesis/latest/APIReference/API_DescribeStream.md "../../../kinesis/latest/APIReference/API_DescribeStream.md")
- [`kinesis:DescribeStreamSummary`](../../../kinesis/latest/APIReference/API_DescribeStreamSummary.md "../../../kinesis/latest/APIReference/API_DescribeStreamSummary.md")
- [`kinesis:GetRecords`](../../../kinesis/latest/APIReference/API_GetRecords.md "../../../kinesis/latest/APIReference/API_GetRecords.md")
- [`kinesis:GetShardIterator`](../../../kinesis/latest/APIReference/API_GetShardIterator.md "../../../kinesis/latest/APIReference/API_GetShardIterator.md")
- [`kinesis:ListShards`](../../../kinesis/latest/APIReference/API_ListShards.md "../../../kinesis/latest/APIReference/API_ListShards.md")
- [`kinesis:ListStreams`](../../../kinesis/latest/APIReference/API_ListStreams.md "../../../kinesis/latest/APIReference/API_ListStreams.md")
- [`kinesis:SubscribeToShard`](../../../kinesis/latest/APIReference/API_SubscribeToShard.md "../../../kinesis/latest/APIReference/API_SubscribeToShard.md")

To send records of failed batches to the pipe dead-letter queue, your pipe execution role needs the following permission:

- [`sqs:SendMessage`](../../../AWSSimpleQueueService/latest/APIReference/API_SendMessage.md "../../../AWSSimpleQueueService/latest/APIReference/API_SendMessage.md")

## Amazon MQ execution role permissions

For Amazon MQ, EventBridge Pipes requires the following permissions
to manage resources that are related to your Amazon MQ message broker.

- [`mq:DescribeBroker`](../../../amazon-mq/latest/api-reference/brokers-broker-id.md#brokers-broker-id-http-methods "../../../amazon-mq/latest/api-reference/brokers-broker-id.md#brokers-broker-id-http-methods")
- [`secretsmanager:GetSecretValue`](../../../secretsmanager/latest/apireference/API_GetSecretValue.md "../../../secretsmanager/latest/apireference/API_GetSecretValue.md")
- [`ec2:CreateNetworkInterface`](../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md "../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md")
- [`ec2:DeleteNetworkInterface`](../../../AWSEC2/latest/APIReference/API_DeleteNetworkInterface.md "../../../AWSEC2/latest/APIReference/API_DeleteNetworkInterface.md")
- [`ec2:DescribeNetworkInterfaces`](../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md "../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md")
- [`ec2:DescribeSecurityGroups`](../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md "../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md")
- [`ec2:DescribeSubnets`](../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md "../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md")
- [`ec2:DescribeVpcs`](../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md "../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md")
- [`logs:CreateLogGroup`](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md")
- [`logs:CreateLogStream`](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md")
- [`logs:PutLogEvents`](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md")

## Amazon MSK execution role permissions

For Amazon MSK, EventBridge requires the following permissions to
manage resources that are related to your Amazon MSK topic.

###### Note

If you're using IAM role-based authentication, your execution role will need the permissions listed in [IAM role-based authentication](eb-pipes-msk.md#pipes-msk-permissions-iam-policy "eb-pipes-msk.md#pipes-msk-permissions-iam-policy")
in addition the ones listed below.

- [`kafka:DescribeClusterV2`](../../../MSK/2.0/APIReference/v2-clusters-clusterarn.md#v2-clusters-clusterarnget "../../../MSK/2.0/APIReference/v2-clusters-clusterarn.md#v2-clusters-clusterarnget")
- [`kafka:GetBootstrapBrokers`](../../../msk/1.0/apireference/clusters-clusterarn-bootstrap-brokers.md#clusters-clusterarn-bootstrap-brokersget "../../../msk/1.0/apireference/clusters-clusterarn-bootstrap-brokers.md#clusters-clusterarn-bootstrap-brokersget")
- [`ec2:CreateNetworkInterface`](../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md "../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md")
- [`ec2:DescribeNetworkInterfaces`](../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md "../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md")
- [`ec2:DescribeVpcs`](../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md "../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md")
- [`ec2:DeleteNetworkInterface`](../../../AWSEC2/latest/APIReference/API_DeleteNetworkInterface.md "../../../AWSEC2/latest/APIReference/API_DeleteNetworkInterface.md")
- [`ec2:DescribeSubnets`](../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md "../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md")
- [`ec2:DescribeSecurityGroups`](../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md "../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md")
- [`logs:CreateLogGroup`](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md")
- [`logs:CreateLogStream`](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md")
- [`logs:PutLogEvents`](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md")

## Self managed Apache Kafka execution role permissions

For self managed Apache Kafka, EventBridge requires the following permissions
to manage resources that are related to your self managed Apache Kafka stream.

### Required permissions

To create and store logs in a log group in Amazon CloudWatch Logs, your pipe must have the following permissions in its execution role:

- [`logs:CreateLogGroup`](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md")
- [`logs:CreateLogStream`](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md")
- [`logs:PutLogEvents`](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md")

### Optional permissions

Your pipe might also need permissions to:

- Describe your Secrets Manager secret.
- Access your AWS Key Management Service (AWS KMS) customer managed key.
- Access your Amazon VPC.

### Secrets Manager and AWS KMS permissions

Depending on the type of access control that you're configuring for your Apache Kafka brokers,
your pipe might need permission to access your Secrets Manager secret or to decrypt your AWS KMS
customer managed key. To access these resources, your function's execution role must have
the following permissions:

- [`secretsmanager:GetSecretValue`](../../../secretsmanager/latest/apireference/API_GetSecretValue.md "../../../secretsmanager/latest/apireference/API_GetSecretValue.md")
- [`kms:Decrypt`](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md")

### VPC permissions

If only users within a VPC can access your self managed Apache Kafka cluster, your pipe must have permission to access your Amazon VPC resources. These resources include your VPC, subnets,
security groups, and network interfaces. To access these resources, your pipe's execution role must have the following permissions:

- [`ec2:CreateNetworkInterface`](../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md "../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md")
- [`ec2:DescribeNetworkInterfaces`](../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md "../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md")
- [`ec2:DescribeVpcs`](../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md "../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md")
- [`ec2:DeleteNetworkInterface`](../../../AWSEC2/latest/APIReference/API_DeleteNetworkInterface.md "../../../AWSEC2/latest/APIReference/API_DeleteNetworkInterface.md")
- [`ec2:DescribeSubnets`](../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md "../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md")
- [`ec2:DescribeSecurityGroups`](../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md "../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md")

## Amazon SQS execution role permissions

For Amazon SQS, EventBridge requires the following permissions to
manage resources that are related to your Amazon SQS queue.

- [`sqs:ReceiveMessage`](../../../AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.md "../../../AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.md")
- [`sqs:DeleteMessage`](../../../AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.md "../../../AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.md")
- [`sqs:GetQueueAttributes`](../../../AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.md "../../../AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.md")

## Enrichment and target permissions

To make API calls on the resources that you own, EventBridge Pipes needs appropriate
permission. EventBridge Pipes uses the IAM role that you specify on the pipe for enrichment
and target calls using the IAM principal `pipes.amazonaws.com`.
