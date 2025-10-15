# Configuring your bucket to use an S3 Bucket Key with
 SSE-KMS for new objects

When you configure server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS), you can
 configure your bucket to use an S3 Bucket Key for SSE-KMS on new objects. S3 Bucket Keys decrease the
 request traffic from Amazon S3 to AWS KMS and reduce the cost of SSE-KMS. For more information, see
 [Reducing the cost of SSE-KMS with Amazon S3 Bucket Keys](bucket-key.md "bucket-key.md").

You can configure your bucket to use an S3 Bucket Key for SSE-KMS on new objects by using
 the Amazon S3 console, REST API, AWS SDKs, AWS Command Line Interface (AWS CLI), or AWS CloudFormation. If you want to enable or
 disable an S3 Bucket Key for existing objects, you can use a `CopyObject` operation. For
 more information, see [Configuring an S3 Bucket Key at the object
 level](configuring-bucket-key-object.md "configuring-bucket-key-object.md") and [Using Batch Operations to enable S3 Bucket Keys for
 SSE-KMS](batch-ops-copy-example-bucket-key.md "batch-ops-copy-example-bucket-key.md").

When an S3 Bucket Key is enabled for the source or destination bucket, the encryption
 context will be the bucket Amazon Resource Name (ARN) and not the object ARN, for example,
 `arn:aws:s3:::`bucket_ARN``. You need to update your
 IAM policies to use the bucket ARN for the encryption context. For more information, see
 [S3 Bucket Keys and replication](replication-config-for-kms-objects.md#bk-replication "replication-config-for-kms-objects.md#bk-replication").

The following examples illustrate how an S3 Bucket Key works with replication. For more
 information, see [Replicating encrypted objects (SSE-S3,
 SSE-KMS, DSSE-KMS, SSE-C)](replication-config-for-kms-objects.md "replication-config-for-kms-objects.md"). 


###### Prerequisites


Before you configure your bucket to use an S3 Bucket Key, review [Changes to note before enabling an S3 Bucket Key](bucket-key.md#bucket-key-changes "bucket-key.md#bucket-key-changes").


###### Topics

In the S3 console, you can enable or disable an S3 Bucket Key for a new or existing
 bucket. Objects in the S3 console inherit their S3 Bucket Key setting from the bucket
 configuration. When you enable an S3 Bucket Key for your bucket, new objects that you
 upload to the bucket use an S3 Bucket Key for SSE-KMS. 


###### Uploading, copying, or modifying objects in buckets that have an S3 Bucket Key
 enabled


If you upload, modify, or copy an object in a bucket that has an S3 Bucket Key
 enabled, the S3 Bucket Key settings for that object might be updated to align with the
 bucket configuration.


If an object already has an S3 Bucket Key enabled, the S3 Bucket Key settings for that
 object don't change when you copy or modify the object. However, if you modify or copy an
 object that doesn’t have an S3 Bucket Key enabled, and the destination bucket has an
 S3 Bucket Key configuration, the object inherits the destination bucket's S3 Bucket Key
 settings. For example, if your source object doesn't have an S3 Bucket Key enabled but the
 destination bucket has S3 Bucket Key enabled, an S3 Bucket Key is enabled for the
 object.

###### To enable an S3 Bucket Key when you create a new bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. Choose **Create bucket**.
4. Enter your bucket name, and choose your AWS Region.
5. Under **Default encryption**, for **Encryption key
 type**, choose **AWS Key Management Service key (SSE-KMS)**.
6. Under **AWS KMS key**, do one of the following to choose your
 KMS key:




	* To choose from a list of available KMS keys, choose **Choose from
	 your AWS KMS keys**, and then choose your
	 **KMS key** from the list of available keys.
	
	
	Both the AWS managed key (`aws/s3`) and your customer managed keys appear
	 in this list. For more information about customer managed keys, see [Customer keys and AWS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt") in the
	 *AWS Key Management Service Developer Guide*.
	* To enter the KMS key ARN, choose **Enter AWS KMS key
	 ARN**, and enter your KMS key ARN in the field that appears.
	* To create a new customer managed key in the AWS KMS console, choose **Create a
	 KMS key**.
	
	
	For more information about creating an AWS KMS key, see [Creating
	 Keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html "https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html") in the *AWS Key Management Service Developer Guide*.
7. Under **Bucket Key**, choose **Enable**.
8. Choose **Create bucket**. 


Amazon S3 creates your bucket with an S3 Bucket Key enabled. New objects that you upload
 to the bucket will use an S3 Bucket Key. 


To disable an S3 Bucket Key, follow the previous steps, and choose
 **Disable**.
###### To enable an S3 Bucket Key for an existing bucket

1. Open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. In the **Buckets** list, choose the bucket that you want to
 enable an S3 Bucket Key for.
4. Choose the **Properties** tab.
5. Under **Default encryption**, choose
 **Edit**.
6. Under **Default encryption**, for **Encryption key
 type**, choose **AWS Key Management Service key (SSE-KMS)**.
7. Under **AWS KMS key**, do one of the following to choose your
 KMS key:




	* To choose from a list of available KMS keys, choose **Choose from
	 your AWS KMS keys**, and then choose your
	 **KMS key** from the list of available keys.
	
	
	Both the AWS managed key (`aws/s3`) and your customer managed keys appear
	 in this list. For more information about customer managed keys, see [Customer keys and AWS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt") in the
	 *AWS Key Management Service Developer Guide*.
	* To enter the KMS key ARN, choose **Enter AWS KMS key
	 ARN**, and enter your KMS key ARN in the field that appears.
	* To create a new customer managed key in the AWS KMS console, choose **Create a
	 KMS key**.
	
	
	For more information about creating an AWS KMS key, see [Creating
	 Keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html "https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html") in the *AWS Key Management Service Developer Guide*.
8. Under **Bucket Key**, choose **Enable**.
9. Choose **Save changes**.


Amazon S3 enables an S3 Bucket Key for new objects added to your bucket. Existing
 objects don't use the S3 Bucket Key. To configure an S3 Bucket Key for existing objects,
 you can use a `CopyObject` operation. For more information, see [Configuring an S3 Bucket Key at the object
 level](configuring-bucket-key-object.md "configuring-bucket-key-object.md").


To disable an S3 Bucket Key, follow the previous steps, and choose
 **Disable**.
You can use [PutBucketEncryption](../API/API_PutBucketEncryption.md "../API/API_PutBucketEncryption.md") to
 enable or disable an S3 Bucket Key for your bucket. To configure an S3 Bucket Key with
 `PutBucketEncryption`, use the [ServerSideEncryptionRule](../API/API_ServerSideEncryptionRule.md "../API/API_ServerSideEncryptionRule.md") data type, which includes default encryption with
 SSE-KMS. You can also optionally use a customer managed key by specifying the KMS key ID for the
 customer managed key.  

For more information and example syntax, see [PutBucketEncryption](../API/API_PutBucketEncryption.md "../API/API_PutBucketEncryption.md").
 

The following example enables default bucket encryption with SSE-KMS and an
 S3 Bucket Key by using the AWS SDK for Java.


Java

```
AmazonS3 s3client = AmazonS3ClientBuilder.standard()
    .withRegion(Regions.DEFAULT_REGION)
    .build();
    
ServerSideEncryptionByDefault serverSideEncryptionByDefault = new ServerSideEncryptionByDefault()
    .withSSEAlgorithm(SSEAlgorithm.KMS);
ServerSideEncryptionRule rule = new ServerSideEncryptionRule()
    .withApplyServerSideEncryptionByDefault(serverSideEncryptionByDefault)
    .withBucketKeyEnabled(true);
ServerSideEncryptionConfiguration serverSideEncryptionConfiguration =
    new ServerSideEncryptionConfiguration().withRules(Collections.singleton(rule));

SetBucketEncryptionRequest setBucketEncryptionRequest = new SetBucketEncryptionRequest()
    .withServerSideEncryptionConfiguration(serverSideEncryptionConfiguration)
    .withBucketName(bucketName);
            
s3client.setBucketEncryption(setBucketEncryptionRequest);
```


The following example enables default bucket encryption with SSE-KMS and an
 S3 Bucket Key by using the AWS CLI. Replace the ``user input
 placeholders`` with your own information.


```
aws s3api put-bucket-encryption --bucket `amzn-s3-demo-bucket` --server-side-encryption-configuration '{
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
For more information about configuring an S3 Bucket Key with AWS CloudFormation, see [AWS::S3::Bucket ServerSideEncryptionRule](../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionrule.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionrule.md") in the
 *AWS CloudFormation User Guide*.
