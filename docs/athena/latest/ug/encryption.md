# Encryption at rest

You can run queries in Amazon Athena on encrypted data in Amazon S3 in the same Region and
across a limited number of Regions. You can also encrypt the query results in Amazon S3 and
the data in the AWS Glue Data Catalog.

You can encrypt the following assets in Athena:

- The results of all queries in Amazon S3, which Athena stores in a location known as
  the Amazon S3 results location. You can encrypt query results stored in Amazon S3 whether
  the underlying dataset is encrypted in Amazon S3 or not. For information, see [Encrypt Athena query results
  stored in Amazon S3](encrypting-query-results-stored-in-s3.md "encrypting-query-results-stored-in-s3.md").
- The data in the AWS Glue Data Catalog. For information, see [Permissions to encrypted metadata in the AWS Glue
  Data Catalog](#glue-encryption "#glue-encryption").

###### Note

When you use Athena to read an encrypted table, Athena uses the encryption options
specified for the table data, not the encryption option for the query results. If
separate encryption methods or keys are configured for query results and table data,
Athena reads the table data without using the encryption option and key used to
encrypt or decrypt the query results.

However, if you use Athena to insert data into a table that has encrypted data,
Athena uses the encryption configuration that was specified for the query results to
encrypt the inserted data. For example, if you specify `CSE_KMS`
encryption for query results, Athena uses the same AWS KMS key ID that you used for
query results encryption to encrypt the inserted table data with
`CSE_KMS`.

###### Topics

- [Supported Amazon S3 encryption
  options](#encryption-options-S3-and-Athena "#encryption-options-S3-and-Athena")
- [Permissions to
  encrypted data in Amazon S3](#permissions-for-encrypting-and-decrypting-data "#permissions-for-encrypting-and-decrypting-data")
- [Permissions to encrypted metadata in the AWS Glue
  Data Catalog](#glue-encryption "#glue-encryption")
- [Migrate from CSE-KMS to SSE-KMS](migrating-csekms-ssekms.md "migrating-csekms-ssekms.md")
- [Encrypt Athena query results
  stored in Amazon S3](encrypting-query-results-stored-in-s3.md "encrypting-query-results-stored-in-s3.md")
- [Create tables
  based on encrypted datasets in Amazon S3](creating-tables-based-on-encrypted-datasets-in-s3.md "creating-tables-based-on-encrypted-datasets-in-s3.md")

## Supported Amazon S3 encryption

options

Athena supports the following encryption options for datasets and query results in
Amazon S3.

| Encryption type                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Cross-Region support |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| [SSE-S3](../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md "../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md")                                                                                                          | Server side encryption (SSE) with an Amazon S3-managed key.                                                                                                                                                                                                                                                                                                                                                                                                                                                | Yes                  |
| [SSE-KMS](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md")<br>(Recommended)                                                                                                      | Server-side encryption (SSE) with an AWS Key Management Service customer managed key.                                                                                                                                                                                                                                                                                                                                                                                                                      | Yes                  |
| [CSE-KMS](../../../AmazonS3/latest/userguide/UsingClientSideEncryption.md#client-side-encryption-kms-managed-master-key-intro "../../../AmazonS3/latest/userguide/UsingClientSideEncryption.md#client-side-encryption-kms-managed-master-key-intro") | Client-side encryption (CSE) with a AWS KMS customer managed key. In<br>Athena, this option requires that you use a `CREATE<br>TABLE` statement with a `TBLPROPERTIES`<br>clause that specifies `'has_encrypted_data'='true'`<br>or `'encryption_option'='CSE_KMS'` with `'kms_key'='kms_key_arn'`.<br>For more information, see [Create tables<br>based on encrypted datasets in Amazon S3](creating-tables-based-on-encrypted-datasets-in-s3.md "creating-tables-based-on-encrypted-datasets-in-s3.md"). | No                   |

For more information about AWS KMS encryption with Amazon S3, see [What is AWS Key Management Service](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") and [How Amazon Simple Storage Service (Amazon S3) uses AWS KMS](../../../kms/latest/developerguide/services-s3.md "../../../kms/latest/developerguide/services-s3.md") in
the _AWS Key Management Service Developer Guide_. For more information about using SSE-KMS
or CSE-KMS with Athena, see [Launch:
Amazon Athena adds support for querying encrypted data](https://aws.amazon.com/blogs/aws/launch-amazon-athena-adds-support-for-querying-encrypted-data/ "https://aws.amazon.com/blogs/aws/launch-amazon-athena-adds-support-for-querying-encrypted-data/") from the _AWS Big Data Blog_.

### Encryption recommendations

When you encrypt and decrypt table data and query results with customer-managed
KMS keys, we recommend that you use SSE-KMS encryption over SSE-S3 or CSE-KMS
encryption methods. SSE-KMS provides a balance of control, simplicity, and
performance that makes it a recommended method when you use managed KMS keys for
data encryption.

**Benefits of SSE-KMS over SSE-S3**

- SSE-KMS allows you to specify and manage your own keys, providing
  greater control. You can define key policies, oversee key life cycles,
  and monitor key usage.

**Benefits of SSE-KMS over CSE-KMS**

- SSE-KMS eliminates the need for additional infrastructure to encrypt and
  decrypt data, unlike CSE-KMS which requires ongoing maintenance of an S3
  encryption client.
- CSE-KMS might face compatibility issues between newer and older S3
  encryption clients due to evolving encryption algorithms, a problem
  SSE-KMS avoids.
- SSE-KMS makes fewer API calls to the KMS service for key retrieval during
  the encryption and decryption processes, resulting in better performance
  compared to CSE-KMS.

### Unsupported options

The following encryption options aren't supported:

- SSE with customer-provided keys (SSE-C).
- Client-side encryption using a client-side managed key.
- Asymmetric keys.

To compare Amazon S3 encryption options, see [Protecting data using
encryption](../../../AmazonS3/latest/userguide/UsingEncryption.md "../../../AmazonS3/latest/userguide/UsingEncryption.md") in the _Amazon Simple Storage Service User Guide_.

### Tools for client-side

encryption

For client-side encryption, note that two tools are available:

- [Amazon S3 encryption client](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/AmazonS3EncryptionClient.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/AmazonS3EncryptionClient.md") – This encrypts data for Amazon S3
  only and is supported by Athena.
- [AWS Encryption SDK](../../../encryption-sdk/latest/developer-guide/introduction.md "../../../encryption-sdk/latest/developer-guide/introduction.md") – The SDK can be used to encrypt
  data anywhere across AWS but is not directly supported by
  Athena.

These tools aren't compatible, and data encrypted using one tool cannot be
decrypted by the other. Athena only supports the Amazon S3 Encryption Client directly.
If you use the SDK to encrypt your data, you can run queries from Athena, but the
data is returned as encrypted text.

If you want to use Athena to query data that has been encrypted with the AWS
Encryption SDK, you must download and decrypt your data, and then encrypt it
again using the Amazon S3 Encryption Client.

## Permissions to

encrypted data in Amazon S3

Depending on the type of encryption you use in Amazon S3, you might need to add
permissions, also known as "Allow" actions, to your policies used in Athena:

- SSE-S3 – If you use SSE-S3 for
  encryption, Athena users require no additional permissions in their policies.
  It is sufficient to have the appropriate Amazon S3 permissions for the
  appropriate Amazon S3 location and for Athena actions. For more information about
  policies that allow appropriate Athena and Amazon S3 permissions, see [AWS managed policies for Amazon Athena](managed-policies.md "managed-policies.md") and [Control access to Amazon S3 from Athena](s3-permissions.md "s3-permissions.md").
- AWS KMS – If you use AWS KMS for
  encryption, Athena users must be allowed to perform particular AWS KMS actions
  in addition to Athena and Amazon S3 permissions. You allow these actions by
  editing the key policy for the customer managed key that are used to encrypt data in
  Amazon S3. To add key users to the appropriate AWS KMS key policies, you can use
  the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms"). For information about how to add a
  user to a AWS KMS key policy, see [Allows key users to use the customer managed key](../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-users "../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-users") in the
  _AWS Key Management Service Developer Guide_.

###### Note

Advanced key policy administrators can adjust key policies.
`kms:Decrypt` is the minimum allowed action for an Athena
user to work with an encrypted dataset. To work with encrypted query
results, the minimum allowed actions are
`kms:GenerateDataKey` and
`kms:Decrypt`.

When using Athena to query datasets in Amazon S3 with a large number of objects
that are encrypted with AWS KMS, AWS KMS might throttle query results. This is
more likely when there are a large number of small objects. Athena backs off
retry requests, but a throttling error might still occur. If you are working
with a large number of encrypted objects and experience this issue, one
option is to enable Amazon S3 bucket keys to reduce the number of calls to KMS.
For more information, see [Reducing the cost of
SSE-KMS with Amazon S3 Bucket keys](../../../AmazonS3/latest/userguide/bucket-key.md "../../../AmazonS3/latest/userguide/bucket-key.md") in the _Amazon Simple Storage Service User Guide_. Another option is to increase your service
quotas for AWS KMS. For more information, see [Quotas](../../../kms/latest/developerguide/limits.md#requests-per-second "../../../kms/latest/developerguide/limits.md#requests-per-second") in the
_AWS Key Management Service Developer Guide_.

For troubleshooting information about permissions when using Amazon S3 with Athena, see
the [Permissions](troubleshooting-athena.md#troubleshooting-athena-permissions "troubleshooting-athena.md#troubleshooting-athena-permissions") section of the [Troubleshoot issues in Athena](troubleshooting-athena.md "troubleshooting-athena.md")
topic.

## Permissions to encrypted metadata in the AWS Glue

Data Catalog

If you [encrypt metadata in
the AWS Glue Data Catalog](../../../glue/latest/dg/encrypt-glue-data-catalog.md "../../../glue/latest/dg/encrypt-glue-data-catalog.md"), you must add `"kms:GenerateDataKey"`,
`"kms:Decrypt"`, and `"kms:Encrypt"` actions to the
policies you use for accessing Athena. For information, see [Configure access from Athena to
encrypted metadata in the AWS Glue Data Catalog](access-encrypted-data-glue-data-catalog.md "access-encrypted-data-glue-data-catalog.md").
