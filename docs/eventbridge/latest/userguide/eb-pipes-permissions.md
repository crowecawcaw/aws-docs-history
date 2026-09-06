

# Event source permissions for Amazon EventBridge Pipes
<a name="eb-pipes-permissions"></a>

When setting up a pipe, you can use an existing execution role, or have EventBridge create one for you with the needed permissions. The permissions EventBridge Pipes requires vary based on the source type, and are listed below. If you’re setting up your own execution role, you must add these permissions yourself.

**Note**  
If you’re unsure of the exact well-scoped permissions required to access the source, use the EventBridge Pipes console to create a new role, then inspect the actions listed in the policy.

**Topics**
+ [DynamoDB execution role permissions](#pipes-perms-ddb)
+ [Kinesis execution role permissions](#pipes-perms-ak)
+ [Amazon MQ execution role permissions](#pipes-perms-mq)
+ [Amazon MSK execution role permissions](#pipes-perms-msk)
+ [Self managed Apache Kafka execution role permissions](#pipes-perms-kafka)
+ [Amazon SQS execution role permissions](#pipes-perms-sqs)
+ [Enrichment and target permissions](#pipes-perms-enhance-target)

## DynamoDB execution role permissions
<a name="pipes-perms-ddb"></a>

For DynamoDB Streams, EventBridge Pipes requires the following permissions to manage resources that are related to your DynamoDB data stream.
+ [`dynamodb:DescribeStream`](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_DescribeStream.html)
+ [`dynamodb:GetRecords`](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetRecords.html)
+ [`dynamodb:GetShardIterator`](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetShardIterator.html)
+ [`dynamodb:ListStreams`](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_ListStreams.html)

To send records of failed batches to the pipe dead-letter queue, your pipe execution role needs the following permission:
+ [`sqs:SendMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html)

## Kinesis execution role permissions
<a name="pipes-perms-ak"></a>

For Kinesis, EventBridge Pipes requires the following permissions to manage resources that are related to your Kinesis data stream.
+ [`kinesis:DescribeStream`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStream.html)
+ [`kinesis:DescribeStreamSummary`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStreamSummary.html)
+ [`kinesis:GetRecords`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetRecords.html)
+ [`kinesis:GetShardIterator`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html)
+ [`kinesis:ListShards`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListShards.html)
+ [`kinesis:ListStreams`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreams.html)
+ [`kinesis:SubscribeToShard`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_SubscribeToShard.html)

To send records of failed batches to the pipe dead-letter queue, your pipe execution role needs the following permission:
+ [`sqs:SendMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html)

## Amazon MQ execution role permissions
<a name="pipes-perms-mq"></a>

For Amazon MQ, EventBridge Pipes requires the following permissions to manage resources that are related to your Amazon MQ message broker.
+ [`mq:DescribeBroker`](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers-broker-id.html#brokers-broker-id-http-methods)
+ [`secretsmanager:GetSecretValue`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html)
+ [`ec2:CreateNetworkInterface`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html)
+ [`ec2:DeleteNetworkInterface`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInterface.html)
+ [`ec2:DescribeNetworkInterfaces`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.html)
+ [`ec2:DescribeSecurityGroups`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html)
+ [`ec2:DescribeSubnets`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html)
+ [`ec2:DescribeVpcs`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcs.html)
+ [`logs:CreateLogGroup`](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.html)
+ [`logs:CreateLogStream`](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.html)
+ [`logs:PutLogEvents`](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html)

## Amazon MSK execution role permissions
<a name="pipes-perms-msk"></a>

For Amazon MSK, EventBridge requires the following permissions to manage resources that are related to your Amazon MSK topic.

**Note**  
If you're using IAM role-based authentication, your execution role will need the permissions listed in [IAM role-based authentication](eb-pipes-msk.md#pipes-msk-permissions-iam-policy) in addition the ones listed below.
+ [`kafka:DescribeClusterV2`](https://docs.aws.amazon.com/MSK/2.0/APIReference/v2-clusters-clusterarn.html#v2-clusters-clusterarnget)
+ [`kafka:GetBootstrapBrokers`](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-bootstrap-brokers.html#clusters-clusterarn-bootstrap-brokersget)
+ [`ec2:CreateNetworkInterface`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html)
+ [`ec2:DescribeNetworkInterfaces`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.html)
+ [`ec2:DescribeVpcs`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcs.html)
+ [`ec2:DeleteNetworkInterface`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInterface.html)
+ [`ec2:DescribeSubnets`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html)
+ [`ec2:DescribeSecurityGroups`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html)
+ [`logs:CreateLogGroup`](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.html)
+ [`logs:CreateLogStream`](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.html)
+ [`logs:PutLogEvents`](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html)

## Self managed Apache Kafka execution role permissions
<a name="pipes-perms-kafka"></a>

For self managed Apache Kafka, EventBridge requires the following permissions to manage resources that are related to your self managed Apache Kafka stream.

### Required permissions
<a name="pipes-perms-kafka-req"></a>

To create and store logs in a log group in Amazon CloudWatch Logs, your pipe must have the following permissions in its execution role:
+ [`logs:CreateLogGroup`](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.html)
+ [`logs:CreateLogStream`](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.html)
+ [`logs:PutLogEvents`](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html)

### Optional permissions
<a name="pipes-perms-kafka-optional"></a>

Your pipe might also need permissions to:
+ Describe your Secrets Manager secret.
+ Access your AWS Key Management Service (AWS KMS) customer managed key.
+ Access your Amazon VPC.

### Secrets Manager and AWS KMS permissions
<a name="pipes-perms-kafka-sm-kms"></a>

Depending on the type of access control that you're configuring for your Apache Kafka brokers, your pipe might need permission to access your Secrets Manager secret or to decrypt your AWS KMS customer managed key. To access these resources, your function's execution role must have the following permissions:
+ [`secretsmanager:GetSecretValue`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html)
+ [`kms:Decrypt`](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html)

### VPC permissions
<a name="pipes-perms-kafka-vpc"></a>

If only users within a VPC can access your self managed Apache Kafka cluster, your pipe must have permission to access your Amazon VPC resources. These resources include your VPC, subnets, security groups, and network interfaces. To access these resources, your pipe's execution role must have the following permissions:
+ [`ec2:CreateNetworkInterface`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html)
+ [`ec2:DescribeNetworkInterfaces`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.html)
+ [`ec2:DescribeVpcs`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcs.html)
+ [`ec2:DeleteNetworkInterface`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInterface.html)
+ [`ec2:DescribeSubnets`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html)
+ [`ec2:DescribeSecurityGroups`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html)

## Amazon SQS execution role permissions
<a name="pipes-perms-sqs"></a>

For Amazon SQS, EventBridge requires the following permissions to manage resources that are related to your Amazon SQS queue. 
+ [`sqs:ReceiveMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html)
+ [`sqs:DeleteMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.html)
+ [`sqs:GetQueueAttributes`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html)

## Enrichment and target permissions
<a name="pipes-perms-enhance-target"></a>

To make API calls on the resources that you own, EventBridge Pipes needs appropriate permission. EventBridge Pipes uses the IAM role that you specify on the pipe for enrichment and target calls using the IAM principal `pipes.amazonaws.com`. 