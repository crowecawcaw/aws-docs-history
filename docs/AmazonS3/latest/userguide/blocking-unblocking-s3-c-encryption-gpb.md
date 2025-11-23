# Blocking or unblocking SSE-C for a general purpose bucket

Most modern use cases in Amazon S3 no longer use server-side encryption with customer-provided
keys (SSE-C) because it lacks the flexibility of server-side encryption with Amazon S3 managed
keys (SSE-S3) or server-side encryption with AWS KMS keys (SSE-KMS). SSE-C's requirement to
provide the encryption key each time you interact with your SSE-C encrypted data makes it
impractical to share your SSE-C key with other users, roles, or AWS services who read data from
your S3 buckets in order to operate on your data.

To limit the server-side encryption types you can use in your general purpose buckets, you can choose to block SSE-C write requests by updating your default encryption configuration for your buckets. This bucket-level configuration blocks requests to upload objects that specify SSE-C. When SSE-C is blocked for a bucket, any `PutObject`, `CopyObject`, `PostObject`, or Multipart Upload or replication requests that specify SSE-C encryption will be rejected with an HTTP 403 `AccessDenied` error.

This setting is a parameter on the `PutBucketEncryption` API and can also be updated using the S3 Console, AWS CLI, and AWS SDKs, if you have the `s3:PutEncryptionConfiguration` permission.

Valid values are `SSE-C`, which blocks SSE-C encryption for the general purpose bucket, and `NONE`, which allows the use SSE-C for writes to the bucket.

###### Important

