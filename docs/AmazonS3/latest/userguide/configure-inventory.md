# Configuring Amazon S3 Inventory

Amazon S3 Inventory provides a flat file list of your objects and metadata, on a schedule that
you define. You can use S3 Inventory as a scheduled alternative to the Amazon S3 synchronous
`List` API operation. S3 Inventory provides comma-separated values (CSV), [Apache optimized row columnar (ORC)](https://orc.apache.org/ "https://orc.apache.org/"), or
[Apache Parquet (Parquet)](https://parquet.apache.org/ "https://parquet.apache.org/")
output files that list your objects and their corresponding metadata.

You can configure S3 Inventory to create inventory lists on a daily or weekly basis for an
S3 bucket or for objects that share a prefix (objects that have names that begin with the same
string). For more information, see [Cataloging and analyzing your data with S3 Inventory](storage-inventory.md "storage-inventory.md").

This section describes how to configure an inventory, including details about the inventory
source and destination buckets.

###### Topics

- [Overview](#storage-inventory-setting-up "#storage-inventory-setting-up")
- [Creating a destination bucket
  policy](#configure-inventory-destination-bucket-policy "#configure-inventory-destination-bucket-policy")
- [Granting Amazon S3 permission to use your
  customer managed key for encryption](#configure-inventory-kms-key-policy "#configure-inventory-kms-key-policy")
- [Configuring inventory by using the S3
  console](#configure-inventory-console "#configure-inventory-console")
- [Using the REST API to work with S3 Inventory](#rest-api-inventory "#rest-api-inventory")

## Overview

Amazon S3 Inventory helps you manage your storage by creating lists of the objects in an S3
bucket on a defined schedule. You can configure multiple inventory lists for a bucket. The
inventory lists are published to CSV, ORC, or Parquet files in a destination
bucket.

The easiest way to set up an inventory is by using the Amazon S3 console, but you can also use
the Amazon S3 REST API, AWS Command Line Interface (AWS CLI), or AWS SDKs. The console performs the first step of
the following procedure for you: adding a bucket policy to the destination bucket.

**To set up Amazon S3 Inventory for an S3 bucket**

1. **Add a bucket policy for the destination
   bucket.**

You must create a bucket policy on the destination bucket that grants permissions to
Amazon S3 to write objects to the bucket in the defined location. For an example policy, see
[Grant permissions for S3 Inventory
and S3 analytics](example-bucket-policies.md#example-bucket-policies-s3-inventory-1 "example-bucket-policies.md#example-bucket-policies-s3-inventory-1"). 2. **Configure an inventory to list the objects in a source bucket
and publish the list to a destination bucket.**

When you configure an inventory list for a source bucket, you specify the destination
bucket where you want the list to be stored, and whether you want to generate the list
daily or weekly. You can also configure whether to list all object versions or only
current versions and what object metadata to include.

Some object metadata fields in S3 Inventory report configurations are optional,
meaning that they're available by default but they can be restricted when you grant a user
the `s3:PutInventoryConfiguration` permission. You can control whether users
can include these optional metadata fields in their reports by using the
`s3:InventoryAccessibleOptionalFields` condition key.

For more information about the optional metadata fields available in S3 Inventory, see
[OptionalFields](../API/API_PutBucketInventoryConfiguration.md#API_PutBucketInventoryConfiguration_RequestBody "../API/API_PutBucketInventoryConfiguration.md#API_PutBucketInventoryConfiguration_RequestBody") in the _Amazon Simple Storage Service API Reference_. For more information about restricting access to certain
optional metadata fields in an inventory configuration, see [Control S3 Inventory report
configuration creation](example-bucket-policies.md#example-bucket-policies-s3-inventory-2 "example-bucket-policies.md#example-bucket-policies-s3-inventory-2").

You can specify that the inventory list file be encrypted by using server-side
encryption with an Amazon S3 managed key (SSE-S3) or an AWS Key Management Service (AWS KMS) customer managed key (SSE-KMS).

###### Note

The AWS managed key (`aws/s3`) is not supported for SSE-KMS encryption
with S3 Inventory.

For more information about SSE-S3 and SSE-KMS, see [Protecting data with server-side encryption](serv-side-encryption.md "serv-side-encryption.md"). If you plan to
use SSE-KMS encryption, see Step 3.

    * For information about how to use the console to configure an inventory list, see
     [Configuring inventory by using the S3
     console](#configure-inventory-console "#configure-inventory-console").
    * To use the Amazon S3 API to configure an inventory list, use the [PutBucketInventoryConfiguration](../API/RESTBucketPUTInventoryConfig.md "../API/RESTBucketPUTInventoryConfig.md") REST API operation or the
     equivalent from the AWS CLI or AWS SDKs.

3. **To encrypt the inventory list file with SSE-KMS, grant Amazon S3
   permission to use the AWS KMS key.**

You can configure encryption for the inventory list file by using the Amazon S3 console,
Amazon S3 REST API, AWS CLI, or AWS SDKs. Whichever way you choose, you must grant Amazon S3
permission to use the customer managed key to encrypt the inventory file. You [grant Amazon S3 permission
by modifying the key policy for the customer managed key](configure-inventory.md#configure-inventory-kms-key-policy "configure-inventory.md#configure-inventory-kms-key-policy") that you want to use to encrypt the
inventory file. Make sure that you've provided a KMS key ARN in the S3 Inventory
configuration or the destination bucket’s encryption settings. If no KMS key ARN has been
specified and the default encryption settings are being used, you won’t be able to access
your S3 Inventory report.

The destination bucket that stores the inventory list file can be owned by a different
AWS account than the account that owns the source bucket. If you use SSE-KMS encryption
for the cross-account operations of Amazon S3 Inventory, we recommend that you use a fully
qualified KMS key ARN when you configure S3 inventory. For more information, see [Using SSE-KMS encryption for cross-account
operations](bucket-encryption.md#bucket-encryption-update-bucket-policy "bucket-encryption.md#bucket-encryption-update-bucket-policy") and [ServerSideEncryptionByDefault](../API/API_ServerSideEncryptionByDefault.md "../API/API_ServerSideEncryptionByDefault.md") in the _Amazon Simple Storage Service API Reference_.

###### Note

If you can’t access your S3 Inventory report, use the [GetBucketEncryption](../API/API_GetBucketEncryption.md "../API/API_GetBucketEncryption.md") API, and check whether the destination bucket
has the default SSE-KMS encryption enabled. If no KMS key ARN has been specified and the
default encryption settings are being used, you won’t be able to access your S3
Inventory report. To access S3 Inventory reports again, either provide a KMS key ARN in the
S3 Inventory configuration or in the destination bucket’s encryption settings.

## Creating a destination bucket

policy

If you create your inventory configuration through the Amazon S3 console, Amazon S3 automatically
creates a bucket policy on the destination bucket that grants Amazon S3 write permission to the
bucket. However, if you create your inventory configuration through the AWS CLI, AWS SDKs, or
the Amazon S3 REST API, you must manually add a bucket policy on the destination bucket. The S3 Inventory destination
bucket policy allows Amazon S3 to write data for the inventory reports to the bucket.

The following is the example bucket policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "InventoryExamplePolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "s3.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": [
 "arn:aws:s3:::DOC-EXAMPLE-DESTINATION-BUCKET/*"
 ],
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:s3:::DOC-EXAMPLE-SOURCE-BUCKET"
 },
 "StringEquals": {
 "aws:SourceAccount": "source-123456789012",
 "s3:x-amz-acl": "bucket-owner-full-control"
 }
 }
 }
 ]
}`

```

For more
information, see [Grant permissions for S3 Inventory
and S3 analytics](example-bucket-policies.md#example-bucket-policies-s3-inventory-1 "example-bucket-policies.md#example-bucket-policies-s3-inventory-1").

If an error occurs when you try to create the bucket policy, you are given instructions on
how to fix it. For example, if you choose a destination bucket in another AWS account and
don't have permissions to read and write to the bucket policy, you see an error
message.

In this case, the destination bucket owner must add the bucket policy to the destination
bucket. If the policy is not added to the destination bucket, you won't get an inventory
report because Amazon S3 doesn't have permission to write to the destination bucket. If the source
bucket is owned by a different account than that of the current user, the correct account ID
of the source bucket owner must be substituted in the policy.

###### Note

Ensure that there are no Deny statements added to the destination bucket policy that would prevent the delivery of inventory reports into this bucket. For more information, see [Why can't I generate an Amazon S3 Inventory Report?](https://repost.aws/knowledge-center/s3-inventory-report "https://repost.aws/knowledge-center/s3-inventory-report") .

## Granting Amazon S3 permission to use your

customer managed key for encryption

To grant Amazon S3 permission to use your AWS Key Management Service (AWS KMS) customer managed key for server-side encryption,
you must use a key policy. To update your key policy so that you can use your customer managed key, use the following procedure.

###### To grant Amazon S3 permissions to encrypt by using your customer managed key

1. Using the AWS account that owns the customer managed key, sign into the AWS Management Console.
2. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
3. To change the AWS Region, use the Region selector in the upper-right corner of the page.
4. In the left navigation pane, choose **Customer managed keys**.
5. Under **Customer managed keys**, choose the customer managed key that you want to use to encrypt your inventory files.
6. In the **Key policy** section, choose **Switch to policy view**.
7. To update the key policy, choose **Edit**.
8. On the **Edit key policy** page, add the following lines to the existing key
   policy. For `source-account-id` and `amzn-s3-demo-source-bucket`,
   supply the appropriate values for your use case.

```
{
    "Sid": "Allow Amazon S3 use of the customer managed key",
    "Effect": "Allow",
    "Principal": {
        "Service": "s3.amazonaws.com"
    },
    "Action": [
        "kms:GenerateDataKey"
    ],
    "Resource": "*",
    "Condition":{
      "StringEquals":{
         "aws:SourceAccount":"`source-account-id`"
     },
      "ArnLike":{
        "aws:SourceARN": "arn:aws:s3:::``amzn-s3-demo-source-bucket``"
     }
   }
}
```

9. Choose **Save changes**.

For more information about creating customer managed keys and using key policies,
see the following links in the _AWS Key Management Service Developer Guide_:

- [Managing keys](../../../kms/latest/developerguide/getting-started.md "../../../kms/latest/developerguide/getting-started.md")
- [Key policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md")

###### Note

Ensure that there are no Deny statements added to the destination bucket policy that would prevent the delivery of inventory reports into this bucket. For more information, see [Why can't I generate an Amazon S3 Inventory Report?](https://repost.aws/knowledge-center/s3-inventory-report "https://repost.aws/knowledge-center/s3-inventory-report") .

## Configuring inventory by using the S3

console

Use these instructions to configure inventory by using the S3 console.

###### Note

It might take up to 48 hours for Amazon S3 to deliver the first inventory report.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. In the buckets list, choose the name of the bucket that you want to
   configure Amazon S3 Inventory for.
4. Choose the **Management** tab.
5. Under **Inventory configurations**, choose **Create inventory
   configuration**.
6. For **Inventory configuration name**, enter a name.
7. For **Inventory scope**, do the following:
   - Enter an optional prefix.
   - Choose which object versions to include, either **Current versions
     only** or **Include all versions**.

8. Under **Report details**, choose the location of the AWS account
   that you want to save the reports to: **This account** or **A
   different account**.
9. Under **Destination**, choose the destination bucket where you want
   the inventory reports to be saved.

The destination bucket must be in the same AWS Region as the bucket for which you
are setting up the inventory. The destination bucket can be in a different AWS account.
When specifying the destination bucket, you can also include an optional prefix to group
your inventory reports together.

Under the **Destination** bucket field, you see the
**Destination bucket permission** statement that is added to the
destination bucket policy to allow Amazon S3 to place data in that bucket. For more
information, see [Creating a destination bucket
policy](#configure-inventory-destination-bucket-policy "#configure-inventory-destination-bucket-policy"). 10. Under **Frequency**, choose how often the report will be generated,
**Daily** or **Weekly**. 11. For **Output format**, choose one of the following formats for the
report:

    * **CSV** – If you plan to use this inventory report with
     S3 Batch Operations or if you want to analyze this report in another tool, such as
     Microsoft Excel, choose **CSV**.
    * **Apache ORC**
    * **Apache Parquet**

12. Under **Status**, choose **Enable** or
    **Disable**.
13. To configure server-side encryption, under **Inventory report
    encryption**, follow these steps:
    1.  Under **Server-side encryption**, choose either **Do not
        specify an encryption key** or **Specify an encryption
        key** to encrypt data.
        - To keep the bucket settings for default server-side encryption of objects when
          storing them in Amazon S3, choose **Do not specify an encryption
          key**. As long as the bucket destination has S3 Bucket Keys enabled, the copy
          operation applies an S3 Bucket Key at the destination bucket.

        ###### Note

        If the bucket policy for the specified destination requires objects to be
        encrypted before storing them in Amazon S3, you must choose **Specify an
        encryption key**. Otherwise, copying objects to the destination will
        fail.
        - To encrypt objects before storing them in Amazon S3, choose **Specify an
          encryption key**.

    2.  If you chose **Specify an encryption key**, under
        **Encryption type**, you must choose either **Amazon S3 managed
        key (SSE-S3)** or **AWS Key Management Service key (SSE-KMS)**.

    SSE-S3 uses one of the strongest block ciphers—256-bit Advanced Encryption
    Standard (AES-256) to encrypt each object. SSE-KMS provides you with more control over
    your key. For more information about SSE-S3, see [Using server-side encryption with Amazon S3 managed keys
    (SSE-S3)](UsingServerSideEncryption.md "UsingServerSideEncryption.md"). For
    more information about SSE-KMS, see [Using server-side encryption with AWS KMS keys
    (SSE-KMS)](UsingKMSEncryption.md "UsingKMSEncryption.md").

    ###### Note

    To encrypt the inventory list file with SSE-KMS, you must grant Amazon S3 permission
    to use the customer managed key. For instructions, see [Grant Amazon S3 Permission to Encrypt
    Using Your KMS Keys](#configure-inventory-kms-key-policy "#configure-inventory-kms-key-policy"). 3. If you chose **AWS Key Management Service key (SSE-KMS)**, under
    **AWS KMS key**, you can specify your AWS KMS key through one of
    the following options.

    ###### Note

    If the destination bucket that stores the inventory list file is owned by a
    different AWS account, make sure that you use a fully qualified KMS key ARN to
    specify your KMS key.

        * To choose from a list of available KMS keys, choose **Choose from
         your AWS KMS keys**, and choose a symmetric encryption KMS key from the
         list of available keys. Make sure the KMS key is in the same Region as your
         bucket.


        ###### Note

        Both the AWS managed key (`aws/s3`) and your customer managed keys appear
         in the list. However, the AWS managed key (`aws/s3`) is not
         supported for SSE-KMS encryption with S3 Inventory.
        * To enter the KMS key ARN, choose **Enter AWS KMS key ARN**,
         and enter your KMS key ARN in the field that appears.
        * To create a new customer managed key in the AWS KMS console, choose **Create a
         KMS key**.

14. For **Additional metadata fields**, select one or more of the
    following to add to the inventory report:

        * **Size** – The object size in bytes, not including the
         size of incomplete multipart uploads, object metadata, and delete markers.
        * **Last modified date** – The object creation date or the
         last modified date, whichever is the latest.
        * **Multipart upload** – Specifies that the object was uploaded
         as a multipart upload. For more information, see [Uploading and copying objects using multipart upload in Amazon S3](mpuoverview.md "mpuoverview.md").
        * **Replication status** – The replication status of the
         object. For more information, see [Getting replication status information](replication-status.md "replication-status.md").
        * **Encryption status** – The server-side encryption type
         that's used to encrypt the object. For more information, see [Protecting data with server-side encryption](serv-side-encryption.md "serv-side-encryption.md").
        * **Bucket Key status** – Indicates whether a
         bucket-level key generated by AWS KMS applies to the object. For more information, see
         [Reducing the cost of SSE-KMS with Amazon S3 Bucket Keys](bucket-key.md "bucket-key.md").
        * **Object access control list** – An access
         control list (ACL) for each object that defines which AWS accounts or groups are
         granted access to this object and the type of access that is granted. For more
         information about this field, see [Working with the Object ACL field](objectacl.md "objectacl.md"). For more information about ACLs, see [Access control list (ACL) overview](acl-overview.md "acl-overview.md").
        * **Object owner** – The owner of the
         object.
        * **Storage class** – The storage class that's used for
         storing the object.
        * **Intelligent-Tiering: Access tier** –
         Indicates the access tier (frequent or infrequent) of the object if it was stored in
         the S3 Intelligent-Tiering storage class. For more information, see [Storage class for automatically optimizing data with
         changing or unknown access patterns](storage-class-intro.md#sc-dynamic-data-access "storage-class-intro.md#sc-dynamic-data-access").
        * **ETag** – The entity tag (ETag) is a hash of the object.
         The ETag reflects changes only to the contents of an object, not to its metadata. The
         ETag might or might not be an MD5 digest of the object data. Whether it is depends on
         how the object was created and how it is encrypted. For more information, see [Object](../API/API_Object.md "../API/API_Object.md") in the *Amazon Simple Storage Service API Reference*.
        * **Checksum algorithm** – Indicates the
         algorithm that is used to create the checksum for the object. For more information, see [Using supported checksum algorithms](checking-object-integrity-upload.md#using-additional-checksums "checking-object-integrity-upload.md#using-additional-checksums").
        * **All Object Lock configurations** – The Object Lock
         status of the object, including the following settings:




        	+ **Object Lock: Retention mode** – The level of
        	 protection applied to the object, either *Governance* or
        	 *Compliance*.
        	+ **Object Lock: Retain until date** – The date until
        	 which the locked object cannot be deleted.
        	+ **Object Lock: Legal hold status** – The legal hold
        	 status of the locked object.
        For information about S3 Object Lock, see [How S3 Object Lock works](object-lock.md#object-lock-overview "object-lock.md#object-lock-overview").
        * **Lifecycle Expiration Date** – The lifecycle expiration
         timestamp for objects in your Inventory report. This field will only be populated, if
         the object is to be expired by an applicable lifecycle rule. In other cases, the
         field will be empty. For more information, see [Expiring objects](lifecycle-expire-general-considerations.md "lifecycle-expire-general-considerations.md").

    For more information about the contents of an inventory report, see [Amazon S3 Inventory list](storage-inventory.md#storage-inventory-contents "storage-inventory.md#storage-inventory-contents").

For more information about restricting access to certain optional metadata fields in
an inventory configuration, see [Control S3 Inventory report
configuration creation](example-bucket-policies.md#example-bucket-policies-s3-inventory-2 "example-bucket-policies.md#example-bucket-policies-s3-inventory-2"). 15. Choose **Create**.

## Using the REST API to work with S3 Inventory

The following are the REST operations that you can use to work with Amazon S3 Inventory.

- [DeleteBucketInventoryConfiguration](../API/RESTBucketDELETEInventoryConfiguration.md "../API/RESTBucketDELETEInventoryConfiguration.md")
- [GetBucketInventoryConfiguration](../API/RESTBucketGETInventoryConfig.md "../API/RESTBucketGETInventoryConfig.md")
- [ListBucketInventoryConfigurations](../API/RESTBucketListInventoryConfigs.md "../API/RESTBucketListInventoryConfigs.md")
- [PutBucketInventoryConfiguration](../API/RESTBucketPUTInventoryConfig.md "../API/RESTBucketPUTInventoryConfig.md")
