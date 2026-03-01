# Data protection and encryption in S3 Vectors

Amazon S3 Vectors provides 99.999999999% (11 9s) of durability for your vector data, which
ensures exceptional reliability for your vector storage needs. This durability is backed by
the proven infrastructure of Amazon S3, which is designed to maintain data integrity and
availability even in the face of hardware failures or other disruptions.

Data protection in S3 Vectors encompasses multiple layers of security controls designed
to protect your vector data both at rest and in transit.

By default, all new vectors in Amazon S3 Vectors vector buckets use server-side
encryption with Amazon S3 managed keys (SSE-S3). When you create a vector bucket with SSE-S3
encryption, all subsequent operations on the bucket automatically use encryption.

S3 Vectors also integrates with AWS Key Management Service (KMS) to provide flexible
encryption key management options, allowing you to choose customer-managed keys for
permission control and auditability.

When creating a vector index within a vector bucket, you can optionally override the vector bucket level encryption settings and provide an encryption configuration (SSE-S3 or KMS) at the vector index level. If no specific encryption is specified upon vector index creation, the index will inherit the encryption configuration from the vector bucket it belongs to.

## Setting server-side encryption behavior for Amazon S3 vector buckets and indexes

Encryption configuration in S3 Vectors is a fundamental security setting to specify
when you create a vector bucket. This design ensures that all vector data stored in
the bucket is encrypted from the moment of creation. By default, the encryption configuration
applies to all vectors, vector indexes, and metadata within the bucket, providing
consistent protection across your entire vector dataset in a vector bucket. You can also optionally override the vector bucket level encryption settings and provide a dedicated encryption configuration (SSE-S3 or AWS KMS) at the vector index level.

###### Important

Encryption settings for a vector bucket can't be changed after the
vector bucket is created. You must carefully consider your encryption requirements
during the bucket creation process, including compliance requirements, key
management preferences, and integration with existing security
infrastructure.

When you set the SSE-S3 or SSE-KMS encryption type at the vector bucket level, by default it applies
to all vector indexes and vectors within the bucket. The encryption configuration
applies to not only the vector data itself but also all associated metadata.

You can also optionally override the vector bucket level encryption settings and provide a dedicated encryption configuration (SSE-S3 or KMS) at the vector index level. Encryption settings for a vector index can't be changed after the vector index is created.

### Using SSE-S3 encryption

Server-side encryption with Amazon S3 managed keys (SSE-S3) provides a simple and
effective encryption solution for vector buckets where AWS manages all aspects
of the encryption process. This encryption method uses `AES-256`
encryption and is designed to provide strong security with minimal operational
overhead, providing organizations with robust encryption without the complexity of
the needs to manage encryption keys.

With SSE-S3, Amazon S3 handles the generation, rotation, and management of encryption
keys automatically. SSE-S3 provides strong security with no additional configuration
or ongoing management requirements. The encryption and decryption processes are
handled automatically by the service, and there are no additional charges for using
SSE-S3 encryption beyond the standard S3 Vectors pricing.

### Using SSE-KMS encryption

Server-side encryption with AWS Key Management Service keys (SSE-KMS) provides
enhanced control over encryption keys and enables detailed audit logging of key
usage. This encryption method is ideal for organizations with strict compliance
requirements, those that need to implement custom key rotation policies, or
environments where detailed audit trails of data access are required.

SSE-KMS allows you to use customer managed keys (CMKs) for encrypting your vector
data. Customer managed keys provide the highest level of control, allowing you to
define key policies, enable or disable keys, and monitor key usage through AWS
CloudTrail. This level of control makes SSE-KMS particularly suitable for regulated
industries or organizations with specific data governance requirements.

When using SSE-KMS with customer managed keys, you have complete control over who
can use the keys to encrypt and decrypt data. You can create detailed key policies
that specify which users, roles, or services can access the keys.

#### Important considerations for SSE-KMS

- **KMS key format requirements:**
  S3 Vectors requires that you specify KMS keys using the full Amazon
  Resource Name (ARN) format. Key IDs or key aliases aren't
  supported.
- **Service principal permissions:** When
  you use customer managed keys with S3 Vectors, you must explicitly
  grant permissions to the S3 Vectors service principal to use your KMS
  key. This requirement ensures that the service can encrypt and decrypt
  your data on your behalf. The service principal that requires access is
  `indexing.s3vectors.amazonaws.com`.

**Example: KMS key policy for
S3 Vectors**

To use a customer managed KMS key with S3 Vectors, you must update your key
policy to include permissions for the S3 Vectors service principal. Here's a
comprehensive key policy example.

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowS3VectorsServicePrincipal",
            "Effect": "Allow",
            "Principal": {
                "Service": "indexing.s3vectors.amazonaws.com"
            },
            "Action": "kms:Decrypt",
            "Resource": "*",
            "Condition": {
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:s3vectors:``aws-region``:`123456789012`:bucket/*"
                },
                "StringEquals": {
                    "aws:SourceAccount": "`123456789012`"
                },
                "ForAnyValue:StringEquals": {
                    "kms:EncryptionContextKeys": ["aws:s3vectors:arn", "aws:s3vectors:resource-id"]
                }
            }
        },
        {
            "Sid": "AllowApplicationAccess",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam:`123456789012`:role/VectorApplicationRole",
                    "arn:aws:iam:`123456789012`:user/DataScientist"
                ]
            },
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "s3vectors.``aws-region``.amazonaws.com"
                },
                "ForAnyValue:StringEquals": {
                    "kms:EncryptionContextKeys": ["aws:s3vectors:arn", "aws:s3vectors:resource-id"]
                }
            }
        }
    ]
}

```

- **Required KMS permissions:**
  - S3 Vectors service principal permission:
    - `kms:Decrypt` – Required by the
      S3 Vectors service principal
      (`indexing.s3vectors.amazonaws.com`) on
      your customer managed key to maintain and optimize the
      index in background operations

  - IAM principal permissions:
    - `kms:Decrypt` – Required for all vector-level operations ([PutVectors](../API/API_S3VectorBuckets_PutVectors.md "../API/API_S3VectorBuckets_PutVectors.md"), [GetVectors](../API/API_S3VectorBuckets_GetVectors.md "../API/API_S3VectorBuckets_GetVectors.md"), [QueryVectors](../API/API_S3VectorBuckets_QueryVectors.md "../API/API_S3VectorBuckets_QueryVectors.md"), [DeleteVectors](../API/API_S3VectorBuckets_DeleteVectors.md "../API/API_S3VectorBuckets_DeleteVectors.md"), [ListVectors](../API/API_S3VectorBuckets_ListVectors.md "../API/API_S3VectorBuckets_ListVectors.md"))
    - `kms:GenerateDataKey` – Required to create a vector bucket by using the customer managed key

- **Cross-account access considerations:**
  When implementing cross-account access patterns with SSE-KMS, you must
  ensure that the KMS key policy allows access from the appropriate
  principals in other accounts. The key ARN format becomes particularly
  important in cross-account scenarios, as it provides an unambiguous
  reference to the key regardless of the account context from which it's
  being accessed.
