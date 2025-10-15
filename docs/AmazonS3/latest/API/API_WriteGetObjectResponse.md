# WriteGetObjectResponse

###### Note

This operation is not supported for directory buckets.

Passes transformed objects to a `GetObject` operation when using Object Lambda access points. For information
 about Object Lambda access points, see [Transforming objects with Object Lambda access points](../userguide/transforming-objects.md "../userguide/transforming-objects.md") in the *Amazon S3 User Guide*.

This operation supports metadata that can be returned by [GetObject](API_GetObject.md "API_GetObject.md"), in addition to
 `RequestRoute`, `RequestToken`, `StatusCode`, `ErrorCode`,
 and `ErrorMessage`. The `GetObject` response metadata is supported so that the
 `WriteGetObjectResponse` caller, typically an AWS Lambda function, can provide the same
 metadata when it internally invokes `GetObject`. When `WriteGetObjectResponse` is
 called by a customer-owned Lambda function, the metadata returned to the end user `GetObject`
 call might differ from what Amazon S3 would normally return.

You can include any number of metadata headers. When including a metadata header, it should be
 prefaced with `x-amz-meta`. For example, `x-amz-meta-my-custom-header:
 MyCustomValue`. The primary use case for this is to forward `GetObject`
 metadata.


 AWS provides some prebuilt Lambda functions that you can use with S3 Object Lambda to detect and
 redact personally identifiable information (PII) and decompress S3 objects. These Lambda functions are
 available in the AWS Serverless Application Repository, and can be selected through the AWS
 Management Console when you create your Object Lambda access point.

Example 1: PII Access Control - This Lambda function uses Amazon Comprehend, a natural
 language processing (NLP) service using machine learning to find insights and relationships in text. It
 automatically detects personally identifiable information (PII) such as names, addresses, dates, credit
 card numbers, and social security numbers from documents in your Amazon S3 bucket. 

Example 2: PII Redaction - This Lambda function uses Amazon Comprehend, a natural language
 processing (NLP) service using machine learning to find insights and relationships in text. It
 automatically redacts personally identifiable information (PII) such as names, addresses, dates, credit
 card numbers, and social security numbers from documents in your Amazon S3 bucket. 

Example 3: Decompression - The Lambda function S3ObjectLambdaDecompression, is equipped to
 decompress objects stored in S3 in one of six compressed file formats including bzip2, gzip, snappy,
 zlib, zstandard and ZIP. 

For information on how to view and use these functions, see [Using AWS built Lambda functions](../userguide/olap-examples.md "../userguide/olap-examples.md") in the
 *Amazon S3 User Guide*.

###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
POST /WriteGetObjectResponse HTTP/1.1
Host: s3.amazonaws.com
x-amz-request-route: `RequestRoute`
x-amz-request-token: `RequestToken`
x-amz-fwd-status: `StatusCode`
x-amz-fwd-error-code: `ErrorCode`
x-amz-fwd-error-message: `ErrorMessage`
x-amz-fwd-header-accept-ranges: `AcceptRanges`
x-amz-fwd-header-Cache-Control: `CacheControl`
x-amz-fwd-header-Content-Disposition: `ContentDisposition`
x-amz-fwd-header-Content-Encoding: `ContentEncoding`
x-amz-fwd-header-Content-Language: `ContentLanguage`
Content-Length: `ContentLength`
x-amz-fwd-header-Content-Range: `ContentRange`
x-amz-fwd-header-Content-Type: `ContentType`
x-amz-fwd-header-x-amz-checksum-crc32: `ChecksumCRC32`
x-amz-fwd-header-x-amz-checksum-crc32c: `ChecksumCRC32C`
x-amz-fwd-header-x-amz-checksum-crc64nvme: `ChecksumCRC64NVME`
x-amz-fwd-header-x-amz-checksum-sha1: `ChecksumSHA1`
x-amz-fwd-header-x-amz-checksum-sha256: `ChecksumSHA256`
x-amz-fwd-header-x-amz-delete-marker: `DeleteMarker`
x-amz-fwd-header-ETag: `ETag`
x-amz-fwd-header-Expires: `Expires`
x-amz-fwd-header-x-amz-expiration: `Expiration`
x-amz-fwd-header-Last-Modified: `LastModified`
x-amz-fwd-header-x-amz-missing-meta: `MissingMeta`
x-amz-fwd-header-x-amz-object-lock-mode: `ObjectLockMode`
x-amz-fwd-header-x-amz-object-lock-legal-hold: `ObjectLockLegalHoldStatus`
x-amz-fwd-header-x-amz-object-lock-retain-until-date: `ObjectLockRetainUntilDate`
x-amz-fwd-header-x-amz-mp-parts-count: `PartsCount`
x-amz-fwd-header-x-amz-replication-status: `ReplicationStatus`
x-amz-fwd-header-x-amz-request-charged: `RequestCharged`
x-amz-fwd-header-x-amz-restore: `Restore`
x-amz-fwd-header-x-amz-server-side-encryption: `ServerSideEncryption`
x-amz-fwd-header-x-amz-server-side-encryption-customer-algorithm: `SSECustomerAlgorithm`
x-amz-fwd-header-x-amz-server-side-encryption-aws-kms-key-id: `SSEKMSKeyId`
x-amz-fwd-header-x-amz-server-side-encryption-customer-key-MD5: `SSECustomerKeyMD5`
x-amz-fwd-header-x-amz-storage-class: `StorageClass`
x-amz-fwd-header-x-amz-tagging-count: `TagCount`
x-amz-fwd-header-x-amz-version-id: `VersionId`
x-amz-fwd-header-x-amz-server-side-encryption-bucket-key-enabled: `BucketKeyEnabled`

