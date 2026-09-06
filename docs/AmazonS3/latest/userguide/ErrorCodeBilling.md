

# Billing for Amazon S3 error responses
<a name="ErrorCodeBilling"></a>

 In general, S3 bucket owners are billed for requests with HTTP `200 OK` successful responses and HTTP `4XX` client error responses. Bucket owners aren't billed for HTTP `5XX` server error responses, such as HTTP `503 Slow Down` errors. For more information about billing charges if your bucket is configured as a Requester Pays bucket, see [How Requester Pays charges work](RequesterPaysBuckets.md#ChargeDetails). 

The following table lists specific error codes under HTTP `3XX` and `4XX` status codes that aren't billed. For buckets configured with website hosting, applicable request and other charges will still apply when S3 returns a [custom error document](CustomErrorDocSupport.md) or for custom redirects. 

**Note**  
For `AccessDenied` (HTTP `403 Forbidden`), S3 doesn't charge the bucket owner when the request is initiated outside of the bucket owner's individual AWS account or the bucket owner's AWS organization. 




- **301 Moved Permanently**
  - **Error code:** PermanentRedirect / **Description of error code:** The bucket that you are attempting to access must be addressed using the specified endpoint. Send all future requests to this endpoint.
  - **Error code:** PermanentRedirectControlError / **Description of error code:** The API operation you are attempting to access must be addressed using the specified endpoint. Send all future requests to this endpoint.

- **307 Temporary Redirect**
  - **Error code:** TemporaryRedirect
  - **Description of error code:** You are being redirected to the bucket while the Domain Name System (DNS) server is being updated.