Starting in April 2026, AWS will disable server-side encryption with customer-provided keys (SSE-C) for all new buckets. In addition, SSE-C encryption will be disabled for all existing buckets in AWS accounts that do not have any SSE-C encrypted data. With these changes, the few applications that need SSE-C encryption must deliberately enable the use SSE-C via the [PutBucketEncryption](../API/API_PutBucketEncryption.md "../API/API_PutBucketEncryption.md") API after creating the bucket. In these cases, you might need to update automation scripts, CloudFormation templates, or other infrastructure configuration tools to configure these settings. For more information, see the [AWS Storage Blog post](https://aws.amazon.com/blogs/storage/advanced-notice-amazon-s3-to-disable-the-use-of-sse-c-encryption-by-default-for-all-new-buckets-and-select-existing-buckets-in-april-2026/ "https://aws.amazon.com/blogs/storage/advanced-notice-amazon-s3-to-disable-the-use-of-sse-c-encryption-by-default-for-all-new-buckets-and-select-existing-buckets-in-april-2026/").

## Permissions

Use the `PutBucketEncryption` API or the S3 Console, AWS SDKs, or AWS CLI to block or unblock encryption types for a general purpose bucket. You must have the following permission:

- `s3:PutEncryptionConfiguration`

Use the `GetBucketEncryption` API or the S3 Console, AWS SDKs, or AWS CLI to view blocked encryption types for a general purpose bucket. You must have the following permission:

- `s3:GetEncryptionConfiguration`

## Considerations before blocking SSE-C encryption

After you block SSE-C for any bucket, the following encryption behavior applies:

- There is no
  change to the encryption of the objects that existed in the bucket before you blocked SSE-C
  encryption.
- After you block SSE-C encryption, you can continue to make GetObject and HeadObject
  requests on pre-existing objects encrypted with SSE-C as long as you provide the required SSE-C
  headers on the requests.
- When SSE-C is blocked for a bucket, any `PutObject`,
  `CopyObject`, `PostObject`, or Multipart Upload requests that
  specify SSE-C encryption will be rejected with an HTTP 403 `AccessDenied` error.
- If a destination bucket for replication has SSE-C blocked and the source objects being
  replicated are encrypted with SSE-C, the replication will fail with an HTTP 403
  `AccessDenied` error.

If you want to review if you're using SSE-C encryption in
any of your buckets before blocking this encryption type, you can use tools such as [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/") to monitor access to your data. This [blog post](https://aws.amazon.com/blogs/storage/auditing-amazon-s3-server-side-encryption-methods-for-object-uploads/ "https://aws.amazon.com/blogs/storage/auditing-amazon-s3-server-side-encryption-methods-for-object-uploads/") shows you how to audit
encryption methods for object uploads in real time. You can also reference this [re:Post article](https://repost.aws/articles/ARhGC12rOiTBCKHcAe9GZXCA/how-to-detect-existing-use-of-sse-c-in-your-amazon-s3-buckets "https://repost.aws/articles/ARhGC12rOiTBCKHcAe9GZXCA/how-to-detect-existing-use-of-sse-c-in-your-amazon-s3-buckets") to guide you through the querying S3 Inventory reports to see if you have any SSE-C
encrypted objects.

### Steps

You can block or unblock server-side encryption with customer-provided keys (SSE-C) for a general purpose bucket by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

To block or unblock SSE-C encryption for a bucket using the Amazon S3 console:

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   https://console.aws.amazon.com/s3/.
2. In the left navigation pane, choose **general purpose
   buckets**.
3. Select the bucket that you would like to block SSE-C encryption for.
4. Select the **Properties** tab for the bucket.
5. Navigate to the **Default Encryption** properties panel for the
   bucket and select **Edit**.
6. In the **Blocked encryption types** section, check the box next
   to **Server-side encryption with customer-provided keys (SSE-C)** to block SSE-C encryption or uncheck this box to allow SSE-C.
7. Select **Save Changes**.

To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

The following CLI example shows you how to block or unblock SSE-C encryption for a general purpose bucket by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.

**Request to block SSE-C encryption for a general purpose bucket:**

```
aws s3api put-bucket-encryption \
  --bucket amzn-s3-demo-bucket \
  --server-side-encryption-configuration '{
    "Rules": [{
      "BlockEncryptionTypes": {
        "EncryptionType": "SSE-C"
      }
    }]
  }'
```

**Request to enable the use of SSE-C encryption on a general purpose bucket:**

```
aws s3api put-bucket-encryption \
  --bucket amzn-s3-demo-bucket \
  --server-side-encryption-configuration '{
    "Rules": [{
      "BlockEncryptionTypes": {
        "EncryptionType": "NONE"
      }
    }]
  }'
```

SDK for Java 2.x
The following examples show you how to block or unblock SSE-C encryption writes to your general purpose buckets by using the AWS SDKs

**Example - PutBucketEncryption request setting the default encryption configuration to SSE-S3 and blocking SSE-C**

```
S3Client s3Client = ...;
ServerSideEncryptionByDefault defaultSse = ServerSideEncryptionByDefault
        .builder()
        .sseAlgorithm(ServerSideEncryption.AES256)
        .build();
BlockedEncryptionTypes blockedEncryptionTypes = BlockedEncryptionTypes
        .builder()
        .encryptionType(EncryptionType.SSE_C)
        .build();
ServerSideEncryptionRule rule = ServerSideEncryptionRule.builder()
        .applyServerSideEncryptionByDefault(defaultSse)
        .blockedEncryptionTypes(blockedEncryptionTypes)
        .build();
s3Client.putBucketEncryption(be -> be
        .bucket(bucketName)
        .serverSideEncryptionConfiguration(c -> c.rules(rule)));

```

**Example - PutBucketEncryption request setting the default encryption configuration to SSE-S3 and unblocking SSE-C**

```
S3Client s3Client = ...;
ServerSideEncryptionByDefault defaultSse = ServerSideEncryptionByDefault
        .builder()
        .sseAlgorithm(ServerSideEncryption.AES256)
        .build();
BlockedEncryptionTypes blockedEncryptionTypes = BlockedEncryptionTypes
        .builder()
        .encryptionType(EncryptionType.NONE)
        .build();
ServerSideEncryptionRule rule = ServerSideEncryptionRule.builder()
        .applyServerSideEncryptionByDefault(defaultSse)
        .blockedEncryptionTypes(blockedEncryptionTypes)
        .build();
s3Client.putBucketEncryption(be -> be
        .bucket(bucketName)
        .serverSideEncryptionConfiguration(c -> c.rules(rule)));
```

SDK for Python Boto3
**Example - PutBucketEncryption request setting the default encryption configuration to SSE-S3 and blocking SSE-C**

```
s3 = boto3.client("s3")
s3.put_bucket_encryption(
    Bucket="amzn-s3-demo-bucket",
    ServerSideEncryptionConfiguration={
        "Rules":[{
            "ApplyServerSideEncryptionByDefault": {
                "SSEAlgorithm": "AES256"
            },
            "BlockedEncryptionTypes": {
                "EncryptionType": ["SSE-C"]
            }
        }]
    }
)
```

**Example - PutBucketEncryption request setting the default encryption configuration to SSE-S3 and unblocking SSE-C**

```
s3 = boto3.client("s3")
s3.put_bucket_encryption(
    Bucket="amzn-s3-demo-bucket",
    ServerSideEncryptionConfiguration={
        "Rules":[{
            "ApplyServerSideEncryptionByDefault": {
                "SSEAlgorithm": "AES256"
            },
            "BlockedEncryptionTypes": {
                "EncryptionType": ["NONE"]
            }
        }]
    }
)
```

For information about the Amazon S3 REST API support for bloacking or unblocking SSE-C encryption for a general purpose bucket, see the following section in the _Amazon Simple Storage Service API Reference_:

- [BlockedEncryptionTypes](../API/API_BlockedEncryptionTypes.md "../API/API_BlockedEncryptionTypes.md") data type used in the [ServerSideEncryptionRule](../API/API_ServerSideEncryptionRule.md "../API/API_ServerSideEncryptionRule.md") data type of the [PutBucketEncryption](../API/API_PutBucketEncryption.md "../API/API_PutBucketEncryption.md") and [GetBucketEncryption](../API/API_GetBucketEncryption.md "../API/API_GetBucketEncryption.md") API operations.
