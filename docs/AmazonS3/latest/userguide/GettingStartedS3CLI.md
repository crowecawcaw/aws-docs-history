# Getting started with Amazon S3 using the AWS CLI

You can get started with Amazon S3 by using the AWS Command Line Interface (AWS CLI) to work with general purpose buckets and
objects. A bucket is a container for objects. An object is a file and any metadata that
describes that file.

To store an object in Amazon S3, you create a bucket and then upload the object to the bucket.
When the object is in the bucket, you can open it, download it, and move it. When you no
longer need an object or a bucket, you can clean up your resources.

With Amazon S3, you pay only for what you use. For more information about Amazon S3 features and
pricing, see [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/"). If you are a new Amazon S3 customer,
you can get started with Amazon S3 for free. For more information, see [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/").

###### Note

For more information about using the Amazon S3 Express One Zone storage class with
directory buckets, see [Tutorial: Getting started with S3 Express One Zone](s3-express-getting-started.md "s3-express-getting-started.md") and [Working with directory buckets](directory-buckets-overview.md "directory-buckets-overview.md").

## Setting up

Before you begin using the AWS CLI with Amazon S3, make sure that you have:

- Signed up for an AWS account. For instructions, see [Setting up Amazon S3](GetStartedWithS3.md#setting-up-s3 "GetStartedWithS3.md#setting-up-s3").
- Created a user with `s3:*` permissions. For instructions, see [Setting up Amazon S3](GetStartedWithS3.md#setting-up-s3 "GetStartedWithS3.md#setting-up-s3").
- Installed and configured the AWS CLI. For instructions, see [Installing or updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the
  _AWS Command Line Interface User Guide_.

To verify that the AWS CLI is properly configured, run the following command:

```
aws sts get-caller-identity
```

For more information, see [get-caller-identity](../../../cli/latest/reference/sts/get-caller-identity.md "../../../cli/latest/reference/sts/get-caller-identity.md")
in the _AWS CLI Command Reference_.

This command displays a list of available Amazon S3 commands if the AWS CLI is properly
installed and configured.

## Step 1: Create your first Amazon S3

bucket

After you set up the AWS CLI, you're ready to create a bucket in Amazon S3. Every object in
Amazon S3 is stored in a bucket. Before you can store data in Amazon S3, you must create a
bucket.

###### Note

You are not charged for creating a bucket. You are charged only for storing
objects in the bucket and for transferring objects in and out of the bucket. The
charges that you incur through following the examples in this guide are minimal
(less than $1). For more information about storage charges, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

###### To create a bucket

1. Create a bucket using the `s3api create-bucket` command. Replace
   `amzn-s3-demo-bucket` with a unique bucket name and
   `us-east-1` with your desired Region:

```
aws s3api create-bucket --bucket `amzn-s3-demo-bucket` --region `us-east-1`
```

For Regions other than us-east-1, you need to specify the location
constraint:

```
aws s3api create-bucket --bucket `amzn-s3-demo-bucket` --region `us-west-2` --create-bucket-configuration LocationConstraint=`us-west-2`
```

###### Note

    * After you create a bucket, you can't change its Region.
    * To minimize latency and costs and address regulatory requirements,
     choose a Region close to you. Objects stored in a Region never leave
     that Region unless you explicitly transfer them to another Region.
     For a list of Amazon S3 AWS Regions, see [AWS service
     endpoints](../../../general/latest/gr/rande.md#s3_region "../../../general/latest/gr/rande.md#s3_region") in the
     *Amazon Web Services General Reference*.
    * The bucket name must:




    	+ Be unique within a partition. A partition is a grouping of
    	 Regions. AWS currently has three partitions:
    	 `aws` (commercial Regions),
    	 `aws-cn` (China Regions), and
    	 `aws-us-gov` (AWS GovCloud (US) Regions).
    	+ Be between 3 and 63 characters long.
    	+ Consist only of lowercase letters, numbers, periods (.),
    	 and hyphens (-). For best compatibility, we recommend that
    	 you avoid using periods (.) in bucket names, except for
    	 buckets that are used only for static website
    	 hosting.
    	+ Begin and end with a letter or number.
    * After you create the bucket, you can't change its name.
    * Don't include sensitive information in the bucket name. The bucket
     name is visible in the URLs that point to the objects in the
     bucket.

2. Verify that your bucket was created by listing all buckets:

```
aws s3 ls
```

3. For [Object Ownership](about-object-ownership.md "about-object-ownership.md"), you can disable or enable ACLs
   and control ownership of objects uploaded to your bucket.

**ACLs disabled**

To set **Bucket owner enforced** (default) – ACLs
are disabled, and the bucket owner automatically owns and has full control over
every object in the general purpose bucket:

```
aws s3api put-bucket-ownership-controls --bucket `amzn-s3-demo-bucket` --ownership-controls="Rules=[{ObjectOwnership=BucketOwnerEnforced}]"
```

###### Note

By default, ACLs are disabled. A majority of modern use cases in Amazon S3 no
longer require the use of ACLs. We recommend that you keep ACLs disabled,
except in circumstances where you must control access for each
object individually. For more information, see [Controlling ownership of objects and disabling ACLs
for your bucket](about-object-ownership.md "about-object-ownership.md").

**ACLs enabled**

    * To set **Bucket owner preferred** – The
     bucket owner owns and has full control over new objects that other
     accounts write to the bucket with the
     `bucket-owner-full-control` canned ACL:



    ```
    aws s3api put-bucket-ownership-controls --bucket `amzn-s3-demo-bucket` --ownership-controls="Rules=[{ObjectOwnership=BucketOwnerPreferred}]"
    ```

    If you apply the **Bucket owner
     preferred** setting and want to require all Amazon S3 uploads to
     include the `bucket-owner-full-control` canned ACL, you can
     [Requiring the bucket-owner-full-control
     canned ACL for Amazon S3 PUT operations (bucket owner preferred)](ensure-object-ownership.md#ensure-object-ownership-bucket-policy "ensure-object-ownership.md#ensure-object-ownership-bucket-policy") that allows
     only object uploads that use this ACL.
    * To set **Object writer** – The AWS
     account that uploads an object owns the object, has full control over
     it, and can grant other users access to it through ACLs:



    ```
    aws s3api put-bucket-ownership-controls --bucket `amzn-s3-demo-bucket` --ownership-controls="Rules=[{ObjectOwnership=ObjectWriter}]"
    ```

###### Note

The default setting is **Bucket owner
enforced**. To apply the default setting and keep ACLs
disabled, only the `s3:CreateBucket` permission is needed. To
enable ACLs, you must have the `s3:PutBucketOwnershipControls`
permission.

To check the current Object Ownership setting for your bucket:

```
aws s3api get-bucket-ownership-controls --bucket `amzn-s3-demo-bucket`
```

4. To verify that **Block Public Access** is enabled
   (it's enabled by default for new buckets):

```
aws s3api get-public-access-block --bucket `amzn-s3-demo-bucket`
```

By default, all four **Block Public Access**
settings are enabled for new buckets. We recommend that you keep all settings
enabled, unless you know that you need to turn off one or more of them for your
specific use case. For more information about blocking public access, see [Blocking public access to your Amazon S3
storage](access-control-block-public-access.md "access-control-block-public-access.md").

If you need to enable **Block Public Access**,
use the following command:

```
aws s3api put-public-access-block --bucket `amzn-s3-demo-bucket` --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
```

###### Note

To enable all Block Public Access settings, only the
`s3:CreateBucket` permission is required. To turn off any
Block Public Access settings, you must have the
`s3:PutBucketPublicAccessBlock` permission. 5. To enable versioning for your bucket:

```
aws s3api put-bucket-versioning --bucket `amzn-s3-demo-bucket` --versioning-configuration Status=Enabled
```

By default, Bucket Versioning is disabled. Versioning is a means of keeping
multiple variants of an object in the same bucket. You can use versioning to
preserve, retrieve, and restore every version of every object stored in your
bucket. With versioning, you can recover more easily from both unintended user
actions and application failures. For more information about versioning, see
[Retaining multiple versions of objects with S3 Versioning](Versioning.md "Versioning.md"). 6. Amazon S3 Object Lock helps protect new objects from being deleted or overwritten.
For more information, see [Locking objects with Object Lock](object-lock.md "object-lock.md"). To enable [Locking objects with Object Lock](object-lock.md "object-lock.md") (requires bucket versioning):

For a new bucket:

```
aws s3api create-bucket --bucket `amzn-s3-demo-bucket` --region `us-east-1` --object-lock-enabled-for-bucket
```

For an existing bucket:

```
aws s3api put-object-lock-configuration --bucket `amzn-s3-demo-bucket` --object-lock-configuration '{"ObjectLockEnabled": "Enabled"}'
```

If you want to set a default [Locking objects with Object Lock](object-lock.md "object-lock.md") along with enabling Object Lock, you can
use:

```
aws s3api put-object-lock-configuration --bucket `amzn-s3-demo-bucket` --object-lock-configuration '{"ObjectLockEnabled":"Enabled","Rule":{"DefaultRetention":{"Mode":"COMPLIANCE","Days":30}}}'
```

You can replace `"COMPLIANCE"` with `"GOVERNANCE"` for a
less restrictive mode, and adjust the number of days as needed.

###### Note

To create an Object Lock enabled bucket, you must have the following
permissions: `s3:CreateBucket`,
`s3:PutBucketVersioning`, and
`s3:PutBucketObjectLockConfiguration`. 7. You can add tags to your bucket. With AWS cost allocation, you can use
bucket tags to annotate billing for your use of a bucket. A tag is a key-value
pair that represents a label that you assign to a bucket. For more information,
see [Using cost allocation S3 bucket tags](CostAllocTagging.md "CostAllocTagging.md").

To add tags to your bucket:

```
aws s3api put-bucket-tagging --bucket `amzn-s3-demo-bucket` --tagging 'TagSet=[{Key=Purpose,Value=Testing},{Key=Environment,Value=Development}]'
```

8. Buckets and new objects are encrypted by using server-side encryption with
   Amazon S3 managed keys (`SSE-S3`) as the base level of encryption
   configuration. To verify the default encryption of your bucket, use the
   following command:

```
aws s3api get-bucket-encryption --bucket `amzn-s3-demo-bucket`
```

You can also configure server-side encryption with AWS KMS keys
(`SSE-KMS`) and dual-layer server-side encryption with AWS KMS keys
(`DSSE-KMS`) for your bucket. Both the AWS managed key
(`aws/s3`) and your customer managed keys can be used as your
AWS KMS key for `SSE-KMS` and `DSSE-KMS` encryption
configuration. For more information about customer managed keys, see [Customer keys and AWS keys](../../../kms/latest/developerguide/concepts.md#key-mgmt "../../../kms/latest/developerguide/concepts.md#key-mgmt") in the
_AWS Key Management Service Developer Guide_. For more information about creating an
AWS KMS key, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in
the _AWS Key Management Service Developer Guide_.

###### Important

The AWS KMS key must be in the same AWS Region as your Amazon S3 bucket.
Cross-region KMS keys aren't supported for Amazon S3 bucket encryption.

When you configure your bucket to use default encryption with SSE-KMS, you can
also use Amazon S3 Bucket Keys. Amazon S3 Bucket Keys lower the cost of encryption by
decreasing request traffic from Amazon S3 to AWS KMS. For more information, see [Reducing the cost of SSE-KMS with Amazon S3 Bucket Keys](bucket-key.md "bucket-key.md"). Amazon S3 Bucket Keys aren't
supported for DSSE-KMS. In the AWS CLI, Amazon S3 Bucket Keys are NOT enabled by
default when creating a new bucket. This is different from the console behavior
where they are enabled by default.

To configure `SSE-KMS` and enable Amazon S3 Bucket Keys:

```
aws s3api put-bucket-encryption --bucket `amzn-s3-demo-bucket` --server-side-encryption-configuration "{\"Rules\":[{\"ApplyServerSideEncryptionByDefault\":{\"SSEAlgorithm\":\"aws:kms\",\"KMSMasterKeyID\":\"YOUR-KMS-KEY-ARN\"},\"BucketKeyEnabled\":true}]}"
```

To check whether Amazon S3 Bucket Keys are enabled for a bucket:

```
aws s3api get-bucket-encryption --bucket `amzn-s3-demo-bucket`
```

The output will include a `BucketKeyEnabled` field set to either
`true` or `false`.

To configure `DSSE-KMS`, use the following command:

```
aws s3api put-bucket-encryption --bucket `amzn-s3-demo-bucket` --server-side-encryption-configuration '{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"aws:kms:dsse","KMSMasterKeyID":"`YOUR-KMS-KEY-ARN`"}}]}'
```

For more information about default encryption, see [Setting default server-side encryption behavior for Amazon S3
buckets](bucket-encryption.md "bucket-encryption.md"). For more
information about SSE-S3, see [Using server-side encryption with Amazon S3 managed keys
(SSE-S3)](UsingServerSideEncryption.md "UsingServerSideEncryption.md").

###### Important

If you use the SSE-KMS or DSSE-KMS option for your default encryption
configuration, you are subject to the requests per second (RPS) quota of
AWS KMS. You can reduce KMS API calls by enabling Amazon S3 Bucket Keys, which
decreases the number of requests sent to AWS KMS. For more information about
AWS KMS quotas and how to request a quota increase, see [Quotas](../../../kms/latest/developerguide/limits.md "../../../kms/latest/developerguide/limits.md") in the _AWS Key Management Service Developer Guide_.

You've created a bucket in Amazon S3. Next step is to upload an object to your
bucket.

## Step 2: Upload an object to your

bucket

After creating a bucket in Amazon S3, you're ready to upload an object to the bucket. An
object can be any kind of file: a text file, a photo, a video, and so on.

###### To upload an object to a bucket

1. Create a simple text file to upload. You can use any text editor or run the
   following command:

```
echo 'Hello, Amazon S3!' > example.txt
```

2. Upload the file to your bucket using the s3 cp command:

```
aws s3 cp example.txt s3://`amzn-s3-demo-bucket`/
```

If the upload is successful, you'll see output similar to:

```
upload: ./example.txt to s3://`amzn-s3-demo-bucket`/example.txt
```

3. Verify that the object was uploaded by listing the contents of your
   bucket:

```
aws s3 ls s3://`amzn-s3-demo-bucket`/
```

You've successfully uploaded an object to your bucket. Next step is to download an
object.

## Step 3: Download an object

After you upload an object to a bucket, you can view information about your object and
download the object to your local computer.

###### To download an object from an Amazon S3 bucket

1. To get information about your object:

```
aws s3api head-object --bucket `amzn-s3-demo-bucket` --key example.txt
```

This command returns metadata about the object, including its content type,
content length, and last modified date. 2. Download the object to your local computer:

```
aws s3 cp s3://`amzn-s3-demo-bucket`/example.txt downloaded-example.txt
```

If the download is successful, you'll see output similar to:

```
download: s3://`amzn-s3-demo-bucket`/example.txt to ./downloaded-example.txt
```

3. Verify the contents of the downloaded file:

```
cat downloaded-example.txt
```

###### Note

- Unlike the console, the AWS CLI can download multiple objects at once using
  wildcards or the `--recursive` flag.
- When downloading objects with the AWS CLI, periods (.) at the end of object
  key names are preserved, unlike in the console where they are removed. This
  is important if your object keys end with periods.

Example of downloading multiple objects:

To download multiple objects from an Amazon S3 bucket with specific file extensions, use
the recursive copy command with `exclude` and `include` filters as
shown in the example.

```
aws s3 cp s3://`amzn-s3-demo-bucket`/ . --recursive --exclude "*" --include "*.txt"
```

You've successfully downloaded your object. Next step is to copy your object to a
folder.

## Step 4: Copy your object to a folder

You've already added an object to a bucket and downloaded the object. Now, you create
a folder and copy the object to the folder.

###### To copy an object to a folder

1. In Amazon S3, folders are represented by prefixes in object keys. Create a "folder"
   by copying an object with a prefix:

```
aws s3 cp s3://`amzn-s3-demo-source-bucket`/example.txt s3://`amzn-s3-demo-destination-bucket`/favorite-files/example.txt
```

If the copy is successful, you'll see output similar to:

```
copy: s3://`amzn-s3-demo-source-bucket`/example.txt to s3://`amzn-s3-demo-destination-bucket`/favorite-files/example.txt
```

2. Verify that the object was copied by listing the contents of the
   folder:

```
aws s3 ls s3://`amzn-s3-demo-destination-bucket`/favorite-files/
```

You've successfully copied your object to a folder. Next step is to delete your
objects and bucket.

## Step 5: Delete your objects and

bucket

When you no longer need an object or a bucket, we recommend that you delete them to
prevent further charges. If you completed this getting started walkthrough as a learning
exercise, and you don't plan to use your bucket or objects, we recommend that you delete
your bucket and objects so that charges no longer accrue.

Before you delete your bucket, empty the bucket or delete the objects in the bucket.
After you delete your objects and bucket, they are no longer available.

If you want to continue to use the same bucket name, we recommend that you delete the
objects or empty the bucket, but don't delete the bucket. After you delete a bucket, the
name becomes available to reuse. However, another AWS account might create a bucket
with the same name before you have a chance to reuse it.

### Deleting an object

If you want to choose which objects you delete without emptying all the objects
from your bucket, you can delete an object.

Delete a specific object:

```
aws s3 rm s3://`amzn-s3-demo-bucket`/example.txt
```

If the deletion is successful, you'll see output similar to:

```
delete: s3://`amzn-s3-demo-bucket`/example.txt
```

### Emptying your

bucket

If you plan to delete your bucket, you must first empty your bucket, which deletes
all the objects, versions, and delete markers in the bucket.

###### To empty a bucket

###### Important

Emptying the bucket cannot be undone. Objects added to the bucket while
the empty bucket action is in progress will be deleted.

1. **Option 1:** For smaller buckets, use the
   `rm` command with the `--recursive` flag to delete
   all objects in the bucket:

```
aws s3 rm s3://`amzn-s3-demo-bucket` --recursive
```

This command deletes all objects in the bucket, including objects in
folders.

###### Note

If your bucket contains many objects or large objects, this command
might time out. For buckets with large amounts of data, use the Amazon S3
Lifecycle rule to expire objects in the buckets.

**Option 2:** Use Amazon S3 Lifecycle rules
(recommended for large buckets)

For buckets with many objects or large objects, use an Amazon S3 Lifecycle rule
to automatically expire and delete all objects. Wait for the lifecycle rule
to process (this may take up to 24 hours). For more information about using
lifecycle rules to empty buckets, see [How do
I empty an Amazon S3 bucket using a lifecycle configuration
rule?](https://repost.aws/knowledge-center/s3-empty-bucket-lifecycle-rule "https://repost.aws/knowledge-center/s3-empty-bucket-lifecycle-rule"). 2. Verify that the bucket is empty:

```
aws s3 ls s3://`amzn-s3-demo-bucket`
```

3. If your bucket has versioning enabled, use the following commands to
   delete versioned objects and delete markers.

Remove versioned objects:

```
aws s3api delete-objects --bucket `amzn-s3-demo-bucket` --delete "$(aws s3api list-object-versions --bucket `amzn-s3-demo-bucket` --output json --query='{Objects: Versions[].{Key:Key,VersionId:VersionId}}')"
```

Remove delete markers:

```
aws s3api delete-objects --bucket `amzn-s3-demo-bucket` --delete "$(aws s3api list-object-versions --bucket `amzn-s3-demo-bucket` --output json --query='{Objects: DeleteMarkers[].{Key:Key,VersionId:VersionId}}')"
```

4. Verify that the bucket is empty of all object versions and delete
   markers:

```
aws s3api list-object-versions --bucket `amzn-s3-demo-bucket`
```

The output should show no versions or delete markers remaining.

### Deleting your

bucket

After you empty your bucket or delete all the objects from your bucket, you can
delete your bucket.

###### Important

Deleting a bucket can't be undone. Bucket names are unique. If you delete your
bucket, another AWS user can use the name. If you want to continue to use the
same bucket name, don't delete your bucket. Instead, empty and keep the
bucket.

###### To delete your bucket

1. Delete your bucket:

```
aws s3api delete-bucket --bucket `amzn-s3-demo-bucket`
```

2. Verify that the bucket was deleted by listing all your buckets:

```
aws s3 ls
```

## Next steps

In the preceding examples, you learned how to perform some basic Amazon S3 tasks using the
AWS CLI.

The following topics explain the learning paths that you can use to gain a deeper
understanding of Amazon S3 so that you can implement it in your applications.

- [Understand common use cases](GetStartedWithS3.md#s3-use-cases "GetStartedWithS3.md#s3-use-cases")
- [Control access to your buckets and
  objects](GetStartedWithS3.md#control-access-resources "GetStartedWithS3.md#control-access-resources")
- [Protect and monitor your storage](GetStartedWithS3.md#manage-monitor-storage "GetStartedWithS3.md#manage-monitor-storage")
- [Develop with Amazon S3](GetStartedWithS3.md#develop-with-s3 "GetStartedWithS3.md#develop-with-s3")
- [Understand common use cases](GetStartedWithS3.md#s3-getting-started-tutorials-list "GetStartedWithS3.md#s3-getting-started-tutorials-list")
- [Explore training and support](GetStartedWithS3.md#explore-training-and-support "GetStartedWithS3.md#explore-training-and-support")

The following list shows common AWS CLI commands for Amazon S3:

- [cp](../../../cli/latest/reference/s3/cp.md "../../../cli/latest/reference/s3/cp.md") –
  Copies files or objects between your local file system and Amazon S3, or between Amazon S3
  locations
- [ls](../../../cli/latest/reference/s3/ls.md "../../../cli/latest/reference/s3/ls.md") –
  Lists Amazon S3 objects and common prefixes under a specified bucket and
  prefix
- [mb](../../../cli/latest/reference/s3/mb.md "../../../cli/latest/reference/s3/mb.md") –
  Creates an Amazon S3 bucket
- [mv](../../../cli/latest/reference/s3/mv.md "../../../cli/latest/reference/s3/mv.md") –
  Moves files or objects between your local file system and Amazon S3, or between Amazon S3
  locations
- [presign](../../../cli/latest/reference/s3/presign.md "../../../cli/latest/reference/s3/presign.md") – Generates a pre-signed URL for an Amazon S3 object that allows
  temporary access without AWS credentials
- [rb](../../../cli/latest/reference/s3/rb.md "../../../cli/latest/reference/s3/rb.md") –
  Removes an empty Amazon S3 bucket. You can use the `--force` flag to
  automatically empty and delete a bucket with contents in a single command. This
  action can't be undone.
- [rm](../../../cli/latest/reference/s3/rm.md "../../../cli/latest/reference/s3/rm.md") –
  Deletes objects from Amazon S3
- [sync](../../../cli/latest/reference/s3/sync.md "../../../cli/latest/reference/s3/sync.md") – Syncs directories and Amazon S3 prefixes by recursively copying
  new and updated files from the source directory to the destination.
- [website](../../../cli/latest/reference/s3/website.md "../../../cli/latest/reference/s3/website.md") – Configures a bucket as a static website

For more information about the AWS CLI commands for Amazon S3, see the following
resources:

- [s3](../../../cli/latest/reference/s3/index.md "../../../cli/latest/reference/s3/index.md") – High-level Amazon S3 commands that simplify common
  operations
- [s3api](../../../cli/latest/reference/s3api/index.md "../../../cli/latest/reference/s3api/index.md") – Direct access to all Amazon S3 API operations
- [s3control](../../../cli/latest/reference/s3control/index.md "../../../cli/latest/reference/s3control/index.md") – Direct access to all Amazon S3 Control API operations