`Body`
```

## URI Request Parameters


The request uses the following URI parameters.





**[Content-Length](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


The size of the content body in bytes.




**[x-amz-fwd-error-code](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


A string that uniquely identifies an error condition. Returned in the <Code> tag of the error
 XML response for a corresponding `GetObject` call. Cannot be used with a successful
 `StatusCode` header or when the transformed object is provided in the body. All error codes
 from S3 are sentence-cased. The regular expression (regex) value is
 `"^[A-Z][a-zA-Z]+$"`.




**[x-amz-fwd-error-message](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


Contains a generic description of the error condition. Returned in the <Message> tag of the
 error XML response for a corresponding `GetObject` call. Cannot be used with a successful
 `StatusCode` header or when the transformed object is provided in body.




**[x-amz-fwd-header-accept-ranges](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


Indicates that a range of bytes was specified.




**[x-amz-fwd-header-Cache-Control](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


Specifies caching behavior along the request/reply chain.




**[x-amz-fwd-header-Content-Disposition](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


Specifies presentational information for the object.




**[x-amz-fwd-header-Content-Encoding](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


Specifies what content encodings have been applied to the object and thus what decoding mechanisms
 must be applied to obtain the media-type referenced by the Content-Type header field.




**[x-amz-fwd-header-Content-Language](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


The language the content is in.




**[x-amz-fwd-header-Content-Range](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


The portion of the object returned in the response.




**[x-amz-fwd-header-Content-Type](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


A standard MIME type describing the format of the object data.




**[x-amz-fwd-header-ETag](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


An opaque identifier assigned by a web server to a specific version of a resource found at a URL.
 




**[x-amz-fwd-header-Expires](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


The date and time at which the object is no longer cacheable.




**[x-amz-fwd-header-Last-Modified](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


The date and time that the object was last modified.




**[x-amz-fwd-header-x-amz-checksum-crc32](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


This header can be used as a data integrity check to verify that the data received is the same data
 that was originally sent. This specifies the Base64 encoded, 32-bit `CRC32` checksum of the
 object returned by the Object Lambda function. This may not match the checksum for the object stored in
 Amazon S3. Amazon S3 will perform validation of the checksum values only when the original `GetObject`
 request required checksum validation. For more information about checksums, see [Checking object
 integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in the *Amazon S3 User Guide*.


Only one checksum header can be specified at a time. If you supply multiple checksum headers, this
 request will fail.





**[x-amz-fwd-header-x-amz-checksum-crc32c](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


This header can be used as a data integrity check to verify that the data received is the same data
 that was originally sent. This specifies the Base64 encoded, 32-bit `CRC32C` checksum of the
 object returned by the Object Lambda function. This may not match the checksum for the object stored in
 Amazon S3. Amazon S3 will perform validation of the checksum values only when the original `GetObject`
 request required checksum validation. For more information about checksums, see [Checking object
 integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in the *Amazon S3 User Guide*.


Only one checksum header can be specified at a time. If you supply multiple checksum headers, this
 request will fail.




**[x-amz-fwd-header-x-amz-checksum-crc64nvme](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


This header can be used as a data integrity check to verify that the data received is the same data
 that was originally sent. This header specifies the Base64 encoded, 64-bit `CRC64NVME`
 checksum of the part. For more information, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.




**[x-amz-fwd-header-x-amz-checksum-sha1](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


This header can be used as a data integrity check to verify that the data received is the same data
 that was originally sent. This specifies the Base64 encoded, 160-bit `SHA1` digest of the
 object returned by the Object Lambda function. This may not match the checksum for the object stored in
 Amazon S3. Amazon S3 will perform validation of the checksum values only when the original `GetObject`
 request required checksum validation. For more information about checksums, see [Checking object
 integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in the *Amazon S3 User Guide*.


Only one checksum header can be specified at a time. If you supply multiple checksum headers, this
 request will fail.




**[x-amz-fwd-header-x-amz-checksum-sha256](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


This header can be used as a data integrity check to verify that the data received is the same data
 that was originally sent. This specifies the Base64 encoded, 256-bit `SHA256` digest of the
 object returned by the Object Lambda function. This may not match the checksum for the object stored in
 Amazon S3. Amazon S3 will perform validation of the checksum values only when the original `GetObject`
 request required checksum validation. For more information about checksums, see [Checking object
 integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in the *Amazon S3 User Guide*.


Only one checksum header can be specified at a time. If you supply multiple checksum headers, this
 request will fail.




**[x-amz-fwd-header-x-amz-delete-marker](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


Specifies whether an object stored in Amazon S3 is (`true`) or is not (`false`) a
 delete marker. To learn more about delete markers, see [Working with delete markers](../userguide/DeleteMarker.md "../userguide/DeleteMarker.md").




**[x-amz-fwd-header-x-amz-expiration](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


If the object expiration is configured (see PUT Bucket lifecycle), the response includes this
 header. It includes the `expiry-date` and `rule-id` key-value pairs that provide
 the object expiration information. The value of the `rule-id` is URL-encoded. 




**[x-amz-fwd-header-x-amz-missing-meta](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


Set to the number of metadata entries not returned in `x-amz-meta` headers. This can
 happen if you create metadata using an API like SOAP that supports more flexible metadata than the REST
 API. For example, using SOAP, you can create metadata whose values are not legal HTTP headers.




**[x-amz-fwd-header-x-amz-mp-parts-count](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


The count of parts this object has.




**[x-amz-fwd-header-x-amz-object-lock-legal-hold](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


Indicates whether an object stored in Amazon S3 has an active legal hold.


Valid Values: `ON | OFF`





**[x-amz-fwd-header-x-amz-object-lock-mode](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


Indicates whether an object stored in Amazon S3 has Object Lock enabled. For more information about S3
 Object Lock, see [Object
 Lock](../userguide/object-lock.md "../userguide/object-lock.md").


Valid Values: `GOVERNANCE | COMPLIANCE`





**[x-amz-fwd-header-x-amz-object-lock-retain-until-date](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


The date and time when Object Lock is configured to expire.




**[x-amz-fwd-header-x-amz-replication-status](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


Indicates if request involves bucket that is either a source or destination in a Replication rule.
 For more information about S3 Replication, see [Replication](../userguide/replication.md "../userguide/replication.md").


Valid Values: `COMPLETE | PENDING | FAILED | REPLICA | COMPLETED`





**[x-amz-fwd-header-x-amz-request-charged](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


If present, indicates that the requester was successfully charged for the request. For more
 information, see [Using Requester Pays buckets for storage transfers and usage](../userguide/RequesterPaysBuckets.md "../userguide/RequesterPaysBuckets.md") in the *Amazon Simple
 Storage Service user guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





**[x-amz-fwd-header-x-amz-restore](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


Provides information about object restoration operation and expiration time of the restored object
 copy.




**[x-amz-fwd-header-x-amz-server-side-encryption](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


 The server-side encryption algorithm used when storing requested object in Amazon S3 or Amazon FSx.


###### Note

When accessing data stored in Amazon FSx file systems using S3 access points, the only valid server side
 encryption option is `aws:fsx`.


Valid Values: `AES256 | aws:fsx | aws:kms | aws:kms:dsse`





**[x-amz-fwd-header-x-amz-server-side-encryption-aws-kms-key-id](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


 If present, specifies the ID (Key ID, Key ARN, or Key Alias) of the AWS Key Management Service
 (AWS KMS) symmetric encryption customer managed key that was used for stored in Amazon S3 object. 




**[x-amz-fwd-header-x-amz-server-side-encryption-bucket-key-enabled](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


 Indicates whether the object stored in Amazon S3 uses an S3 bucket key for server-side encryption with
 AWS KMS (SSE-KMS).




**[x-amz-fwd-header-x-amz-server-side-encryption-customer-algorithm](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


Encryption algorithm used if server-side encryption with a customer-provided encryption key was
 specified for object stored in Amazon S3.




**[x-amz-fwd-header-x-amz-server-side-encryption-customer-key-MD5](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


 128-bit MD5 digest of customer-provided encryption key used in Amazon S3 to encrypt data stored in S3.
 For more information, see [Protecting data using
 server-side encryption with customer-provided encryption keys (SSE-C)](../userguide/ServerSideEncryptionCustomerKeys.md "../userguide/ServerSideEncryptionCustomerKeys.md").




**[x-amz-fwd-header-x-amz-storage-class](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


Provides storage class information of the object. Amazon S3 returns this header for all objects except
 for S3 Standard storage class objects.


For more information, see [Storage Classes](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html").


Valid Values: `STANDARD | REDUCED_REDUNDANCY | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | GLACIER | DEEP_ARCHIVE | OUTPOSTS | GLACIER_IR | SNOW | EXPRESS_ONEZONE | FSX_OPENZFS`





**[x-amz-fwd-header-x-amz-tagging-count](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


The number of tags, if any, on the object.




**[x-amz-fwd-header-x-amz-version-id](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


An ID used to reference a specific version of the object.




**[x-amz-fwd-status](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


The integer status code for an HTTP response of a corresponding `GetObject` request. The
 following is a list of status codes.



* `200 - OK`
* `206 - Partial Content`
* `304 - Not Modified`
* `400 - Bad Request`
* `401 - Unauthorized`
* `403 - Forbidden`
* `404 - Not Found`
* `405 - Method Not Allowed`
* `409 - Conflict`
* `411 - Length Required`
* `412 - Precondition Failed`
* `416 - Range Not Satisfiable`
* `500 - Internal Server Error`
* `503 - Service Unavailable`



**[x-amz-request-route](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


Route prefix to the HTTP URL generated.


Required: Yes




**[x-amz-request-token](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**


A single use encrypted token that maps `WriteGetObjectResponse` to the end user
 `GetObject` request.


Required: Yes




## Request Body


The request accepts the following binary data.





**[Body](#API_WriteGetObjectResponse_RequestSyntax "#API_WriteGetObjectResponse_RequestSyntax")**



## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Sample Response


The following illustrates a sample response.



```

             HTTP/1.1 200 OK
             x-amz-request-id: 19684529-d1aa-413e-9382-9ff490962d12
             Date: Wed, 24 Feb 2021 10:57:53 GMT
             Content-Length: 0
