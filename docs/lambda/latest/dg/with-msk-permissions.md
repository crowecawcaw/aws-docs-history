# Configuring Lambda permissions for Amazon MSK event source mappings

To access the Amazon MSK cluster, your function and event source mapping need permissions to perform various Amazon MSK API actions.
Add these permissions to the function's [execution role](lambda-intro-execution-role.md "lambda-intro-execution-role.md"). If your users
need access, add the required permissions to the identity policy for the user or role.

The [AWSLambdaMSKExecutionRole](../../../aws-managed-policy/latest/reference/AWSLambdaMSKExecutionRole.md "../../../aws-managed-policy/latest/reference/AWSLambdaMSKExecutionRole.md") managed policy
contains the minimum required permissions for Amazon MSK Lambda event source mappings. To simplify the permissions process, you can:

- Attach the [AWSLambdaMSKExecutionRole](../../../aws-managed-policy/latest/reference/AWSLambdaMSKExecutionRole.md "../../../aws-managed-policy/latest/reference/AWSLambdaMSKExecutionRole.md") managed policy
  to your execution role.
- Let the Lambda console generate the permissions for you. When you [create an Amazon MSK event source mapping in the console](msk-esm-create.md#msk-console "msk-esm-create.md#msk-console"), Lambda evaluates your execution role and alerts you if any permissions are missing. Choose **Generate permissions** to automatically update your execution role. This doesn't work if you manually created or modified your execution role policies, or if the policies are attached to multiple roles. Note that additional permissions may still be required in your execution role when using advanced features such as [On-Failure Destination](kafka-on-failure.md "kafka-on-failure.md") or [AWS Glue Schema Registry](services-consume-kafka-events.md "services-consume-kafka-events.md").

###### Topics

- [Required permissions](#msk-required-permissions "#msk-required-permissions")
- [Optional permissions](#msk-optional-permissions "#msk-optional-permissions")

## Required permissions

Your Lambda function execution role must have the following required permissions for Amazon MSK event source mappings. These permissions are included in the [AWSLambdaMSKExecutionRole](../../../aws-managed-policy/latest/reference/AWSLambdaMSKExecutionRole.md "../../../aws-managed-policy/latest/reference/AWSLambdaMSKExecutionRole.md") managed policy.

### CloudWatch Logs permissions

The following permissions allow Lambda to create and store logs in Amazon CloudWatch Logs.

- [logs:CreateLogGroup](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md")
- [logs:CreateLogStream](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md")
- [logs:PutLogEvents](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md")

### MSK cluster permissions

The following permissions allow Lambda to access your Amazon MSK cluster on your behalf:

- [kafka:DescribeCluster](../../../msk/1.0/apireference/clusters-clusterarn.md "../../../msk/1.0/apireference/clusters-clusterarn.md")
- [kafka:DescribeClusterV2](../../../MSK/2.0/APIReference/v2-clusters-clusterarn.md "../../../MSK/2.0/APIReference/v2-clusters-clusterarn.md")
- [kafka:GetBootstrapBrokers](../../../msk/1.0/apireference/clusters-clusterarn-bootstrap-brokers.md "../../../msk/1.0/apireference/clusters-clusterarn-bootstrap-brokers.md")

We recommend using [kafka:DescribeClusterV2](../../../MSK/2.0/APIReference/v2-clusters-clusterarn.md "../../../MSK/2.0/APIReference/v2-clusters-clusterarn.md") instead of [kafka:DescribeCluster](../../../msk/1.0/apireference/clusters-clusterarn.md "../../../msk/1.0/apireference/clusters-clusterarn.md"). The v2 permission works with both provisioned and serverless Amazon MSK clusters. You only need one of these permissions in your policy.

### VPC permissions

The following permissions allow Lambda to create and manage network interfaces when connecting to your Amazon MSK cluster:

- [ec2:CreateNetworkInterface](../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md "../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md")
- [ec2:DescribeNetworkInterfaces](../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md "../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md")
- [ec2:DescribeVpcs](../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md "../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md")
- [ec2:DeleteNetworkInterface](../../../AWSEC2/latest/APIReference/API_DeleteNetworkInterface.md "../../../AWSEC2/latest/APIReference/API_DeleteNetworkInterface.md")
- [ec2:DescribeSubnets](../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md "../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md")
- [ec2:DescribeSecurityGroups](../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md "../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md")

## Optional permissions

Your Lambda function might also need permissions to:

- Access cross-account Amazon MSK clusters. For cross-account event source mappings, you need [kafka:DescribeVpcConnection](../../../msk/1.0/apireference/vpc-connection-arn.md "../../../msk/1.0/apireference/vpc-connection-arn.md") in the execution role. An IAM principal creating a cross-account event source mapping needs [kafka:ListVpcConnections](../../../msk/1.0/apireference/vpc-connections.md "../../../msk/1.0/apireference/vpc-connections.md").
- Access your SCRAM secret, if you're using [SASL/SCRAM authentication](msk-cluster-auth.md#msk-sasl-scram "msk-cluster-auth.md#msk-sasl-scram"). This lets your function use a username and password to connect to Kafka.
- Describe your Secrets Manager secret, if you're using SASL/SCRAM or [mTLS authentication](msk-cluster-auth.md#msk-mtls "msk-cluster-auth.md#msk-mtls"). This allows your function to retrieve the credentials or certificates needed for secure connections.
- Access your AWS KMS customer managed key, if your AWS Secrets Manager secret is encrypted with an AWS KMS customer managed key.
- Access your schema registry secrets, if you're using a schema registry with authentication:
  - For AWS Glue Schema Registry: Your function needs `glue:GetRegistry` and `glue:GetSchemaVersion` permissions. These allow your function to look up and use the message format rules stored in AWS Glue.
  - For [Confluent Schema Registry](https://docs.confluent.io/platform/current/schema-registry/security/index.html "https://docs.confluent.io/platform/current/schema-registry/security/index.html") with `BASIC_AUTH` or `CLIENT_CERTIFICATE_TLS_AUTH`: Your function needs
    `secretsmanager:GetSecretValue` permission for the secret containing the authentication credentials. This lets your function retrieve the username/password or certificates needed to access the Confluent Schema Registry.
  - For private CA certificates: Your function needs secretsmanager:GetSecretValue permission for the secret containing the certificate. This allows your function to verify the identity of schema registries that use custom certificates.

- Access Kafka cluster consumer groups and poll messages from the topic, if you're using IAM authentication for the event source mapping.

These correspond to the following required permissions:

- [kafka:ListScramSecrets](../../../msk/1.0/apireference/clusters-clusterarn-scram-secrets.md "../../../msk/1.0/apireference/clusters-clusterarn-scram-secrets.md") - Allows listing of SCRAM secrets for Kafka authentication
- [secretsmanager:GetSecretValue](../../../secretsmanager/latest/apireference/API_GetSecretValue.md "../../../secretsmanager/latest/apireference/API_GetSecretValue.md") - Enables retrieval of secrets from Secrets Manager
- [kms:Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") - Permits decryption of encrypted data using AWS KMS
- [glue:GetRegistry](../../../glue/latest/webapi/API_GetRegistry.md "../../../glue/latest/webapi/API_GetRegistry.md") - Allows access to AWS Glue Schema Registry
- [glue:GetSchemaVersion](../../../glue/latest/webapi/API_GetSchemaVersion.md "../../../glue/latest/webapi/API_GetSchemaVersion.md") - Enables retrieval of specific schema versions from AWS Glue Schema Registry
- [kafka-cluster:Connect](../../../service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.md "../../../service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.md") - Grants permission to connect and authenticate to the cluster
- [kafka-cluster:AlterGroup](../../../service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.md "../../../service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.md") - Grants permission to join groups on a cluster, equivalent to Apache Kafka's READ GROUP ACL
- [kafka-cluster:DescribeGroup](../../../service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.md "../../../service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.md") - Grants permission to describe groups on a cluster, equivalent to Apache Kafka's DESCRIBE GROUP ACL
- [kafka-cluster:DescribeTopic](../../../service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.md "../../../service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.md") - Grants permission to describe topics on a cluster, equivalent to Apache Kafka's DESCRIBE TOPIC ACL
- [kafka-cluster:ReadData](../../../service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.md "../../../service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.md") - Grants permission to read data from topics on a cluster, equivalent to Apache Kafka's READ TOPIC ACL

Additionally, if you want to send records of failed invocations to an on-failure destination, you'll need the following permissions depending on the destination type:

- For Amazon SQS destinations: [sqs:SendMessage](../../../AWSSimpleQueueService/latest/APIReference/API_SendMessage.md "../../../AWSSimpleQueueService/latest/APIReference/API_SendMessage.md") - Allows sending messages to an Amazon SQS queue
- For Amazon SNS destinations: [sns:Publish](../../../sns/latest/api/API_Publish.md "../../../sns/latest/api/API_Publish.md") - Permits publishing messages to an Amazon SNS topic
- For Amazon S3 bucket destinations:
  [s3:PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md") and
  [s3:ListBucket](../../../AmazonS3/latest/API/API_ListBucket.md "../../../AmazonS3/latest/API/API_ListBucket.md") - Enables writing and listing objects in an Amazon S3 bucket

For troubleshooting authentication and authorization errors, see [Troubleshooting Kafka event source mapping errors](with-kafka-troubleshoot.md "with-kafka-troubleshoot.md").
