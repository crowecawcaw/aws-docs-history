# Copying objects from or to a

directory bucket

The copy operation creates a copy of an object that is already stored in Amazon S3. You can
copy objects between directory buckets and general purpose buckets. You can also copy
objects within a bucket and across buckets of the same type, for example, from directory
bucket to directory bucket.

###### Note

Copying objects across different AWS Regions isn't supported when the source or destination bucket is in an AWS Local Zone. The
source and destination buckets must have the same parent AWS Region. The source and destination buckets can be different bucket location types (Availability Zone or Local Zone).

You can create a copy of object up to 5 GB in a single atomic operation. However, to copy

an object that is greater than 5 GB, you must use the multipart upload API operations. For
more information, see [Using multipart uploads with
directory buckets](s3-express-using-multipart-upload.md "s3-express-using-multipart-upload.md").

###### Permissions

To copy objects, you must have the following permissions:

- To copy objects from one directory bucket to another directory bucket, you
  must have the `s3express:CreateSession` permission.
- To copy objects from directory buckets to general purpose buckets, you must have the
  `s3express:CreateSession` permission and the
  `s3:PutObject` permission to write the object copy to the destination
  bucket.
- To copy objects from general purpose buckets to directory buckets, you must have the
  `s3express:CreateSession` permission and `s3:GetObject`
  permission to read the source object that is being copied.

For more information, see [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md")
in the _Amazon Simple Storage Service API Reference_.

###### Encryption

Amazon S3 automatically encrypts all new objects that are uploaded to an S3 bucket. The
default encryption configuration of an S3 bucket is always enabled and is at a minimum
set to server-side encryption with Amazon S3 managed keys (SSE-S3).

For directory buckets, SSE-S3 and server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS) are supported. When the destination bucket is a directory bucket, we recommend that the destination bucket's default encryption uses the desired encryption configuration and you don't override the bucket default encryption. Then, new objects
are automatically encrypted with the desired encryption settings. Also, S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets
to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md"). In this case, Amazon S3 makes a call to AWS KMS every time a copy request is made for a KMS-encrypted object. For more information about the encryption overriding behaviors in directory buckets, see [Specifying server-side encryption with AWS KMS for new object uploads](s3-express-specifying-kms-encryption.md "s3-express-specifying-kms-encryption.md").

For general purpose buckets, you can use
SSE-S3 (the default), server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS),
dual-layer server-side encryption with AWS KMS keys (DSSE-KMS), or server-side encryption with
customer-provided keys (SSE-C).

If you make a copy request that specifies to use DSSE-KMS or SSE-C for a directory
bucket (either the source or destination bucket), the response returns an error.

###### Tags

