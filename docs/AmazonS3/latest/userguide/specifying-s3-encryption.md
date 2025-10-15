# Specifying server-side encryption with Amazon S3 managed
 keys (SSE-S3)

All Amazon S3 buckets have encryption configured by default, and all new objects that are uploaded 
to an S3 bucket are automatically encrypted at rest. Server-side encryption with Amazon S3 managed keys (SSE-S3) is the default encryption 
configuration for every bucket in Amazon S3. To use a different type of encryption, you can either specify the type of server-side encryption 
to use in your S3 `PUT` requests, or you can update the default encryption configuration in the destination bucket. 

If you want to specify a different encryption type in your `PUT` requests, you can use server-side encryption with 
AWS Key Management Service (AWS KMS) keys (SSE-KMS), dual-layer server-side encryption with AWS KMS keys (DSSE-KMS), or server-side encryption with 
customer-provided keys (SSE-C). If you want to set a different default encryption configuration in the destination bucket, you can use 
SSE-KMS or DSSE-KMS.

For more information about changing the default encryption configuration for your general purpose buckets, see [Configuring default encryption](default-bucket-encryption.md "default-bucket-encryption.md"). 

When you change the default encryption configuration of your bucket to SSE-KMS, the encryption type of the existing Amazon S3 objects in the bucket is not changed. To change the encryption type of your pre-existing objects after updating the default encryption configuration to SSE-KMS, you can use Amazon S3 Batch Operations. You provide S3 Batch Operations with a list of objects, and Batch Operations calls the respective API operation. You can use the [Copy objects](batch-ops-copy-object.md "batch-ops-copy-object.md") action to copy existing objects, which writes them back to the same bucket as SSE-KMS encrypted objects. A single Batch Operations job can perform the specified operation on billions of objects. For more information, see [Performing object operations in bulk with Batch Operations](batch-ops.md "batch-ops.md") and the *AWS Storage Blog* post [How to retroactively encrypt existing objects in Amazon S3 using S3 Inventory, Amazon Athena, and S3 Batch Operations](https://aws.amazon.com/blogs/security/how-to-retroactively-encrypt-existing-objects-in-amazon-s3-using-s3-inventory-amazon-athena-and-s3-batch-operations/ "https://aws.amazon.com/blogs/security/how-to-retroactively-encrypt-existing-objects-in-amazon-s3-using-s3-inventory-amazon-athena-and-s3-batch-operations/"). 

You can specify SSE-S3 by using the S3 console, REST APIs, AWS SDKs, and AWS Command Line Interface
 (AWS CLI). For more information, see [Setting default server-side encryption behavior for Amazon S3
 buckets](bucket-encryption.md "bucket-encryption.md").

This topic describes how to set or change the type of encryption an object by using the
 AWS Management Console. When you copy an object by using the console, Amazon S3 copies the object as is. That
 means that if the source object is encrypted, the target object is also encrypted. You can use
 the console to add or change encryption for an object. 

###### Note


* You can change an object's encryption if your object is less than 5 GB. If your object is greater than 5 GB, you must use the [AWS CLI](mpu-upload-object.md#UsingCLImpUpload "mpu-upload-object.md#UsingCLImpUpload") or [AWS SDKs](CopyingObjectsMPUapi.md "CopyingObjectsMPUapi.md") to change an object's encryption.
* For a list of additional permissions required to change an object's encryption, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md"). For example policies that grant this permission, see [Identity-based policy examples for Amazon S3](example-policies-s3.md "example-policies-s3.md").
* If you change an object's encryption, a new object is created to replace the old one.
 If S3 Versioning is enabled, a new version of the object is created, and the existing
 object becomes an older version. The role that changes the property also becomes the owner
 of the new object (or object version).
###### To change encryption for an object

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Buckets**, and then choose
 the **General purpose buckets** tab. Navigate to the Amazon S3 bucket or
 folder that contains the objects you want to change.
3. Select the check box for the objects you want to
 change.
4. On the **Actions** menu, choose **Edit server-side encryption** from
 the list of options that appears.
5. Scroll to the **Server-side encryption** section.
6. Under **Encryption settings**, choose **Use bucket settings for default encryption** or **Override bucket settings for default encryption**.
7. If you chose **Override bucket settings for default encryption**,
 configure the following encryption settings.


	1. Under **Encryption type**, choose **Server-side encryption with Amazon S3 managed keys (SSE-S3)**.
	 SSE-S3 uses one of the strongest block ciphers—256-bit Advanced Encryption
	 Standard (AES-256) to encrypt each object. For more information, see [Using server-side encryption with Amazon S3 managed keys
	 (SSE-S3)](UsingServerSideEncryption.md "UsingServerSideEncryption.md").
8. Under **Additional copy settings**, choose whether you want to **Copy source settings**, **Don’t specify settings**, or **Specify settings**. **Copy source settings** is the default option. If you only want to copy the object without the source settings attributes, choose **Don’t specify settings**. Choose **Specify settings** to specify settings for storage class, ACLs, object tags, metadata, server-side encryption, and additional checksums.
9. Choose **Save changes**.
###### Note

This action applies encryption to all specified objects. When you're encrypting folders,
 wait for the save operation to finish before adding new objects to the folder.

At the time of object creation—that is, when you are uploading a new object or
 making a copy of an existing object—you can specify if you want Amazon S3 to encrypt your
 data with Amazon S3 managed keys (SSE-S3) by adding the `x-amz-server-side-encryption`
 header to the request. Set the value of the header to the encryption algorithm
 `AES256`, which Amazon S3 supports. Amazon S3 confirms that your object is stored with
 SSE-S3 by returning the response header `x-amz-server-side-encryption`. 

The following REST upload API operations accept the
 `x-amz-server-side-encryption` request header.


* [PUT Object](../API/RESTObjectPUT.md "../API/RESTObjectPUT.md")
* [PUT Object - Copy](../API/RESTObjectCOPY.md "../API/RESTObjectCOPY.md")
* [POST Object](../API/RESTObjectPOST.md "../API/RESTObjectPOST.md")
* [Initiate Multipart
 Upload](../API/mpUploadInitiate.md "../API/mpUploadInitiate.md")
When uploading large objects by using the multipart upload API operation, you can
 specify server-side encryption by adding the `x-amz-server-side-encryption`
 header to the Initiate Multipart Upload request. When you're copying an existing object,
 regardless of whether the source object is encrypted or not, the destination object is not
 encrypted unless you explicitly request server-side encryption.

The response headers of the following REST API operations return the
 `x-amz-server-side-encryption` header when an object is stored using SSE-S3. 


* [PUT Object](../API/RESTObjectPUT.md "../API/RESTObjectPUT.md")
* [PUT Object - Copy](../API/RESTObjectCOPY.md "../API/RESTObjectCOPY.md")
* [POST Object](../API/RESTObjectPOST.md "../API/RESTObjectPOST.md")
* [Initiate Multipart
 Upload](../API/mpUploadInitiate.md "../API/mpUploadInitiate.md")
* [Upload Part](../API/mpUploadUploadPart.md "../API/mpUploadUploadPart.md")
* [Upload Part -
 Copy](../API/mpUploadUploadPartCopy.md "../API/mpUploadUploadPartCopy.md")
* [Complete Multipart
 Upload](../API/mpUploadComplete.md "../API/mpUploadComplete.md")
* [Get Object](../API/RESTObjectGET.md "../API/RESTObjectGET.md")
* [Head Object](../API/RESTObjectHEAD.md "../API/RESTObjectHEAD.md")
###### Note

Do not send encryption request headers for `GET` requests and
 `HEAD` requests if your object uses SSE-S3, or you'll get an HTTP status code
 400 (Bad Request) error.

When using AWS SDKs, you can request Amazon S3 to use server-side encryption with Amazon S3
 managed encryption keys (SSE-S3). This section provides examples of using the AWS SDKs in
 multiple languages. For information about other SDKs, go to [Sample Code and Libraries](https://aws.amazon.com/code "https://aws.amazon.com/code"). 


Java
When you use the AWS SDK for Java to upload an object, you can use SSE-S3 to encrypt it.
 To request server-side encryption, use the `ObjectMetadata` property of the
 `PutObjectRequest` to set the `x-amz-server-side-encryption`
 request header. When you call the `putObject()` method of the
 `AmazonS3Client`, Amazon S3 encrypts and saves the data.


You can also request SSE-S3 encryption when uploading objects with the multipart
 upload API operation: 



* When using the high-level multipart upload API operation, you use the
 `TransferManager` methods to apply server-side encryption to objects
 as you upload them. You can use any of the upload methods that take
 `ObjectMetadata` as a parameter. For more information, see [Uploading an object using multipart upload](mpu-upload-object.md "mpu-upload-object.md").
* When using the low-level multipart upload API operation, you specify
 server-side encryption when you initiate the multipart upload. You add the
 `ObjectMetadata` property by calling the
 `InitiateMultipartUploadRequest.setObjectMetadata()` method. For more
 information, see [Using the AWS SDKs (low-level API)](mpu-upload-object.md#mpu-upload-low-level "mpu-upload-object.md#mpu-upload-low-level").

You can't directly change the encryption state of an object (encrypting an
 unencrypted object or decrypting an encrypted object). To change an object's
 encryption state, you make a copy of the object, specifying the desired encryption
 state for the copy, and then delete the original object. Amazon S3 encrypts the copied
 object only if you explicitly request server-side encryption. To request encryption of
 the copied object through the Java API, use the `ObjectMetadata` property
 to specify server-side encryption in the `CopyObjectRequest`.


###### Example

The following example shows how to set server-side encryption by using the
 AWS SDK for Java. It shows how to perform the following tasks:


* Upload a new object by using SSE-S3.
* Change an object's encryption state (in this example, encrypting a
 previously unencrypted object) by making a copy of the object.
* Check the encryption state of the object.
For more information about server-side encryption, see [Using the REST API](#SSEUsingRESTAPI "#SSEUsingRESTAPI"). For instructions on
 creating and testing a working sample, see [Getting
 Started](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/getting-started.html "https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/getting-started.html") in the AWS SDK for Java Developer Guide.


```

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.internal.SSEResultBase;
import com.amazonaws.services.s3.model.*;

import java.io.ByteArrayInputStream;

public class SpecifyServerSideEncryption {

    public static void main(String[] args) {
        Regions clientRegion = Regions.DEFAULT_REGION;
        String bucketName = "*** Bucket name ***";
        String keyNameToEncrypt = "*** Key name for an object to upload and encrypt ***";
        String keyNameToCopyAndEncrypt = "*** Key name for an unencrypted object to be encrypted by copying ***";
        String copiedObjectKeyName = "*** Key name for the encrypted copy of the unencrypted object ***";

        try {
            AmazonS3 s3Client = AmazonS3ClientBuilder.standard()
                    .withRegion(clientRegion)
                    .withCredentials(new ProfileCredentialsProvider())
                    .build();

            // Upload an object and encrypt it with SSE.
            uploadObjectWithSSEEncryption(s3Client, bucketName, keyNameToEncrypt);

            // Upload a new unencrypted object, then change its encryption state
            // to encrypted by making a copy.
            changeSSEEncryptionStatusByCopying(s3Client,
                    bucketName,
                    keyNameToCopyAndEncrypt,
                    copiedObjectKeyName);
        } catch (AmazonServiceException e) {
            // The call was transmitted successfully, but Amazon S3 couldn't process
            // it, so it returned an error response.
            e.printStackTrace();
        } catch (SdkClientException e) {
            // Amazon S3 couldn't be contacted for a response, or the client
            // couldn't parse the response from Amazon S3.
            e.printStackTrace();
        }
    }

    private static void uploadObjectWithSSEEncryption(AmazonS3 s3Client, String bucketName, String keyName) {
        String objectContent = "Test object encrypted with SSE";
        byte[] objectBytes = objectContent.getBytes();

        // Specify server-side encryption.
        ObjectMetadata objectMetadata = new ObjectMetadata();
        objectMetadata.setContentLength(objectBytes.length);
        objectMetadata.setSSEAlgorithm(ObjectMetadata.AES_256_SERVER_SIDE_ENCRYPTION);
        PutObjectRequest putRequest = new PutObjectRequest(bucketName,
                keyName,
                new ByteArrayInputStream(objectBytes),
                objectMetadata);

        // Upload the object and check its encryption status.
        PutObjectResult putResult = s3Client.putObject(putRequest);
        System.out.println("Object \"" + keyName + "\" uploaded with SSE.");
        printEncryptionStatus(putResult);
    }

    private static void changeSSEEncryptionStatusByCopying(AmazonS3 s3Client,
            String bucketName,
            String sourceKey,
            String destKey) {
        // Upload a new, unencrypted object.
        PutObjectResult putResult = s3Client.putObject(bucketName, sourceKey, "Object example to encrypt by copying");
        System.out.println("Unencrypted object \"" + sourceKey + "\" uploaded.");
        printEncryptionStatus(putResult);

        // Make a copy of the object and use server-side encryption when storing the
        // copy.
        CopyObjectRequest request = new CopyObjectRequest(bucketName,
                sourceKey,
                bucketName,
                destKey);
        ObjectMetadata objectMetadata = new ObjectMetadata();
        objectMetadata.setSSEAlgorithm(ObjectMetadata.AES_256_SERVER_SIDE_ENCRYPTION);
        request.setNewObjectMetadata(objectMetadata);

        // Perform the copy operation and display the copy's encryption status.
        CopyObjectResult response = s3Client.copyObject(request);
        System.out.println("Object \"" + destKey + "\" uploaded with SSE.");
        printEncryptionStatus(response);

        // Delete the original, unencrypted object, leaving only the encrypted copy in
        // Amazon S3.
        s3Client.deleteObject(bucketName, sourceKey);
        System.out.println("Unencrypted object \"" + sourceKey + "\" deleted.");
    }

    private static void printEncryptionStatus(SSEResultBase response) {
        String encryptionStatus = response.getSSEAlgorithm();
        if (encryptionStatus == null) {
            encryptionStatus = "Not encrypted with SSE";
        }
        System.out.println("Object encryption status is: " + encryptionStatus);
    }
}


```


.NET
When you upload an object, you can direct Amazon S3 to encrypt it. To change the
 encryption state of an existing object, you make a copy of the object and delete the
 source object. By default, the copy operation encrypts the target only if you
 explicitly request server-side encryption of the target object. To specify SSE-S3 in
 the `CopyObjectRequest`, add the following:



```
 ServerSideEncryptionMethod = ServerSideEncryptionMethod.AES256
```

For a working sample of how to copy an object, see [Using the AWS SDKs](copy-object.md#CopyingObjectsUsingSDKs "copy-object.md#CopyingObjectsUsingSDKs"). 


The following example uploads an object. In the request, the example directs Amazon S3
 to encrypt the object. The example then retrieves object metadata and verifies the
 encryption method that was used. For
 information about setting up and running the code examples, see [Getting Started
 with the AWS SDK for .NET](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/net-dg-setup.html "https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/net-dg-setup.html") in the *AWS SDK for .NET Developer
 Guide*. 



```
using Amazon;
using Amazon.S3;
using Amazon.S3.Model;
using System;
using System.Threading.Tasks;

namespace Amazon.DocSamples.S3
{
    class SpecifyServerSideEncryptionTest
    {
        private const string bucketName = "*** bucket name ***";
        private const string keyName = "*** key name for object created ***";
        // Specify your bucket region (an example region is shown).
        private static readonly RegionEndpoint bucketRegion = RegionEndpoint.USWest2;
        private static IAmazonS3 client;

        public static void Main()
        {
            client = new AmazonS3Client(bucketRegion);
            WritingAnObjectAsync().Wait();
        }

        static async Task WritingAnObjectAsync()
        {
            try
            {
                var putRequest = new PutObjectRequest
                {
                    BucketName = bucketName,
                    Key = keyName,
                    ContentBody = "sample text",
                    ServerSideEncryptionMethod = ServerSideEncryptionMethod.AES256
                };

                var putResponse = await client.PutObjectAsync(putRequest);

                // Determine the encryption state of an object.
                GetObjectMetadataRequest metadataRequest = new GetObjectMetadataRequest
                {
                    BucketName = bucketName,
                    Key = keyName
                };
                GetObjectMetadataResponse response = await client.GetObjectMetadataAsync(metadataRequest);
                ServerSideEncryptionMethod objectEncryption = response.ServerSideEncryptionMethod;

                Console.WriteLine("Encryption method used: {0}", objectEncryption.ToString());
            }
            catch (AmazonS3Exception e)
            {
                Console.WriteLine("Error encountered ***. Message:'{0}' when writing an object", e.Message);
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
This topic shows how to use classes from version 3 of the AWS SDK for PHP to add SSE-S3
 to objects that you upload to Amazon S3. For more information about the AWS SDK for Ruby API, go to [AWS SDK for Ruby - Version
 2](https://docs.aws.amazon.com/sdkforruby/api/index.html "https://docs.aws.amazon.com/sdkforruby/api/index.html").


To upload an object to Amazon S3, use the [Aws\S3\S3Client::putObject()](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#putobject "https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#putobject") method. To add the
 `x-amz-server-side-encryption` request header to your upload request,
 specify the `ServerSideEncryption` parameter with the value
 `AES256`, as shown in the following code example. For information about
 server-side encryption requests, see [Using the REST API](#SSEUsingRESTAPI "#SSEUsingRESTAPI").



```
 require 'vendor/autoload.php';

use Aws\S3\S3Client;

$bucket = '*** Your Bucket Name ***';
$keyname = '*** Your Object Key ***';

// $filepath should be an absolute path to a file on disk.
$filepath = '*** Your File Path ***';

$s3 = new S3Client([
    'version' => 'latest',
    'region'  => 'us-east-1'
]);

// Upload a file with server-side encryption.
$result = $s3->putObject([
    'Bucket'               => $bucket,
    'Key'                  => $keyname,
    'SourceFile'           => $filepath,
    'ServerSideEncryption' => 'AES256',
]);


```

In response, Amazon S3 returns the `x-amz-server-side-encryption` header
 with the value of the encryption algorithm that was used to encrypt your object's
 data. 


When you upload large objects by using the multipart upload API operation, you can
 specify SSE-S3 for the objects that you are uploading, as follows: 



* When you're using the low-level multipart upload API operation, specify
 server-side encryption when you call the  [Aws\S3\S3Client::createMultipartUpload()](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#createmultipartupload "https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#createmultipartupload") method. To add the
 `x-amz-server-side-encryption` request header to your request,
 specify the `array` parameter's `ServerSideEncryption` key
 with the value `AES256`. For more information about the low-level
 multipart upload API operation, see [Using the AWS SDKs (low-level API)](mpu-upload-object.md#mpu-upload-low-level "mpu-upload-object.md#mpu-upload-low-level").
* When you're using the high-level multipart upload API operation, specify
 server-side encryption by using the `ServerSideEncryption` parameter of
 the [CreateMultipartUpload](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#createmultipartupload "https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#createmultipartupload") API operation. For an example of using the
 `setOption()` method with the high-level multipart upload API
 operation, see [Uploading an object using multipart upload](mpu-upload-object.md "mpu-upload-object.md").

To determine the encryption state of an existing object, retrieve the object
 metadata by calling the [Aws\S3\S3Client::headObject()](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#headobject "https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#headobject") method as shown in the following PHP code
 example.



```
 require 'vendor/autoload.php';

use Aws\S3\S3Client;

$bucket = '*** Your Bucket Name ***';
$keyname = '*** Your Object Key ***';

$s3 = new S3Client([
    'version' => 'latest',
    'region'  => 'us-east-1'
]);

// Check which server-side encryption algorithm is used.
$result = $s3->headObject([
    'Bucket' => $bucket,
    'Key'    => $keyname,
]);
echo $result['ServerSideEncryption'];


```

To change the encryption state of an existing object, make a copy of the object by
 using the [Aws\S3\S3Client::copyObject()](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#copyobject "https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#copyobject") method and delete the source object. By
 default, `copyObject()` does not encrypt the target unless you explicitly
 request server-side encryption of the destination object by using the
 `ServerSideEncryption` parameter with the value `AES256`. The
 following PHP code example makes a copy of an object and adds server-side encryption
 to the copied object.



```
 require 'vendor/autoload.php';

use Aws\S3\S3Client;

$sourceBucket = '*** Your Source Bucket Name ***';
$sourceKeyname = '*** Your Source Object Key ***';

$targetBucket = '*** Your Target Bucket Name ***';
$targetKeyname = '*** Your Target Object Key ***';

$s3 = new S3Client([
    'version' => 'latest',
    'region'  => 'us-east-1'
]);

// Copy an object and add server-side encryption.
$s3->copyObject([
    'Bucket'               => $targetBucket,
    'Key'                  => $targetKeyname,
    'CopySource'           => "$sourceBucket/$sourceKeyname",
    'ServerSideEncryption' => 'AES256',
]);


```

For more information, see the following topics:



* [AWS SDK for PHP for Amazon S3 Aws\S3\S3Client Class](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html "https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html")
* [AWS SDK for PHP
 Documentation](http://aws.amazon.com/documentation/sdk-for-php/ "http://aws.amazon.com/documentation/sdk-for-php/")


Ruby
When using the AWS SDK for Ruby to upload an object, you can specify that the object be
 stored encrypted at rest with SSE-S3. When you read the object back, it is
 automatically decrypted.


The following AWS SDK for Ruby Version 3 example demonstrates how to specify that a file
 uploaded to Amazon S3 be encrypted at rest.



```
require 'aws-sdk-s3'

# Wraps Amazon S3 object actions.
class ObjectPutSseWrapper
  attr_reader :object

  # @param object [Aws::S3::Object] An existing Amazon S3 object.
  def initialize(object)
    @object = object
  end

  def put_object_encrypted(object_content, encryption)
    @object.put(body: object_content, server_side_encryption: encryption)
    true
  rescue Aws::Errors::ServiceError => e
    puts "Couldn't put your content to #{object.key}. Here's why: #{e.message}"
    false
  end
end

# Example usage:
def run_demo
  bucket_name = "amzn-s3-demo-bucket"
  object_key = "my-encrypted-content"
  object_content = "This is my super-secret content."
  encryption = "AES256"

  wrapper = ObjectPutSseWrapper.new(Aws::S3::Object.new(bucket_name, object_content))
  return unless wrapper.put_object_encrypted(object_content, encryption)

  puts "Put your content into #{bucket_name}:#{object_key} and encrypted it with #{encryption}."
end

run_demo if $PROGRAM_NAME == __FILE__

```

The following code example demonstrates how to determine the encryption state of
 an existing object.



```
require 'aws-sdk-s3'

# Wraps Amazon S3 object actions.
class ObjectGetEncryptionWrapper
  attr_reader :object

  # @param object [Aws::S3::Object] An existing Amazon S3 object.
  def initialize(object)
    @object = object
  end

  # Gets the object into memory.
  #
  # @return [Aws::S3::Types::GetObjectOutput, nil] The retrieved object data if successful; otherwise nil.
  def object
    @object.get
  rescue Aws::Errors::ServiceError => e
    puts "Couldn't get object #{@object.key}. Here's why: #{e.message}"
  end
end

# Example usage:
def run_demo
  bucket_name = "amzn-s3-demo-bucket"
  object_key = "my-object.txt"

  wrapper = ObjectGetEncryptionWrapper.new(Aws::S3::Object.new(bucket_name, object_key))
  obj_data = wrapper.get_object
  return unless obj_data

  encryption = obj_data.server_side_encryption.nil? ? 'no' : obj_data.server_side_encryption
  puts "Object #{object_key} uses #{encryption} encryption."
end

run_demo if $PROGRAM_NAME == __FILE__

```

If server-side encryption is not used for the object that is stored in Amazon S3, the
 method returns `null`.


To change the encryption state of an existing object, make a copy of the object
 and delete the source object. By default, the copy methods do not encrypt the target
 unless you explicitly request server-side encryption. You can request the encryption
 of the target object by specifying the `server_side_encryption` value in
 the option's hash argument, as shown in the following Ruby code example. The code
 example demonstrates how to copy an object and encrypt the copy with SSE-S3. 



```
require 'aws-sdk-s3'

# Wraps Amazon S3 object actions.
class ObjectCopyEncryptWrapper
  attr_reader :source_object

  # @param source_object [Aws::S3::Object] An existing Amazon S3 object. This is used as the source object for
  #                                        copy actions.
  def initialize(source_object)
    @source_object = source_object
  end

  # Copy the source object to the specified target bucket, rename it with the target key, and encrypt it.
  #
  # @param target_bucket [Aws::S3::Bucket] An existing Amazon S3 bucket where the object is copied.
  # @param target_object_key [String] The key to give the copy of the object.
  # @return [Aws::S3::Object, nil] The copied object when successful; otherwise, nil.
  def copy_object(target_bucket, target_object_key, encryption)
    @source_object.copy_to(bucket: target_bucket.name, key: target_object_key, server_side_encryption: encryption)
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
  target_encryption = "AES256"

  source_bucket = Aws::S3::Bucket.new(source_bucket_name)
  wrapper = ObjectCopyEncryptWrapper.new(source_bucket.object(source_key))
  target_bucket = Aws::S3::Bucket.new(target_bucket_name)
  target_object = wrapper.copy_object(target_bucket, target_key, target_encryption)
  return unless target_object

  puts "Copied #{source_key} from #{source_bucket_name} to #{target_object.bucket_name}:#{target_object.key} and "\
       "encrypted the target with #{target_object.server_side_encryption} encryption."
end

run_demo if $PROGRAM_NAME == __FILE__

```


To specify SSE-S3 when you upload an object by using the AWS CLI, use the following
 example.


```
aws s3api put-object --bucket ``amzn-s3-demo-bucket1`` --key `object-key-name` --server-side-encryption AES256  --body `file path`
```
For more information, see [put-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html") in the *AWS CLI reference*. To specify SSE-S3 when
 you copy an object by using the AWS CLI, see [copy-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/copy-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/copy-object.html").

For examples of setting up encryption using AWS CloudFormation, see [Create a bucket with default encryption](../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionrule.md#aws-properties-s3-bucket-serversideencryptionrule--examples--Create_a_bucket_with_default_encryption "../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionrule.md#aws-properties-s3-bucket-serversideencryptionrule--examples--Create_a_bucket_with_default_encryption") and the [Create a bucket by using AWS KMS server-side encryption with an S3 Bucket Key](../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionrule.md#aws-properties-s3-bucket-serversideencryptionrule--examples--Create_a_bucket_using_AWS_KMS_server-side_encryption_with_an_S3_Bucket_Key "../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionrule.md#aws-properties-s3-bucket-serversideencryptionrule--examples--Create_a_bucket_using_AWS_KMS_server-side_encryption_with_an_S3_Bucket_Key")
 example in the `AWS::S3::Bucket ServerSideEncryptionRule` topic in the
 *AWS CloudFormation User Guide*.
