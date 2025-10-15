# Using multipart uploads with
 directory buckets

You can use the multipart upload process to upload a single object as a set of parts. Each
 part is a contiguous portion of the object's data. You can upload these object parts
 independently and in any order. If transmission of any part fails, you can retransmit that
 part without affecting other parts. After all parts of your object are uploaded, Amazon S3
 assembles these parts and creates the object. In general, when your object size reaches 100
 MB, you should consider using multipart uploads instead of uploading the object in a single
 operation.

Using multipart upload provides the following advantages:


* **Improved throughput** – You can upload parts
 in parallel to improve throughput.
* **Quick recovery from any network issues** –
 Smaller part sizes minimize the impact of restarting a failed upload because of a
 network error.
* **Pause and resume object uploads** – You can
 upload object parts over time. After you initiate a multipart upload, there is no
 expiration date. You must explicitly complete or abort the multipart upload.
* **Begin an upload before you know the final object
 size** – You can upload an object as you are creating it.
We recommend that you use multipart uploads in the following ways:


* If you're uploading large objects over a stable high-bandwidth network, use
 multipart uploads to maximize the use of your available bandwidth by uploading
 object parts in parallel for multi-threaded performance.
* If you're uploading over a spotty network, use multipart uploads to increase
 resiliency to network errors by avoiding upload restarts. When using multipart
 uploads, you need to retry uploading only the parts that are interrupted during the
 upload. You don't need to restart uploading your object from the beginning.
When you're using multipart uploads to upload objects to the Amazon S3 Express One Zone storage class in
 directory buckets, the multipart upload process is similar to the process of using multipart
 upload to upload objects to general purpose buckets. However, there are some notable
 differences. 

For more information about using multipart uploads to upload objects to S3 Express One Zone, see
 the following topics.

###### Topics

