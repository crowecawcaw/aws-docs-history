# Copying, moving, and renaming objects

The `CopyObject` operation creates a copy of an object that's already stored in
Amazon S3.

You can create a copy of an object up to 5 GB in a single atomic operation. However, to
copy an object that's larger than 5 GB, you must use a multipart upload using the AWS CLI or
AWS SDKs. For more information, see [Copying an object using multipart upload](CopyingObjectsMPUapi.md "CopyingObjectsMPUapi.md").

###### Note

To maintain the performance benefit of an object you uploaded using multipart upload, you must copy the object using multipart upload using the AWS CLI or AWS SDK instead of the S3 console. For more information, see [Copying an object using multipart upload](CopyingObjectsMPUapi.md "CopyingObjectsMPUapi.md").

Using the `CopyObject` operation, you can:

- Create additional copies of objects.
- Rename objects by copying them and deleting the original ones.
- Copy or move objects from one bucket to another, including across AWS Regions
  (for example, from `us-west-1` to `eu-west-2`). When you move
  an object, Amazon S3 copies the object to the specified destination and then deletes the
  source object.

###### Note

Copying or moving objects across AWS Regions incurs bandwidth charges. For
more information, see [Amazon S3
Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

- Change object metadata. Each Amazon S3 object has metadata. This metadata is a set of
  name-value pairs. You can set object metadata at the time you upload an object.
  After you upload the object, you can't modify the object metadata. The only way to
  modify object metadata is to make a copy of the object and set the metadata. To do
  so, in the copy operation, set the same object as the source and target.

Some object metadata is system metadata and other is user-defined. You can control
some of the system metadata. For example, you can control the storage class and the
type of server-side encryption to use for the object. When you copy an object,
user-controlled system metadata and user-defined metadata are also copied. Amazon S3
resets the system-controlled metadata. For example, when you copy an object, Amazon S3
resets the creation date of the copied object. You don't need to set any of these
system-controlled metadata values in your copy request.

When copying an object, you might decide to update some of the metadata values.
For example, if your source object is configured to use S3 Standard storage, you
might choose to use S3 Intelligent-Tiering for the object copy. You might also decide
to alter some of the user-defined metadata values present on the source object. If
you choose to update any of the object's user-configurable metadata (system or
user-defined) during the copy, then you must explicitly specify all of the
user-configurable metadata present on the source object in your request, even if you
are changing only one of the metadata values.

###### Note

When copying an object by using the Amazon S3 console, you might receive the error
message **`"Copied metadata can't be verified."`** The console
uses headers to retrieve and set metadata for your object. If your network or
browser configuration modifies your network requests, this behavior might cause
unintended metadata (such as modified `Cache-Control` headers) to be
written to your copied object. Amazon S3 can't verify this unintended
metadata.

To address this issue, check your network and browser configuration to make sure it
doesn't modify headers, such as `Cache-Control`. For more information, see
[The Shared Responsibility Model](../../../whitepapers/latest/applying-security-practices-to-network-workload-for-csps/the-shared-responsibility-model.md "../../../whitepapers/latest/applying-security-practices-to-network-workload-for-csps/the-shared-responsibility-model.md").

For more information about object metadata, see [Working with object metadata](UsingMetadata.md "UsingMetadata.md").

###### Copying archived and restored objects

If the source object is archived in S3 Glacier Flexible Retrieval or
S3 Glacier Deep Archive, you must first restore a temporary copy before you can
copy the object to another bucket. For information about archiving objects, see [Working with archived objects](archived-objects.md "archived-objects.md").

The **Copy** operation in the Amazon S3 console isn't supported
for restored objects in the S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive
storage classes. To copy these restored objects, use the AWS Command Line Interface (AWS CLI), the AWS SDKs,
or the Amazon S3 REST API.

###### Copying encrypted objects

Amazon S3 automatically encrypts all new objects that are copied to an S3 bucket. If you
don't specify encryption information in your copy request, the encryption setting of the
target object is set to the default encryption configuration of the destination bucket.
By default, all buckets have a base level of encryption configuration that uses
server-side encryption with Amazon S3 managed keys (SSE-S3). If the destination bucket has a
default encryption configuration that uses server-side encryption with an AWS Key Management Service
(AWS KMS) key (SSE-KMS), or a customer-provided encryption key (SSE-C), Amazon S3 uses the
corresponding KMS key, or a customer-provided key to encrypt the target object
copy.