```

### Sample Request


The following illustrates a sample request from a POST.



```

             POST /WriteGetObjectResponse HTTP/1.1
             Host: <RequestRoute>.s3-object-lambda.<Region>.amazonaws.com
             x-amz-request-token: <RequestToken>
             Authorization: authorization string
             Content-Type: text/plain
             Content-Length: 16
             [16 bytes of object data]
```

### Sample Error Response


The following response returns a `ValidationError` error because the RequestToken
 could not be decrypted.



```

            <?xml version="1.0" encoding="UTF-8"?>
            <Error>
            <Code>ValidationError</Code>
            <Message>Invalid token</Message>
            <RequestId>fcd2cd5e-def0-4001-8030-1fd1d61d2c9d</RequestId>
            </Error>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/WriteGetObjectResponse "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/WriteGetObjectResponse")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/WriteGetObjectResponse "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/WriteGetObjectResponse")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/WriteGetObjectResponse "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/WriteGetObjectResponse")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/WriteGetObjectResponse "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/WriteGetObjectResponse")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/WriteGetObjectResponse "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/WriteGetObjectResponse")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/WriteGetObjectResponse "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/WriteGetObjectResponse")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/WriteGetObjectResponse "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/WriteGetObjectResponse")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/WriteGetObjectResponse "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/WriteGetObjectResponse")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/WriteGetObjectResponse "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/WriteGetObjectResponse")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/WriteGetObjectResponse "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/WriteGetObjectResponse")
