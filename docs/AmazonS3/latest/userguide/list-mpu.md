# Listing multipart uploads

You can use the AWS CLI, REST API, or AWS SDKs, to retrieve a list of in-progress
multipart uploads in Amazon S3. You can use the multipart upload to programmatically upload a
single object to Amazon S3. Multipart uploads move objects into Amazon S3 by moving a portion of an
object's data at a time. For more general information about multipart uploads, see [Uploading and copying objects using multipart upload in Amazon S3](mpuoverview.md "mpuoverview.md").

For an end-to-end procedure on uploading an object with multipart upload with an additional checksum, see
[Tutorial: Upload an object through multipart upload and
verify its data integrity](tutorial-s3-mpu-additional-checksums.md "tutorial-s3-mpu-additional-checksums.md").

The following section show how to list in-progress multipart uploads with the AWS Command Line Interface,
the Amazon S3 REST API, and AWS SDKs.

The following sections in the AWS Command Line Interface describe the operations for listing multipart
uploads.

- [list-parts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-parts.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-parts.html")‐list the uploaded parts for a specific multipart upload.
- [list-multipart-uploads](../../../cli/latest/reference/s3api/list-multipart-uploads.md "../../../cli/latest/reference/s3api/list-multipart-uploads.md")‐list in-progress multipart uploads.
  The following sections in the _Amazon Simple Storage Service API Reference_ describe the REST API for listing multipart uploads:

- [ListParts](../API/API_ListParts.md "../API/API_ListParts.md")‐list the uploaded parts for a specific multipart upload.
- [ListMultipartUploads](../API/API_ListMultipartUploads.md "../API/API_ListMultipartUploads.md")‐list in-progress multipart uploads.

Java
To list all in-progress multipart uploads on a bucket using the AWS SDK for Java, you can use the low-level API classes to:

Low-level API multipart uploads listing process| 1 | Create an instance of the `ListMultipartUploadsRequest` class and
provide the bucket name. |
| 2 | Run the S3Client `listMultipartUploads` method. The method returns an instance of the `ListMultipartUploadsResponse` class that gives you information about the multipart uploads in progress. | For examples of how to list multipart uploads with the AWS SDK for Java, see [List multipart uploads](../API/s3_example_s3_ListMultipartUploads_section.md "../API/s3_example_s3_ListMultipartUploads_section.md") in the _Amazon S3 API Reference_. .NETTo list all of the in-progress multipart uploads on a specific bucket, use the SDK for .NET low-level multipart upload API's `ListMultipartUploadsRequest` class. The `AmazonS3Client.ListMultipartUploads` method returns an instance of the `ListMultipartUploadsResponse` class that provides information about the in-progress multipart uploads. An in-progress multipart upload is a multipart upload that has been initiated using the initiate multipart upload request, but has not yet been completed or stopped. For more information about Amazon S3 multipart uploads, see [Uploading and copying objects using multipart upload in Amazon S3](mpuoverview.md "mpuoverview.md"). The following C# example shows how to use the SDK for .NET to list all in-progress multipart uploads on a bucket. For information about setting up and running the code examples, see [Getting Started with the AWS SDK for .NET](../../../sdk-for-net/latest/developer-guide/net-dg-setup.md "../../../sdk-for-net/latest/developer-guide/net-dg-setup.md") in the _AWS SDK for .NET Developer Guide_. `ListMultipartUploadsRequest request = new ListMultipartUploadsRequest { BucketName = bucketName // Bucket receiving the uploads. }; ListMultipartUploadsResponse response = await AmazonS3Client.ListMultipartUploadsAsync(request);` PHPThis topic shows how to use the low-level API classes from version 3 of the AWS SDK for PHP to list all in-progress multipart uploads on a bucket. For more information about the AWS SDK for Ruby API, go to [AWS SDK for Ruby - Version 2](../../../sdkforruby/api/index.md "../../../sdkforruby/api/index.md"). The following PHP example demonstrates listing all in-progress multipart uploads on a bucket. `require 'vendor/autoload.php'; use Aws\S3\S3Client; $bucket = '*** Your Bucket Name ***'; $s3 = new S3Client([ 'version' => 'latest', 'region'  => 'us-east-1' ]); // Retrieve a list of the current multipart uploads. $result = $s3->listMultipartUploads([ 'Bucket' => $bucket ]); // Write the list of uploads to the page. print_r($result->toArray());`
