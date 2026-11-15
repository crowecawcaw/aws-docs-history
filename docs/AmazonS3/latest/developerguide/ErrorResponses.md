

# Error responses
<a name="ErrorResponses"></a>

This section provides reference information about Amazon S3 errors.

**Note**  
In general, S3 bucket owners are billed for requests with HTTP `200 OK` successful responses and HTTP `4XX` client error responses. Bucket owners aren't billed for HTTP `5XX` server error responses, such as HTTP `503 Slow Down` errors. For more information on S3 error codes under HTTP `3XX` and `4XX` status codes that aren't billed, see [Billing for Amazon S3 error responses](/AmazonS3/latest/userguide/ErrorCodeBilling.html) in the Amazon S3 User Guide. For more information about billing charges if your bucket is configured as a Requester Pays bucket, see [How Requester Pays charges work](/AmazonS3/latest/userguide/RequesterPaysBuckets.html#ChargeDetails) in the Amazon S3 User Guide.

**Topics**
+ [REST error responses](#RESTErrorResponses)
+ [List of error codes](#ErrorCodeList)
+ [List of SELECT Object Content Error Codes](#SelectObjectContentErrorCodeList)
+ [List of Replication-related error codes](#ReplicationErrorCodeList)
+ [List of Tagging-related error codes](#S3TaggingErrorCodeList)
+ [List of Amazon S3 annotation-related error codes](#S3AnnotationErrorCodeList)
+ [List of Amazon S3 on Outposts error codes](#S3OutpostsErrorCodeList)
+ [List of Amazon S3 Storage Lens error codes](#S3LensErrorCodeList)
+ [List of Amazon S3 Object Lambda error codes](#S3ObjectLambdaErrorCodeList)
+ [List of Amazon S3 asynchronous error codes](#S3AsynchronousErrorCodeList)
+ [List of Amazon S3 Access Grants error codes](#S3AccessGrantsErrorCodeList)
+ [List of Amazon FSx-related error codes](#FSXErrorCodeList)
+ [List of Amazon S3 Tables error codes](#S3TablesErrorCodeList)
+ [Amazon S3 error best practices](ErrorBestPractices.md)

## REST error responses
<a name="RESTErrorResponses"></a>

When an error occurs, the header information contains the following:
+ Content-Type: application/xml 
+ An appropriate 3xx, 4xx, or 5xx HTTP status code

The body of the response also contains information about the error. The following sample error response shows the structure of response elements common to all REST error responses.

```
1. <?xml version="1.0" encoding="UTF-8"?>
2. <Error>
3.   <Code>NoSuchKey</Code>
4.   <Message>The resource you requested does not exist</Message>
5.   <Resource>/mybucket/myfoto.jpg</Resource> 
6.   <RequestId>4442587FB7D0A2F9</RequestId>
7. </Error>
```

The following table explains the REST error response elements.


|  Name  |  Description  | 
| --- | --- | 
|  Code  | The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type. For more information, see [List of error codes](#ErrorCodeList).<br />Type: String<br />Ancestor: `Error` | 
| Error  | Container for all error elements.<br />Type: Container<br />Ancestor: None | 
|  Message  | The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.<br />Type: String<br />Ancestor: `Error` | 
|  RequestId  | ID of the request associated with the error.<br />Type: String<br />Ancestor: `Error` | 
|  Resource  | The bucket or object that is involved in the error.<br />Type: String<br />Ancestor: `Error` | 

Many error responses contain additional structured data meant to be read and understood by a developer diagnosing programming errors. For example, if you send a Content-MD5 header with a REST PUT request that doesn't match the digest calculated on the server, you receive a `BadDigest` error. The error response also includes as detail elements the digest that the server calculated, and the digest that you told the server to expect. During development, you can use this information to diagnose the error. In production, a well-behaved program might include this information in its error log.

For information about general response elements, go to [Error responses](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingRESTError.html).

## List of error codes
<a name="ErrorCodeList"></a>

The following table lists Amazon S3 error codes.



- **`AccessControlListNotSupported`**
  - **Description:** The bucket does not allow ACLs.
  - **HTTP status code:** 400 Bad Request

- **`AccessDenied`**
  - **Description:** Access Denied
  - **HTTP status code:** 403 Forbidden

- **`AccessPointAlreadyOwnedByYou`**
  - **Description:** An access point with an identical name already exists in your account.
  - **HTTP status code:** 409 Conflict

- **`AccountProblem`**
  - **Description:** There is a problem with your AWS account that prevents the operation from completing successfully. For further assistance, see [Contact Us](https://aws.amazon.com/contact-us/).
  - **HTTP status code:** 403 Forbidden

- **`AllAccessDisabled`**
  - **Description:** All access to this Amazon S3 resource has been disabled. For further assistance, see [Contact Us](https://aws.amazon.com/contact-us/).
  - **HTTP status code:** 403 Forbidden

- ** `AmbiguousGrantByEmailAddress` **
  - **Description:** The email address that you provided is associated with more than one account.
  - **HTTP status code:** 400 Bad Request

- ** `AuthorizationHeaderMalformed` **
  - **Description:** The authorization header that you provided is not valid.
  - **HTTP status code:** 400 Bad Request

- ** `AuthorizationQueryParametersError` **
  - **Description:** The authorization query parameters that you provided are not valid.
  - **HTTP status code:** 400 Bad Request

- **`BadDigest`**
  - **Description:** The Content-MD5 or checksum value that you specified did not match what the server received.
  - **HTTP status code:** 400 Bad Request

- **`BucketAlreadyExists`**
  - **Description:** The requested bucket name is not available. The bucket namespace is shared by all users of the system. Specify a different name and try again.
  - **HTTP status code:** 409 Conflict

- **`BucketAlreadyOwnedByYou`**
  - **Description:** The bucket that you tried to create already exists, and you own it. Amazon S3 returns this error in all AWS Regions except in the US East (N. Virginia) Region (us-east-1). For legacy compatibility, if you re-create an existing bucket that you already own in us-east-1, Amazon S3 returns 200 OK and resets the bucket access control lists (ACLs). For Amazon S3 on Outposts, the bucket that you tried to create already exists in your Outpost and you own it. 
  - **HTTP status code:** `409 Conflict` (in all Regions except us-east-1)

- **`BucketHasAccessPointsAttached`**
  - **Description:** The bucket you tried to delete has access points attached. Delete your access points before deleting your bucket.
  - **HTTP status code:** 400 Bad Request

- **`BucketNotEmpty`**
  - **Description:** The bucket that you tried to delete is not empty.
  - **HTTP status code:** 409 Conflict

- **`ClientTokenConflict`**
  - **Description:** Your Multi-Region Access Point idempotency token was already used for a different request.
  - **HTTP status code:** 409 Conflict

- **`ConnectionClosedByRequester`**
  - **Description:** Returned to the original caller when an error is encountered while reading the WriteGetObjectResponse body.
  - **HTTP status code:** 400 Bad Request

- **`ConditionalRequestConflict`**
  - **Description:** A conflicting operation occurred. If using PutObject you can retry the request. If using multipart upload you should initiate another CreateMultipartUpload request and re-upload each part.
  - **HTTP status code:** 409 Conflict

- **`CredentialsNotSupported`**
  - **Description:** This request does not support credentials.
  - **HTTP status code:** 400 Bad Request

- **`CrossLocationLoggingProhibited`**
  - **Description:** Cross-Region logging is not allowed. Buckets in one AWS Region cannot log information to a bucket in another Region.
  - **HTTP status code:** 403 Forbidden

- **`DeviceNotActiveError`**
  - **Description:** The device is not currently active.
  - **HTTP status code:** 400 Bad Request

- **`EndpointNotFound`**
  - **Description:** Direct requests to the correct endpoint.
  - **HTTP status code:** 400 Bad Request

- **`EntityTooSmall`**
  - **Description:** Your proposed upload is smaller than the minimum allowed object size.
  - **HTTP status code:** 400 Bad Request

- **`EntityTooLarge`**
  - **Description:** Your proposed upload exceeds the maximum allowed object size. For more information, see [Amazon Simple Storage Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html) in the AWS General Reference. / **HTTP status code:** 400 Bad Request
  - **Description:** Your proposed download exceeds the maximum allowed size.  / **HTTP status code:** 405 Method Not Allowed

- **`ExpiredToken`**
  - **Description:** The provided token has expired.
  - **HTTP status code:** 400 Bad Request

- **`IllegalLocationConstraintException`**
  - **Description:** This error might occur for the following reasons:+  You are trying to access a bucket from a different Region than where the bucket exists. <br />+  You attempt to create a bucket with a location constraint that corresponds to a different region than the regional endpoint the request was sent to. 
  - **HTTP status code:** 400 Bad Request

- **`IllegalVersioningConfigurationException` **
  - **Description:** The versioning configuration specified in the request is not valid.
  - **HTTP status code:** 400 Bad Request

- **`IncompleteBody`**
  - **Description:** You did not provide the number of bytes specified by the Content-Length HTTP header.
  - **HTTP status code:** 400 Bad Request

- **`IncorrectEndpoint`**
  - **Description:** The specified bucket exists in another Region. Direct requests to the correct endpoint.
  - **HTTP status code:** 400 Bad Request

- **`IncorrectNumberOfFilesInPostRequest`**
  - **Description:** POST requires exactly one file upload per request.
  - **HTTP status code:** 400 Bad Request

- **`InlineDataTooLarge`**
  - **Description:** The inline data exceeds the maximum allowed size.
  - **HTTP status code:** 400 Bad Request

- **`InternalError`**
  - **Description:** An internal error occurred. Try again.
  - **HTTP status code:** 500 Internal Server Error

- **`InvalidAccessKeyId`**
  - **Description:** The AWS access key ID that you provided does not exist in our records.
  - **HTTP status code:** 403 Forbidden

- **`InvalidAccessPoint`**
  - **Description:** The specified access point name or account is not valid.
  - **HTTP status code:** 400 Bad Request

- **`InvalidAccessPointAliasError`**
  - **Description:** The specified access point alias name is not valid.
  - **HTTP status code:** 400 Bad Request

- **`InvalidAddressingHeader`**
  - **Description:** You must specify the Anonymous role.
  - **HTTP status code:** N/A

- **`InvalidArgument`**
  - **Description:** This error might occur for the following reasons:+  A ListBuckets request is made to a Regional endpoint that is different from the Region specified in the `bucket-region` parameter. <br />+  The specified argument was not valid. <br />+  The request was missing a required header. <br />+  The specified argument was incomplete or in the wrong format. <br />+  The specified argument must have a length greater than or equal to 3. 
  - **HTTP status code:** 400 Bad Request

- **`InvalidBucketAclWithObjectOwnership`**
  - **Description:** Bucket cannot have ACLs set with ObjectOwnership's BucketOwnerEnforced setting.
  - **HTTP status code:** 400 Bad Request

- **`InvalidBucketName`**
  - **Description:** The specified bucket is not valid.
  - **HTTP status code:** 400 Bad Request

- **`InvalidBucketOwnerAWSAccountID`**
  - **Description:** The value of the expected bucket owner parameter must be an AWS account ID.
  - **HTTP status code:** 400 Bad Request

- **`InvalidBucketState`**
  - **Description:** The request is not valid for the current state of the bucket.
  - **HTTP status code:** 409 Conflict

- **`InvalidDigest`**
  - **Description:** The Content-MD5 or checksum value that you specified is not valid.
  - **HTTP status code:** 400 Bad Request

- **`InvalidEncryptionAlgorithmError`**
  - **Description:** The encryption request that you specified is not valid. The valid value is AES256.
  - **HTTP status code:** 400 Bad Request

- **`InvalidHostHeader`**
  - **Description:** The host headers provided in the request used the incorrect style addressing.
  - **HTTP status code:** 400 Bad Request

- **`InvalidHttpMethod`**
  - **Description:** The request is made using an unexpected HTTP method.
  - **HTTP status code:** 400 Bad Request

- **`InvalidLocationConstraint`**
  - **Description:** The specified location (Region) constraint is not valid. For more information about selecting a Region for your buckets, see [Buckets overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html#access-bucket-intro). 
  - **HTTP status code:** 400 Bad Request

- **`InvalidObjectState`**
  - **Description:** The operation is not valid for the current state of the object.
  - **HTTP status code:** 403 Forbidden

- **`InvalidPart`**
  - **Description:** One or more of the specified parts could not be found. The part might not have been uploaded, or the specified entity tag might not have matched the part's entity tag.
  - **HTTP status code:** 400 Bad Request

- **`InvalidPartOrder`**
  - **Description:** The list of parts was not in ascending order. The parts list must be specified in order by part number.
  - **HTTP status code:** 400 Bad Request

- **`InvalidPayer`**
  - **Description:** All access to this object has been disabled. For further assistance, see [Contact Us](https://aws.amazon.com/contact-us/).
  - **HTTP status code:** 403 Forbidden

- **`InvalidPolicyDocument`**
  - **Description:** The content of the form does not meet the conditions specified in the policy document.
  - **HTTP status code:** 400 Bad Request

- **InvalidRange**
  - **Description:** The requested range cannot be satisfied.
  - **HTTP status code:** 416 Requested Range Not Satisfiable

- **InvalidRegion**
  - **Description:** You've attempted to create a Multi-Region Access Point in a Region that you haven't opted in to.
  - **HTTP status code:** 403 Forbidden

- **`InvalidRequest`**
  - **Description:** This error might occur for the following reasons:+  An unpaginated ListBuckets request is made from an account that has an approved general purpose bucket quota higher than 10,000. You must make paginated requests to list the buckets in an account with more than 10,000 buckets. <br />+  The request is using the wrong signature version. Use `AWS4-HMAC-SHA256` (Signature Version 4). <br />+  An access point can be created only for an existing bucket. <br />+  The access point is not in a state where it can be deleted. <br />+  An access point can be listed only for an existing bucket. <br />+  The next token is not valid. <br />+  At least one action must be specified in a lifecycle rule. <br />+  At least one lifecycle rule must be specified. <br />+  The number of lifecycle rules must not exceed the allowed limit of 1000 rules. <br />+  The range for the `MaxResults` parameter is not valid. <br />+  Amazon S3 Transfer Acceleration is not supported for buckets with non-DNS compliant names. <br />+  Amazon S3 Transfer Acceleration is not supported for buckets with periods (.) in their names. <br />+  The Amazon S3 Transfer Acceleration endpoint supports only virtual style requests. <br />+  Amazon S3 Transfer Acceleration is not configured on this bucket. <br />+  Amazon S3 Transfer Acceleration is disabled on this bucket. <br />+  Amazon S3 Transfer Acceleration is not supported on this bucket. For assistance, contact [Support](https://aws.amazon.com/contact-us/). <br />+  Amazon S3 Transfer Acceleration cannot be enabled on this bucket. For assistance, contact [Support](https://aws.amazon.com/contact-us/). <br />+   Conflicting values provided in HTTP headers and query parameters.  <br />+   Conflicting values provided in HTTP headers and POST form fields.  <br />+  CopyObject request made on objects larger than 5GB in size. 
  - **HTTP status code:** 400 Bad Request

- **`InvalidSessionException`**
  - **Description:** Returned if the session doesn't exist anymore because it timed out or expired.
  - **HTTP status code:** 400 Bad Request

- **`InvalidSignature`**
  - **Description:** The request signature that the server calculated does not match the signature that you provided. Check your AWS secret access key and signing method. For more information, see [Signing and authenticating REST requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RESTAuthentication.html).
  - **HTTP status code:** 400 Bad Request

- **`InvalidSecurity`**
  - **Description:** The provided security credentials are not valid.
  - **HTTP status code:** 403 Forbidden

- **`InvalidStorageClass`**
  - **Description:** The storage class that you specified is not valid.
  - **HTTP status code:** 400 Bad Request

- **`InvalidTargetBucketForLogging`**
  - **Description:** The target bucket for logging either does not exist, is not owned by you, or does not have the appropriate grants for the log-delivery group. 
  - **HTTP status code:** 400 Bad Request

- **`InvalidToken`**
  - **Description:** The provided token is malformed or otherwise not valid.
  - **HTTP status code:** 400 Bad Request

- **`InvalidURI`**
  - **Description:** The specified URI couldn't be parsed.
  - **HTTP status code:** 400 Bad Request

- **`KeyTooLongError`**
  - **Description:** Your key is too long.
  - **HTTP status code:** 400 Bad Request

- **`KMS.DisabledException`**
  - **Description:** The request was rejected because the specified KMS key is not enabled.
  - **HTTP status code:** 400 Bad Request

- **`KMS.InvalidKeyUsageException`**
  - **Description:** The request was rejected for one of the following reasons: + The KeyUsage value of the KMS key is incompatible with the API operation. <br />+ The encryption algorithm or signing algorithm specified for the operation is incompatible with the type of key material in the KMS key (KeySpec). For encrypting, decrypting, re-encrypting, and generating data keys, the KeyUsage must be ENCRYPT\_DECRYPT. For signing and verifying messages, the KeyUsage must be SIGN\_VERIFY. For generating and verifying message authentication codes (MACs), the KeyUsage must be GENERATE\_VERIFY\_MAC. For deriving key agreement secrets, the KeyUsage must be KEY\_AGREEMENT. To find the KeyUsage of a KMS key, use the DescribeKey operation.  To find the encryption or signing algorithms supported for a particular KMS key, use the DescribeKey operation.
  - **HTTP status code:** 400 Bad Request

- **`KMS.KMSInvalidStateException`**
  - **Description:** The request was rejected because the state of the specified resource is not valid for this request. This exception means one of the following: + The key state of the KMS key is not compatible with the operation.<br />To find the key state, use the DescribeKey operation. For more information about which key states are compatible with each KMS operation, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the *AWS Key Management Service Developer Guide*. <br />+ For cryptographic operations on KMS keys in custom key stores, this exception represents a general failure with many possible causes. To identify the cause, see the error message that accompanies the exception. 
  - **HTTP status code:** 400 Bad Request

- **`KMS.NotFoundException`**
  - **Description:** The request was rejected because the specified entity or resource could not be found.
  - **HTTP status code:** 400 Bad Request

- **`MalformedACLError`**
  - **Description:** The ACL that you provided was not well formed or did not validate against our published schema.
  - **HTTP status code:** 400 Bad Request

- **`MalformedPOSTRequest` **
  - **Description:** The body of your POST request is not well-formed multipart/form-data.
  - **HTTP status code:** 400 Bad Request

- **`MalformedXML`**
  - **Description:** The XML that you provided was not well formed or did not validate against our published schema.
  - **HTTP status code:** 400 Bad Request

- **`MaxMessageLengthExceeded`**
  - **Description:** Your request was too large.
  - **HTTP status code:** 400 Bad Request

- **`MaxPostPreDataLengthExceededError`**
  - **Description:** Your POST request fields preceding the upload file were too large.
  - **HTTP status code:** 400 Bad Request

- **`MetadataTooLarge`**
  - **Description:** Your metadata headers exceed the maximum allowed metadata size.
  - **HTTP status code:** 400 Bad Request

- **`MethodNotAllowed`**
  - **Description:** The specified method is not allowed against this resource.
  - **HTTP status code:** 405 Method Not Allowed

- **`MissingAuthenticationToken`**
  - **Description:** The request was not signed.  
  - **HTTP status code:** 403 Forbidden

- **`MissingContentLength`**
  - **Description:** You must provide the Content-Length HTTP header.
  - **HTTP status code:** 411 Length Required

- **`MissingRequestBodyError`**
  - **Description:** You sent an empty XML document as a request. 
  - **HTTP status code:** 400 Bad Request

- **`MissingSecurityHeader`**
  - **Description:** Your request is missing a required header.
  - **HTTP status code:** 400 Bad Request

- **`NoLoggingStatusForKey`**
  - **Description:** There is no such thing as a logging status subresource for a key.
  - **HTTP status code:** 400 Bad Request

- **`NoSuchAsyncRequest`**
  - **Description:** The specified request was not found.
  - **HTTP status code:** 404 Not Found

- **`NoSuchBucket`**
  - **Description:** The specified bucket does not exist.
  - **HTTP status code:** 404 Not Found

- **`NoSuchBucketPolicy`**
  - **Description:** The specified bucket does not have a bucket policy.
  - **HTTP status code:** 404 Not Found

- **`NoSuchCORSConfiguration`**
  - **Description:** The specified bucket does not have a CORS configuration.
  - **HTTP status code:** 404 Not Found

- **`NoSuchKey`**
  - **Description:** The specified key does not exist.
  - **HTTP status code:** 404 Not Found

- **`NoSuchLifecycleConfiguration`**
  - **Description:** The specified lifecycle configuration does not exist. 
  - **HTTP status code:** 404 Not Found

- **`NoSuchMultiRegionAccessPoint`**
  - **Description:** The specified Multi-Region Access Point does not exist.
  - **HTTP status code:** 404 Not Found

- **`NoSuchObjectLockConfiguration`**
  - **Description:** The specified object does not have an ObjectLock configuration.
  - **HTTP status code:** 404 Not Found

- **`NoSuchWebsiteConfiguration`**
  - **Description:** The specified bucket does not have a website configuration.
  - **HTTP status code:** 404 Not Found

- **`NoSuchTagSet`**
  - **Description:** The specified tag does not exist.
  - **HTTP status code:** 404 Not Found

- **`NoSuchUpload`**
  - **Description:** The specified multipart upload does not exist. The upload ID might not be valid, or the multipart upload might have been aborted or completed.
  - **HTTP status code:** 404 Not Found

- **`NoSuchVersion` **
  - **Description:** The version ID specified in the request does not match an existing version.
  - **HTTP status code:** 404 Not Found

- **`NotDeviceOwnerError`**
  - **Description:** The device that generated the token is not owned by the authenticated user.
  - **HTTP status code:** 400 Bad Request

- **`NotImplemented`**
  - **Description:** A header that you provided implies functionality that is not implemented.
  - **HTTP status code:** 501 Not Implemented

- **`NotModified`**
  - **Description:** The resource was not changed.
  - **HTTP status code:** 304 Not Modified

- **`NoTransformationDefined`**
  - **Description:** No transformation found for this Object Lambda Access Point.
  - **HTTP status code:** 404 Not Found

- **`NotSignedUp`**
  - **Description:** Your account is not signed up for the Amazon S3 service. You must sign up before you can use Amazon S3. You can sign up at the following URL: [https://aws.amazon.com/s3](https://aws.amazon.com/s3/) 
  - **HTTP status code:** 403 Forbidden

- **`ObjectLockConfigurationNotFoundError`**
  - **Description:** The Object Lock configuration does not exist for this bucket.
  - **HTTP status code:** 404 Not Found

- **`OwnershipControlsNotFoundError`**
  - **Description:** The bucket ownership controls were not found.
  - **HTTP status code:** 404 Not Found

- **`OperationAborted`**
  - **Description:** A conflicting conditional operation is currently in progress against this resource. Try again.
  - **HTTP status code:** 409 Conflict

- **`PermanentRedirect`**
  - **Description:** The bucket that you are attempting to access must be addressed using the specified endpoint. Send all future requests to this endpoint.
  - **HTTP status code:** 301 Moved Permanently

- **`PermanentRedirectControlError`**
  - **Description:** The API operation you are attempting to access must be addressed using the specified endpoint. Send all future requests to this endpoint.
  - **HTTP status code:** 301 Moved Permanently

- **`PreconditionFailed`**
  - **Description:** At least one of the preconditions that you specified did not hold.
  - **HTTP status code:** 412 Precondition Failed

- **`Redirect`**
  - **Description:** Temporary redirect. You are being redirected to the bucket while the Domain Name System (DNS) server is being updated.
  - **HTTP status code:** 307 Temporary Redirect

- **`RequestHeaderSectionTooLarge`**
  - **Description:** The request header and query parameters used to make the request exceed the maximum allowed size.
  - **HTTP status code:** 400 Bad Request

- **`RequestIsNotMultiPartContent`**
  - **Description:** A bucket POST request must be of the enclosure-type multipart/form-data.
  - **HTTP status code:** 412 Precondition Failed

- **`RequestTimeout`**
  - **Description:** Your socket connection to the server was not read from or written to within the timeout period.
  - **HTTP status code:** 400 Bad Request

- **`RequestTimeTooSkewed`**
  - **Description:** The difference between the request time and the server's time is too large.
  - **HTTP status code:** 403 Forbidden

- **`RequestTorrentOfBucketError`**
  - **Description:** Requesting the torrent file of a bucket is not permitted.
  - **HTTP status code:** 400 Bad Request

- **`ResponseInterrupted`**
  - **Description:** Returned to the original caller when an error is encountered while reading the WriteGetObjectResponse body. 
  - **HTTP status code:** 400 Bad Request

- **`RestoreAlreadyInProgress`**
  - **Description:** The object restore is already in progress.
  - **HTTP status code:** 409 Conflict

- **`ServerSideEncryptionConfigurationNotFoundError`**
  - **Description:** The server-side encryption configuration was not found.
  - **HTTP status code:** 400 Bad Request

- **`ServiceUnavailable`**
  - **Description:** Service is unable to handle request.
  - **HTTP status code:** 503 Service Unavailable

- **`SignatureDoesNotMatch`**
  - **Description:** The request signature that the server calculated does not match the signature that you provided. Check your AWS secret access key and signing method. For more information, see [REST Authentication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RESTAuthentication.html).
  - **HTTP status code:** 403 Forbidden

- **`SlowDown`**
  - **Description:** Please reduce your request rate.
  - **HTTP status code:** 503 Slow Down

- **`503 SlowDown`**
  - **Description:** Slow Down
  - **HTTP status code:** 503 Slow Down

- **`TagPolicyException`**
  - **Description:** The tag policy does not allow the specified value for the following tag key.
  - **HTTP status code:** 400 Bad Request

- **`TemporaryRedirect`**
  - **Description:** You are being redirected to the bucket while the Domain Name System (DNS) server is being updated.
  - **HTTP status code:** 307 Temporary Redirect

- **`TokenCodeInvalidError`**
  - **Description:** The serial number and/or token code you provided is not valid.
  - **HTTP status code:** 400 Bad Request

- **`TokenRefreshRequired`**
  - **Description:** The provided token must be refreshed.
  - **HTTP status code:** 400 Bad Request

- **`TooManyAccessPoints`**
  - **Description:** You have attempted to create more access points than are allowed for an account. For more information, see [Amazon Simple Storage Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html) in the AWS General Reference.
  - **HTTP status code:** 400 Bad Request

- **`TooManyBuckets`**
  - **Description:** You have attempted to create more buckets than are allowed for an account. For more information, see [Amazon Simple Storage Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html) in the AWS General Reference.
  - **HTTP status code:** 400 Bad Request

- **`TooManyMultiRegionAccessPointregionsError`**
  - **Description:** You have attempted to create a Multi-Region Access Point with more Regions than are allowed for an account. For more information, see [Amazon Simple Storage Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html) in the AWS General Reference.
  - **HTTP status code:** 400 Bad Request

- **`TooManyMultiRegionAccessPoints`**
  - **Description:** You have attempted to create more Multi-Region Access Points than are allowed for an account. For more information, see [Amazon Simple Storage Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html) in the AWS General Reference.
  - **HTTP status code:** 400 Bad Request

- **`UnauthorizedAccessError`**
  - **Description:** Applicable in China Regions only. Returned when a request is made to a bucket that doesn't have an ICP license. For more information, see [ICP Recordal](https://www.amazonaws.cn/en/support/icp/).
  - **HTTP status code:** 403 Forbidden

- **`UnexpectedContent`**
  - **Description:** This request contains unsupported content.
  - **HTTP status code:** 400 Bad Request

- **`UnexpectedIPError`**
  - **Description:** Applicable in China Regions only. This request was rejected because the IP was unexpected. 
  - **HTTP status code:** 403 Forbidden

- **`UnsupportedArgument`**
  - **Description:** The request contained an unsupported argument.
  - **HTTP status code:** 400 Bad Request

- **`UnsupportedSignature`**
  - **Description:** The provided request is signed with an unsupported STS Token version or the signature version is not supported.
  - **HTTP status code:** 400 Bad Request

- **`UnresolvableGrantByEmailAddress`**
  - **Description:** The email address that you provided does not match any account on record.
  - **HTTP status code:** 400 Bad Request

- **`UserKeyMustBeSpecified`**
  - **Description:** The bucket POST request must contain the specified field name. If it is specified, check the order of the fields.
  - **HTTP status code:** 400 Bad Request

- **`NoSuchAccessPoint`**
  - **Description:** The specified access point does not exist.
  - **HTTP status code:** 404 Not Found

- **`InvalidTag`**
  - **Description:** Your request contains tag input that is not valid. For example, your request might contain duplicate keys, keys or values that are too long, or system tags.
  - **HTTP status code:** 400 Bad Request

- **`MalformedPolicy`**
  - **Description:** Your policy contains a principal that is not valid.
  - **HTTP status code:** 400 Bad Request



## List of SELECT Object Content Error Codes
<a name="SelectObjectContentErrorCodeList"></a>

**Important**  
Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can continue to use the feature as usual. [Learn more](https://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/)

The following table contains special errors that `SELECT Object Content` might return. For general information about Amazon S3 errors and a list of error codes, see [Error responses](#ErrorResponses).


| Error code | Description | HTTP status code | 
| --- | --- | --- | 
| AmbiguousFieldName | The field name matches to multiple fields in the file. Check the SQL expression and the file, and try again. | 400 | 
| Busy | The service is unavailable. Try again later. | 503 | 
| CastFailed | An attempt to convert from one data type to another using CAST failed in the SQL expression. | 400 | 
| ColumnTooLong | The length of a column in the result is greater than maxCharsPerColumn of 1 MB. | 400 | 
| CSVEscapingRecordDelimiter | A quoted record delimiter was found in the file. To allow quoted record delimiters, set AllowQuotedRecordDelimiter to 'TRUE'. | 400 | 
| CSVParsingError | An error occurred while parsing the CSV file. Check the file and try again. | 400 | 
| CSVUnescapedQuote | An unescaped quote was found while parsing the CSV file. To allow quoted record delimiters, set AllowQuotedRecordDelimiter to 'TRUE'. | 400 | 
| EmptyRequestBody | The request body cannot be empty. | 400 | 
| EvaluatorBindingDoesNotExist | A column name or a path provided does not exist in the SQL expression. | 400 | 
| EvaluatorInvalidArguments | There is an incorrect number of arguments in the function call in the SQL expression. | 400 | 
| EvaluatorInvalidTimestampFormatPattern | The timestamp format string in the SQL expression is not valid. | 400 | 
| EvaluatorInvalidTimestampFormatPatternSymbol | The timestamp format pattern contains a symbol in the SQL expression that is not valid. | 400 | 
| EvaluatorInvalidTimestampFormatPatternSymbolForParsing | The timestamp format pattern contains a valid format symbol that cannot be applied to timestamp parsing in the SQL expression. | 400 | 
| EvaluatorInvalidTimestampFormatPatternToken | The timestamp format pattern contains a token in the SQL expression that is not valid. | 400 | 
| EvaluatorLikePatternInvalidEscapeSequence | An argument given to the LIKE expression was not valid. | 400 | 
| EvaluatorNegativeLimit | LIMIT must not be negative. | 400 | 
| EvaluatorTimestampFormatPatternDuplicateFields | The timestamp format pattern contains multiple format specifiers representing the timestamp field in the SQL expression. | 400 | 
| EvaluatorTimestampFormatPatternHourClockAmPmMismatch | The timestamp format pattern contains a 12-hour hour of day format symbol but doesn't also contain an AM/PM field, or it contains a 24-hour hour of day format specifier and contains an AM/PM field in the SQL expression. | 400 | 
| EvaluatorUnterminatedTimestampFormatPatternToken | The timestamp format pattern contains an unterminated token in the SQL expression. | 400 | 
| ExpressionTooLong | The SQL expression is too long. The maximum byte-length for an SQL expression is 256 KB. | 400 | 
| ExternalEvalException | The query cannot be evaluated. Check the file and try again. | 400 | 
| IllegalSqlFunctionArgument | An illegal argument was used in the SQL function. | 400 | 
| IncorrectSqlFunctionArgumentType | An incorrect argument type was specified in a function call in the SQL expression. | 400 | 
| IntegerOverflow | An integer overflow or underflow occurred in the SQL expression. | 400 | 
| InternalError | An internal error occurred. | 500 | 
| InvalidCast | An attempt to convert from one data type to another using CAST failed in the SQL expression. | 400 | 
| InvalidColumnIndex | The column index in the SQL expression is not valid. | 400 | 
| InvalidCompressionFormat | The file is not in a supported compression format. Only GZIP and BZIP2 are supported. | 400 | 
| InvalidDataSource | The data source type is not valid. Only CSV, JSON, and Parquet are supported. | 400 | 
| InvalidDataType | The SQL expression contains a data type that is not valid. | 400 | 
| InvalidExpressionType | The ExpressionType value is not valid. Only SQL expressions are supported. | 400 | 
| InvalidFileHeaderInfo | The FileHeaderInfo value is not valid. Only NONE, USE, and IGNORE are supported. | 400 | 
| InvalidJsonType | The JsonType value is not valid. Only DOCUMENT and LINES are supported. | 400 | 
| InvalidKeyPath | The key path in the SQL expression is not valid. | 400 | 
| InvalidQuoteFields | The QuoteFields value is not valid. Only ALWAYS and ASNEEDED are supported. | 400 | 
| InvalidRequestParameter | The value of a parameter in the SelectRequest element is not valid. Check the service API documentation and try again. | 400 | 
| InvalidScanRange | The provided scan range is not valid. | 400 | 
| InvalidTableAlias | The SQL expression contains a table alias that is not valid. | 400 | 
| InvalidTextEncoding | The encoding type is not valid. Only UTF-8 encoding is supported. | 400 | 
| JSONParsingError | An error occurred while parsing the JSON file. Check the file and try again. | 400 | 
| LexerInvalidChar | The SQL expression contains a character that is not valid. | 400 | 
| LexerInvalidIONLiteral | The SQL expression contains an operator that is not valid. | 400 | 
| LexerInvalidLiteral | The SQL expression contains an operator that is not valid. | 400 | 
| LexerInvalidOperator | The SQL expression contains a literal that is not valid. | 400 | 
| LikeInvalidInputs | The argument given to the LIKE clause in the SQL expression is not valid. | 400 | 
| MalformedXML |  The XML provided was not well formed or did not validate against our published schema. Check the service documentation and try again. | 400 | 
| MaxOperatorsExceeded | Failed to parse SQL expression, try reducing complexity. For example, reduce number of operators used. | 400 | 
| MethodNotAllowed | The specified method is not allowed against this resource. | 405 Method Not Allowed | 
| MissingRequiredParameter | The SelectRequest entity is missing a required parameter. Check the service documentation and try again. | 400 | 
| MultipleDataSourcesUnsupported | Multiple data sources are not supported. | 400 | 
| NumberFormatError | An error occurred while parsing a number. This error can be caused by underflow or overflow of integers. | 400 | 
| ObjectSerializationConflict | InputSerialization specifies more than one format (CSV, JSON, or Parquet), or OutputSerialization specifies more than one format (CSV or JSON). For InputSerialization and OutputSerialization, you can specify only one format for each. | 400 | 
| OverMaxColumn | The number of columns in the result is greater than the maximum allowable number of columns. | 400 | 
| OverMaxParquetBlockSize | The Parquet file is above the max row group size. | 400 | 
| OverMaxRecordSize | The length of a record in the input or result is greater than the maxCharsPerRecord limit of 1 MB. | 400 | 
| ParquetParsingError | An error occurred while parsing the Parquet file. Check the file and try again. | 400 | 
| ParquetUnsupportedCompressionCodec | The specified Parquet compression codec is not supported. | 400 | 
| ParseAsteriskIsNotAloneInSelectList | Other expressions are not allowed in the SELECT list when \* is used without dot notation in the SQL expression. | 400 | 
| ParseCannotMixSqbAndWildcardInSelectList | Cannot mix [] and \* in the same expression in a SELECT list in the SQL expression. | 400 | 
| ParseCastArity | The SQL expression CAST has incorrect arity. | 400 | 
| ParseEmptySelect | The SQL expression contains an empty SELECT clause. | 400 | 
| ParseExpected2TokenTypes | The expected token in the SQL expression was not found. | 400 | 
| ParseExpectedArgumentDelimiter | The expected argument delimiter in the SQL expression was not found. | 400 | 
| ParseExpectedDatePart | The expected date part in the SQL expression was not found. | 400 | 
| ParseExpectedExpression | The expected SQL expression was not found. | 400 | 
| ParseExpectedIdentForAlias | The expected identifier for the alias in the SQL expression was not found. | 400 | 
| ParseExpectedIdentForAt | The expected identifier for AT name in the SQL expression was not found. | 400 | 
| ParseExpectedIdentForGroupName | GROUP is not supported in the SQL expression. | 400 | 
| ParseExpectedKeyword | The expected keyword in the SQL expression was not found. | 400 | 
| ParseExpectedLeftParenAfterCast | The expected left parenthesis after CAST in the SQL expression was not found. | 400 | 
| ParseExpectedLeftParenBuiltinFunctionCall | The expected left parenthesis in the SQL expression was not found. | 400 | 
| ParseExpectedLeftParenValueConstructor | The expected left parenthesis in the SQL expression was not found. | 400 | 
| ParseExpectedMember | The SQL expression contains an unsupported use of MEMBER. | 400 | 
| ParseExpectedNumber | The expected number in the SQL expression was not found. | 400 | 
| ParseExpectedRightParenBuiltinFunctionCall | The expected right parenthesis character in the SQL expression was not found. | 400 | 
| ParseExpectedTokenType | The expected token in the SQL expression was not found. | 400 | 
| ParseExpectedTypeName | The expected type name in the SQL expression was not found. | 400 | 
| ParseExpectedWhenClause | The expected WHEN clause in the SQL expression was not found. CASE is not supported. | 400 | 
| ParseInvalidContextForWildcardInSelectList | The use of \* in the SELECT list in the SQL expression is not valid. | 400 | 
| ParseInvalidPathComponent | The SQL expression contains a path component that is not valid. | 400 | 
| ParseInvalidTypeParam | The SQL expression contains a parameter value that is not valid. | 400 | 
| ParseMalformedJoin | JOIN is not supported in the SQL expression. | 400 | 
| ParseMissingIdentAfterAt | The expected identifier after the @ symbol in the SQL expression was not found. | 400 | 
| ParseNonUnaryAgregateFunctionCall | Only one argument is supported for aggregate functions in the SQL expression. | 400 | 
| ParseSelectMissingFrom | The SQL expression contains a missing FROM after the SELECT list. | 400 | 
| ParseUnExpectedKeyword | The SQL expression contains an unexpected keyword. | 400 | 
| ParseUnexpectedOperator | The SQL expression contains an unexpected operator. | 400 | 
| ParseUnexpectedTerm | The SQL expression contains an unexpected term. | 400 | 
| ParseUnexpectedToken | The SQL expression contains an unexpected token. | 400 | 
| ParseUnknownOperator | The SQL expression contains an operator that is not valid. | 400 | 
| ParseUnsupportedAlias | The SQL expression contains an unsupported use of ALIAS. | 400 | 
| ParseUnsupportedCallWithStar | Only COUNT with (\*) as a parameter is supported in the SQL expression. | 400 | 
| ParseUnsupportedCase | The SQL expression contains an unsupported use of CASE. | 400 | 
| ParseUnsupportedCaseClause | The SQL expression contains an unsupported use of CASE. | 400 | 
| ParseUnsupportedLiteralsGroupBy | The SQL expression contains an unsupported use of GROUP BY. | 400 | 
| ParseUnsupportedSelect | The SQL expression contains an unsupported use of SELECT. | 400 | 
| ParseUnsupportedSyntax | The SQL expression contains unsupported syntax. | 400 | 
| ParseUnsupportedToken | The SQL expression contains an unsupported token. | 400 | 
| TruncatedInput | Object decompression failed. Check that the object is properly compressed using the format specified in the request. | 400 | 
| UnauthorizedAccess | You are not authorized to perform this operation. | 401 | 
| UnrecognizedFormatException | The record type is not valid. | 400 | 
| UnsupportedFunction | S3 encountered an unsupported SQL function. | 400 | 
| UnsupportedParquetType | The specified Parquet type is not supported. | 400 | 
| UnsupportedRangeHeader | A range header is not supported for this operation. | 400 | 
| UnsupportedScanRangeInput | Scan range queries are not supported on this type of object. | 400 | 
| UnsupportedSqlOperation | S3 encountered an unsupported SQL operation. | 400 | 
| UnsupportedSqlStructure | S3 encountered an unsupported SQL structure. Check the SQL Reference. | 400 | 
| UnsupportedStorageClass | The storage class is not supported. Only STANDARD, STANDARD\_IA, and ONEZONE\_IA storage classes are supported. | 400 | 
| UnsupportedSyntax | The syntax is not valid. | 400 | 
| UnsupportedTypeForQuerying | Your query contains an unsupported type for comparison (e.g. verifying that a Parquet INT96 column type is greater than 0). | 400 | 
| ValueParseFailure | A timestamp parse failure occurred in the SQL expression. | 400 | 

## List of Replication-related error codes
<a name="ReplicationErrorCodeList"></a>

The following table contains special errors that the `Replication` operation might return. For general information about Amazon S3 errors and a list of error codes, see [Error responses](#ErrorResponses).


| Error code | Description | HTTP status code | 
| --- | --- | --- | 
| InvalidArgument | This error might occur for the following reasons:+  The `<Account>` element is empty. It must contain a valid account ID. <br />+  The AWS account specified in the `<Account>` element must match the destination bucket owner. <br />+  `ReplicationTime-Status` must contain a value. <br />+  `ReplicationTime-ReplicationTimeValue` must contain a value. <br />+  `Replication-ReplicationTimeValue-Minutes` value must be 15. <br />+  `ReplicationMetrics` must contain a `Status`. <br />+  `ReplicationMetrics` must contain an `EventThreshold`. <br />+  `EventThreshold-ReplicationTimeValue-Minutes` value must be 15. <br />+  `Rule ID` must not contain non-ASCII characters.  | 400 | 
| InvalidRequest | This error might occur for the following reasons:+  The `<Owner>` in `<AccessControlTranslation>` has a value, so the `<Account>` element must be specified.  <br />+  The `<Account>` element is empty. It must contain a valid account ID. <br />+  The replication `destination` must contain both `ReplicationTime` and `Metrics`, or neither. <br />+  `ReplicationTime` and `ReplicationMetrics` must have the same status. <br />+  S3 Replication Time Control (S3 RTC) is not supported in this AWS Region.  | 400 | 
| ReplicationConfigurationNotFoundError | There is no replication configuration for this bucket. | 404 Not Found | 

## List of Tagging-related error codes
<a name="S3TaggingErrorCodeList"></a>

The following table contains special errors that the `TagResource`, `UntagResource`, and `ListTagsForResource` operations might return for Storage Lens groups. For general information about general Amazon S3 errors and a list of error codes, see [Error responses](#ErrorResponses).


| Error Code | Description | HTTP Status Code | 
| --- | --- | --- | 
| InvalidRequest | The AWS Region in the resource ARN doesn't match the Region that's specified in this request. The AWS account in the resource ARN doesn't match the account ID that's specified in this request. The AWS partition in the resourceArn is invalid. | 400 Bad Request | 
| InvalidTag | This request contains a tag key or value that isn't valid. Valid characters include the following: `[a-zA-Z+-=._:/]`. Tag keys can contain up to 128 characters. Tag values can contain up to 256 characters. There are duplicate tag keys in your request. User-defined tag keys can't start with `aws:`. | 400 Bad Request | 
| NoSuchResource | The specified resource doesn't exist. | 404 Not Found | 
| TagPolicyException | The tag policy does not allow the specified value for the following tag key. | 400 Bad Request | 
| TooManyTags | The number of tags exceeds the limit of 50 tags. | 400 Bad Request | 

## List of Amazon S3 annotation-related error codes
<a name="S3AnnotationErrorCodeList"></a>

The following table contains special errors that annotation operations (`PutObjectAnnotation`, `GetObjectAnnotation`, `ListObjectAnnotations`, `DeleteObjectAnnotation`, `UpdateBucketMetadataAnnotationTableConfiguration`) and annotation-related `CopyObject` behavior might return. For general information about Amazon S3 errors and a list of error codes, see [Error responses](#ErrorResponses).


| Error Code | Description | HTTP Status Code | 
| --- | --- | --- | 
| AccessDenied | Access Denied. The caller does not have permission to perform the requested annotation operation, or the object is protected by Object Lock in COMPLIANCE mode. | 403 Forbidden | 
| AnnotationLimitExceeded | The object annotation count exceeds the limit (1000). | 400 Bad Request | 
| AnnotationNameTooLong | Your annotation name is too long. Annotation names can be up to 512 bytes in length. | 400 Bad Request | 
| AnnotationRequestConflict | A conflicting operation is currently in progress against this annotation. This can occur when a source annotation is deleted during a cross-Region copy. | 409 Conflict | 
| EntityTooSmall | Your proposed upload is smaller than the minimum allowed size. The annotation payload must be at least 1 byte. | 400 Bad Request | 
| InvalidAnnotationName | Your annotation name contains invalid characters, or the name starts with a reserved prefix (`aws` or `s3`, case-insensitive). Annotation names can contain only Unicode letters, numbers, underscore (`_`), period (`.`), and hyphen (`-`). | 400 Bad Request | 
| InvalidArgument | The annotation directive is not valid. Valid values are `COPY` and `EXCLUDE`. For `ListObjectAnnotations`, `max-annotation-results` must be between 1 and 1000. | 400 Bad Request | 
| InvalidPrefix | The annotation prefix you have provided is not valid. | 400 Bad Request | 
| InvalidRequest | This error might occur for the following reasons: The object is encrypted with SSE-C, which does not support annotations. The source object has annotations that cannot be copied to the destination because the destination is in an unsupported Region. The annotation table configuration request is not valid (for example, disabling the table while specifying encryption, enabling a table that is already enabled, updating a table in CREATING status, or submitting an empty request). | 400 Bad Request | 
| MethodNotAllowed | The specified method is not allowed against this resource. For example, this error occurs when the request targets a delete marker. | 405 Method Not Allowed | 
| NoSuchAnnotation | The specified annotation does not exist. | 404 Not Found | 
| NoSuchKey | The specified key does not exist. | 404 Not Found | 
| NoSuchVersion | The version ID specified in the request does not match an existing version. | 404 Not Found | 
| NotImplemented | Annotations are not supported for Amazon S3 directory buckets. | 501 Not Implemented | 
| OperationAborted | A conflicting conditional operation is currently in progress against this resource. This can occur during concurrent modifications or when a source annotation count or ETag changes during a cross-Region copy. Try again. | 409 Conflict | 
| PreconditionFailed | At least one of the preconditions that you specified did not hold. The `x-amz-object-if-match` ETag does not match the current object ETag. | 412 Precondition Failed | 
| UnsupportedMediaType | The request payload contains an unsupported media type. The annotation payload must be valid UTF-8 encoded text. | 415 Unsupported Media Type | 
| UserAnnotationNameMustBeSpecified | You must specify a user annotation name. | 400 Bad Request | 

## List of Amazon S3 on Outposts error codes
<a name="S3OutpostsErrorCodeList"></a>

The following table contains special errors that an Amazon S3 on Outposts operation might return. For general information about Amazon S3 errors and a list of error codes, see [Error responses](#ErrorResponses).


| Error code | Description | HTTP status code | 
| --- | --- | --- | 
| BadRequest | The bucket is in a transitional state because of a previous deletion attempt. Try again later. | 400 Bad Request | 
| InvalidRequest | This error might occur for the following reasons:+  Amazon VPC configuration is required. <br />+  Public access is not allowed on S3 on Outposts access points.  | 400 Bad Request | 
| InvalidOutpostState | The request is not valid for the current state of the Outpost. | 409 Conflict | 
| InvalidRequest | The access point is not in a state where it can be deleted. | 400 Bad Request | 
| NoSuchOutpost | The specified Outpost does not exist. | 404 Not Found | 
| UnsupportedOperation | The specified action was not supported. | 404 Not Found | 
| InsufficientCapacity | Insufficient capacity. | 507 Insufficient Storage | 

## List of Amazon S3 Storage Lens error codes
<a name="S3LensErrorCodeList"></a>

The following table contains special errors that Amazon S3 Storage Lens operations might return. For general information about general Amazon S3 errors and a list of error codes, see [Error responses](#ErrorResponses).


| Error code | Description | HTTP status code | 
| --- | --- | --- | 
| AccessDenied | This Region is not supported as a home Region for S3 Storage Lens. | 403 Forbidden | 
| AccountNotAuthorized | This account not authorized to use AWS Organizations. Use your management account or delegated administrator account.  | 403 Forbidden | 
| ActivityMetricsMustEnabled | Activity metrics must be enabled. | 400 Bad Request | 
| AWSOrganizationsNotInUseException | This account is not part of your organization. | 403 Forbidden | 
| DefaultConfigurationDeleteForbidden | The Default configuration cannot be deleted. | 403 Forbidden | 
| DuplicateStorageLensGroupARN | There are two or more entries of the same Storage Lens group ARN in this configuration. | 400 Bad Request | 
| EmptyExcludeContainer | This error occurs for the following reasons:+  The exclude container cannot be empty. <br />+  The exclude container cannot have zero buckets. <br />+  The exclude container cannot have zero Regions.  | 400 Bad Request | 
| EmptyExcludeElement | You must specify a Storage Lens group with your Exclude element. | 400 Bad Request | 
| EmptyIncludeContainer | This error occurs for the following reasons:+  The include container cannot be empty. <br />+  The include container cannot have zero buckets. <br />+  The include container cannot have zero Regions.  | 400 Bad Request | 
| InvalidAWSOrgArn | There is a malformed AWS Organizations ARN in the configuration. | 400 Bad Request | 
| EmptyIncludeElement | You must specify a Storage Lens group with your Include element. | 400 Bad Request | 
| InvalidBucketFilter | Organization-level configurations do not support bucket filters. | 400 Bad Request | 
| InvalidConfigId | The configuration ID is not valid. | 400 Bad Request | 
| InvalidDestination | The S3 bucket ARN is malformed. | 400 Bad Request | 
| InvalidEncryptionMethod | Only one encryption method can be specified. | 400 Bad Request | 
| InvalidFilterForDefaultConfiguration | The default configuration must not include any filters. | 400 Bad Request | 
| InvalidIncludeExcludeContainers | You can specify either an Include container or an Exclude container in a configuration. You cannot specify both in a configuration. | 400 Bad Request | 
| InvalidIncludeExcludeElements | Only one Include or Exclude element is allowed. At least one Include or Exclude element must be present. | 400 Bad Request | 
| InvalidKMSEncryptionKeyId | The KMS key ID ARN is not valid. | 400 Bad Request | 
| InvalidMaximumPrefixDepth | `MaxDepth` must be within the range [1,10]. | 400 Bad Request | 
| InvalidMinimumStorageBytesPercentage | `MinStorageBytesPercentage` must be within the range [1.00,100.00]. | 400 Bad Request | 
| InvalidOrganizationARN | The AWS Organizations ARN in the configuration is not valid. | 400 Bad Request | 
| InvalidOrganizationForDefaultConfiguration | The default configuration does not support organization-level metrics. | 400 Bad Request | 
| InvalidRegionForDefaultConfiguration | The specified Region is not supported for default configuration. | 400 Bad Request | 
| InvalidRegionName | The Region name is not valid. | 400 Bad Request | 
| InvalidStorageLensArn | The S3 Storage Lens ARN is not required in input. | 400 Bad Request | 
| InvalidStorageLensGroupARN | This Storage Lens group ARN isn't valid or only Storage Lens groups in your account are allowed. Additionally, you must follow the Storage Lens group ARN structure: `arn::s3:::storage-lens-group/` and adhere to the 64 character limit. Storage Lens group names can also contain only the following characters: a-z, A-Z, 0-9, hyphens (-), and underscores (\_).  | 400 Bad Request | 
| MissingAccountLevelActivityMetrics | Activity metrics must be enabled at the account level when activity metrics are enabled at the bucket level. | 400 Bad Request | 
| MissingBucketLevelActivityMetrics | Activity metrics must be enabled at the bucket level when activity metrics are enabled at the account level. | 400 Bad Request | 
| MissingEncryptionMethod | The encryption method cannot be blank. Specify either `SSE-KMS` or `SSE-S3`. | 400 Bad Request | 
| MissingPrefixLevelStorageMetrics | Storage metrics at the prefix level are mandatory when the prefix level is enabled. | 400 Bad Request | 
| OrganizationAccessDenied | This account is not authorized to add AWS Organizations. | 403 Forbidden | 
| OrgConfigurationNotSupported | The specified Region does not support AWS Organizations in the configuration. | 403 Forbidden | 
| ServiceNotEnabledForOrg | The S3 Storage Lens service-linked role is not enabled for the organization. | 403 Forbidden | 
| StorageMetricsMustEnabled | Prefix-level storage metrics must be enabled. | 400 Bad Request | 
| TooManyBuckets | The buckets container cannot have more than 50 buckets. | 400 Bad Request | 
| TooManyRegions | The Regions container cannot have more than 50 Regions. | 400 Bad Request | 
| TooManyStorageLensGroups | You can't attach more than 50 Storage Lens groups to your Storage Lens dashboard. | 400 Bad Request | 

The following table contains special errors that S3 Storage Lens groups operations might return. For general information about general Amazon S3 errors and a list of error codes, see [Error responses](#ErrorResponses).


| Error code | Description | HTTP status code | 
| --- | --- | --- | 
| AccessDenied | You don't have permission to perform Storage Lens group actions. This Region is not supported as home Region for S3 Storage Lens groups. | 403 Forbidden | 
| ConfigurationAlreadyExists | The specified configuration already exists. | 409 Conflict | 
| DuplicateElement | Tags must be unique. The `And` logical operator includes duplicate tag keys. The `Or` logical operator includes duplicate tags. Logical operator includes duplicate prefixes or suffixes. | 400 Bad Request | 
| InvalidAge | `DaysLessThan` and `DaysGreaterThan` must be positive numbers. | 400 Bad Request | 
| InvalidFilter | A filter must include one of the following elements: `And`, `Or`, `MatchAnyTag`, `MatchAnyPrefix`, `MatchAnySuffix`, `MatchObjectAge`, `MatchObjectSize`. | 400 Bad Request | 
| InvalidLogicalOperator | At least two sub elements must be present in the logical operators `And` or `Or`. | 400 Bad Request | 
| InvalidMatchAnyPrefix | The `MatchAnyPrefix` parameter can't be empty. | 400 Bad Request | 
| InvalidMatchAnySuffix | The `MatchAnySuffix` parameter can't be empty. | 400 Bad Request | 
| InvalidMatchAnyTag | The `MatchAnyTag` parameter can't be empty. | 400 Bad Request | 
| InvalidMatchObjectAge | The `MatchObjectAge` parameter can't be empty. | 400 Bad Request | 
| InvalidMatchObjectSize | The `MatchObjectSize` parameter can't be empty. | 400 Bad Request | 
| InvalidName | Storage Lens group Name parameter must be between 1 and 64 characters. The Storage Lens group `Name` parameter must use the `^[a-zA-Z0-9\-_]+$` pattern. | 400 Bad Request | 
| InvalidNumericCombination | This object age or object size combination isn't valid. | 400 Bad Request | 
| InvalidPrefix | The maximum length of a prefix is 1,024 characters. The prefix string can't be empty. | 400 Bad Request | 
| InvalidSize | `BytesLessThan` and `BytesGreaterThan` must be positive numbers. The maximum object size can't exceed 50 TB. The minimum object size can't be greater than or equal to 50 TB. | 400 Bad Request | 
| InvalidSuffix | The maximum length of a suffix is 1,024 characters. The suffix string can't be empty. | 400 Bad Request | 
| InvalidTag | The object tag key can't exceed 128 characters. The object tag key string can't be null or empty. The maximum length of a tag value is 256 characters. The object tag key contains characters that aren't valid. The object tag key must contain only a-z, A-Z, 0-9, spaces, and the following characters: `^(_.:/=+\-@]*)$`. | 400 Bad Request | 
| MismatchedName | The name specified in the request doesn't match the Storage Lens group name. | 400 Bad Request | 
| TooManyConfigurations | You have attempted to create more Storage Lens group configurations than the 50 allowed. | 400 Bad Request | 
| TooManyElements | The `Element` exceeds the maximum number of elements allowed within a logical operator. Only 10 prefixes, suffixes, or tags are allowed.  | 400 Bad Request | 

## List of Amazon S3 Object Lambda error codes
<a name="S3ObjectLambdaErrorCodeList"></a>

The following table contains special errors that S3 Object Lambda might return. For information about general Amazon S3 errors and a list of error codes, see [Error responses](#ErrorResponses).

Error responses received from the supporting access points during non-`GetObject` requests are sent to the caller unaltered.


| Error code | Description | HTTP status code | 
| --- | --- | --- | 
| LambdaInvalidResponse | Returned to the original caller when `WriteGetObjectResponse` responds with `ValidationError` to AWS Lambda.<br />See the `ValidationError` message for more details. Not all cases of `ValidationError` result in a `LambdaInvalidResponse` error. | 400 Bad Request | 
| LambdaInvocationFailed | Lambda function invocation failed.<br />Callers might receive the following error when S3 Object Lambda is unable to successfully invoke the configured Lambda function.<br />The error message might contain details about an eventual error returned by the AWS Lambda service when invoking the function (for example, status code, error code, error message and request ID). | 400 Bad Request | 
| LambdaNotFound | The AWS Lambda function was not found.<br />The configured Lambda function, version, or alias was not found when attempting to invoke it. Ensure that the S3 Object Lambda Access Point configuration points to the correct Lambda function ARN.<br />The error message might contain details about an eventual error returned by the AWS Lambda service when invoking the function (for example, status code, error code, error message and request ID). | 404 Not Found | 
| LambdaPermissionError | The caller is not authorized to invoke the Lambda function.<br />The caller must have permission to invoke the Lambda function. Check the policies attached to the caller and ensure that they've been allowed to use `lambda:Invoke` for the configured function.<br />The error message might contain details about an eventual error returned by the AWS Lambda service when invoking the function (for example, status code, error code, error message and request ID). | 403 Forbidden | 
| LambdaResponseNotReceived | The Lambda function exited without successfully calling `WriteGetObjectResponse`.<br />`GetObject` response data is provided by the Lambda function by calling the `WriteGetObjectResponse` API operation. The Amazon CloudWatch logs for the function might provide more insight into why the function did not successfully call this API operation despite exiting normally. | 500 Internal Service Error | 
| LambdaRuntimeError | The Lambda function failed during execution.<br />An explicit error was received from the Lambda function. For details about the failure, check the AWS CloudFormation logs. | 500 Internal Service Error | 
| LambdaTimeout | The Lambda function did not respond in the allowed time.<br />The Lambda function failed to complete its call to `WriteGetObjectResponse` within 60 seconds. | 500 Internal Service Error | 
| SlowDown | Reduce your request rate for operations involving AWS Lambda.<br />The function invocation was throttled by AWS Lambda, perhaps because it has reached its configured concurrency limitation. For more information, see [Managing concurrency for a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html) in the *AWS Lambda Developer Guide*.<br />The error message might contain details about an eventual error returned by the AWS Lambda service when invoking the function (for example, status code, error code, error message and request ID). | 503 Slow Down | 
| ValidationError | Validation errors might be returned from the `WriteGetObjectResponse` API operation and can occur for numerous reasons. See the error message for more details. | 400 Bad Request | 

## List of Amazon S3 asynchronous error codes
<a name="S3AsynchronousErrorCodeList"></a>

The following table contains special errors that asynchronous requests might return. For general information about Amazon S3 errors and a list of error codes, see [Error responses](#ErrorResponses).

These errors are returned when you query about the state of an asynchronous request, such as by using `DescribeMultiRegionAccessPointOperation`. Because these requests are asynchronous, all of these errors have a status code of `200 OK`.


| Error code | Description | HTTP status code | 
| --- | --- | --- | 
| AccessDenied | Access denied. | 200 OK | 
| InternalErrors | An internal server error occurred. | 200 OK | 
| MalformedPolicy | The specified policy syntax is not valid. | 200 OK | 
| MultiRegionAccessPointAlreadyOwnedByYou | You already have a Multi-Region Access Point with the same name. | 200 OK | 
| MultiRegionAccessPointModifiedByAnotherRequest | The action failed because another request is modifying the specified resource. Try resubmitting your request after the previous request has been completed. | 200 OK | 
| MultiRegionAccessPointNotReady | The specified Multi-Region Access Point is not ready to be updated. | 200 OK | 
| MultiRegionAccessPointSameBucketRegion | The buckets used to create a Multi-Region Access Point cannot be in the same Region. | 200 OK | 
| MultiRegionAccessPointUnsupportedRegion | One of the buckets supplied to create the Multi-Region Access Point is in a Region that is not supported. | 200 OK | 
| NoSuchBucket | The specified bucket does not exist. | 200 OK | 
| NoSuchMultiRegionAccessPoint | The specified Multi-Region Access Point does not exist. | 200 OK | 

## List of Amazon S3 Access Grants error codes
<a name="S3AccessGrantsErrorCodeList"></a>

The following table contains special errors that S3 Access Grants requests might return. For general information about Amazon S3 errors and a list of error codes, see [Error responses](#ErrorResponses).


| Error Code | Description | HTTP Status Code | 
| --- | --- | --- | 
| AccessGrantAlreadyExists | The specified access grant already exists | 409 | 
| AccessGrantsInstanceAlreadyExists | Access Grants Instance already exists | 409 | 
| AccessGrantsInstanceNotEmptyError | Please clean up locations before deleting the access grants instance | 400 | 
| AccessGrantsInstanceNotExistsError | Access Grants Instance does not exist | 404 | 
| AccessGrantsInstanceResourcePolicyNotExists | Access Grants Instance Resource Policy does not exist | 404 | 
| AccessGrantsLocationAlreadyExistsError | The specified access grants location already exists | 409 | 
| AccessGrantsLocationNotEmptyError | Please clean up access grants before deleting access grants location | 400 | 
| AccessGrantsLocationsQuotaExceededError | The access grants location quota has been exceeded. Access Grants Locations Quota: {{<value>}}. Please reach out to S3 if an increase is required. | 409 | 
| AccessGrantsQuotaExceededError | The access grants quota has been exceeded. Access Grants Quota: {{<value>}}. Please reach out to S3 if an increase is required. | 409 | 
| InvalidTag | There are duplicate tag keys in your request. Remove the duplicate tag keys and try again. | 400 | 
| InvalidAccessGrant | The specified Access Grant is invalid | 400 | 
| InvalidAccessGrantsLocation | The specified Access Grants Location is invalid | 400 | 
| InvalidIamRole | The specified IAM Role is invalid | 400 | 
| InvalidIdentityCenterInstance | The specified identity center instance is invalid | 400 | 
| InvalidResourcePolicy | The specified Resource Policy is invalid | 400 | 
| InvalidResourcePolicy | The specified Resource Policy is invalid | 400 | 
| InvalidTag | This request contains a tag key or value that isn't valid. Valid characters include the following: [a-zA-Z\+-=.\_:/]. Tag keys can contain up to 128 characters. Tag values can contain up to 256 characters. | 400 | 
| NoSuchAccessGrantError | The specified access grant does not exist | 404 | 
| NoSuchAccessGrantsLocationError | The specified access grants location does not exist | 404 | 
| AccessDenied | You do not have {{<requested permission>}} permissions to the requested S3 Prefix: {{<requested target>}} | 403 Forbidden | 
| StsNotAuthorizedError | An error occurred (`StsNotAuthorizedError`) when calling the GetDataAccess operation: User: `access-grants.s3.amazonaws.com` is not authorized to perform: `sts:AssumeRole` on resource: {{<IAM Role ARN>}} | 403 | 
| StsPackedPolicyTooLargeError | An error occurred (`StsPackedPolicyTooLargeError`) when calling the GetDataAccess operation: Serialized token too large for session | 400 | 
| StsValidationError | *The error message varies depending on the validation error.* | 400 | 
| InvalidTags | Tag keys cannot start with AWS reserved prefix for system tags." | 400 | 
| TooManyTags | The number of tags exceeds the limit of 50 tags. Remove some tags and try again. | 400 | 

## List of Amazon FSx-related error codes
<a name="FSXErrorCodeList"></a>

The following table contains special errors that requests made to Amazon FSx through an Amazon S3 access point might return. For general information about Amazon S3 errors and a list of error codes, see [Error responses](#ErrorResponses).


| Error Code | Description | HTTP Status Code | 
| --- | --- | --- | 
| AccessDenied | This error might occur for the following reasons:+  Caller is not authorized to preform specified S3 operation. <br />+  Caller is not authorized to access the Amazon FSx resource for the specified key.  | 403 Forbidden | 
| InsufficientCapacity | Maximum storage capacity of file system has been reached. | 507 Insufficient Capacity | 
| InvalidKey | The specified key is not valid. | 400 Bad Request | 
| SlowDown | Please reduce your request rate. | 503 Slow Down | 

## List of Amazon S3 Tables error codes
<a name="S3TablesErrorCodeList"></a>

The following table contains special errors that Amazon S3 Tables operations might return. For general information about Amazon S3 errors and a list of error codes, see [Error responses](#ErrorResponses).


| Error Code | Description | HTTP Status Code | 
| --- | --- | --- | 
| AccessDeniedException | The action cannot be performed because you do not have the required permission. | 403 Forbidden | 
| BadRequestException | The request is invalid or malformed. | 400 Bad Request | 
| ConflictException | The request failed because there is a conflict with a previous write. You can retry the request. | 409 Conflict | 
| ForbiddenException | The caller isn't authorized to make the request. | 403 Forbidden | 
| InternalServerErrorException | The request failed due to an internal server error. | 500 Internal Server Error | 
| NotFoundException | The request was rejected because the specified resource could not be found. | 404 Not Found | 
| TooManyRequestsException | The limit on the number of requests per second was exceeded. | 429 Too Many Requests | 