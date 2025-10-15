# Setting and monitoring default encryption for directory buckets

Amazon S3 buckets have bucket encryption enabled by default, and new objects are automatically
 encrypted by using server-side encryption with Amazon S3 managed keys (SSE-S3). This encryption
 applies to all new objects in your Amazon S3 buckets, and comes at no cost to you.

If you need more control over your encryption keys, such as managing key rotation and access
 policy grants, you can elect to use server-side encryption with AWS Key Management Service (AWS KMS) keys
 (SSE-KMS).

###### Note


* We recommend that the bucket's default encryption uses the desired encryption configuration and you don't override the bucket default encryption in your 
 `CreateSession` requests or `PUT` object requests. Then, new objects 
 are automatically encrypted with the desired encryption settings. For more information about the encryption overriding behaviors in directory buckets, see [Specifying server-side encryption with AWS KMS for new object uploads](s3-express-specifying-kms-encryption.md "s3-express-specifying-kms-encryption.md").
* To encrypt new objects in a directory bucket with SSE-KMS, you must specify SSE-KMS as the directory bucket's default encryption configuration with a KMS key (specifically, a customer managed key). Then, when a session is created for Zonal endpoint API operations, new objects are automatically encrypted and decrypted with SSE-KMS and S3 Bucket Keys during the session.
* When you set default bucket encryption to SSE-KMS, S3 Bucket Keys are always enabled for `GET` and `PUT` operations in a directory bucket and can’t be disabled. S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets 
to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md"), [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md"), [the Copy operation in Batch Operations](directory-buckets-objects-Batch-Ops.md "directory-buckets-objects-Batch-Ops.md"), or 
 [the import jobs](create-import-job.md "create-import-job.md"). In this case, Amazon S3 makes a call to AWS KMS every time a copy request is made for a KMS-encrypted object. For more information about how S3 Bucket Keys reduce your AWS KMS request costs, see [Reducing the cost of SSE-KMS with Amazon S3 Bucket Keys](bucket-key.md "bucket-key.md").
