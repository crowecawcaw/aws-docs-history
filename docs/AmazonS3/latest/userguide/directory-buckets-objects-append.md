# Appending data to objects in directory

buckets

You can add data to the end of existing objects stored in the S3 Express One Zone storage class in directory buckets.
We recommend that you use the ability to append data to an object if the data is written continuously over a period of time or if
you need to read the object while you are writing to the object. Appending data to objects is common for use-cases
such as adding new log entries to log files or adding new video segments to video files as
they are transcoded then streamed. By appending data to objects, you can simplify applications
that previously combined data in local storage before copying the final object to Amazon S3.

There is no minimum size requirement for the data you can append to an object.
However, the maximum size of the data that you can append to an object in a single request is 5GB.
This is the same limit as the largest request size when uploading data using any Amazon S3 API.

With each successful append operation,
you create a part of the object and each object can have up to 10,000 parts.
This means you can append data to an object up to 10,000 times.
If an object is created using S3 multipart upload, each uploaded part is counted towards
the total maximum of 10,000 parts. For example, you can append up to 9,000 times to an object created
by multipart upload comprising of 1,000 parts.

###### Note

If you hit the limit of parts, you will receive a [TooManyParts](../API/API_PutObject.md#API_PutObject_Errors "../API/API_PutObject.md#API_PutObject_Errors") error.
You can use the `CopyObject` API to reset the count.

If you want to upload parts to an object in parallel and you don’t need to read the parts while the parts are being uploaded,
we recommend that you use Amazon S3 multipart upload.
For more information, see [Using multipart
upload](s3-express-using-multipart-upload.md "s3-express-using-multipart-upload.md").

Appending data to objects is only supported for objects in directory buckets that are
stored in the S3 Express One Zone storage class. For more information on S3 Express One Zone
Zone, see [Getting started with S3
Express One Zone](s3-express-getting-started.md "s3-express-getting-started.md").

To get started appending data to objects in your directory buckets, you can use the AWS
SDKs, AWS CLI, and the `PutObject` API . When you make a `PutObject`
request, you set the `x-amz-write-offset-bytes` header to the size of the object
that you are appending to. To use the `PutObject` API operation, you must use the
`CreateSession` API to establish temporary security credentials to access the
objects in your directory buckets. For more information, see
[`PutObject`](../API/API_PutObject.md "../API/API_PutObject.md") and [`CreateSession`](../API/API_CreateSession.md "../API/API_CreateSession.md") in the _Amazon S3 API Reference_.

Each successful append operation is billed as a `PutObject` request. To learn
more about pricing, see [`Amazon S3
 pricing`](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

###### Note

Starting with the 1.12 release, Mountpoint for Amazon S3 supports appending data to objects stored in S3 Express One Zone.
To get started, you must opt-in by setting the `--incremental-upload` flag. For more information on Mountpoint, see [Working
with Mountpoint](mountpoint.md "mountpoint.md").

If you use a CRC (Cyclic Redundancy Check) algorithm while uploading the appended data,
you can retrieve full object CRC-based checksums using the `HeadObject` or
`GetObject` request. If you use the SHA-1 or SHA-256 algorithm while
uploading your appended data, you can retrieve a checksum of the appended parts and verify
their integrity using the SHA checksums returned on prior PutObject responses. For more
information, see [Data protection and encryption](s3-express-data-protection.md "s3-express-data-protection.md").

## Appending data to your objects by using the

AWS CLI, AWS SDKs and the REST API

You can append data to your objects by using the AWS Command Line Interface (AWS CLI), AWS SDKs and
REST API.

The following `put-object` example command shows how you can use
the AWS CLI to append data to an object. To run this command, replace the
`user input placeholders` with your own
information

```
aws s3api put-object --bucket `amzn-s3-demo-bucket`--`azid`--x-s3 --key `sampleinput/file001.bin` --body bucket-seed/file001.bin --write-offset-bytes size-of-sampleinput/file001.bin
```

SDK for Java
You can use the AWS SDK for Java to append data to your
objects.

```
var putObjectRequestBuilder = PutObjectRequest.builder()
                                              .key(key)
                                              .bucket(bucketName)
                                              .writeOffsetBytes(9);
var response = s3Client.putObject(putObjectRequestBuilder.build());
```

SDK for Python

```
s3.put_object(Bucket='`amzn-s3-demo-bucket`--`use2-az2`--x-s3', Key='2024-11-05-sdk-test', Body=b'123456789', WriteOffsetBytes=9)
```

You can send REST requests to append data to an object. For more information, see
[`PutObject`](../API/API_PutObject.md#API_PutObject "../API/API_PutObject.md#API_PutObject").