When copying an object, if you want to use a different type of encryption setting for the
target object, you can request that Amazon S3 encrypt the target object with a KMS key, an Amazon S3
managed key, or a customer-provided key. If the encryption setting in your request is
different from the default encryption configuration of the destination bucket, the
encryption setting in your request takes precedence. If the source object for the copy is
encrypted with SSE-C, you must provide the necessary encryption information in your request
so that Amazon S3 can decrypt the object for copying. For more information, see [Protecting data with encryption](UsingEncryption.md "UsingEncryption.md").

###### Using checksums when copying objects

When copying objects, you can choose to use a different checksum algorithm for the
object. Whether you choose to use the same algorithm or a new one, Amazon S3 calculates a new
checksum value after the object is copied. Amazon S3 doesn't directly copy the value of the
checksum. All copied objects without checksums and specified destination checksum
algorithms automatically gain a `CRC-64NVME` checksum algorithm. For more
information about how the checksum is calculated, see [Uploading and copying objects using multipart upload in Amazon S3](mpuoverview.md "mpuoverview.md").

###### Copying multiple objects in a single request

To copy more than one Amazon S3 object with a single request, you can also use
S3 Batch Operations.
You provide S3 Batch Operations with a list of objects to operate on. S3 Batch Operations calls the
respective API operation to perform the specified operation. A single Batch Operations job can perform the
specified operation on billions of objects containing exabytes of data.

