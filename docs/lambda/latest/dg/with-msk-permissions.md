# Configuring Lambda execution role permissions

To access the Amazon MSK cluster, your function and event source mapping need permissions to perform various Amazon MSK API actions.
Add these permissions to the function's [execution role](lambda-intro-execution-role.md "lambda-intro-execution-role.md"). If your users
need access, add the required permissions to the identity policy for the user or role.

To cover all required permissions, you can attach the [AWSLambdaMSKExecutionRole](../../../aws-managed-policy/latest/reference/AWSLambdaMSKExecutionRole.md "../../../aws-managed-policy/latest/reference/AWSLambdaMSKExecutionRole.md") managed policy
to your execution role. Alternatively, you can add each permission manually.

###### Topics

- [Basic permissions](#msk-basic-permissions "#msk-basic-permissions")
- [Cluster access permissions](#msk-cluster-access-permissions "#msk-cluster-access-permissions")
- [VPC permissions](#msk-vpc-permissions "#msk-vpc-permissions")
- [Optional permissions](#msk-optional-permissions "#msk-optional-permissions")

## Basic permissions

Your Lambda function execution role must have the following required permissions to create and store logs in CloudWatch Logs.

- [logs:CreateLogGroup](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md")
- [logs:CreateLogStream](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md")
- [logs:PutLogEvents](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md")

## Cluster access permissions

For Lambda to access your Amazon MSK cluster on your behalf, your Lambda function must have the following permissions in
its execution role:

- [kafka:DescribeCluster](../../../msk/1.0/apireference/clusters-clusterarn.md "../../../msk/1.0/apireference/clusters-clusterarn.md")
- [kafka:DescribeClusterV2](../../../MSK/2.0/APIReference/v2-clusters-clusterarn.md "../../../MSK/2.0/APIReference/v2-clusters-clusterarn.md")
- [kafka:GetBootstrapBrokers](../../../msk/1.0/apireference/clusters-clusterarn-bootstrap-brokers.md "../../../msk/1.0/apireference/clusters-clusterarn-bootstrap-brokers.md")
- [kafka:DescribeVpcConnection](../../../msk/1.0/apireference/vpc-connection-arn.md "../../../msk/1.0/apireference/vpc-connection-arn.md"):
  Only required for cross-account event source mappings.
- [kafka:ListVpcConnections](../../../msk/1.0/apireference/vpc-connections.md "../../../msk/1.0/apireference/vpc-connections.md"):
  Not required in execution role, but required for an IAM principal that is creating a cross-account event source mapping.

You only need to add one of either [kafka:DescribeCluster](../../../msk/1.0/apireference/clusters-clusterarn.md "../../../msk/1.0/apireference/clusters-clusterarn.md") or [kafka:DescribeClusterV2](../../../MSK/2.0/APIReference/v2-clusters-clusterarn.md "../../../MSK/2.0/APIReference/v2-clusters-clusterarn.md"). For provisioned Amazon MSK clusters, either permission works. For serverless Amazon MSK clusters,
you must use [kafka:DescribeClusterV2](../../../MSK/2.0/APIReference/v2-clusters-clusterarn.md "../../../MSK/2.0/APIReference/v2-clusters-clusterarn.md").

###### Note

Lambda eventually plans to remove the [kafka:DescribeCluster](../../../msk/1.0/apireference/clusters-clusterarn.md "../../../msk/1.0/apireference/clusters-clusterarn.md") permission from the [AWSLambdaMSKExecutionRole](../../../aws-managed-policy/latest/reference/AWSLambdaMSKExecutionRole.md "../../../aws-managed-policy/latest/reference/AWSLambdaMSKExecutionRole.md") managed policy.
If you use this policy, migrate any applications using [kafka:DescribeCluster](../../../msk/1.0/apireference/clusters-clusterarn.md "../../../msk/1.0/apireference/clusters-clusterarn.md") to use [kafka:DescribeClusterV2](../../../MSK/2.0/APIReference/v2-clusters-clusterarn.md "../../../MSK/2.0/APIReference/v2-clusters-clusterarn.md") instead.

## VPC permissions

If your Amazon MSK cluster is in a private subnet of your VPC, your Lambda function must have additional permissions to
access your Amazon VPC resources. These include your VPC, subnets, security groups, and network interfaces. Your function's
execution role must have the following permissions:

- [ec2:CreateNetworkInterface](../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md "../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md")
- [ec2:DescribeNetworkInterfaces](../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md "../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md")
- [ec2:DescribeVpcs](../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md "../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md")
- [ec2:DeleteNetworkInterface](../../../AWSEC2/latest/APIReference/API_DeleteNetworkInterface.md "../../../AWSEC2/latest/APIReference/API_DeleteNetworkInterface.md")
- [ec2:DescribeSubnets](../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md "../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md")
- [ec2:DescribeSecurityGroups](../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md "../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md")

## Optional permissions

Your Lambda function might also need permissions to:

- Access your SCRAM secret, if you're using [SASL/SCRAM authentication](msk-cluster-auth.md#msk-sasl-scram "msk-cluster-auth.md#msk-sasl-scram"). This lets your function use a username and password to connect to Kafka.
- Describe your Secrets Manager secret, if you're using SASL/SCRAM or [mTLS authentication](msk-cluster-auth.md#msk-mtls "msk-cluster-auth.md#msk-mtls"). This allows your function to retrieve the credentials or certificates needed for secure connections.
- Access your AWS KMS customer-managed key, if you want to [encrypt your filter criteria](invocation-eventfiltering.md "invocation-eventfiltering.md"). This helps keep your message filtering rules secret.
- Access your schema registry secrets, if you're using a schema registry with authentication:
  - For AWS Glue Schema Registry: Your function needs `glue:GetRegistry` and `glue:GetSchemaVersion` permissions. These allow your function to look up and use the message format rules stored in AWS Glue.
  - For [Confluent Schema Registry](https://docs.confluent.io/platform/current/schema-registry/security/index.html "https://docs.confluent.io/platform/current/schema-registry/security/index.html") with `BASIC_AUTH` or `CLIENT_CERTIFICATE_TLS_AUTH`: Your function needs
    `secretsmanager:GetSecretValue` permission for the secret containing the authentication credentials. This lets your function retrieve the username/password or certificates needed to access the Confluent Schema Registry.
  - For private CA certificates: Your function needs secretsmanager:GetSecretValue permission for the secret containing the certificate. This allows your function to verify the identity of schema registries that use custom certificates.

These correspond to the following required permissions:

- [kafka:ListScramSecrets](../../../msk/1.0/apireference/clusters-clusterarn-scram-secrets.md "../../../msk/1.0/apireference/clusters-clusterarn-scram-secrets.md") - Allows listing of SCRAM secrets for Kafka authentication
- [secretsmanager:GetSecretValue](../../../secretsmanager/latest/apireference/API_GetSecretValue.md "../../../secretsmanager/latest/apireference/API_GetSecretValue.md") - Enables retrieval of secrets from Secrets Manager
- [kms:Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") - Permits decryption of encrypted data using AWS KMS
- [glue:GetRegistry](../../../glue/latest/webapi/API_GetRegistry.md "../../../glue/latest/webapi/API_GetRegistry.md") - Allows access to AWS Glue Schema Registry
- [glue:GetSchemaVersion](../../../glue/latest/webapi/API_GetSchemaVersion.md "../../../glue/latest/webapi/API_GetSchemaVersion.md") - Enables retrieval of specific schema versions from AWS Glue Schema Registry

Additionally, if you want to send records of failed invocations to an on-failure destination, you'll need the following permissions depending on the destination type:

- For Amazon SQS destinations: [sqs:SendMessage](../../../AWSSimpleQueueService/latest/APIReference/API_SendMessage.md "../../../AWSSimpleQueueService/latest/APIReference/API_SendMessage.md") - Allows sending messages to an Amazon SQS queue
- For Amazon SNS destinations: [sns:Publish](../../../sns/latest/api/API_Publish.md "../../../sns/latest/api/API_Publish.md") - Permits publishing messages to an Amazon SNS topic
- For Amazon S3 bucket destinations:
  [s3:PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md") and
  [s3:ListBucket](../../../AmazonS3/latest/API/API_ListBucket.md "../../../AmazonS3/latest/API/API_ListBucket.md") - Enables writing and listing objects in an Amazon S3 bucket

For troubleshooting authentication and authorization errors, see [Troubleshooting Kafka event source mapping errors](with-kafka-troubleshoot.md "with-kafka-troubleshoot.md").
