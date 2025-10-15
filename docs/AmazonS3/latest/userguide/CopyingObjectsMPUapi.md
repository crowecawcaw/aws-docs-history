# Copying an object using multipart upload

Multipart upload allows you to copy objects as a set of parts. The examples in this
 section show you how to copy objects greater than 5 GB using the multipart upload API. For
 information about multipart uploads, see [Uploading and copying objects using multipart upload in Amazon S3](mpuoverview.md "mpuoverview.md").

You can copy objects less than 5 GB in a single operation without using the multipart
 upload API. You can copy objects less than 5 GB using the AWS Management Console, AWS CLI, REST API, or
 AWS SDKs. For more information, see [Copying, moving, and renaming objects](copy-object.md "copy-object.md"). 

For an end-to-end procedure on uploading an object with multipart upload with an additional checksum, see 
 [Tutorial: Upload an object through multipart upload and
 verify its data integrity](tutorial-s3-mpu-additional-checksums.md "tutorial-s3-mpu-additional-checksums.md").

The following section show how to copy an object with multipart upload with the REST API or AWS SDKs.

The following sections in the *Amazon Simple Storage Service API Reference* describe the
 REST API for multipart upload. For copying an existing object, use the Upload Part
 (Copy) API and specify the source object by adding the
 `x-amz-copy-source` request header in your request. 


* [Initiate Multipart
 Upload](../API/mpUploadInitiate.md "../API/mpUploadInitiate.md")
* [Upload
 Part](../API/mpUploadUploadPart.md "../API/mpUploadUploadPart.md")
* [Upload Part
 (Copy)](../API/mpUploadUploadPartCopy.md "../API/mpUploadUploadPartCopy.md")
* [Complete Multipart
 Upload](../API/mpUploadComplete.md "../API/mpUploadComplete.md")
* [Abort Multipart
 Upload](../API/mpUploadAbort.md "../API/mpUploadAbort.md")
* [List Parts](../API/mpUploadListParts.md "../API/mpUploadListParts.md")
* [List Multipart
 Uploads](../API/mpUploadListMPUpload.md "../API/mpUploadListMPUpload.md")
You can use these APIs to make your own REST requests, or you can use one of the
 SDKs we provide. For more information about using Multipart Upload with the AWS CLI,
 see [Using the AWS CLI](mpu-upload-object.md#UsingCLImpUpload "mpu-upload-object.md#UsingCLImpUpload"). For more
 information about the SDKs, see [AWS SDK support for multipart upload](mpuoverview.md#sdksupportformpu "mpuoverview.md#sdksupportformpu").

To copy an object using the low-level API, do the following:


* Initiate a multipart upload by calling the
 `AmazonS3Client.initiateMultipartUpload()` method.
* Save the upload ID from the response object that the
 `AmazonS3Client.initiateMultipartUpload()` method returns.
 You provide this upload ID for each part-upload operation.
* Copy all of the parts. For each part that you need to copy, create a new
 instance of the `CopyPartRequest` class. Provide the part
 information, including the source and destination bucket names, source and
 destination object keys, upload ID, locations of the first and last bytes of
 the part, and part number.
* Save the responses of the `AmazonS3Client.copyPart()` method
 calls. Each response includes the `ETag` value and part number
 for the uploaded part. You need this information to complete the multipart
 upload.
* Call the `AmazonS3Client.completeMultipartUpload()` method to
 complete the copy operation.

Java
For examples of how to copy objects using multipart upload with the AWS SDK for Java, see [Copy part of an object from another object](../API/s3_example_s3_UploadPartCopy_section.md "../API/s3_example_s3_UploadPartCopy_section.md") in the *Amazon S3 API Reference*.



.NET
The following C# example shows how to use the SDK for .NET to copy an Amazon S3
 object that is larger than 5 GB from one source location to another,
 such as from one bucket to another. To copy objects that are smaller
 than 5 GB, use the single-operation copy procedure described in [Using the AWS SDKs](copy-object.md#CopyingObjectsUsingSDKs "copy-object.md#CopyingObjectsUsingSDKs"). For more information
 about Amazon S3 multipart uploads, see [Uploading and copying objects using multipart upload in Amazon S3](mpuoverview.md "mpuoverview.md").


This example shows how to copy an Amazon S3 object that is larger than 5 GB
 from one S3 bucket to another using the SDK for .NET multipart upload
 API.



```
using Amazon;
using Amazon.S3;
using Amazon.S3.Model;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Amazon.DocSamples.S3
{
    class CopyObjectUsingMPUapiTest
    {
        private const string sourceBucket = "*** provide the name of the bucket with source object ***";
        private const string targetBucket = "*** provide the name of the bucket to copy the object to ***";
        private const string sourceObjectKey = "*** provide the name of object to copy ***";
        private const string targetObjectKey = "*** provide the name of the object copy ***";
        // Specify your bucket region (an example region is shown).
        private static readonly RegionEndpoint bucketRegion = RegionEndpoint.USWest2; 
        private static IAmazonS3 s3Client;

        public static void Main()
        {
            s3Client = new AmazonS3Client(bucketRegion);
            Console.WriteLine("Copying an object");
            MPUCopyObjectAsync().Wait();
        }
        private static async Task MPUCopyObjectAsync()
        {
            // Create a list to store the upload part responses.
            List<UploadPartResponse> uploadResponses = new List<UploadPartResponse>();
            List<CopyPartResponse> copyResponses = new List<CopyPartResponse>();

            // Setup information required to initiate the multipart upload.
            InitiateMultipartUploadRequest initiateRequest =
                new InitiateMultipartUploadRequest
                {
                    BucketName = targetBucket,
                    Key = targetObjectKey
                };

            // Initiate the upload.
            InitiateMultipartUploadResponse initResponse =
                await s3Client.InitiateMultipartUploadAsync(initiateRequest);

            // Save the upload ID.
            String uploadId = initResponse.UploadId;

            try
            {
                // Get the size of the object.
                GetObjectMetadataRequest metadataRequest = new GetObjectMetadataRequest
                {
                    BucketName = sourceBucket,
                    Key = sourceObjectKey
                };

                GetObjectMetadataResponse metadataResponse =
                    await s3Client.GetObjectMetadataAsync(metadataRequest);
                long objectSize = metadataResponse.ContentLength; // Length in bytes.

                // Copy the parts.
                long partSize = 5 * (long)Math.Pow(2, 20); // Part size is 5 MB.

                long bytePosition = 0;
                for (int i = 1; bytePosition < objectSize; i++)
                {
                    CopyPartRequest copyRequest = new CopyPartRequest
                    {
                        DestinationBucket = targetBucket,
                        DestinationKey = targetObjectKey,
                        SourceBucket = sourceBucket,
                        SourceKey = sourceObjectKey,
                        UploadId = uploadId,
                        FirstByte = bytePosition,
                        LastByte = bytePosition + partSize - 1 >= objectSize ? objectSize - 1 : bytePosition + partSize - 1,
                        PartNumber = i
                    };

                    copyResponses.Add(await s3Client.CopyPartAsync(copyRequest));

                    bytePosition += partSize;
                }

                // Set up to complete the copy.
                CompleteMultipartUploadRequest completeRequest =
                new CompleteMultipartUploadRequest
                {
                    BucketName = targetBucket,
                    Key = targetObjectKey,
                    UploadId = initResponse.UploadId
                };
                completeRequest.AddPartETags(copyResponses);

                // Complete the copy.
                CompleteMultipartUploadResponse completeUploadResponse = 
                    await s3Client.CompleteMultipartUploadAsync(completeRequest);
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