- **400 Bad Request**
  - **Error code:** AuthorizationHeaderMalformed / **Description of error code:** The authorization header that you provided is not valid.
  - **Error code:** AuthorizationQueryParametersError / **Description of error code:** The authorization query parameters that you provided are not valid.
  - **Error code:** ConnectionClosedByRequester / **Description of error code:** Returned to the original caller when an error is encountered while reading the WriteGetObjectResponse body.
  - **Error code:** DeviceNotActiveError / **Description of error code:** The device is not currently active.
  - **Error code:** EndpointNotFound / **Description of error code:** Direct requests to the correct endpoint.
  - **Error code:** ExpiredToken / **Description of error code:** The provided token has expired.
  - **Error code:** IllegalLocationConstraintException / **Description of error code:** You are trying to access a bucket from a different Region than where the bucket exists. To avoid this error, use the --region option. For example: aws s3 cp {{awsexample.txt}} s3://{{amzn-s3-demo-bucket}}/ --region {{ap-east-1}}.
  - **Error code:** InvalidArgument / **Description of error code:** This error might occur for the following reasons:+  The specified argument was not valid. <br />+  The request was missing a required header. <br />+  The specified argument was incomplete or in the wrong format. <br />+  The specified argument must have a length greater than or equal to 3. 
  - **Error code:** InvalidBucketOwnerAWSAccountID / **Description of error code:** The value of the expected bucket owner parameter must be an AWS account ID.
  - **Error code:** InvalidDigest / **Description of error code:** The Content-MD5 or checksum value that you specified is not valid.
  - **Error code:** InvalidEncryptionAlgorithmError / **Description of error code:** The encryption request that you specified is not valid. The valid value is AES256.
  - **Error code:** InvalidHostHeader / **Description of error code:** The host headers provided in the request used the incorrect style addressing.
  - **Error code:** InvalidHttpMethod / **Description of error code:** The request is made using an unexpected HTTP method.
  - **Error code:** InvalidRequest / **Description of error code:** This error might occur for the following reasons:+  The request is using the wrong signature version. Use `AWS4-HMAC-SHA256` (Signature Version 4). <br />+  An access point can be created only for an existing bucket. <br />+  The access point is not in a state where it can be deleted. <br />+  An access point can be listed only for an existing bucket. <br />+  The next token is not valid. <br />+  At least one action must be specified in a lifecycle rule. <br />+  At least one lifecycle rule must be specified. <br />+  The number of lifecycle rules must not exceed the allowed limit of 1000 rules. <br />+  The range for the `MaxResults` parameter is not valid. <br />+  SOAP requests must be made over an HTTPS connection. <br />+  Amazon S3 Transfer Acceleration is not supported for buckets with non-DNS compliant names. <br />+  Amazon S3 Transfer Acceleration is not supported for buckets with periods (.) in their names. <br />+  The Amazon S3 Transfer Acceleration endpoint supports only virtual style requests. <br />+  Amazon S3 Transfer Acceleration is not configured on this bucket. <br />+  Amazon S3 Transfer Acceleration is disabled on this bucket. <br />+  Amazon S3 Transfer Acceleration is not supported on this bucket. For assistance, contact [Support](https://aws.amazon.com/contact-us/). <br />+  Amazon S3 Transfer Acceleration cannot be enabled on this bucket. For assistance, contact [Support](https://aws.amazon.com/contact-us/). <br />+   Conflicting values provided in HTTP headers and query parameters.  <br />+   Conflicting values provided in HTTP headers and POST form fields.  <br />+  CopyObject request made on objects larger than 5GB in size. 
  - **Error code:** InvalidSessionException / **Description of error code:** Returned if the session doesn't exist anymore because it timed out or expired.
  - **Error code:** InvalidSignature / **Description of error code:** The request signature that the server calculated does not match the signature that you provided. Check your AWS secret access key and signing method. For more information, see [Signing and authenticating REST requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RESTAuthentication.html).
  - **Error code:** InvalidSOAPRequest / **Description of error code:** The SOAP request body is not valid.
  - **Error code:** InvalidStorageClass / **Description of error code:** The storage class that you specified is not valid.
  - **Error code:** InvalidTag / **Description of error code:** Your request contains tag input that is not valid. For example, your request might contain duplicate keys, keys or values that are too long, or system tags.
  - **Error code:** InvalidToken / **Description of error code:** The provided token is malformed or otherwise not valid.
  - **Error code:** InvalidURI / **Description of error code:** The specified URI couldn't be parsed.
  - **Error code:** KeyTooLongError / **Description of error code:** Your key is too long.
  - **Error code:** KMS.DisabledException / **Description of error code:** The request was rejected because the specified KMS key is not enabled.
  - **Error code:** KMS.InvalidKeyUsageException / **Description of error code:** The request was rejected for one of the following reasons: + The KeyUsage value of the KMS key is incompatible with the API operation. <br />+ The encryption algorithm or signing algorithm specified for the operation is incompatible with the type of key material in the KMS key (KeySpec). For encrypting, decrypting, re-encrypting, and generating data keys, the KeyUsage must be ENCRYPT\_DECRYPT. For signing and verifying messages, the KeyUsage must be SIGN\_VERIFY. For generating and verifying message authentication codes (MACs), the KeyUsage must be GENERATE\_VERIFY\_MAC. For deriving key agreement secrets, the KeyUsage must be KEY\_AGREEMENT. To find the KeyUsage of a KMS key, use the DescribeKey operation. To find the encryption or signing algorithms supported for a particular KMS key, use the DescribeKey operation.
  - **Error code:** KMS.KMSInvalidStateException / **Description of error code:** The request was rejected because the state of the specified resource is not valid for this request. This exception means one of the following: + The key state of the KMS key is not compatible with the operation. <br />To find the key state, use the DescribeKey operation. For more information about which key states are compatible with each KMS operation, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the *AWS Key Management Service Developer Guide*.  <br />+ For cryptographic operations on KMS keys in custom key stores, this exception represents a general failure with many possible causes. To identify the cause, see the error message that accompanies the exception.
  - **Error code:** KMS.NotFoundException / **Description of error code:** The request was rejected because the specified entity or resource could not be found.
  - **Error code:** LambdaInvalidResponse / **Description of error code:** Returned to the original caller when WriteGetObjectResponse responds with ValidationError to AWS Lambda. See the ValidationError message for more details. Not all cases of ValidationError result in a LambdaInvalidResponse error.
  - **Error code:** LambdaInvocationFailed / **Description of error code:** Lambda function invocation failed. Callers might receive the following error when S3 Object Lambda is unable to successfully invoke the configured Lambda function. The error message might contain details about an eventual error returned by the AWS Lambda service when invoking the function (for example, status code, error code, error message and request ID).
  - **Error code:** MalformedACLError / **Description of error code:** The ACL that you provided was not well formed or did not validate against our published schema.
  - **Error code:** MalformedPOSTRequest / **Description of error code:** The body of your POST request is not well-formed multipart/form-data.
  - **Error code:** MalformedXML / **Description of error code:** The XML that you provided was not well formed or did not validate against our published schema.
  - **Error code:** MaxPostPreDataLengthExceededError / **Description of error code:** Your POST request fields preceding the upload file were too large.
  - **Error code:** MetadataTooLarge / **Description of error code:** Your metadata headers exceed the maximum allowed metadata size.
  - **Error code:** MissingAttachment / **Description of error code:** A SOAP attachment was expected, but none was found.
  - **Error code:** MissingRequestBodyError / **Description of error code:** You sent an empty XML document as a request.
  - **Error code:** MissingSecurityHeader / **Description of error code:** Your request is missing a required header.
  - **Error code:** NoLoggingStatusForKey / **Description of error code:** There is no such thing as a logging status subresource for a key.
  - **Error code:** NotDeviceOwnerError / **Description of error code:** The device that generated the token is not owned by the authenticated user.
  - **Error code:** ResponseInterrupted / **Description of error code:** Returned to the original caller when an error is encountered while reading the WriteGetObjectResponse body. 
  - **Error code:** RequestHeaderSectionTooLarge / **Description of error code:** The request header and query parameters used to make the request exceed the maximum allowed sizes
  - **Error code:** TokenCodeInvalidError / **Description of error code:** The serial number and/or token code you provided is not valid.
  - **Error code:** UnexpectedContent / **Description of error code:** This request contains unsupported content.
  - **Error code:** UnsupportedArgument / **Description of error code:** The request contained an unsupported argument.
  - **Error code:** UnsupportedSignature / **Description of error code:** The provided request is signed with an unsupported STS Token version or the signature version is not supported.
  - **Error code:** UserKeyMustBeSpecified / **Description of error code:** The bucket POST request must contain the specified field name. If it is specified, check the order of the fields.
  - **Error code:** IncorrectEndpoint / **Description of error code:** The specified bucket exists in another Region. Direct requests to the correct endpoint.
  - **Error code:** ValidationError / **Description of error code:** Validation errors might be returned from the WriteGetObjectResponse API operation and can occur for numerous reasons. See the error message for more details.

- **403 Forbidden**
  - **Error code:** RequestTimeTooSkewed / **Description of error code:** The difference between the request time and the server's time is too large.
  - **Error code:** SignatureDoesNotMatch / **Description of error code:** The request signature that the server calculated does not match the signature that you provided. Check your AWS secret access key and signing method. For more information, see [REST Authentication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RESTAuthentication.html) and [SOAP Authentication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/SOAPAuthentication.html).
  - **Error code:** NotSignedUp / **Description of error code:** Your account is not signed up for the Amazon S3 service. You must sign up before you can use Amazon S3. You can sign up at the following URL: [https://aws.amazon.com/s3](https://aws.amazon.com/s3/)
  - **Error code:** InvalidSecurity / **Description of error code:** The provided security credentials are not valid.
  - **Error code:** InvalidPayer / **Description of error code:** All access to this object has been disabled. For further assistance, see [Contact Us](https://aws.amazon.com/contact-us/).
  - **Error code:** InvalidAccessKeyId / **Description of error code:** The AWS access key ID that you provided does not exist in our records.
  - **Error code:** AccountProblem / **Description of error code:** There is a problem with your AWS account that prevents the operation from completing successfully. For further assistance, see [Contact Us](https://aws.amazon.com/contact-us/).
  - **Error code:** UnauthorizedAccessError / **Description of error code:** Applicable in China Regions only. Returned when a request is made to a bucket that doesn't have an ICP license. For more information, see [ICP Recordal](https://www.amazonaws.cn/en/support/icp/).
  - **Error code:** UnexpectedIPError / **Description of error code:** Applicable in China Regions only. This request was rejected because the IP was unexpected. 
  - **Error code:** MissingAuthenticationToken / **Description of error code:** The request was not signed.  
  - **Error code:** LambdaPermissionError / **Description of error code:** The caller is not authorized to invoke the Lambda function. The caller must have permission to invoke the Lambda function. Check the policies attached to the caller and ensure that they've been allowed to use lambda:Invoke for the configured function. The error message might contain details about an eventual error returned by the Lambda service when invoking the function (for example, status code, error code, error message and request ID).

- **404 Not Found**
  - **Error code:** LambdaNotFound / **Description of error code:** The AWS Lambda function was not found. The configured Lambda function, version, or alias was not found when attempting to invoke it. Ensure that the S3 Object Lambda Access Point configuration points to the correct Lambda function ARN. The error message might contain details about an eventual error returned by the AWS Lambda service when invoking the function (for example, status code, error code, error message and request ID).
  - **Error code:** NoSuchAsyncRequest / **Description of error code:** The specified request was not found.
  - **Error code:** NoSuchObjectLockConfiguration / **Description of error code:** The specified object does not have an ObjectLock configuration.
  - **Error code:** NoSuchUpload / **Description of error code:** The specified multipart upload does not exist. The upload ID might not be valid, or the multipart upload might have been aborted or completed.
  - **Error code:** NoSuchWebsiteConfiguration / **Description of error code:** The specified bucket does not have a website configuration.
  - **Error code:** NoTransformationDefined / **Description of error code:** No transformation found for this Object Lambda Access Point.
  - **Error code:** ObjectLockConfigurationNotFoundError / **Description of error code:** The Object Lock configuration does not exist for this bucket.

- **405 Method Not Allowed**
  - **Error code:** MethodNotAllowed
  - **Description of error code:** The specified method is not allowed against this resource.

- **409 Conflict**
  - **Error code:** BucketAlreadyExists / **Description of error code:** The requested bucket name is not available. The bucket namespace is shared by all users of the system. Specify a different name and try again.
  - **Error code:** InvalidBucketState / **Description of error code:** The request is not valid for the current state of the bucket.
  - **Error code:** OperationAborted / **Description of error code:** A conflicting conditional operation is currently in progress against this resource. Try again.

- **411 Length Required**
  - **Error code:** MissingContentLength
  - **Description of error code:** You must provide the Content-Length HTTP header.

- **412 Precondition Failed**
  - **Error code:** RequestIsNotMultiPartContent
  - **Description of error code:** A bucket POST request must be of the enclosure-type multipart/form-data.

- **416 Requested Range Not Satisfiable**
  - **Error code:** InvalidRange
  - **Description of error code:** The requested range is not valid for the request. Try another range.