* When you specify an [AWS KMS customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk") for encryption in your directory bucket, only use the key ID or key ARN. The key alias format of the KMS key isn't supported.
* Dual-layer server-side encryption with AWS KMS keys (DSSE-KMS) and server-side encryption with customer-provided keys (SSE-C) aren't supported for default
 encryption in directory buckets.
For more information
 about configuring default encryption, see [Configuring default encryption](default-bucket-encryption.md "default-bucket-encryption.md").

For more information about the permissions required for default encryption, see [PutBucketEncryption](../API/API_PutBucketEncryption.md "../API/API_PutBucketEncryption.md") in the
 *Amazon Simple Storage Service API Reference*.

You can configure Amazon S3 default encryption for an S3 bucket by using the Amazon S3 console, the
 AWS SDKs, the Amazon S3 REST API, and the AWS Command Line Interface (AWS CLI).

###### To configure default encryption on an Amazon S3 bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. In the **Buckets** list, choose the name of the bucket that you
 want.
4. Choose the **Properties** tab.
5. Under **Server-side encryption settings**, directory buckets use 
 Server-side encryption with **Amazon S3 managed keys
 (SSE-S3)**.
6. Choose **Save changes**.
These examples show you how to configure default encryption by using SSE-S3 or by using
 SSE-KMS with an S3 Bucket Key.

For more information about default encryption, see [Setting default server-side encryption behavior for Amazon S3
 buckets](bucket-encryption.md "bucket-encryption.md"). For more information about using the AWS CLI to
 configure default encryption, see [put-bucket-encryption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-encryption.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-encryption.html").

###### Example – Default encryption with SSE-S3

This example configures default bucket encryption with Amazon S3 managed keys. To use the command, replace the `user input placeholders` 
 with your own information.


```
aws s3api put-bucket-encryption --bucket `bucket-base-name`--`zone-id`--x-s3 --server-side-encryption-configuration '{
    "Rules": [
        {
            "ApplyServerSideEncryptionByDefault": {
                "SSEAlgorithm": "AES256"
            }
        }
    ]
}'
```
###### Example – Default encryption with SSE-KMS using an S3 Bucket Key

This example configures default bucket encryption with SSE-KMS using an S3 Bucket Key. To use the command, replace the `user input placeholders` 
 with your own information.


```
aws s3api put-bucket-encryption --bucket `bucket-base-name`--`zone-id`--x-s3 --server-side-encryption-configuration '{
    "Rules": [
            {
                "ApplyServerSideEncryptionByDefault": {
                    "SSEAlgorithm": "aws:kms",
                    "KMSMasterKeyID": "`KMS-Key-ARN`"
                },
                "BucketKeyEnabled": true
            }
        ]
    }'
```
Use the REST API `PutBucketEncryption` operation to set default encryption
 with a type of server-side encryption to use — SSE-S3, or SSE-KMS. 

For more information, see [PutBucketEncryption](../API/RESTBucketPUTencryption.md "../API/RESTBucketPUTencryption.md") in the *Amazon Simple Storage Service API Reference*.

When using AWS SDKs, you can request Amazon S3 to use AWS KMS keys for server-side
 encryption. The following AWS SDKs for Java and
 .NET examples configure default encryption configuration for a directory bucket with SSE-KMS and an S3 Bucket Key. For information about other SDKs, see [Sample code
 and libraries](https://aws.amazon.com/code "https://aws.amazon.com/code") on the AWS Developer Center.

###### Important

When you use an AWS KMS key for server-side encryption in Amazon S3, you must choose a symmetric encryption KMS key. 
Amazon S3 supports only symmetric encryption KMS keys. For more information about these keys, see 
[Symmetric encryption KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#symmetric-cmks "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#symmetric-cmks") in the *AWS Key Management Service Developer Guide*.


Java
With the AWS SDK for Java 2.x, you can request Amazon S3 to use an
 AWS KMS key by using the `applyServerSideEncryptionByDefault` method to specify the default encryption configuration of your directory bucket for 
 data encryption with SSE-KMS. 
 
 You create a symmetric
 encryption KMS key and specify that in the request.



```

import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.PutBucketEncryptionRequest;
import software.amazon.awssdk.services.s3.model.ServerSideEncryption;
import software.amazon.awssdk.services.s3.model.ServerSideEncryptionByDefault;
import software.amazon.awssdk.services.s3.model.ServerSideEncryptionConfiguration;
import software.amazon.awssdk.services.s3.model.ServerSideEncryptionRule;

public class Main {
    public static void main(String[] args) {
        S3Client s3 = S3Client.create();
        String bucketName = "bucket-base-name--zoneid--x-s3";
        String kmsKeyId = "your-kms-customer-managed-key-id";

        // AWS managed KMS keys aren't supported. Only customer-managed keys are supported.
        ServerSideEncryptionByDefault serverSideEncryptionByDefault = ServerSideEncryptionByDefault.builder()
                .sseAlgorithm(ServerSideEncryption.AWS_KMS)
                .kmsMasterKeyID(kmsKeyId)
                .build();

        // The bucketKeyEnabled field is enforced to be true.
        ServerSideEncryptionRule rule = ServerSideEncryptionRule.builder()
                .bucketKeyEnabled(true)
                .applyServerSideEncryptionByDefault(serverSideEncryptionByDefault)
                .build();
  
        ServerSideEncryptionConfiguration serverSideEncryptionConfiguration = ServerSideEncryptionConfiguration.builder()
                .rules(rule)
                .build();

        PutBucketEncryptionRequest putRequest = PutBucketEncryptionRequest.builder()
                .bucket(bucketName)
                .serverSideEncryptionConfiguration(serverSideEncryptionConfiguration)
                .build();

        s3.putBucketEncryption(putRequest);
        
    }
}
                 
                            
```

For more information about creating customer managed keys, see [Programming the AWS KMS API](https://docs.aws.amazon.com/kms/latest/developerguide/programming-top.html "https://docs.aws.amazon.com/kms/latest/developerguide/programming-top.html") in
 the *AWS Key Management Service Developer Guide*.


For working code examples of uploading an object, see the following topics. To
 use these examples, you must update the code examples and provide encryption
 information as shown in the preceding code fragment.



* For uploading an object in a single operation, see [Uploading objects to a directory
 bucket](directory-buckets-objects-upload.md "directory-buckets-objects-upload.md").
* For multipart upload
 API operations, see [Using multipart uploads with
 directory buckets](s3-express-using-multipart-upload.md "s3-express-using-multipart-upload.md").


.NET
With the AWS SDK for .NET, you can request Amazon S3 to use an
 AWS KMS key by using the `ServerSideEncryptionByDefault` property to specify the default encryption configuration of your directory bucket for 
 data encryption with SSE-KMS. You create a symmetric encryption customer managed key and specify that in the
 request.



```

    // Set the bucket server side encryption to use AWSKMS with a customer-managed key id.
    // bucketName: Name of the directory bucket. "bucket-base-name--zonsid--x-s3"
    // kmsKeyId: The Id of the customer managed KMS Key. "your-kms-customer-managed-key-id"
    // Returns True if successful.
    public static async Task<bool> SetBucketServerSideEncryption(string bucketName, string kmsKeyId)
    {
        var serverSideEncryptionByDefault = new ServerSideEncryptionConfiguration
        {
            ServerSideEncryptionRules = new List<ServerSideEncryptionRule>
            {
                new ServerSideEncryptionRule
                {
                    ServerSideEncryptionByDefault = new ServerSideEncryptionByDefault
                    {
                        ServerSideEncryptionAlgorithm = ServerSideEncryptionMethod.AWSKMS,
                        ServerSideEncryptionKeyManagementServiceKeyId = kmsKeyId
                    }
                }
            }
        };
        try
        {
            var encryptionResponse =await _s3Client.PutBucketEncryptionAsync(new PutBucketEncryptionRequest
            {
                BucketName = bucketName,
                ServerSideEncryptionConfiguration = serverSideEncryptionByDefault,
            });
            
            return encryptionResponse.HttpStatusCode == HttpStatusCode.OK;
        }
        catch (AmazonS3Exception ex)
        {
            Console.WriteLine(ex.ErrorCode == "AccessDenied"
                ? $"This account does not have permission to set encryption on {bucketName}, please try again."
                : $"Unable to set bucket encryption for bucket {bucketName}, {ex.Message}");
        }
        return false;
    }
     
       
                            
```

For more information about creating customer managed keys, see [Programming the AWS KMS API](https://docs.aws.amazon.com/kms/latest/developerguide/programming-top.html "https://docs.aws.amazon.com/kms/latest/developerguide/programming-top.html") in
 the *AWS Key Management Service Developer Guide*. 


For working code examples of uploading an object, see the following topics. To
 use these examples, you must update the code examples and provide encryption
 information as shown in the preceding code fragment.



* For uploading an object in a single operation, see [Uploading objects to a directory
 bucket](directory-buckets-objects-upload.md "directory-buckets-objects-upload.md").
* For multipart upload
 API operations, see [Using multipart uploads with
 directory buckets](s3-express-using-multipart-upload.md "s3-express-using-multipart-upload.md").



## Monitoring default encryption for directory buckets with
 AWS CloudTrail


You can track default encryption configuration requests for Amazon S3 directory buckets by using AWS CloudTrail
 events. The following API event names are used in CloudTrail logs:



* `PutBucketEncryption`
* `GetBucketEncryption`
* `DeleteBucketEncryption`

###### Note


* EventBridge isn't supported in directory buckets.
* Dual-layer server-side encryption with AWS Key Management Service (AWS KMS) keys (DSSE-KMS) or server-side encryption with customer-provided encryption keys (SSE-C) aren't supported in directory buckets.

For more information about monitoring default encryption with
 AWS CloudTrail, see [Monitoring default encryption with
 AWS CloudTrail and Amazon EventBridge](bucket-encryption-tracking.md "bucket-encryption-tracking.md").