* [The multipart upload process](#s3-express-mpu-process "#s3-express-mpu-process")
* [Checksums with multipart upload
 operations](#s3-express-mpuchecksums "#s3-express-mpuchecksums")
* [Concurrent multipart upload
 operations](#s3-express-distributedmpupload "#s3-express-distributedmpupload")
* [Multipart uploads and pricing](#s3-express-mpuploadpricing "#s3-express-mpuploadpricing")
* [Multipart upload API operations and
 permissions](#s3-express-mpuAndPermissions "#s3-express-mpuAndPermissions")
* [Examples](#directory-buckets-multipart-upload-examples "#directory-buckets-multipart-upload-examples")

## The multipart upload process


A multipart upload is a three-step process: 



* You initiate the upload.
* You upload the object parts.
* After you have uploaded all of the parts, you complete the multipart
 upload.


Upon receiving the complete multipart upload request, Amazon S3 constructs the object from
 the uploaded parts, and you can then access the object as you would any other object in
 your bucket. 


###### Multipart upload initiation


When you send a request to initiate a multipart upload, Amazon S3 returns a response
 with an upload ID, which is a unique identifier for your multipart upload. You must
 include this upload ID whenever you upload parts, list the parts, complete an
 upload, or abort an upload. 


###### Parts upload


When uploading a part, in addition to the upload ID, you must specify a part
 number. When you're using a multipart upload with S3 Express One Zone, the multipart part
 numbers must be consecutive part numbers. If you try to complete a multipart upload
 request with nonconsecutive part numbers, an `HTTP 400 Bad Request`
 (Invalid Part Order) error is generated. 


A part number uniquely identifies a part and its position in the object that you are
 uploading. If you upload a new part by using the same part number as a previously
 uploaded part, the previously uploaded part is overwritten. 


Whenever you upload a part, Amazon S3 returns an entity tag (ETag) header in its response.
 For each part upload, you must record the part number and the ETag value. The ETag
 values for all object part uploads will remain the same, but each part will be assigned
 a different part number. You must include these values in the subsequent request to
 complete the multipart upload.


Amazon S3 automatically encrypts all new objects that are uploaded to an S3 bucket. When
 doing a multipart upload, if you don't specify encryption information in your request,
 the encryption setting of the uploaded parts is set to the default encryption
 configuration of the destination bucket. The default encryption configuration of an Amazon S3
 bucket is always enabled and is at a minimum set to server-side encryption with Amazon S3
 managed keys (SSE-S3). For directory buckets, SSE-S3 and server-side encryption with AWS KMS keys
 (SSE-KMS) are supported. For more
 information, see [Data protection and encryption](s3-express-data-protection.md "s3-express-data-protection.md").


###### Multipart upload completion


When you complete a multipart upload, Amazon S3 creates the object by concatenating the
 parts in ascending order based on the part number. After a successful
 *complete* request, the parts no longer exist. 


Your *complete multipart upload* request must include the upload ID
 and a list of both part numbers and their corresponding ETag values. The Amazon S3 response
 includes an ETag that uniquely identifies the combined object data. This ETag is not an
 MD5 hash of the object data. 


###### Multipart upload listings


You can list the parts of a specific multipart upload or all in-progress multipart
 uploads. The list parts operation returns the parts information that you have
 uploaded for a specific multipart upload. For each list parts request, Amazon S3 returns
 the parts information for the specified multipart upload, up to a maximum of 1,000
 parts. If there are more than 1,000 parts in the multipart upload, you must use
 pagination to retrieve all the parts. 


The returned list of parts doesn't include parts that haven't finished uploading.
 Using the *list multipart uploads* operation, you can obtain a list
 of multipart uploads that are in progress.


An in-progress multipart upload is an upload that you have initiated, but have not yet
 completed or aborted. Each request returns at most 1,000 multipart uploads. If there are
 more than 1,000 multipart uploads in progress, you must send additional requests to
 retrieve the remaining multipart uploads. Use the returned listing only for
 verification. Do not use the result of this listing when sending a *complete
 multipart upload* request. Instead, maintain your own list of the part
 numbers that you specified when uploading parts and the corresponding ETag values that
 Amazon S3 returns.


For more information about multipart upload listings, see [ListParts](../API/API_ListParts.md "../API/API_ListParts.md") in the
 *Amazon Simple Storage Service API Reference*. 


## Checksums with multipart upload
 operations


When you upload an object to, you can specify a checksum algorithm to check object
 integrity. MD5 is not supported for directory buckets. You can specify one of the
 following Secure Hash Algorithms (SHA) or Cyclic Redundancy Check (CRC) data-integrity
 check algorithms:



* CRC32
* CRC32C
* SHA-1
* SHA-256

You can use the Amazon S3 REST API or the AWS SDKs to retrieve the checksum value for
 individual parts by using `GetObject` or `HeadObject`. If you want
 to retrieve the checksum values for individual parts of multipart uploads still in
 process, you can use `ListParts`.


###### Important

When using the preceding checksum algorithms, the multipart part numbers must use
 consecutive part numbers. If you try to complete a multipart upload request with
 nonconsecutive part numbers, Amazon S3 generates an `HTTP 400 Bad Request`
 (Invalid Part Order) error.


 For more information about how checksums work with multipart upload objects, see [Checking object integrity in Amazon S3](checking-object-integrity.md "checking-object-integrity.md").


## Concurrent multipart upload
 operations


In a distributed development environment, your application can initiate several
 updates on the same object at the same time. For example, your application might
 initiate several multipart uploads by using the same object key. For each of these
 uploads, your application can then upload parts and send a complete upload request to
 Amazon S3 to create the object. For S3 Express One Zone, the object creation time is the completion
 date of the multipart upload.


###### Important

Versioning isn’t supported for objects that are stored in
 directory buckets.


## Multipart uploads and pricing


After you initiate a multipart upload, Amazon S3 retains all the parts until you either
 complete or abort the upload. Throughout its lifetime, you are billed for all storage,
 bandwidth, and requests for this multipart upload and its associated parts. If you abort
 the multipart upload, Amazon S3 deletes the upload artifacts and any parts that you have
 uploaded, and you are no longer billed for them. There are no early delete charges for
 deleting incomplete multipart uploads, regardless of the storage class specified. For
 more information about pricing, see [Amazon S3
 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").


###### Important

If the complete multipart upload request isn't sent successfully, the object parts
 aren't assembled and an object isn't created. You are billed for all storage associated
 with uploaded parts. It's important that you either complete the multipart upload to
 have the object created or abort the multipart upload to remove any uploaded parts. 

Before you can delete a directory bucket, you must complete or abort all
 in-progress multipart uploads. Directory buckets don't support S3 Lifecycle
 configurations. If needed, you can list your active multipart uploads, then abort
 the uploads, and then delete your bucket. 


## Multipart upload API operations and
 permissions


To allow access to object management API operations on a directory bucket, you grant
 the `s3express:CreateSession` permission in a bucket policy or an AWS Identity and Access Management
 (IAM) identity-based policy.


You must have the necessary permissions to use the multipart upload operations. You
 can use bucket policies or IAM identity-based policies to grant IAM principals
 permissions to perform these operations. The following table lists the required
 permissions for various multipart upload operations. 


You can identify the initiator of a multipart upload through the
 `Initiator` element. If the initiator is an AWS account, this element
 provides the same information as the `Owner` element. If the initiator is an
 IAM user, this element provides the user ARN
 and
 display name.




| Action | Required permissions |
| --- | --- |
| Create a multipart upload | To create the multipart upload, you must be allowed to perform the
 `s3express:CreateSession` action on the directory
 bucket.  |
| Initiate a multipart upload | To initiate the multipart upload, you must be allowed to perform
 the `s3express:CreateSession` action on the directory
 bucket.  |
| Upload a part | To upload a part, you must be allowed to perform the
 `s3express:CreateSession` action on the directory
 bucket. 
For the initiator to upload a part, the bucket owner must allow
 the initiator to perform the `s3express:CreateSession`
 action on the directory bucket. |
| Upload a part (copy) | To upload a part, you must be allowed to perform the
 `s3express:CreateSession` action on the directory
 bucket. 
For the initiator to upload a part for an object, the owner of the
 bucket must allow the initiator to perform the
 `s3express:CreateSession` action on the
 object. |
| Complete a multipart upload | To complete a multipart upload, you must be allowed to perform the
 `s3express:CreateSession` action on the directory
 bucket. 
For the initiator to complete a multipart upload, the bucket owner
 must allow the initiator to perform the
 `s3express:CreateSession` action on the
 object. |
| Abort a multipart upload | To abort a multipart upload, you must be allowed to perform the
 `s3express:CreateSession` action. 
For the initiator to abort a multipart upload, the initiator must
 be granted explicit allow access to perform the
 `s3express:CreateSession` action.  |
| List parts | To list the parts in a multipart upload, you must be allowed to
 perform the `s3express:CreateSession` action on the
 directory bucket. |
| List in-progress multipart uploads | To list the in-progress multipart uploads to a bucket, you must be
 allowed to perform the `s3:ListBucketMultipartUploads`
 action on that bucket. |


### API operation support for multipart
 uploads


The following sections in the Amazon Simple Storage Service API Reference describe the Amazon S3 REST API operations
 for multipart uploads. 



* [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md")
* [UploadPart](../API/API_UploadPart.md "../API/API_UploadPart.md")
* [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")
* [CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md")
* [AbortMultipartUpload](../API/API_AbortMultipartUpload.md "../API/API_AbortMultipartUpload.md")
* [ListParts](../API/API_ListParts.md "../API/API_ListParts.md")
* [ListMultipartUploads](../API/API_ListMultipartUploads.md "../API/API_ListMultipartUploads.md")

## Examples


To use a multipart upload to upload an object to S3 Express One Zone in a directory bucket,
 see the following examples.


###### Topics

* [Creating a
 multipart upload](#directory-buckets-multipart-upload-examples-create "#directory-buckets-multipart-upload-examples-create")
* [Uploading
 the parts of a multipart upload](#directory-buckets-multipart-upload-examples-upload-part "#directory-buckets-multipart-upload-examples-upload-part")
* [Completing a
 multipart upload](#directory-buckets-multipart-upload-examples-complete "#directory-buckets-multipart-upload-examples-complete")
* [Aborting a
 multipart upload](#directory-buckets-multipart-upload-examples-abort "#directory-buckets-multipart-upload-examples-abort")
* [Creating a multipart upload copy operation](#directory-buckets-multipart-upload-examples-upload-part-copy "#directory-buckets-multipart-upload-examples-upload-part-copy")
* [Listing
 in-progress multipart uploads](#directory-buckets-multipart-upload-examples-list "#directory-buckets-multipart-upload-examples-list")
* [Listing the
 parts of a multipart upload](#directory-buckets-multipart-upload-examples-list-parts "#directory-buckets-multipart-upload-examples-list-parts")

### Creating a
 multipart upload


###### Note

For directory buckets, when you perform a `CreateMultipartUpload` operation and an `UploadPartCopy` operation, 
 the bucket's default encryption must use the desired encryption configuration, and 
 the request headers you provide in the `CreateMultipartUpload` request must match the default encryption configuration of the destination bucket. 


The following examples show how to create a multipart upload.
 
 



SDK for Java 2.x

```
/**
 * This method creates a multipart upload request that generates a unique upload ID that is used to track
 * all the upload parts
 *
 * @param s3
 * @param bucketName - for example, '`doc-example-bucket`--`use1-az4`--x-s3'
 * @param key
 * @return
 */
 private static String createMultipartUpload(S3Client s3, String bucketName, String key) {
 
     CreateMultipartUploadRequest createMultipartUploadRequest = CreateMultipartUploadRequest.builder() 
             .bucket(bucketName)
             .key(key)
             .build();
             
     String uploadId = null;
     
     try {
         CreateMultipartUploadResponse response = s3.createMultipartUpload(createMultipartUploadRequest);
         uploadId = response.uploadId();
     }
     catch (S3Exception e) {
         System.err.println(e.awsErrorDetails().errorMessage());
         System.exit(1);
     }
     return uploadId;
```


SDK for Python

```
def create_multipart_upload(s3_client, bucket_name, key_name):
    '''
   Create a multipart upload to a directory bucket
   
   :param s3_client: boto3 S3 client
   :param bucket_name: The destination bucket for the multipart upload
   :param key_name: The key name for the object to be uploaded
   :return: The UploadId for the multipart upload if created successfully, else None
   '''
   
   try:
        mpu = s3_client.create_multipart_upload(Bucket = bucket_name, Key = key_name)
        return mpu['UploadId'] 
    except ClientError as e:
        logging.error(e)
        return None
```



This example shows how to create a multipart upload to a
 directory bucket by using the AWS CLI. This command starts a multipart upload to the directory bucket `bucket-base-name`--`zone-id`--x-s3 for the object `KEY_NAME`. To use the command replace the `user input placeholders` with your own information.


```
aws s3api create-multipart-upload --bucket `bucket-base-name`--`zone-id`--x-s3 --key `KEY_NAME`
```
For more information, see [create-multipart-upload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-multipart-upload.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-multipart-upload.html") in the AWS Command Line Interface.


### Uploading
 the parts of a multipart upload


The following examples show how to upload parts of a multipart upload. 



SDK for Java 2.x
The following example shows how to break a single object into
 parts and then upload those parts to a directory bucket by using
 the SDK for Java 2.x. 



```
/**
 * This method creates part requests and uploads individual parts to S3 and then returns all the completed parts
 *
 * @param s3
 * @param bucketName
 * @param key
 * @param uploadId
 * @throws IOException
 */
 private static List`CompletedPart`multipartUpload(S3Client s3, String bucketName, String key, String uploadId, String filePath) throws IOException {

        int partNumber = 1;
        List`CompletedPart` completedParts = new ArrayList<>();
        ByteBuffer bb = ByteBuffer.allocate(1024 * 1024 * 5); // 5 MB byte buffer

        // read the local file, breakdown into chunks and process
        try (RandomAccessFile file = new RandomAccessFile(filePath, "r")) {
            long fileSize = file.length();
            int position = 0;
            while (position < fileSize) {
                file.seek(position);
                int read = file.getChannel().read(bb);

                bb.flip(); // Swap position and limit before reading from the buffer.
                UploadPartRequest uploadPartRequest = UploadPartRequest.builder()
                        .bucket(bucketName)
                        .key(key)
                        .uploadId(uploadId)
                        .partNumber(partNumber)
                        .build();

                UploadPartResponse partResponse = s3.uploadPart(
                        uploadPartRequest,
                        RequestBody.fromByteBuffer(bb));

                CompletedPart part = CompletedPart.builder()
                        .partNumber(partNumber)
                        .eTag(partResponse.eTag())
                        .build();
                completedParts.add(part);

                bb.clear();
                position += read;
                partNumber++;
            }
        } 
        
        catch (IOException e) {
            throw e;
        }
        return completedParts;
    }
```


SDK for Python
The following example shows how to break a single object into
 parts and then upload those parts to a directory bucket by using
 the SDK for Python. 



```
def multipart_upload(s3_client, bucket_name, key_name, mpu_id, part_size):
    '''
    Break up a file into multiple parts and upload those parts to a directory bucket

    :param s3_client: boto3 S3 client
    :param bucket_name: Destination bucket for the multipart upload
    :param key_name: Key name for object to be uploaded and for the local file that's being uploaded
    :param mpu_id: The UploadId returned from the create_multipart_upload call
    :param part_size: The size parts that the object will be broken into, in bytes. 
                      Minimum 5 MiB, Maximum 5 GiB. There is no minimum size for the last part of your multipart upload.
    :return: part_list for the multipart upload if all parts are uploaded successfully, else None
    '''
    
    part_list = []
    try:
        with open(key_name, 'rb') as file:
            part_counter = 1
            while True:
                file_part = file.read(part_size)
                if not len(file_part):
                    break
                upload_part = s3_client.upload_part(
                    Bucket = bucket_name,
                    Key = key_name,
                    UploadId = mpu_id,
                    Body = file_part,
                    PartNumber = part_counter
                )
                part_list.append({'PartNumber': part_counter, 'ETag': upload_part['ETag']})
                part_counter += 1
    except ClientError as e:
        logging.error(e)
        return None
    return part_list
```



This example shows how to break a single object into parts and then upload
 those parts to a directory bucket by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.


```
aws s3api upload-part --bucket `bucket-base-name`--`zone-id`--x-s3 --key `KEY_NAME` --part-number `1` --body `LOCAL_FILE_NAME` --upload-id "`AS_mgt9RaQE9GEaifATue15dAAAAAAAAAAEMAAAAAAAAADQwNzI4MDU0MjUyMBYAAAAAAAAAAA0AAAAAAAAAAAH2AfYAAAAAAAAEBSD0WBKMAQAAAABneY9yBVsK89iFkvWdQhRCcXohE8RbYtc9QvBOG8tNpA`"
```
For more information, see [upload-part](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/upload-part.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/upload-part.html") in the AWS Command Line Interface.


### Completing a
 multipart upload


The following examples show how to complete a multipart upload. 



SDK for Java 2.x
The following examples show how to complete a multipart upload
 by using the SDK for Java 2.x.



```
/**
 * This method completes the multipart upload request by collating all the upload parts
 * @param s3
 * @param bucketName - for example, '`doc-example-bucket`--`usw2-az1`--x-s3'
 * @param key
 * @param uploadId
 * @param uploadParts
 */
 private static void completeMultipartUpload(S3Client s3, String bucketName, String key, String uploadId, List`CompletedPart` uploadParts) {
        CompletedMultipartUpload completedMultipartUpload = CompletedMultipartUpload.builder()
                .parts(uploadParts)
                .build();

        CompleteMultipartUploadRequest completeMultipartUploadRequest =
                CompleteMultipartUploadRequest.builder()
                        .bucket(bucketName)
                        .key(key)
                        .uploadId(uploadId)
                        .multipartUpload(completedMultipartUpload)
                        .build();

        s3.completeMultipartUpload(completeMultipartUploadRequest);
    }

    public static void multipartUploadTest(S3Client s3, String bucketName, String key, String localFilePath)  {
        System.out.println("Starting multipart upload for: " + key);
        try {
            String uploadId = createMultipartUpload(s3, bucketName, key);
            System.out.println(uploadId);
            List`CompletedPart` parts = multipartUpload(s3, bucketName, key, uploadId, localFilePath);
            completeMultipartUpload(s3, bucketName, key, uploadId, parts);
            System.out.println("Multipart upload completed for: " + key);
        } 
        
        catch (Exception e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }
```


SDK for Python
The following examples show how to complete a multipart upload
 by using the SDK for Python.



```
def complete_multipart_upload(s3_client, bucket_name, key_name, mpu_id, part_list):
    '''
    Completes a multipart upload to a directory bucket

    :param s3_client: boto3 S3 client
    :param bucket_name: The destination bucket for the multipart upload
    :param key_name: The key name for the object to be uploaded
    :param mpu_id: The UploadId returned from the create_multipart_upload call
    :param part_list: The list of uploaded part numbers with their associated ETags 
    :return: True if the multipart upload was completed successfully, else False
    '''
    
    try:
        s3_client.complete_multipart_upload(
            Bucket = bucket_name,
            Key = key_name,
            UploadId = mpu_id,
            MultipartUpload = {
                'Parts': part_list
            }
        )
    except ClientError as e:
        logging.error(e)
        return False
    return True
    
if __name__ == '__main__':
    MB = 1024 ** 2
    region = '`us-west-2`'
    bucket_name = '`BUCKET_NAME`'
    key_name = '`OBJECT_NAME`'
    part_size = 10 * MB
    s3_client = boto3.client('s3', region_name = region)
    mpu_id = create_multipart_upload(s3_client, bucket_name, key_name)
    if mpu_id is not None:
        part_list = multipart_upload(s3_client, bucket_name, key_name, mpu_id, part_size)
        if part_list is not None:
            if complete_multipart_upload(s3_client, bucket_name, key_name, mpu_id, part_list):
                print (f'{key_name} successfully uploaded through a ultipart upload to {bucket_name}')
            else:
                print (f'Could not upload {key_name} hrough a multipart upload to {bucket_name}')
```



This example shows how to complete a multipart upload for a
 directory bucket by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.


```
aws s3api complete-multipart-upload --bucket `bucket-base-name`--`zone-id`--x-s3 --key `KEY_NAME` --upload-id "`AS_mgt9RaQE9GEaifATue15dAAAAAAAAAAEMAAAAAAAAADQwNzI4MDU0MjUyMBYAAAAAAAAAAA0AAAAAAAAAAAH2AfYAAAAAAAAEBSD0WBKMAQAAAABneY9yBVsK89iFkvWdQhRCcXohE8RbYtc9QvBOG8tNpA`" --multipart-upload `file://parts.json`
```
This example takes a JSON structure that describes the parts of the
 multipart upload that should be reassembled into the complete file. In this
 example, the `file://` prefix is used to load the JSON structure
 from a file in the local folder named `parts`.

parts.json:


```
parts.json
{
  "Parts": [
    {
      "ETag": "6b78c4a64dd641a58dac8d9258b88147",
      "PartNumber": 1
    }
  ]
}
```
For more information, see [complete-multipart-upload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/complete-multipart-upload.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/complete-multipart-upload.html") in the AWS Command Line Interface.


### Aborting a
 multipart upload


The following examples show how to abort a multipart upload. 



SDK for Java 2.x
The following example shows how to abort a multipart upload by
 using the SDK for Java 2.x.



```
public static void abortMultiPartUploads( S3Client s3, String bucketName ) {

         try {
             ListMultipartUploadsRequest listMultipartUploadsRequest = ListMultipartUploadsRequest.builder()
                     .bucket(bucketName)
                     .build();

             ListMultipartUploadsResponse response = s3.listMultipartUploads(listMultipartUploadsRequest);
             List`MultipartUpload` uploads = response.uploads();

             AbortMultipartUploadRequest abortMultipartUploadRequest;
             for (MultipartUpload upload: uploads) {
                 abortMultipartUploadRequest = AbortMultipartUploadRequest.builder()
                         .bucket(bucketName)
                         .key(upload.key())
                         .uploadId(upload.uploadId())
                         .build();

                 s3.abortMultipartUpload(abortMultipartUploadRequest);
             }

         } 
         
         catch (S3Exception e) {
             System.err.println(e.getMessage());
             System.exit(1);
         }
     }
```


SDK for Python
The following example shows how to abort a multipart upload by
 using the SDK for Python.



```
import logging
import boto3
from botocore.exceptions import ClientError


def abort_multipart_upload(s3_client, bucket_name, key_name, upload_id):
    '''
    Aborts a partial multipart upload in a directory bucket.
    
    :param s3_client: boto3 S3 client
    :param bucket_name: Bucket where the multipart upload was initiated - for example, '`doc-example-bucket`--`usw2-az1`--x-s3'
    :param key_name: Name of the object for which the multipart upload needs to be aborted
    :param upload_id: Multipart upload ID for the multipart upload to be aborted
    :return: True if the multipart upload was successfully aborted, False if not
    '''
    try:
        s3_client.abort_multipart_upload(
            Bucket = bucket_name,
            Key = key_name,
            UploadId = upload_id
        )
    except ClientError as e:
        logging.error(e)
        return False
    return True


if __name__ == '__main__':
    region = '`us-west-2`'
    bucket_name = '`BUCKET_NAME`'
    key_name = '`KEY_NAME`'
        upload_id = '`UPLOAD_ID`'
    s3_client = boto3.client('s3', region_name = region)
    if abort_multipart_upload(s3_client, bucket_name, key_name, upload_id):
        print (f'Multipart upload for object {key_name} in {bucket_name} bucket has been aborted')
    else:
        print (f'Unable to abort multipart upload for object {key_name} in {bucket_name} bucket')
```



The following example shows how to abort a multipart upload by using the
 AWS CLI. To use the command replace the `user input placeholders` with your own information.


```
aws s3api abort-multipart-upload --bucket `bucket-base-name`--`zone-id`--x-s3 --key `KEY_NAME` --upload-id "`AS_mgt9RaQE9GEaifATue15dAAAAAAAAAAEMAAAAAAAAADQwNzI4MDU0MjUyMBYAAAAAAAAAAA0AAAAAAAAAAAH2AfYAAAAAAAAEAX5hFw-MAQAAAAB0OxUFeA7LTbWWFS8WYwhrxDxTIDN-pdEEq_agIHqsbg`"
```
For more information, see [abort-multipart-upload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/abort-multipart-upload.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/abort-multipart-upload.html") in the AWS Command Line Interface.


### Creating a multipart upload copy operation


###### Note


* To encrypt new object part copies in a directory bucket with SSE-KMS, you must specify SSE-KMS as the directory bucket's default encryption configuration with a KMS key (specifically, a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk")). 
 The [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk") (`aws/s3`) isn't supported. Your SSE-KMS configuration can only support 1 [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk") per directory bucket for the lifetime of the bucket. After you specify a customer managed key for SSE-KMS, you can't override the customer managed key for the bucket's SSE-KMS configuration. 
 You can't specify server-side encryption settings for new object part copies with SSE-KMS in the [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")  request headers. 
 Also, the request headers you provide in the `CreateMultipartUpload` request must match the default encryption configuration of the destination bucket.
* S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets 
to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md"). In this case, Amazon S3 makes a call to AWS KMS every time a copy request is made for a KMS-encrypted object.

The following examples show how to copy objects from one bucket to another using a multipart upload. 



SDK for Java 2.x
The following example shows how to use a multipart upload to
 programmatically copy an object from one bucket to another by
 using the SDK for Java 2.x.



```
/**
 * This method creates a multipart upload request that generates a unique upload ID that is used to track
 * all the upload parts.
 *
 * @param s3
 * @param bucketName
 * @param key
 * @return
 */
 private static String createMultipartUpload(S3Client s3, String bucketName, String key) {
        CreateMultipartUploadRequest createMultipartUploadRequest = CreateMultipartUploadRequest.builder()
                .bucket(bucketName)
                .key(key)
                .build();
        String uploadId = null;
        try {
            CreateMultipartUploadResponse response = s3.createMultipartUpload(createMultipartUploadRequest);
            uploadId = response.uploadId();
        } catch (S3Exception e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
        return uploadId;
  }

  /**
   * Creates copy parts based on source object size and copies over individual parts
   *
   * @param s3
   * @param sourceBucket
   * @param sourceKey
   * @param destnBucket
   * @param destnKey
   * @param uploadId
   * @return
   * @throws IOException
   */
    public static List`CompletedPart` multipartUploadCopy(S3Client s3, String sourceBucket, String sourceKey, String destnBucket, String destnKey, String uploadId) throws IOException {

        // Get the object size to track the end of the copy operation.
        HeadObjectRequest headObjectRequest = HeadObjectRequest
                .builder()
                .bucket(sourceBucket)
                .key(sourceKey)
                .build();
        HeadObjectResponse response = s3.headObject(headObjectRequest);
        Long objectSize = response.contentLength();

        System.out.println("Source Object size: " + objectSize);

        // Copy the object using 20 MB parts.
        long partSize = 20 * 1024 * 1024;
        long bytePosition = 0;
        int partNum = 1;
        List`CompletedPart` completedParts = new ArrayList<>();
        while (bytePosition < objectSize) {
            // The last part might be smaller than partSize, so check to make sure
            // that lastByte isn't beyond the end of the object.
            long lastByte = Math.min(bytePosition + partSize - 1, objectSize - 1);

            System.out.println("part no: " + partNum + ", bytePosition: " + bytePosition + ", lastByte: " + lastByte);

            // Copy this part.
            UploadPartCopyRequest req = UploadPartCopyRequest.builder()
                    .uploadId(uploadId)
                    .sourceBucket(sourceBucket)
                    .sourceKey(sourceKey)
                    .destinationBucket(destnBucket)
                    .destinationKey(destnKey)
                    .copySourceRange("bytes="+bytePosition+"-"+lastByte)
                    .partNumber(partNum)
                    .build();
            UploadPartCopyResponse res = s3.uploadPartCopy(req);
            CompletedPart part = CompletedPart.builder()
                    .partNumber(partNum)
                    .eTag(res.copyPartResult().eTag())
                    .build();
            completedParts.add(part);
            partNum++;
            bytePosition += partSize;
        }
        return completedParts;
    }


    public static void multipartCopyUploadTest(S3Client s3, String srcBucket, String srcKey, String destnBucket, String destnKey)  {
        System.out.println("Starting multipart copy for: " + srcKey);
        try {
            String uploadId = createMultipartUpload(s3, destnBucket, destnKey);
            System.out.println(uploadId);
            List`CompletedPart` parts = multipartUploadCopy(s3, srcBucket, srcKey,destnBucket,  destnKey, uploadId);
            completeMultipartUpload(s3, destnBucket, destnKey, uploadId, parts);
            System.out.println("Multipart copy completed for: " + srcKey);
        } catch (Exception e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }
```


SDK for Python
The following example shows how to use a multipart upload to
 programmatically copy an object from one bucket to another by
 using the SDK for Python.



```
import logging
import boto3
from botocore.exceptions import ClientError

def head_object(s3_client, bucket_name, key_name):
    '''
    Returns metadata for an object in a directory bucket

    :param s3_client: boto3 S3 client
    :param bucket_name: Bucket that contains the object to query for metadata
    :param key_name: Key name to query for metadata
    :return: Metadata for the specified object if successful, else None
    '''

    try:
        response = s3_client.head_object(
            Bucket = bucket_name,
            Key = key_name
        )
        return response
    except ClientError as e:
        logging.error(e)
        return None
    
def create_multipart_upload(s3_client, bucket_name, key_name):
    '''
    Create a multipart upload to a directory bucket

    :param s3_client: boto3 S3 client
    :param bucket_name: Destination bucket for the multipart upload
    :param key_name: Key name of the object to be uploaded
    :return: UploadId for the multipart upload if created successfully, else None
    '''
    
    try:
        mpu = s3_client.create_multipart_upload(Bucket = bucket_name, Key = key_name)
        return mpu['UploadId'] 
    except ClientError as e:
        logging.error(e)
        return None

def multipart_copy_upload(s3_client, source_bucket_name, key_name, target_bucket_name, mpu_id, part_size):
    '''
    Copy an object in a directory bucket to another bucket in multiple parts of a specified size
    
    :param s3_client: boto3 S3 client
    :param source_bucket_name: Bucket where the source object exists
    :param key_name: Key name of the object to be copied
    :param target_bucket_name: Destination bucket for copied object
    :param mpu_id: The UploadId returned from the create_multipart_upload call
    :param part_size: The size parts that the object will be broken into, in bytes. 
                      Minimum 5 MiB, Maximum 5 GiB. There is no minimum size for the last part of your multipart upload.
    :return: part_list for the multipart copy if all parts are copied successfully, else None
    '''
    
    part_list = []
    copy_source = {
        'Bucket': source_bucket_name,
        'Key': key_name
    }
    try:
        part_counter = 1
        object_size = head_object(s3_client, source_bucket_name, key_name)
        if object_size is not None:
            object_size = object_size['ContentLength']
        while (part_counter - 1) * part_size <object_size:
            bytes_start = (part_counter - 1) * part_size
            bytes_end = (part_counter * part_size) - 1
            upload_copy_part = s3_client.upload_part_copy (
                Bucket = target_bucket_name,
                CopySource = copy_source,
                CopySourceRange = f'bytes={bytes_start}-{bytes_end}',
                Key = key_name,
                PartNumber = part_counter,
                UploadId = mpu_id
            )
            part_list.append({'PartNumber': part_counter, 'ETag': upload_copy_part['CopyPartResult']['ETag']})
            part_counter += 1
    except ClientError as e:
        logging.error(e)
        return None
    return part_list

def complete_multipart_upload(s3_client, bucket_name, key_name, mpu_id, part_list):
    '''
    Completes a multipart upload to a directory bucket

    :param s3_client: boto3 S3 client
    :param bucket_name: Destination bucket for the multipart upload
    :param key_name: Key name of the object to be uploaded
    :param mpu_id: The UploadId returned from the create_multipart_upload call
    :param part_list: List of uploaded part numbers with associated ETags 
    :return: True if the multipart upload was completed successfully, else False
    '''
    
    try:
        s3_client.complete_multipart_upload(
            Bucket = bucket_name,
            Key = key_name,
            UploadId = mpu_id,
            MultipartUpload = {
                'Parts': part_list
            }
        )
    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__ == '__main__':
    MB = 1024 ** 2
    region = '`us-west-2`'
    source_bucket_name = '`SOURCE_BUCKET_NAME`'
    target_bucket_name = '`TARGET_BUCKET_NAME`'
    key_name = '`KEY_NAME`'
    part_size = 10 * MB
    s3_client = boto3.client('s3', region_name = region)
    mpu_id = create_multipart_upload(s3_client, target_bucket_name, key_name)
    if mpu_id is not None:
        part_list = multipart_copy_upload(s3_client, source_bucket_name, key_name, target_bucket_name, mpu_id, part_size)
        if part_list is not None:
            if complete_multipart_upload(s3_client, target_bucket_name, key_name, mpu_id, part_list):
                print (f'{key_name} successfully copied through multipart copy from {source_bucket_name} to {target_bucket_name}')
            else:
                print (f'Could not copy {key_name} through multipart copy from {source_bucket_name} to {target_bucket_name}')
```



The following example shows how to use a multipart upload to
 programmatically copy an object from one bucket to a directory bucket 
 using the AWS CLI. To use the command replace the `user input placeholders` with your own information.


```
aws s3api upload-part-copy --bucket `bucket-base-name`--`zone-id`--x-s3 --key `TARGET_KEY_NAME` --copy-source `SOURCE_BUCKET_NAME/SOURCE_KEY_NAME` --part-number `1` --upload-id "`AS_mgt9RaQE9GEaifATue15dAAAAAAAAAAEMAAAAAAAAADQwNzI4MDU0MjUyMBYAAAAAAAAAAA0AAAAAAAAAAAH2AfYAAAAAAAAEBnJ4cxKMAQAAAABiNXpOFVZJ1tZcKWib9YKE1C565_hCkDJ_4AfCap2svg`"
```
For more information, see [upload-part-copy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/upload-part-copy.html                          "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/upload-part-copy.html                         ") in the AWS Command Line Interface.


### Listing
 in-progress multipart uploads


To list in-progress multipart uploads to a directory bucket, you can use the AWS SDKs, or the AWS CLI. 
 



SDK for Java 2.x
The following examples show how to list in-progress (incomplete) multipart uploads
 by using the SDK for Java 2.x.



```
 public static void listMultiPartUploads( S3Client s3, String bucketName) {
        try {
            ListMultipartUploadsRequest listMultipartUploadsRequest = ListMultipartUploadsRequest.builder()
                .bucket(bucketName)
                .build();
                
            ListMultipartUploadsResponse response = s3.listMultipartUploads(listMultipartUploadsRequest);
            List MultipartUpload uploads = response.uploads();
            for (MultipartUpload upload: uploads) {
                System.out.println("Upload in progress: Key = \"" + upload.key() + "\", id = " + upload.uploadId());
            }
      }
      catch (S3Exception e) {
            System.err.println(e.getMessage());
            System.exit(1);
      }
  }
```


SDK for Python
The following examples show how to list in-progress (incomplete) multipart uploads
 by using the SDK for Python.



```
import logging
import boto3
from botocore.exceptions import ClientError

def list_multipart_uploads(s3_client, bucket_name):
    '''
    List any incomplete multipart uploads in a directory bucket in e specified gion

    :param s3_client: boto3 S3 client
    :param bucket_name: Bucket to check for incomplete multipart uploads
    :return: List of incomplete multipart uploads if there are any, None if not
    '''
    
    try:
        response = s3_client.list_multipart_uploads(Bucket = bucket_name)
        if 'Uploads' in response.keys():
            return response['Uploads']
        else:
            return None 
    except ClientError as e:
        logging.error(e)

if __name__ == '__main__':
    bucket_name = '`BUCKET_NAME`'
    region = '`us-west-2`'
    s3_client = boto3.client('s3', region_name = region)
    multipart_uploads = list_multipart_uploads(s3_client, bucket_name)
    if multipart_uploads is not None:
        print (f'There are {len(multipart_uploads)} ncomplete multipart uploads for {bucket_name}')
    else:
        print (f'There are no incomplete multipart uploads for {bucket_name}')
```



The following examples show how to list in-progress (incomplete) multipart uploads
 by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.


```
aws s3api list-multipart-uploads --bucket `bucket-base-name`--`zone-id`--x-s3
```
For more information, see [list-multipart-uploads](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-multipart-uploads.html                          "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-multipart-uploads.html                         ") in the AWS Command Line Interface.


### Listing the
 parts of a multipart upload


The following examples show how to list the parts of a multipart upload to a directory bucket.



SDK for Java 2.x
The following examples show how to list the parts of a multipart upload to a directory bucket by using SDK for Java 2.x.



```
public static void listMultiPartUploadsParts( S3Client s3, String bucketName, String objKey, String uploadID) {
         
         try {
             ListPartsRequest listPartsRequest = ListPartsRequest.builder()
                 .bucket(bucketName)
                 .uploadId(uploadID)
                 .key(objKey)
                 .build();

             ListPartsResponse response = s3.listParts(listPartsRequest);
             List`Part` parts = response.parts();
             for (Part part: parts) {
                 System.out.println("Upload in progress: Part number = \"" + part.partNumber() + "\", etag = " + part.eTag());
             }

         } 
         
         catch (S3Exception e) {
             System.err.println(e.getMessage());
             System.exit(1);
         }
         
         
     }
```


SDK for Python
The following examples show how to list the parts of a multipart upload to a directory bucket by using SDK for Python.



```
import logging
import boto3
from botocore.exceptions import ClientError

def list_parts(s3_client, bucket_name, key_name, upload_id):
    '''
    Lists the parts that have been uploaded for a specific multipart upload to a directory bucket.
    
    :param s3_client: boto3 S3 client
    :param bucket_name: Bucket that multipart uploads parts have been uploaded to
    :param key_name: Name of the object that has parts uploaded
    :param upload_id: Multipart upload ID that the parts are associated with
    :return: List of parts associated with the specified multipart upload, None if there are no parts
    '''
    parts_list = []
    next_part_marker = ''
    continuation_flag = True
    try:
        while continuation_flag:
            if next_part_marker == '':
                response = s3_client.list_parts(
                    Bucket = bucket_name,
                    Key = key_name,
                    UploadId = upload_id
                )
            else:
                response = s3_client.list_parts(
                    Bucket = bucket_name,
                    Key = key_name,
                    UploadId = upload_id,
                    NextPartMarker = next_part_marker
                )
            if 'Parts' in response:
                for part in response['Parts']:
                    parts_list.append(part)
                if response['IsTruncated']:
                    next_part_marker = response['NextPartNumberMarker']
                else:
                    continuation_flag = False
            else:
                continuation_flag = False
        return parts_list
    except ClientError as e:
        logging.error(e)
        return None

if __name__ == '__main__':
    region = '`us-west-2`'
    bucket_name = '`BUCKET_NAME`'
    key_name = '`KEY_NAME`'
    upload_id = '`UPLOAD_ID`'
    s3_client = boto3.client('s3', region_name = region)
    parts_list = list_parts(s3_client, bucket_name, key_name, upload_id)
    if parts_list is not None:
        print (f'{key_name} has {len(parts_list)} parts uploaded to {bucket_name}')
    else:
        print (f'There are no multipart uploads with that upload ID for {bucket_name} bucket')
```



The following examples show how to list the parts of a multipart upload to a directory bucket by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.


```
aws s3api list-parts --bucket ``bucket-base-name`--`zone-id`--x-s3` --key `KEY_NAME` --upload-id "`AS_mgt9RaQE9GEaifATue15dAAAAAAAAAAEMAAAAAAAAADQwNzI4MDU0MjUyMBYAAAAAAAAAAA0AAAAAAAAAAAH2AfYAAAAAAAAEBSD0WBKMAQAAAABneY9yBVsK89iFkvWdQhRCcXohE8RbYtc9QvBOG8tNpA`"
```
For more information, see [list-parts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-parts.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-parts.html") in the AWS Command Line Interface.
