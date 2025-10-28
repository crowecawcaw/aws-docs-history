# Encryption of knowledge base resources

Amazon Bedrock encrypts resources related to your knowledge bases. By default,
Amazon Bedrock encrypts this data using an AWS-owned key. Optionally, you can encrypt the
model artifacts using a customer managed key.

Encryption with a KMS key can occur with the following processes:

- Transient data storage while ingesting your data sources
- Passing information to OpenSearch Service if you let Amazon Bedrock set up your vector database
- Querying a knowledge base
  The following resources used by your knowledge bases can be encrypted with a KMS key. If you encrypt them, you need to add permissions to decrypt the KMS key.

- Data sources stored in an Amazon S3 bucket
- Third-party vector stores
  For more information about AWS KMS keys, see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the
  _AWS Key Management Service Developer Guide_.

###### Note

Amazon Bedrock knowledge bases uses TLS encryption for communication with third-party data source connectors
and vector stores where the provider permits and supports TLS encryption in transit.

###### Topics

- [Encryption of transient data storage during data ingestion](#encryption-kb-ingestion "#encryption-kb-ingestion")
- [Encryption of information passed to Amazon OpenSearch Service](#encryption-kb-oss "#encryption-kb-oss")
- [Encryption of information passed to Amazon S3 Vectors](#encryption-kb-s3-vector "#encryption-kb-s3-vector")
- [Encryption of knowledge base retrieval](#encryption-kb-runtime "#encryption-kb-runtime")
- [Permissions to decrypt your AWS KMS key for your data sources in
  Amazon S3](#encryption-kb-ds "#encryption-kb-ds")
- [Permissions to decrypt an AWS Secrets Manager secret for the vector store containing your knowledge base](#encryption-kb-3p "#encryption-kb-3p")

## Encryption of transient data storage during data ingestion

When you set up a data ingestion job for your knowledge base, you can encrypt the job with a custom KMS key.

To allow the creation of a AWS KMS key for transient data storage in the process of ingesting your data source, attach the following policy to your Amazon Bedrock service role. Replace the example values with your own AWS Region, account ID, and AWS KMS key ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ]
 }
 ]
}`

```

## Encryption of information passed to Amazon OpenSearch Service

If you opt to let Amazon Bedrock create a vector store in Amazon OpenSearch Service for your knowledge base, Amazon Bedrock
can pass a KMS key that you choose to Amazon OpenSearch Service for encryption. To learn more about encryption
in Amazon OpenSearch Service, see [Encryption in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/serverless-encryption.md "../../../opensearch-service/latest/developerguide/serverless-encryption.md").

## Encryption of information passed to Amazon S3 Vectors

If you opt to let Amazon Bedrock create an S3 vector bucket and vector index in Amazon S3 Vectors for your
knowledge base, Amazon Bedrock can pass a KMS key that you choose to Amazon S3 Vectors for encryption. To learn more
about encryption in Amazon S3 Vectors, see [Encryption with Amazon S3 Vectors](../../../AmazonS3/latest/userguide/s3-vectors-bucket-encryption.md "../../../AmazonS3/latest/userguide/s3-vectors-bucket-encryption.md").

###### Important

The Amazon S3 Vectors integration with Amazon Bedrock Knowledge Bases is in preview release
and is subject to change.

## Encryption of knowledge base retrieval

You can encrypt sessions in which you generate responses from querying a knowledge base with a KMS key. To do so, include the ARN of a KMS key in the `kmsKeyArn` field when making a [RetrieveAndGenerate](../APIReference/API_agent-runtime_RetrieveAndGenerate.md "../APIReference/API_agent-runtime_RetrieveAndGenerate.md") request. Attach the following policy, replacing the example values with your own AWS Region, account ID, and AWS KMS key ID to allow Amazon Bedrock to encrypt the session context.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "bedrock.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 }
 ]
}`

```

## Permissions to decrypt your AWS KMS key for your data sources in

Amazon S3

You store the data sources for your knowledge base in your Amazon S3 bucket. To encrypt these documents at rest, you
can use the Amazon S3 SSE-S3 server-side encryption option. With this option, objects are
encrypted with service keys managed by the Amazon S3 service.

For more information, see [Protecting data using server-side encryption with Amazon S3-managed encryption keys
(SSE-S3)](../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md "../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md") in the _Amazon Simple Storage Service User Guide_.

If you encrypted your data sources in Amazon S3 with a custom AWS KMS key, attach the following policy to your Amazon Bedrock service role to allow Amazon Bedrock to decrypt your key. Replace the example values with your own AWS Region, account ID, and AWS KMS key ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "KMS:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringEquals": {
 "kms:ViaService": [
 "s3.us-east-1.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

## Permissions to decrypt an AWS Secrets Manager secret for the vector store containing your knowledge base

If the vector store containing your knowledge base is configured with an AWS Secrets Manager secret, you can encrypt the secret with a custom AWS KMS key by following the steps at [Secret encryption and decryption in AWS Secrets Manager](../../../secretsmanager/latest/userguide/security-encryption.md "../../../secretsmanager/latest/userguide/security-encryption.md").

If you do so, you attach the following policy to your Amazon Bedrock service role to allow it to decrypt your key. Replace the example values with your own AWS Region, account ID, and AWS KMS key ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ]
 }
 ]
}`

```
