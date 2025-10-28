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
- [Troubleshooting common authentication and authorization errors](#msk-permissions-errors "#msk-permissions-errors")

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

## Troubleshooting common authentication and authorization errors

If any of the permissions required to consume data from the Amazon MSK cluster are missing, Lambda displays one of
the following error messages in the event source mapping under **LastProcessingResult**.
For more information about each supported authentication method, see [Configuring cluster authentication methods in Lambda](msk-cluster-auth.md "msk-cluster-auth.md").

###### Error messages

- [Cluster failed to authorize Lambda](#msk-authorize-errors "#msk-authorize-errors")
- [SASL authentication failed](#msk-sasl-errors "#msk-sasl-errors")
- [Server failed to authenticate Lambda](#msk-mtls-errors "#msk-mtls-errors")
- [Provided certificate or private key is invalid](#msk-key-errors "#msk-key-errors")

### Cluster failed to authorize Lambda

For SASL/SCRAM or mTLS, this error indicates that the provided user doesn't have all of the following
required Kafka access control list (ACL) permissions:

- DescribeConfigs Cluster
- Describe Group
- Read Group
- Describe Topic
- Read Topic

For IAM access control, your function's execution role is missing one or more of the permissions required
to access the group or topic. Review the list of required permissions on this page.

When you create either Kafka ACLs or an IAM policy with the required Kafka cluster permissions, specify
the topic and group as resources. The topic name must match the topic in the event source mapping. The group
name must match the event source mapping's UUID.

After you add the required permissions to the execution role, it might take several minutes for the changes
to take effect.

### SASL authentication failed

For SASL/SCRAM, this error indicates that the provided user name and password aren't valid.

For IAM access control, the execution role is missing the `kafka-cluster:Connect` permission
for the MSK cluster. Add this permission to the role and specify the cluster's Amazon Resource Name (ARN) as a
resource.

You might see this error occurring intermittently. The cluster rejects connections after the number of TCP
connections exceeds the [Amazon MSK service
quota](../../../msk/latest/developerguide/limits.md "../../../msk/latest/developerguide/limits.md"). Lambda backs off and retries until a connection is successful. After Lambda connects to the
cluster and polls for records, the last processing result changes to `OK`.

### Server failed to authenticate Lambda

This error indicates that the Amazon MSK Kafka brokers failed to authenticate with Lambda. This can occur for
any of the following reasons:

- You didn't provide a client certificate for mTLS authentication.
- You provided a client certificate, but the brokers aren't configured to use mTLS.
- A client certificate isn't trusted by the brokers.

### Provided certificate or private key is invalid

This error indicates that the Amazon MSK consumer couldn't use the provided certificate or private key. Make
sure that the certificate and key use PEM format, and that the private key encryption uses a PBES1
algorithm. See [Configuring the mTLS secret](msk-cluster-auth.md#mtls-auth-secret "msk-cluster-auth.md#mtls-auth-secret") for more information.
