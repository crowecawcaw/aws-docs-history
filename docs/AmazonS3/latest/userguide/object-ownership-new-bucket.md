# Setting Object Ownership when you create

a bucket

When you create a bucket, you can configure S3 Object Ownership. To set
Object Ownership for an existing bucket, see [Setting Object Ownership on an
existing bucket](object-ownership-existing-bucket.md "object-ownership-existing-bucket.md").

S3 Object Ownership is an Amazon S3 bucket-level setting that you can use to disable [access control lists (ACLs)](acl-overview.md "acl-overview.md") and take ownership of every
object in your bucket, simplifying access management for data stored in Amazon S3. By default, S3 Object Ownership
is set to the Bucket owner enforced setting, and ACLs are disabled for new buckets.
With ACLs disabled, the bucket owner owns every object in the bucket and manages access to data
exclusively by using access-management policies. We recommend that you keep ACLs disabled, except in unusual
circumstances where you must control access for each object individually.

Object Ownership has three settings that you can use to control ownership of objects
uploaded to your bucket and to disable or enable ACLs:

###### ACLs disabled

- **Bucket owner enforced (default)** – ACLs are
  disabled, and the bucket owner automatically owns and has full control over every
  object in the bucket. ACLs no longer affect permissions to data in the S3 bucket.
  The bucket uses policies to define access control.

###### ACLs enabled

- **Bucket owner preferred** – The bucket owner owns and
  has full control over new objects that other accounts write to the bucket with the
  `bucket-owner-full-control` canned ACL.
- **Object writer** – The AWS account that
  uploads an object owns the object, has full control over it, and can grant other users access to
  it through ACLs.
  **Permissions**: To apply the **Bucket owner
  enforced** setting or the **Bucket owner preferred**
  setting, you must have the following permissions: `s3:CreateBucket` and
  `s3:PutBucketOwnershipControls`. No additional permissions are needed
  when creating a bucket with the **Object writer** setting applied.
  For more information about Amazon S3 permissions, see [Actions, resources, and condition keys for Amazon S3](../../../service-authorization/latest/reference/list_amazons3.md "../../../service-authorization/latest/reference/list_amazons3.md") in the _Service Authorization
  Reference_.

For more information about the permissions to S3 API operations by S3 resource types, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md").

###### Important

A majority of modern use cases in Amazon S3 no longer require the use of ACLs, and we
recommend that you disable ACLs except in circumstances where you need to
control access for each object individually. With Object Ownership, you can disable
ACLs and rely on policies for access control. When you disable ACLs, you can easily
maintain a bucket with objects uploaded by different AWS accounts.
You, as the bucket owner, own all the objects in the bucket and can manage access to
them using policies.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the currently displayed AWS Region. Next, choose the Region in which you want to create a bucket.