The S3 Batch Operations feature tracks progress, sends notifications, and stores a detailed completion report of all actions,
providing a fully managed, auditable, serverless experience. You can use S3 Batch Operations through
the Amazon S3 console, AWS CLI, AWS SDKs, or REST API. For more information,
see [S3 Batch Operations basics](batch-ops.md#batch-ops-basics "batch-ops.md#batch-ops-basics").

###### Copying objects to directory buckets

For information about copying an object to a directory bucket, see [Copying objects from or to a directory bucket](directory-buckets-objects-copy.md "directory-buckets-objects-copy.md"). For information about using the
Amazon S3 Express One Zone storage class with directory buckets, see [S3 Express One Zone](directory-bucket-high-performance.md#s3-express-one-zone "directory-bucket-high-performance.md#s3-express-one-zone") and [Working with directory buckets](directory-buckets-overview.md "directory-buckets-overview.md").

## To copy an object

To copy an object, use the following methods.

###### Note

The restrictions and limitations when you copy an object with the console are as follows:

- You can copy an object if your object is less than 5 GB. If your object is greater than 5 GB, you must use the [AWS CLI](mpu-upload-object.md#UsingCLImpUpload "mpu-upload-object.md#UsingCLImpUpload") or [AWS SDKs](CopyingObjectsMPUapi.md "CopyingObjectsMPUapi.md") to copy an object.
- For a list of additional permissions required to copy objects, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md"). For example policies that grant this permission, see [Identity-based policy examples for Amazon S3](example-policies-s3.md "example-policies-s3.md").
- The `Copy` action applies to all objects within the specified folders (prefixes). Objects added to these folders while the action is in progress might be affected.
- Cross-Region copying of objects encrypted with SSE-KMS is not supported by the
  Amazon S3 console. To copy objects encrypted with SSE-KMS across Regions, use the
  AWS CLI, AWS SDK, or the Amazon S3 REST API.
- Objects encrypted with customer-provided encryption keys (SSE-C) cannot be
  copied by using the S3 console. To copy objects encrypted with SSE-C, use the
  AWS CLI, AWS SDK, or the Amazon S3 REST API.
- Copied objects will not retain the Object Lock settings from the original objects.
- If the bucket you are copying objects from uses the bucket owner enforced setting for S3 Object Ownership, object ACLs will not be copied to the specified destination.
- If you want to copy objects to a bucket that uses the bucket owner enforced setting for S3 Object Ownership, make sure that the source bucket also uses the bucket owner enforced setting, or remove any object ACL grants to other AWS accounts and groups.

###### To copy an object

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets** or **Directory buckets**.
3. In the list of buckets, choose the name of the bucket that contains the objects that you want to copy.
4. Select the check box to the left of the names of the objects that you want to
   copy.
5. On the **Actions** menu, choose **Copy** from
   the list of options that appears.
6. Select the destination type and destination account. To specify the destination
   path, choose **Browse S3**, navigate to the destination, and select
   the check box to the left of the destination. Choose **Choose
   destination** in the lower-right corner.

Alternatively, enter the destination path. 7. If you do _not_ have bucket versioning enabled, you will see a warning recommending you enable Bucket Versioning to help protect against unintentionally overwriting or deleting objects. If you want to keep all versions of
objects in this bucket, select **Enable Bucket Versioning**. You
can also view the default encryption and S3 Object Lock properties in **Destination details**. 8. Under **Additional copy settings**, choose whether you want to **Copy source settings**, **Don’t specify settings**, or **Specify settings**. **Copy source settings** is the default option. If you only want to copy the object without the source settings attributes, choose **Don’t specify settings**. Choose **Specify settings** to specify settings for storage class, ACLs, object tags, metadata, server-side encryption, and additional checksums. 9. Choose **Copy** in the bottom-right corner. Amazon S3 copies your
objects to the destination.
The examples in this section show how to copy objects up to 5 GB in a single operation. To
copy objects larger than 5 GB, you must use a multipart upload. For more information, see
[Copying an object using multipart upload](CopyingObjectsMPUapi.md "CopyingObjectsMPUapi.md").

Java
For examples of how to copy objects with the AWS SDK for Java, see [Copy an object from one bucket to another](../API/s3_example_s3_CopyObject_section.md "../API/s3_example_s3_CopyObject_section.md") in the _Amazon S3 API Reference_.

.NET
The following C# example uses the high-level SDK for .NET to copy objects that are as
large as 5 GB in a single operation. For objects that are larger than 5 GB, use
the multipart upload copy example described in [Copying an object using multipart upload](CopyingObjectsMPUapi.md "CopyingObjectsMPUapi.md").

This example makes a copy of an object that is a maximum of 5 GB. For
information about setting up and running the code examples, see [Getting Started
with the AWS SDK for .NET](../../../sdk-for-net/latest/developer-guide/net-dg-setup.md "../../../sdk-for-net/latest/developer-guide/net-dg-setup.md") in the _AWS SDK for .NET Developer
Guide_.

```
using Amazon;
using Amazon.S3;
using Amazon.S3.Model;
using System;
using System.Threading.Tasks;

namespace Amazon.DocSamples.S3
{
    class CopyObjectTest
    {
        private const string sourceBucket = "*** provide the name of the bucket with source object ***";
        private const string destinationBucket = "*** provide the name of the bucket to copy the object to ***";
        private const string objectKey = "*** provide the name of object to copy ***";
        private const string destObjectKey = "*** provide the destination object key name ***";
        // Specify your bucket region (an example region is shown).
        private static readonly RegionEndpoint bucketRegion = RegionEndpoint.USWest2;
        private static IAmazonS3 s3Client;

        public static void Main()
        {
            s3Client = new AmazonS3Client(bucketRegion);
            Console.WriteLine("Copying an object");
            CopyingObjectAsync().Wait();
        }

        private static async Task CopyingObjectAsync()
        {
            try
            {
                CopyObjectRequest request = new CopyObjectRequest
                {
                    SourceBucket = sourceBucket,
                    SourceKey = objectKey,
                    DestinationBucket = destinationBucket,
                    DestinationKey = destObjectKey
                };
                CopyObjectResponse response = await s3Client.CopyObjectAsync(request);
            }
            catch (AmazonS3Exception e)
            {
                Console.WriteLine("Error encountered on server. Message:'{0}' when writing an object", e.Message);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unknown encountered on server. Message:'{0}' when writing an object", e.Message);
            }
        }
    }
}

```

PHP
This topic guides you through using classes from version 3 of the AWS SDK for PHP to copy
a single object and multiple objects within Amazon S3, from one bucket to another or within
the same bucket.

For more information about the AWS SDK for Ruby API, go to [AWS SDK for Ruby - Version
2](../../../sdkforruby/api/index.md "../../../sdkforruby/api/index.md").

The following PHP example illustrates the use of the `copyObject()`
method to copy a single object within Amazon S3. It also demonstrates how to make
multiple copies of an object by using a batch of calls to
`CopyObject` with the `getcommand()` method.

Copying objects| 1 | Create an instance of an Amazon S3 client by using the<br>`Aws\S3\S3Client` class constructor. |
| 2 | To make multiple copies of an object, you run a batch of<br>calls to the Amazon S3 client [getCommand()](../../../aws-sdk-php/v3/api/class-Aws.md#_getCommand "../../../aws-sdk-php/v3/api/class-Aws.md#_getCommand") method, which<br>is inherited from the [Aws\CommandInterface](../../../aws-sdk-php/v3/api/class-Aws.md "../../../aws-sdk-php/v3/api/class-Aws.md") class.<br>You provide the `CopyObject` command as the first<br>argument and an array containing the source bucket, source<br>key name, target bucket, and target key name as the second<br>argument. |

```
 require 'vendor/autoload.php';

use Aws\CommandPool;
use Aws\Exception\AwsException;
use Aws\ResultInterface;
use Aws\S3\S3Client;

$sourceBucket = '*** Your Source Bucket Name ***';
$sourceKeyname = '*** Your Source Object Key ***';
$targetBucket = '*** Your Target Bucket Name ***';

$s3 = new S3Client([
    'version' => 'latest',
    'region' => 'us-east-1'
]);

// Copy an object.
$s3->copyObject([
    'Bucket' => $targetBucket,
    'Key' => "$sourceKeyname-copy",
    'CopySource' => "$sourceBucket/$sourceKeyname",
]);

// Perform a batch of CopyObject operations.
$batch = array();
for ($i = 1; $i <= 3; $i++) {
    $batch[] = $s3->getCommand('CopyObject', [
        'Bucket' => $targetBucket,
        'Key' => "{targetKeyname}-$i",
        'CopySource' => "$sourceBucket/$sourceKeyname",
    ]);
}
try {
    $results = CommandPool::batch($s3, $batch);
    foreach ($results as $result) {
        if ($result instanceof ResultInterface) {
            // Result handling here
        }
        if ($result instanceof AwsException) {
            // AwsException handling here
        }
    }
} catch (Exception $e) {
    // General error handling here
}


```

Python

```
class ObjectWrapper:
    """Encapsulates S3 object actions."""

    def __init__(self, s3_object):
        """
        :param s3_object: A Boto3 Object resource. This is a high-level resource in Boto3
                          that wraps object actions in a class-like structure.
        """
        self.object = s3_object
        self.key = self.object.key


```

```
    def copy(self, dest_object):
        """
        Copies the object to another bucket.

        :param dest_object: The destination object initialized with a bucket and key.
                            This is a Boto3 Object resource.
        """
        try:
            dest_object.copy_from(
                CopySource={"Bucket": self.object.bucket_name, "Key": self.object.key}
            )
            dest_object.wait_until_exists()
            logger.info(
                "Copied object from %s:%s to %s:%s.",
                self.object.bucket_name,
                self.object.key,
                dest_object.bucket_name,
                dest_object.key,
            )
        except ClientError:
            logger.exception(
                "Couldn't copy object from %s/%s to %s/%s.",
                self.object.bucket_name,
                self.object.key,
                dest_object.bucket_name,
                dest_object.key,
            )
            raise


```

Ruby
The following tasks guide you through using the Ruby classes to
copy an object in Amazon S3 from one bucket to another or within the same bucket.

Copying objects| 1 | Use the Amazon S3 modularized gem for version 3 of the<br>AWS SDK for Ruby, require `aws-sdk-s3`, and provide<br>your AWS credentials. For more information about how to<br>provide your credentials, see [Making requests using AWS account or IAM user credentials](../API/AuthUsingAcctOrUserCredentials.md "../API/AuthUsingAcctOrUserCredentials.md") in the _Amazon S3 API Reference_. |
| 2 | Provide the request information, such as the source bucket<br>name, source key name, destination bucket name, and<br>destination key. |

The following Ruby code example demonstrates the preceding
tasks by using the `#copy_object` method to copy an object from one
bucket to another.

```
require 'aws-sdk-s3'

# Wraps Amazon S3 object actions.
class ObjectCopyWrapper
  attr_reader :source_object

  # @param source_object [Aws::S3::Object] An existing Amazon S3 object. This is used as the source object for
  #                                        copy actions.
  def initialize(source_object)
    @source_object = source_object
  end

  # Copy the source object to the specified target bucket and rename it with the target key.
  #
  # @param target_bucket [Aws::S3::Bucket] An existing Amazon S3 bucket where the object is copied.
  # @param target_object_key [String] The key to give the copy of the object.
  # @return [Aws::S3::Object, nil] The copied object when successful; otherwise, nil.
  def copy_object(target_bucket, target_object_key)
    @source_object.copy_to(bucket: target_bucket.name, key: target_object_key)
    target_bucket.object(target_object_key)
  rescue Aws::Errors::ServiceError => e
    puts "Couldn't copy #{@source_object.key} to #{target_object_key}. Here's why: #{e.message}"
  end
end

# Example usage:
def run_demo
  source_bucket_name = "amzn-s3-demo-bucket1"
  source_key = "my-source-file.txt"
  target_bucket_name = "amzn-s3-demo-bucket2"
  target_key = "my-target-file.txt"

  source_bucket = Aws::S3::Bucket.new(source_bucket_name)
  wrapper = ObjectCopyWrapper.new(source_bucket.object(source_key))
  target_bucket = Aws::S3::Bucket.new(target_bucket_name)
  target_object = wrapper.copy_object(target_bucket, target_key)
  return unless target_object

  puts "Copied #{source_key} from #{source_bucket_name} to #{target_object.bucket_name}:#{target_object.key}."
end

run_demo if $PROGRAM_NAME == __FILE__

```

This example describes how to copy an object by using the Amazon S3 REST API. For more
information about the REST API, see [CopyObject](../API/RESTObjectCOPY.md "../API/RESTObjectCOPY.md").

This example copies the `flotsam` object from the `amzn-s3-demo-bucket1`
bucket to the `jetsam` object of the `amzn-s3-demo-bucket2` bucket, preserving
its metadata.

```
PUT /jetsam HTTP/1.1
Host: `amzn-s3-demo-bucket2`.s3.amazonaws.com
x-amz-copy-source: /`amzn-s3-demo-bucket1`/flotsam
Authorization: AWS AKIAIOSFODNN7EXAMPLE:ENoSbxYByFA0UGLZUqJN5EUnLDg=
Date: Wed, 20 Feb 2008 22:12:21 +0000
```

The signature was generated from the following information.

```
PUT\r\n
\r\n
\r\n
Wed, 20 Feb 2008 22:12:21 +0000\r\n

x-amz-copy-source:/`amzn-s3-demo-bucket1`/flotsam\r\n
/`amzn-s3-demo-bucket2`/jetsam
```

Amazon S3 returns the following response that specifies the ETag of the object and when
it was last modified.

```
HTTP/1.1 200 OK
x-amz-id-2: Vyaxt7qEbzv34BnSu5hctyyNSlHTYZFMWK4FtzO+iX8JQNyaLdTshL0KxatbaOZt
x-amz-request-id: 6B13C3C5B34AF333
Date: Wed, 20 Feb 2008 22:13:01 +0000

Content-Type: application/xml
Transfer-Encoding: chunked
Connection: close
Server: AmazonS3
<?xml version="1.0" encoding="UTF-8"?>

<CopyObjectResult>
   <LastModified>2008-02-20T22:13:01</LastModified>
   <ETag>"7e9c608af58950deeb370c98608ed097"</ETag>
</CopyObjectResult>
```

You can also use the AWS Command Line Interface (AWS CLI) to copy an S3 object. For more
information, see [copy-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/copy-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/copy-object.html") in the _AWS CLI Command Reference_.

For information about the AWS CLI, see [What
is the AWS Command Line Interface?](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") in the _AWS Command Line Interface User Guide_.

## To move an object

To move an object, use the following methods.

###### Note

- You can move an object if your object is less than 5 GB. If your
  object is greater than 5 GB, you must use the [AWS CLI](mpu-upload-object.md#UsingCLImpUpload "mpu-upload-object.md#UsingCLImpUpload") or [AWS SDKs](CopyingObjectsMPUapi.md "CopyingObjectsMPUapi.md") to move an
  object.
- For a list of additional permissions required to move objects, see
  [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md"). For example
  policies that grant this permission, see [Identity-based policy examples for Amazon S3](example-policies-s3.md "example-policies-s3.md").
- Objects encrypted with customer-provided encryption keys (SSE-C)
  can't be moved by using the Amazon S3 console. To move objects encrypted
  with SSE-C, use the AWS CLI, AWS SDKs, or the Amazon S3 REST API.
- When moving folders, wait for the **Move** operation to finish before making additional
  changes in the folders.
- You can't use S3 access point aliases as the source or destination
  for **Move** operations in the Amazon
  S3 console.

###### To move an object

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**. Navigate to
   the Amazon S3 bucket or folder that contains the objects that you want to
   move.
3. Select the check box for the objects that you want to move.
4. On the **Actions** menu, choose
   **Move**.
5. To specify the destination path, choose **Browse
   S3**, navigate to the destination, and select the destination
   check box. Choose **Choose destination**.

Alternatively, enter the destination path. 6. If you do _not_ have bucket versioning enabled, you
will see a warning recommending you enable Bucket Versioning to help
protect against unintentionally overwriting or deleting objects. If you
want to keep all versions of objects in this bucket, select
**Enable Bucket Versioning**. You can also view the
default encryption and Object Lock properties in **Destination
details**. 7. Under **Additional copy settings**, choose whether
you want to **Copy source settings**, **Don’t
specify settings**, or **Specify
settings**. **Copy source settings** is
the default option. If you only want to copy the object without the
source settings attributes, choose **Don’t specify
settings**. Choose **Specify settings** to
specify settings for storage class, ACLs, object tags, metadata,
server-side encryption, and additional checksums. 8. Choose **Move** in the bottom-right corner. Amazon S3
moves your objects to the destination.
You can also use the AWS Command Line Interface (AWS CLI) to move an S3 object. For more
information, see [mv](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/mv.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/mv.html") in the _AWS CLI Command Reference_.

For information about the AWS CLI, see [What
is the AWS Command Line Interface?](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") in the _AWS Command Line Interface User Guide_.

## To rename an object

To rename an object, use the following procedure.

###### Note

- You can rename an object if your object is less than 5 GB. To rename
  objects greater than 5 GB, you must use the [AWS CLI](mpu-upload-object.md#UsingCLImpUpload "mpu-upload-object.md#UsingCLImpUpload") or [AWS SDKs](CopyingObjectsMPUapi.md "CopyingObjectsMPUapi.md")
  to copy your object with a new name and then delete the original
  object.
- For a list of additional permissions required to copy objects, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md"). For example policies that
  grant this permission, see [Identity-based policy examples for Amazon S3](example-policies-s3.md "example-policies-s3.md").
- Renaming an object creates a copy of the object with a new last-modified
  date, and then adds a delete marker to the original object.
- Bucket settings for default encryption are automatically applied to any
  specified object that's unencrypted.
- You can't use the Amazon S3 console to rename objects with customer-provided
  encryption keys (SSE-C). To rename objects encrypted with SSE-C, use the
  AWS CLI, AWS SDKs, or the Amazon S3 REST API to copy those objects with new
  names.
- If this bucket uses the bucket owner enforced setting for
  S3 Object Ownership, object access control lists (ACLs) won't be
  copied.

###### To rename an object

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Buckets**, and then choose
   the **General purpose buckets** tab. Navigate to the Amazon S3
   bucket or folder that contains the object that you want to rename.
3. Select the check box for the object that you want to rename.
4. On the **Actions** menu, choose **Rename
   object**.
5. In the **New object name** box, enter the new name for the
   object.
6. Under **Additional copy settings**, choose whether you want
   to **Copy source settings**, **Don’t specify
   settings**, or **Specify settings**.
   **Copy source settings** is the default option. If you only
   want to copy the object without the source settings attributes, choose
   **Don’t specify settings**. Choose **Specify
   settings** to specify settings for storage class, ACLs, object
   tags, metadata, server-side encryption, and additional checksums.
7. Choose **Save changes**. Amazon S3 renames your object.
