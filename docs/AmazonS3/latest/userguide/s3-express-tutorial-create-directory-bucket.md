# Step 2: Create a S3 Express One Zone directory

bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the currently displayed AWS Region. Next, choose the Region in which you want to create a bucket.

###### Note

To minimize latency and costs and address regulatory requirements, choose a Region
close to you. Objects stored in a Region never leave that Region unless you explicitly
transfer them to another Region. For a list of Amazon S3 AWS Regions, see [AWS service endpoints](../../../general/latest/gr/rande.md#s3_region "../../../general/latest/gr/rande.md#s3_region") in the
_Amazon Web Services General Reference_. 3. In the left navigation pane, choose **Directory buckets**. 4. Choose **Create bucket**. The **Create bucket** page opens. 5. Under **General configuration**, view the AWS Region where your bucket will be created.

Under **Bucket type**, choose **Directory**.

###### Note

    * If you've chosen a Region that doesn't support directory buckets, the
     **Bucket type** option disappears, and the bucket type
     defaults to a general purpose bucket. To create a directory bucket, you must
     choose a supported Region. For a list of Regions that support directory
     buckets and the Amazon S3 Express One Zone storage class, see [S3 Express One Zone Availability Zones and Regions](s3-express-Endpoints.md "s3-express-Endpoints.md").
    * After you create the bucket, you can't change the bucket type.

###### Note

The Availability Zone can't be changed after the bucket is created. 6. For **Availability Zone**, choose a Availability Zone local to your
compute services. For a list of Availability Zones that support directory buckets and
the S3 Express One Zone storage class, see [S3 Express One Zone Availability Zones and Regions](s3-express-Endpoints.md "s3-express-Endpoints.md").

Under **Availability Zone**, select the check box to acknowledge that in
the event of an Availability Zone outage, your data might be unavailable or lost.

###### Important

Although directory buckets are stored across multiple devices within a single
Availability Zone, directory buckets don't store data redundantly across
Availability Zones. 7. For **Bucket name**, enter a name for your directory bucket.

The following naming rules apply for directory buckets.

    * Be unique within the chosen Zone (AWS Availability Zone or AWS Local Zone).
    * Name must be between 3 (min) and 63 (max) characters long, including the suffix.
    * Consists only of lowercase letters, numbers and hyphens (-).
    * Begin and end with a letter or number.
    * Must include the following suffix:
     `--`zone-id`--x-s3`.
    * Bucket names must not start with the prefix `xn--`.
    * Bucket names must not start with the prefix `sthree-`.
    * Bucket names must not start with the prefix
     `sthree-configurator`.
    * Bucket names must not start with the prefix `amzn-s3-demo-`.
    * Bucket names must not end with the suffix `-s3alias`. This suffix
     is reserved for access point alias names. For more information, see [Access point aliases](access-points-naming.md#access-points-alias "access-points-naming.md#access-points-alias").
    * Bucket names must not end with the suffix `--ol-s3`. This suffix is
     reserved for Object Lambda Access Point alias names. For more information, see [How to use a bucket-style alias for your S3 bucket
     Object Lambda Access Point](olap-use.md#ol-access-points-alias "olap-use.md#ol-access-points-alias").
    * Bucket names must not end with the suffix `.mrap`. This suffix is
     reserved for Multi-Region Access Point names. For more information, see [Rules for naming Amazon S3 Multi-Region Access Points](multi-region-access-point-naming.md "multi-region-access-point-naming.md").

A suffix is automatically added to the base name that you provide when you create a directory bucket using the console. This
suffix includes the Availability Zone ID of the Availability Zone that you
chose.

After you create the bucket, you can't change its name. For more information about
naming buckets, see [General purpose bucket naming rules](bucketnamingrules.md "bucketnamingrules.md").

###### Important

Do not include sensitive information, such as account numbers, in the bucket name.
The bucket name is visible in the URLs that point to the objects in the
bucket. 8. Under **Object Ownership**, the **Bucket owner enforced**
setting is automatically enabled, and all access control lists (ACLs) are disabled. For
directory buckets, ACLs can't be enabled.

**Bucket owner enforced (default)** –
ACLs are disabled, and the bucket owner automatically owns and has full control over every object in the general purpose bucket. ACLs
no longer affect access permissions to data in the S3 general purpose bucket. The bucket uses policies exclusively to define access control. 9. Under **Block Public Access settings for this bucket**, all Block
Public Access settings for your directory bucket are automatically enabled. These
settings can't be modified for directory buckets. For more information about blocking
public access, see [Blocking public access to your Amazon S3
storage](access-control-block-public-access.md "access-control-block-public-access.md"). 10. To configure default encryption, under **Encryption type**,
choose one of the following:

    * **Server-side encryption with Amazon S3 managed key
     (SSE-S3)**
    * **Server-side encryption with AWS Key Management Service key
     (SSE-KMS)**

For more information about using Amazon S3 server-side encryption to encrypt your data,
see [Data protection and encryption](s3-express-data-protection.md "s3-express-data-protection.md").

###### Important

If you use the SSE-KMS option for your default encryption configuration, you are
subject to the requests per second (RPS) quota of AWS KMS. For more information about
AWS KMS quotas and how to request a quota increase, see [Quotas](../../../kms/latest/developerguide/limits.md "../../../kms/latest/developerguide/limits.md") in the
_AWS Key Management Service Developer Guide_.

When you enable default encryption, you might need to update your bucket policy. For
more information, see [Using SSE-KMS encryption for cross-account
operations](bucket-encryption.md#bucket-encryption-update-bucket-policy "bucket-encryption.md#bucket-encryption-update-bucket-policy"). 11. If you chose **Server-side encryption with Amazon S3 managed keys
(SSE-S3)**, under **Bucket Key**,
**Enabled** appears. S3 Bucket Keys are always enabled when you configure
your directory bucket to use default encryption with SSE-S3.
S3 Bucket Keys are always enabled for `GET` and `PUT` operations in a directory bucket and can’t be disabled. S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets
to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md"), [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md"), [the Copy operation in Batch Operations](directory-buckets-objects-Batch-Ops.md "directory-buckets-objects-Batch-Ops.md"), or
[the import jobs](create-import-job.md "create-import-job.md"). In this case, Amazon S3 makes a call to AWS KMS every time a copy request is made for a KMS-encrypted object.

S3 Bucket Keys lower the cost of encryption by decreasing request traffic from Amazon S3 to AWS KMS.
For more information, see [Reducing the cost of SSE-KMS with Amazon S3 Bucket Keys](bucket-key.md "bucket-key.md"). 12. If you chose **Server-side encryption with AWS Key Management Service key (SSE-KMS)**,
under **AWS KMS key**, specify your AWS Key Management Service key in one of the
following ways or create a new key.

    * To choose from a list of available KMS keys, choose **Choose
     from your AWS KMS keys**, and choose your
     **KMS key** from **Available
     AWS KMS keys**.


    Only your customer managed keys appear in this
     list. The AWS managed key (`aws/s3`) isn't supported in directory buckets. For more information about customer managed keys, see [Customer keys and
     AWS keys](../../../kms/latest/developerguide/concepts.md#key-mgmt "../../../kms/latest/developerguide/concepts.md#key-mgmt") in the *AWS Key Management Service Developer Guide*.
    * To enter the KMS key ARN or alias, choose **Enter
     AWS KMS key ARN**, and enter your KMS key ARN or alias
     in **AWS KMS key ARN**.
    * To create a new customer managed key in the AWS KMS console, choose **Create a
     KMS key**.


    For more information about creating an AWS KMS key, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the *AWS Key Management Service Developer Guide*.

###### Important

    * Your SSE-KMS configuration can only support 1 [customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") per directory bucket for the lifetime of the bucket.
    The [AWS managed key](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk") (`aws/s3`) isn't supported. Also, after you specify a customer managed key for SSE-KMS, you can't override the customer managed key for the bucket's SSE-KMS configuration.


    You can identify the customer managed key you specified for the bucket's SSE-KMS configuration, in the following way:




    	+ You make a `HeadObject` API operation request to find the value of `x-amz-server-side-encryption-aws-kms-key-id` in your response.
    To use a new customer managed key for your data, we recommend copying your existing objects to a new directory bucket with a new customer managed key.
    * You can use only KMS keys that are available in the same AWS Region as the
     bucket. The Amazon S3 console lists only the first 100 KMS keys in the same Region as the bucket.
     To use a KMS key that is not listed, you must enter your KMS key ARN. If you want to use
     a KMS key that is owned by a different account, you must first have permission to use the
     key and then you must enter the KMS key ARN. For more information on cross account permissions for KMS keys, see [Creating KMS keys that other accounts can use](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md#cross-account-console "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md#cross-account-console") in the *AWS Key Management Service Developer Guide*. For more information on SSE-KMS, see [Specifying server-side encryption with AWS KMS
     (SSE-KMS) for new object uploads in directory buckets](s3-express-specifying-kms-encryption.md "s3-express-specifying-kms-encryption.md").
    * When you use an AWS KMS key for server-side encryption in directory buckets, you must
     choose a symmetric encryption KMS key. Amazon S3 supports only symmetric encryption KMS keys and not
     asymmetric KMS keys. For more information, see [Identifying symmetric and
     asymmetric KMS keys](../../../kms/latest/developerguide/find-symm-asymm.md "../../../kms/latest/developerguide/find-symm-asymm.md") in the *AWS Key Management Service Developer Guide*.

For
more information about using AWS KMS with Amazon S3, see [Using server-side encryption with AWS KMS keys
(SSE-KMS) in directory buckets](s3-express-UsingKMSEncryption.md "s3-express-UsingKMSEncryption.md"). 13. Choose **Create bucket**. After creating the bucket, you can add files and folders to the bucket. For more
information, see [Working with objects in a directory
bucket](directory-buckets-objects.md "directory-buckets-objects.md").
