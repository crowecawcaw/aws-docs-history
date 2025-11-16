AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Supported Amazon S3 REST API actions on Snowball Edge for data transfer

Following, you can find the list of Amazon S3 REST API actions that are supported for
using the Amazon S3 adapter. The list includes links to information about how the API
actions work with Amazon S3. The list also covers any differences in behavior between the
Amazon S3 API action and the AWS Snowball Edge device counterpart. All responses coming back from an
AWS Snowball Edge device declare `Server` as `AWSSnowball`, as in the
following example.

```
HTTP/1.1 201 OK
x-amz-id-2: JuKZqmXuiwFeDQxhD7M8KtsKobSzWA1QEjLbTMTagkKdBX2z7Il/jGhDeJ3j6s80
x-amz-request-id: 32FE2CEB32F5EE25
Date: Fri, 08 2016 21:34:56 GMT
Server: AWSSnowball
```

Amazon S3 REST API calls require SigV4 signing. If you're using the AWS CLI or an AWS SDK
to make these API calls, the SigV4 signing is handled for you. Otherwise, you need
to implement your own SigV4 signing solution. For more information, see [Authenticating requests
(AWS Signature Version 4)](../../../AmazonS3/latest/userguide/sig-v4-authenticating-requests.md "../../../AmazonS3/latest/userguide/sig-v4-authenticating-requests.md") in the Amazon Simple Storage Service User Guide.

- [GET Bucket (List Objects)
  version 1](../../../AmazonS3/latest/API/RESTBucketGET.md "../../../AmazonS3/latest/API/RESTBucketGET.md")

– Supported. However, in this implemetation of the GET operation, the
following is not supported:

    + Pagination
    + Markers
    + Delimiters
    + When the list is returned, the list is not sorted

Only version 1 is supported. GET Bucket (List Objects) version 2 is not
supported.

- [GET Service](../../../AmazonS3/latest/API/RESTServiceGET.md "../../../AmazonS3/latest/API/RESTServiceGET.md")
- [HEAD Bucket](../../../AmazonS3/latest/API/RESTBucketHEAD.md "../../../AmazonS3/latest/API/RESTBucketHEAD.md")
- [HEAD Object](../../../AmazonS3/latest/API/RESTObjectHEAD.md "../../../AmazonS3/latest/API/RESTObjectHEAD.md")
- [GET Object](../../../AmazonS3/latest/API/RESTObjectGET.md "../../../AmazonS3/latest/API/RESTObjectGET.md") – is
  a DOWNLOAD of an object from the Snow device's S3 bucket.
- [PUT Object](../../../AmazonS3/latest/API/RESTObjectPUT.md "../../../AmazonS3/latest/API/RESTObjectPUT.md") –
  When an object is uploaded to an AWS Snowball Edge device using `PUT
Object`, an ETag is generated.

The ETag is a hash of the object. The ETag reflects changes only to the
contents of an object, not its metadata. The ETag might or might not be an
MD5 digest of the object data. For more information about ETags, see [Common Response
Headers](../../../AmazonS3/latest/API/RESTCommonResponseHeaders.md "../../../AmazonS3/latest/API/RESTCommonResponseHeaders.md") in the _Amazon Simple Storage Service API Reference._

- [DELETE Object](../../../AmazonS3/latest/API/RESTObjectDELETE.md "../../../AmazonS3/latest/API/RESTObjectDELETE.md")
- [Initiate Multipart
  Upload](../../../AmazonS3/latest/API/mpUploadInitiate.md "../../../AmazonS3/latest/API/mpUploadInitiate.md") – In this implementation, initiating a multipart
  upload request for an object already on the AWS Snowball Edge device first deletes that
  object. It then copies it in parts to the AWS Snowball Edge device.
- [List Multipart
  Uploads](../../../AmazonS3/latest/API/mpUploadListMPUpload.md "../../../AmazonS3/latest/API/mpUploadListMPUpload.md")
- [Upload Part](../../../AmazonS3/latest/API/mpUploadUploadPart.md "../../../AmazonS3/latest/API/mpUploadUploadPart.md")
- [Complete Multipart
  Upload](../../../AmazonS3/latest/API/mpUploadComplete.md "../../../AmazonS3/latest/API/mpUploadComplete.md")
- [Abort Multipart Upload](../../../AmazonS3/latest/API/mpUploadAbort.md "../../../AmazonS3/latest/API/mpUploadAbort.md")

###### Note

Any Amazon S3 adapter REST API actions not listed here are not supported. Using any
unsupported REST API actions with your Snowball Edge returns an error message
saying that the action is not supported.