Directory buckets don't support tags. If you copy an object that has tags from a
general purpose bucket to a directory bucket, you receive an HTTP `501 (Not
 Implemented)` response. For more information, see [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") in
the _Amazon Simple Storage Service API Reference_.

###### ETags

Entity tags (ETags) for S3 Express One Zone are random alphanumeric strings and are not MD5
checksums. To help ensure object integrity, use additional checksums.

###### Additional checksums

S3 Express One Zone offers you the option to choose the checksum algorithm that is used to
validate your data during upload or download. You can select one of the following Secure
Hash Algorithms (SHA) or Cyclic Redundancy Check (CRC) data-integrity check algorithms:
CRC32, CRC32C, SHA-1, and SHA-256. MD5-based checksums are not supported with the
S3 Express One Zone storage class.

For more information, see [S3 additional checksum best
practices](s3-express-optimizing-performance.md#s3-express-optimizing-performance-checksums "s3-express-optimizing-performance.md#s3-express-optimizing-performance-checksums").

###### Supported features

For more information about which Amazon S3 features are supported for S3 Express One Zone, see
[Differences for directory buckets](s3-express-differences.md "s3-express-differences.md").

###### Note

The restrictions and limitations when you copy an object to a directory bucket with the console are as follows:

- The `Copy` action applies to all objects within the specified folders (prefixes). Objects added to these folders while the action is in progress might be affected.
- Objects encrypted with customer-provided encryption keys (SSE-C) cannot be
  copied by using the S3 console. To copy objects encrypted with SSE-C, use the
  AWS CLI, AWS SDK, or the Amazon S3 REST API.
- Copied objects will not retain the Object Lock settings from the original objects.
- If the bucket you are copying objects from uses the bucket owner enforced setting for S3 Object Ownership, object ACLs will not be copied to the specified destination.
- If you want to copy objects to a bucket that uses the bucket owner enforced setting for S3 Object Ownership, make sure that the source bucket also uses the bucket owner enforced setting, or remove any object ACL grants to other AWS accounts and groups.
- Objects copied from a general purpose bucket to a directory bucket will not retain object tags, ACLs, or Etag values. Checksum values can be copied, but are not equivalent to an Etag. The checksum value may change compared to when it was added.
- All objects copied to a directory bucket will be with the bucket owner enforced setting for S3 Object Ownership.

###### To copy an object from a general purpose bucket or a directory bucket to a directory

bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, the bucket type that you want to copy objects from:
   - To copy from a general purpose bucket, choose the **General purpose
     buckets** tab.
   - To copy from a directory bucket, choose the **Directory
     buckets** tab.

3. Choose the general purpose bucket or directory bucket that contains the objects that
   you want to copy.
4. Choose the **Objects** tab. On the **Objects** page,
   select the check box to the left of the names of the objects that you want to
   copy.
5. On the **Actions** menu, choose **Copy**.

The **Copy** page appears. 6. Under **Destination**, choose **Directory bucket**
for your destination type. To specify the destination path, choose **Browse
S3**, navigate to the destination, and then choose the option button to the
left of the destination. Choose **Choose destination** in the
lower-right corner.

Alternatively, enter the destination path. 7. Under **Additional copy settings**, choose whether you want to **Copy source settings**, **Don’t specify settings**, or **Specify settings**. **Copy source settings** is the default option. If you only want to copy the object without the source settings attributes, choose **Don’t specify settings**. Choose **Specify settings** to specify settings for server-side encryption, checksums, and metadata. 8. Choose **Copy** in the bottom-right corner. Amazon S3 copies your
objects to the destination.

###### Note

The restrictions and limitations when you copy an object to a general purpose bucket with the console are as follows:

- The `Copy` action applies to all objects within the specified folders (prefixes). Objects added to these folders while the action is in progress might be affected.
- Objects encrypted with customer-provided encryption keys (SSE-C) cannot be
  copied by using the S3 console. To copy objects encrypted with SSE-C, use the
  AWS CLI, AWS SDK, or the Amazon S3 REST API.
- Copied objects will not retain the Object Lock settings from the original objects.
- If the bucket you are copying objects from uses the bucket owner enforced setting for S3 Object Ownership, object ACLs will not be copied to the specified destination.
- If you want to copy objects to a bucket that uses the bucket owner enforced setting for S3 Object Ownership, make sure that the source bucket also uses the bucket owner enforced setting, or remove any object ACL grants to other AWS accounts and groups.

###### To copy an object from a directory bucket to a general purpose bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. Choose the **Directory buckets** tab.
4. Choose the directory bucket that contains the objects that you want to copy.
5. Choose the **Objects** tab. On the **Objects** page,
   select the check box to the left of the names of the objects that you want to
   copy.
6. On the **Actions** menu, choose **Copy**.
7. Under **Destination**, choose **General purpose
   bucket** for your destination type. To specify the destination path, choose
   **Browse S3**, navigate to the destination, and choose the option
   button to the left of the destination. Choose **Choose destination** in
   the lower-right corner.

Alternatively, enter the destination path. 8. Under **Additional copy settings**, choose whether you want to **Copy source settings**, **Don’t specify settings**, or **Specify settings**. **Copy source settings** is the default option. If you only want to copy the object without the source settings attributes, choose **Don’t specify settings**. Choose **Specify settings** to specify settings for storage class, ACLs, object tags, metadata, server-side encryption, and additional checksums. 9. Choose **Copy** in the bottom-right corner. Amazon S3 copies your
objects to the destination.

SDK for Java 2.x

```
 public static void copyBucketObject (S3Client s3, String sourceBucket, String objectKey, String targetBucket) {
      CopyObjectRequest copyReq = CopyObjectRequest.builder()
          .sourceBucket(sourceBucket)
          .sourceKey(objectKey)
          .destinationBucket(targetBucket)
          .destinationKey(objectKey)
          .build();
       String temp = "";

       try {
           CopyObjectResponse copyRes = s3.copyObject(copyReq);
           System.out.println("Successfully copied " + objectKey +" from bucket " + sourceBucket +" into bucket "+targetBucket);
       }

       catch (S3Exception e) {
           System.err.println(e.awsErrorDetails().errorMessage());
           System.exit(1);
       }
 }
```

The following `copy-object` example command shows how you can use the AWS CLI to
copy an object from one bucket to another bucket. You can copy objects between
bucket types. To run this command, replace the user input placeholders with your own information.

```
aws s3api copy-object --copy-source `SOURCE_BUCKET/SOURCE_KEY_NAME` --key `TARGET_KEY_NAME` --bucket `TARGET_BUCKET_NAME`

```

For more information, see [copy-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/copy-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/copy-object.html") in the
_AWS CLI Command Reference_.
