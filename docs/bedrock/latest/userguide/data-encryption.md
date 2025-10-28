# Data encryption

Amazon Bedrock uses encryption to protect data at rest and data in transit.

**Encryption in transit**

Within AWS, all inter-network data in transit supports TLS 1.2 encryption.

Requests to the Amazon Bedrock API and console are made over a secure (SSL) connection. You
pass AWS Identity and Access Management (IAM) roles to Amazon Bedrock to provide permissions to access resources on your
behalf for training and deployment.

**Encryption at rest**

Amazon Bedrock provides [Encryption of custom models](encryption-custom-job.md "encryption-custom-job.md") at rest.

## Key management

Use the AWS Key Management Service to manage the keys that you use to encrypt your resources. For more information, see [AWS Key Management Service
concepts](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys"). You can encrypt the following resources with a KMS key.

- Through Amazon Bedrock
  - Model customization jobs and their output custom models – During job creation in the console or by specifying the `customModelKmsKeyId` field in the [CreateModelCustomizationJob](../APIReference/API_CreateModelCustomizationJob.md "../APIReference/API_CreateModelCustomizationJob.md") API call.
  - Agents – During agent creation in the console or by specifying the `customerEncryptionKeyArn` field in the [CreateAgent](../APIReference/API_agent_CreateAgent.md "../APIReference/API_agent_CreateAgent.md") API call.
  - Data source ingestion jobs for knowledge bases – During knowledge base creation in the console or by specifying the `kmsKeyArn` field in the [CreateDataSource](../APIReference/API_agent_CreateDataSource.md "../APIReference/API_agent_CreateDataSource.md") or [UpdateDataSource](../APIReference/API_agent_UpdateDataSource.md "../APIReference/API_agent_UpdateDataSource.md") API call.
  - Vector stores in Amazon OpenSearch Service – During vector store creation. For more information, see [Creating, listing, and deleting Amazon OpenSearch Service collections](../../../opensearch-service/latest/developerguide/serverless-manage.md "../../../opensearch-service/latest/developerguide/serverless-manage.md") and [Encryption of data at rest for Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/encryption-at-rest.md "../../../opensearch-service/latest/developerguide/encryption-at-rest.md").
  - Model evaluations jobs – When you create a model evaluation job in console or by specify a key ARN in `customerEncryptionKeyId` in the [CreateEvaluationJob](../APIReference/API_CreateEvaluationJob.md "../APIReference/API_CreateEvaluationJob.md") API call.

- Through Amazon S3 – For more information, see [Using server-side encryption with AWS KMS keys (SSE-KMS).](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md")
  - Training, validation, and output data for model customization
  - Data sources for knowledge bases

- Through AWS Secrets Manager – For more information, see [Secret encryption and decryption in AWS Secrets Manager](../../../secretsmanager/latest/userguide/security-encryption.md "../../../secretsmanager/latest/userguide/security-encryption.md")
  - Vector stores for third-party models

After you encrypt a resource, you can find the ARN of the KMS key by selecting a resource and viewing its **Details** in the console or by using the following `Get` API calls.

- [GetModelCustomizationJob](../APIReference/API_GetModelCustomizationJob.md "../APIReference/API_GetModelCustomizationJob.md")
- [GetAgent](../APIReference/API_agent_GetAgent.md "../APIReference/API_agent_GetAgent.md")
- [GetIngestionJob](../APIReference/API_agent_GetIngestionJob.md "../APIReference/API_agent_GetIngestionJob.md")
