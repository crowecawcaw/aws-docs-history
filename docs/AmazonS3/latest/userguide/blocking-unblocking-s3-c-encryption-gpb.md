

# Blocking or unblocking SSE-C for a general purpose bucket
<a name="blocking-unblocking-s3-c-encryption-gpb"></a>

Starting April 2026, Amazon S3 automatically disables server-side encryption with customer-provided keys (SSE-C) for all new general purpose buckets. Amazon S3 also disabled SSE-C for existing buckets in accounts with no SSE-C encrypted objects. This means that by default, requests to upload objects using SSE-C are rejected with an HTTP 403 `AccessDenied` error.

SSE-C requires you to provide the encryption key with every request to read or write encrypted objects, making it difficult to share access with other users, roles, or AWS services that operate on your data. Most workloads use server-side encryption with Amazon S3 managed keys (SSE-S3) or AWS KMS keys (SSE-KMS) instead.

If your workload requires SSE-C, you can explicitly enable it by updating the default encryption configuration for your bucket. Conversely, if you have existing buckets where SSE-C is still allowed, you can block it to prevent new SSE-C uploads.

When SSE-C is blocked for a bucket, any `PutObject`, `CopyObject`, `PostObject`, Multipart Upload, or replication request that specifies SSE-C encryption will be rejected with an HTTP 403 `AccessDenied` error. Existing SSE-C encrypted objects in the bucket are unaffected, you can still read them with `GetObject` or `HeadObject` by providing the required SSE-C headers.

This setting is a parameter on the `PutBucketEncryption` API and can also be updated using the S3 console, AWS CLI, or AWS SDKs. You must have the `s3:PutEncryptionConfiguration` permission.

**Important**  
Amazon Simple Storage Service now applies a new default bucket security setting that automatically disables server-side encryption with customer-provided keys (SSE-C) for all new general purpose buckets. In April 2026, Amazon S3 deployed an update so all new general purpose buckets have SSE-C encryption disabled for all new write requests. For existing buckets in AWS accounts with no SSE-C encrypted objects, Amazon S3 also disabled SSE-C for all new write requests. With this change, applications that need SSE-C encryption must deliberately enable SSE-C by using the [PutBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html) API operation after creating a new bucket. For more information about this change, see [Default SSE-C setting for new buckets FAQ](default-s3-c-encryption-setting-faq.md).

## Permissions
<a name="bucket-encryption-permissions"></a>

Use the `PutBucketEncryption` API or the S3 Console, AWS SDKs, or AWS CLI to block or unblock encryption types for a general purpose bucket. You must have the following permission:
+ `s3:PutEncryptionConfiguration`

Use the `GetBucketEncryption` API or the S3 Console, AWS SDKs, or AWS CLI to view blocked encryption types for a general purpose bucket. You must have the following permission:
+ `s3:GetEncryptionConfiguration`

## Considerations before blocking SSE-C encryption
<a name="considerations-before-blocking-sse-c"></a>

After you block SSE-C for any bucket, the following encryption behavior applies:
+ There is no change to the encryption of the objects that existed in the bucket before you blocked SSE-C encryption.
+ After you block SSE-C encryption, you can continue to make GetObject and HeadObject requests on pre-existing objects encrypted with SSE-C as long as you provide the required SSE-C headers on the requests.
+ When SSE-C is blocked for a bucket, any `PutObject`, `CopyObject`, `PostObject`, or Multipart Upload requests that specify SSE-C encryption will be rejected with an HTTP 403 `AccessDenied` error.
+ If a destination bucket for replication has SSE-C blocked and the source objects being replicated are encrypted with SSE-C, the replication will fail with an HTTP 403 `AccessDenied` error.

If you want to review if you're using SSE-C encryption in any of your buckets before blocking this encryption type, you can use tools such as [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) to monitor access to your data. This [blog post](https://aws.amazon.com/blogs/storage/auditing-amazon-s3-server-side-encryption-methods-for-object-uploads/) shows you how to audit encryption methods for object uploads in real time. You can also reference this [re:Post article](https://repost.aws/articles/ARhGC12rOiTBCKHcAe9GZXCA/how-to-detect-existing-use-of-sse-c-in-your-amazon-s3-buckets) to guide you through the querying S3 Inventory reports to see if you have any SSE-C encrypted objects.

### Steps
<a name="block-sse-c-gpb-steps"></a>

You can block or unblock server-side encryption with customer-provided keys (SSE-C) for a general purpose bucket by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

### Using the S3 console
<a name="block-sse-c-gpb-console"></a>

To block or unblock SSE-C encryption for a bucket using the Amazon S3 console:

1. Sign in to the AWS Management Console and open the Amazon S3 console at https://console.aws.amazon.com/s3/.

1. In the left navigation pane, choose **general purpose buckets**.

1. Select the bucket that you would like to block SSE-C encryption for.

1. Select the **Properties** tab for the bucket.

1. Navigate to the **Default Encryption** properties panel for the bucket and select **Edit**.

1. In the **Blocked encryption types** section, check the box next to **Server-side encryption with customer-provided keys (SSE-C)** to block SSE-C encryption or uncheck this box to allow SSE-C.

1. Select **Save Changes**.

### Using the AWS CLI
<a name="block-sse-c-gpb-cli"></a>

To install the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

The following CLI example shows you how to block or unblock SSE-C encryption for a general purpose bucket by using the AWS CLI. To use the command replace the {{user input placeholders}} with your own information.

**Request to block SSE-C encryption for a general purpose bucket:**

```
aws s3api put-bucket-encryption \
  --bucket amzn-s3-demo-bucket \
  --server-side-encryption-configuration '{
    "Rules": [{
      "BlockedEncryptionTypes": {
        "EncryptionType": ["SSE-C"]
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
      "BlockedEncryptionTypes": {
        "EncryptionType": ["NONE"]
      }
    }]
  }'
```

## Using the AWS SDKs
<a name="block-sse-c-gpb-sdks"></a>

------
#### [ SDK for Java 2.x ]

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

------
#### [ SDK for Python Boto3 ]

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

------

## Using the REST API
<a name="bucket-tag-add-api"></a>

For information about the Amazon S3 REST API support for blocking or unblocking SSE-C encryption for a general purpose bucket, see the following section in the [Amazon Simple Storage Service API Reference](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html):
+ [BlockedEncryptionTypes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_BlockedEncryptionTypes.html) data type used in the [ServerSideEncryptionRule](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ServerSideEncryptionRule.html) data type of the [PutBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html) and [GetBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html) API operations.