###### Note

    * After you create a bucket, you can't change its Region.
    * To minimize latency and costs and address regulatory requirements, choose a Region close to
     you. Objects stored in a Region never leave that Region unless you explicitly transfer them to
     another Region. For a list of Amazon S3 AWS Regions, see [AWS service endpoints](../../../general/latest/gr/rande.md#s3_region "../../../general/latest/gr/rande.md#s3_region") in the *Amazon Web Services General Reference*.

3. In the left navigation pane, choose **General purpose buckets**.
4. Choose **Create bucket**. The **Create bucket** page opens.
5. For **Bucket name**, enter a name for your bucket.

The bucket name must:

    * Be unique within a partition. A partition is a grouping of Regions. AWS currently has
     three partitions: `aws` (commercial Regions), `aws-cn` (China Regions), and
     `aws-us-gov` (AWS GovCloud (US) Regions).
    * Be between 3 and 63 characters long.
    * Consist only of lowercase letters, numbers, periods (`.`), and hyphens
     (`-`). For best compatibility, we recommend that you avoid using periods
     (`.`) in bucket names, except for buckets that are used only for static website
     hosting.
    * Begin and end with a letter or number.
    * For a complete list of bucket-naming rules, see [General purpose bucket naming rules](bucketnamingrules.md "bucketnamingrules.md").

###### Important

    * After you create the bucket, you can't change its name.
    * Don't include sensitive information in the bucket name. The bucket name is visible in the URLs
     that point to the objects in the bucket.

6. (Optional) Under **General configuration**, you can choose to copy an existing
   bucket's settings to your new bucket. If you don't want to copy the settings of an existing bucket, skip
   to the next step.

###### Note

This option:

    * Isn't available in the AWS CLI and is only available in the Amazon S3 console
    * Doesn't copy the bucket policy from the existing bucket to the new bucket

To copy an existing bucket's settings, under **Copy settings from existing
bucket**, select **Choose bucket**. The **Choose bucket**
window opens. Find the bucket with the settings that you want to copy, and select **Choose
bucket**. The **Choose bucket** window closes, and the **Create
bucket** window reopens.

Under **Copy settings from existing bucket**, you now see the name of the
bucket that you selected. The settings of your new bucket now match the settings of the bucket that you
selected. If you want to remove the copied settings, choose **Restore defaults**.
Review the remaining bucket settings on the **Create bucket** page. If you don't want
to make any changes, you can skip to the final step. 7. Under **Object Ownership**, to disable or enable ACLs and control
ownership of objects uploaded in your bucket, choose one of the following
settings:

###### ACLs disabled

    * **Bucket owner enforced (default)** –
     ACLs are disabled, and the bucket owner automatically owns and has full control over every object in the general purpose bucket. ACLs
     no longer affect access permissions to data in the S3 general purpose bucket. The bucket uses policies exclusively to define access control.


    By default, ACLs are disabled. A majority of modern use cases in Amazon S3 no
     longer require the use of ACLs. We recommend that you keep ACLs disabled, except
     in circumstances where you must control access for each object
     individually. For more information, see [Controlling ownership of objects and disabling ACLs
     for your bucket](about-object-ownership.md "about-object-ownership.md").

###### ACLs enabled

    * **Bucket owner preferred** – The bucket owner owns and
     has full control over new objects that other accounts write to the bucket with
     the `bucket-owner-full-control` canned ACL.


    If you apply the **Bucket owner preferred** setting, to
     require all Amazon S3 uploads to include the `bucket-owner-full-control`
     canned ACL, you can [add a
     bucket policy](ensure-object-ownership.md#ensure-object-ownership-bucket-policy "ensure-object-ownership.md#ensure-object-ownership-bucket-policy") that allows only object uploads that use this
     ACL.
    * **Object writer** – The AWS account that uploads an
     object owns the object, has full control over it, and can grant other users
     access to it through ACLs.

###### Note

The default setting is **Bucket owner enforced**. To apply the
default setting and keep ACLs disabled, only the `s3:CreateBucket`
permission is needed. To enable ACLs, you must have the
`s3:PutBucketOwnershipControls` permission. 8. Under **Block Public Access settings for this bucket**, choose the
Block Public Access settings that you want to apply to the bucket.

By default, all four Block Public Access settings are enabled. We recommend that you
keep all settings enabled, unless you know that you need to turn off one or more of them
for your specific use case. For more information about blocking public access, see [Blocking public access to your Amazon S3
storage](access-control-block-public-access.md "access-control-block-public-access.md").

###### Note

To enable all Block Public Access settings, only the `s3:CreateBucket` permission
is required. To turn off any Block Public Access settings, you must have the
`s3:PutBucketPublicAccessBlock` permission. 9. (Optional) By default, **Bucket Versioning** is disabled. Versioning is a means
of keeping multiple variants of an object in the same bucket. You can use versioning to preserve,
retrieve, and restore every version of every object stored in your bucket. With versioning, you can
recover more easily from both unintended user actions and application failures. For more information
about versioning, see [Retaining multiple versions of objects with S3 Versioning](Versioning.md "Versioning.md").

To enable versioning on your bucket, choose **Enable**. 10. (Optional) Under **Tags**, you can choose to add tags to your bucket. With
AWS cost allocation, you can use bucket tags to annotate billing for your use of a bucket. A tag is a
key-value pair that represents a label that you assign to a bucket. For more information, see [Using cost allocation S3 bucket tags](CostAllocTagging.md "CostAllocTagging.md").

To add a bucket tag, enter a **Key** and optionally a
**Value** and choose **Add Tag**. 11. To configure **Default encryption**, under **Encryption type**,
choose one of the following:

    * **Server-side encryption with Amazon S3 managed keys (SSE-S3)**
    * **Server-side encryption with AWS Key Management Service keys (SSE-KMS)**
    * **Dual-layer server-side encryption with AWS Key Management Service (AWS KMS) keys
     (DSSE-KMS)**


    ###### Important

    If you use the SSE-KMS or DSSE-KMS option for your default encryption configuration, you are
     subject to the requests per second (RPS) quota of AWS KMS. For more information about AWS KMS quotas
     and how to request a quota increase, see [Quotas](../../../kms/latest/developerguide/limits.md "../../../kms/latest/developerguide/limits.md") in
     the *AWS Key Management Service Developer Guide*.

Buckets and new objects are encrypted by using server-side encryption with Amazon S3 managed keys
(SSE-S3) as the base level of encryption configuration. For more information about default encryption,
see [Setting default server-side encryption behavior for Amazon S3
buckets](bucket-encryption.md "bucket-encryption.md"). For more information about
SSE-S3, see [Using server-side encryption with Amazon S3 managed keys
(SSE-S3)](UsingServerSideEncryption.md "UsingServerSideEncryption.md").

For more information about using server-side encryption to encrypt your data, see [Protecting data with encryption](UsingEncryption.md "UsingEncryption.md"). 12. If you chose **Server-side encryption with AWS Key Management Service keys (SSE-KMS)** or
**Dual-layer server-side encryption with AWS Key Management Service (AWS KMS) keys (DSSE-KMS)**, do the
following:

    1. Under **AWS KMS key**, specify your KMS key in one of the following ways:




    	* To choose from a list of available KMS keys, choose **Choose from
    	 your AWS KMS keys**, and choose your
    	 **KMS key** from the list of available keys.


    	Both the AWS managed key (`aws/s3`) and your customer managed keys appear in this
    	 list. For more information about customer managed keys, see [Customer keys and
    	 AWS keys](../../../kms/latest/developerguide/concepts.md#key-mgmt "../../../kms/latest/developerguide/concepts.md#key-mgmt") in the *AWS Key Management Service Developer Guide*.
    	* To enter the KMS key ARN, choose **Enter AWS KMS key
    	 ARN**, and enter your KMS key ARN in the field that appears.
    	* To create a new customer managed key in the AWS KMS console, choose **Create a
    	 KMS key**.


    	For more information about creating an AWS KMS key, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the *AWS Key Management Service Developer Guide*.
    ###### Important

    You can use only KMS keys that are available in the same AWS Region as the bucket. The
     Amazon S3 console lists only the first 100 KMS keys in the same Region as the bucket. To use a
     KMS key that isn't listed, you must enter your KMS key ARN. If you want to use a KMS key
     that's owned by a different account, you must first have permission to use the key, and then you
     must enter the KMS key ARN. For more information about cross account permissions for KMS keys,
     see [Creating KMS keys that other accounts can use](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md#cross-account-console "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md#cross-account-console") in the
     *AWS Key Management Service Developer Guide*. For more information about SSE-KMS, see [Specifying server-side encryption with AWS KMS
     (SSE-KMS)](specifying-kms-encryption.md "specifying-kms-encryption.md"). For more
     information about DSSE-KMS, see [Using dual-layer server-side encryption with AWS KMS keys
     (DSSE-KMS)](UsingDSSEncryption.md "UsingDSSEncryption.md").

    When you use an AWS KMS key for server-side encryption in Amazon S3, you must
     choose a symmetric encryption KMS key. Amazon S3 supports only symmetric encryption KMS keys and not
     asymmetric KMS keys. For more information, see [Identifying symmetric and
     asymmetric KMS keys](../../../kms/latest/developerguide/find-symm-asymm.md "../../../kms/latest/developerguide/find-symm-asymm.md") in the *AWS Key Management Service Developer Guide*.
    2. When you configure your bucket to use default encryption with SSE-KMS, you can also use S3 Bucket Keys.
     S3 Bucket Keys lower the cost of encryption by decreasing request traffic from Amazon S3 to AWS KMS. For more
     information, see [Reducing the cost of SSE-KMS with Amazon S3 Bucket Keys](bucket-key.md "bucket-key.md"). S3 Bucket Keys aren't
     supported for DSSE-KMS.


    By default, S3 Bucket Keys are enabled in the Amazon S3 console. We recommend leaving S3 Bucket Keys enabled to
     lower your costs. To disable S3 Bucket Keys for your bucket, under **Bucket Key**, choose
     **Disable**.

13. (Optional) S3 Object Lock helps protect new objects from being deleted or overwritten. For
    more information, see [Locking objects with Object Lock](object-lock.md "object-lock.md"). If you want to enable
    S3 Object Lock, do the following:
    1.  Choose **Advanced settings**.

    ###### Important

    Enabling Object Lock automatically enables versioning for the bucket. After you've
    enabled and successfully created the bucket, you must also configure the Object Lock default
    retention and legal hold settings on the bucket's **Properties** tab. 2. If you want to enable Object Lock, choose
    **Enable**, read the warning that appears, and acknowledge it.###### Note

To create an Object Lock enabled bucket, you must have the following permissions:
`s3:CreateBucket`, `s3:PutBucketVersioning`, and
`s3:PutBucketObjectLockConfiguration`. 14. Choose **Create bucket**.
To set Object Ownership when you create a new bucket, use the
`create-bucket` AWS CLI command with the
`--object-ownership` parameter.

This example applies the Bucket owner enforced setting for a new bucket using the
AWS CLI:

```
aws s3api create-bucket --bucket  `amzn-s3-demo-bucket` --region `us-east-1` --object-ownership BucketOwnerEnforced
```

###### Important

If you don’t set Object Ownership when you create a bucket by using the AWS CLI, the default
setting will be `ObjectWriter` (ACLs enabled).

This example sets the Bucket owner enforced setting for a new bucket using the
AWS SDK for Java:

```
    // Build the ObjectOwnership for CreateBucket
    CreateBucketRequest createBucketRequest = CreateBucketRequest.builder()
            .bucket(bucketName)
            .objectOwnership(ObjectOwnership.BucketOwnerEnforced)
            .build()

     // Send the request to Amazon S3
     s3client.createBucket(createBucketRequest);

```

To use the `AWS::S3::Bucket` CloudFormation resource to set
Object Ownership when you create a new bucket, see [OwnershipControls within
AWS::S3::Bucket](../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.md#cfn-s3-bucket-ownershipcontrols "../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.md#cfn-s3-bucket-ownershipcontrols") in the
_AWS CloudFormation User Guide_.

To apply the Bucket owner enforced setting for S3 Object Ownership, use the
`CreateBucket` API operation with the
`x-amz-object-ownership` request header set to
`BucketOwnerEnforced`. For information and examples, see [CreateBucket](../API/API_CreateBucket.md "../API/API_CreateBucket.md") in the
_Amazon Simple Storage Service API Reference_.

**Next steps**: After you apply the Bucket owner enforced or
bucket owner preferred settings for Object Ownership, you can further take the following steps:

- [Bucket owner enforced](ensure-object-ownership.md#object-ownership-requiring-bucket-owner-enforced "ensure-object-ownership.md#object-ownership-requiring-bucket-owner-enforced") –
  Require that all new buckets are created with ACLs disabled by using an IAM or Organizations policy.
- [Bucket owner preferred](ensure-object-ownership.md#ensure-object-ownership-bucket-policy "ensure-object-ownership.md#ensure-object-ownership-bucket-policy") – Add an
  S3 bucket policy to require the `bucket-owner-full-control` canned ACL for all object uploads
  to your bucket.
