# RenameObject

Renames an existing object in a directory bucket that uses the S3 Express One Zone storage class.
 You can use `RenameObject` by specifying an existing object’s name as the source and the new
 name of the object as the destination within the same directory bucket.

###### Note


`RenameObject` is only supported for objects stored in the S3 Express One Zone storage
 class.

 To prevent overwriting an object, you can use the `If-None-Match` conditional
 header.


* **If-None-Match** - Renames the object only if an object
 with the specified name does not already exist in the directory bucket. If you don't want to
 overwrite an existing object, you can add the `If-None-Match` conditional header with the
 value `‘*’` in the `RenameObject` request. Amazon S3 then returns a `412
 Precondition Failed` error if the object with the specified name already exists. For more
 information, see [RFC 7232](https://datatracker.ietf.org/doc/rfc7232/ "https://datatracker.ietf.org/doc/rfc7232/").


Permissions

 To grant access to the `RenameObject` operation on a directory bucket, we
 recommend that you use the `CreateSession` operation for session-based authorization.
 Specifically, you grant the `s3express:CreateSession` permission to the directory
 bucket in a bucket policy or an IAM identity-based policy. Then, you make the
 `CreateSession` API call on the directory bucket to obtain a session token. With the
 session token in your request header, you can make API requests to this operation. After the
 session token expires, you make another `CreateSession` API call to generate a new
 session token for use. The AWS CLI and SDKs will create and manage your session including
 refreshing the session token automatically to avoid service interruptions when a session expires.
 In your bucket policy, you can specify the `s3express:SessionMode` condition key to
 control who can create a `ReadWrite` or `ReadOnly` session. A
 `ReadWrite` session is required for executing all the Zonal endpoint API operations,
 including `RenameObject`. For more information about authorization, see [`CreateSession`](API_CreateSession.md "API_CreateSession.md"). To learn more about Zonal endpoint API operations, see
 [Authorizing Zonal endpoint API operations with CreateSession](../userguide/s3-express-create-session.md "../userguide/s3-express-create-session.md") in the *Amazon S3 User
 Guide*. 



HTTP Host header syntax


**Directory buckets**  - The HTTP Host header syntax is `*Bucket-name*.s3express-*zone-id*.*region-code*.amazonaws.com`.



###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /{Key+}?renameObject HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-rename-source: `RenameSource`
If-Match: `DestinationIfMatch`
If-None-Match: `DestinationIfNoneMatch`
If-Modified-Since: `DestinationIfModifiedSince`
If-Unmodified-Since: `DestinationIfUnmodifiedSince`
x-amz-rename-source-if-match: `SourceIfMatch`
x-amz-rename-source-if-none-match: `SourceIfNoneMatch`
x-amz-rename-source-if-modified-since: `SourceIfModifiedSince`
x-amz-rename-source-if-unmodified-since: `SourceIfUnmodifiedSince`
x-amz-client-token: `ClientToken`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_RenameObject_RequestSyntax "#API_RenameObject_RequestSyntax")**


The bucket name of the directory bucket containing the object.


 You must use virtual-hosted-style requests in the format
 `Bucket-name.s3express-zone-id.region-code.amazonaws.com`. Path-style requests are not
 supported. Directory bucket names must be unique in the chosen Availability Zone. Bucket names must
 follow the format `bucket-base-name--zone-id--x-s3`  (for example,
 `amzn-s3-demo-bucket--usw2-az1--x-s3`). For information about bucket naming restrictions, see
 [Directory bucket naming rules](../userguide/directory-bucket-naming-rules.md "../userguide/directory-bucket-naming-rules.md") in the *Amazon S3 User Guide*.


Required: Yes




**[If-Match](#API_RenameObject_RequestSyntax "#API_RenameObject_RequestSyntax")**


Renames the object only if the ETag (entity tag) value provided during the operation matches the
 ETag of the object in S3. The `If-Match` header field makes the request method conditional on
 ETags. If the ETag values do not match, the operation returns a `412 Precondition Failed`
 error.


Expects the ETag value as a string.




**[If-Modified-Since](#API_RenameObject_RequestSyntax "#API_RenameObject_RequestSyntax")**


Renames the object if the destination exists and if it has been modified since the specified
 time.




**[If-None-Match](#API_RenameObject_RequestSyntax "#API_RenameObject_RequestSyntax")**


 Renames the object only if the destination does not already exist in the specified directory
 bucket. If the object does exist when you send a request with `If-None-Match:*`, the S3 API
 will return a `412 Precondition Failed` error, preventing an overwrite. The
 `If-None-Match` header prevents overwrites of existing data by validating that there's not
 an object with the same key name already in your directory bucket.


 Expects the `*` character (asterisk).




**[If-Unmodified-Since](#API_RenameObject_RequestSyntax "#API_RenameObject_RequestSyntax")**


Renames the object if it hasn't been modified since the specified time.




**[Key](#API_RenameObject_RequestSyntax "#API_RenameObject_RequestSyntax")**


Key name of the object to rename.


Length Constraints: Minimum length of 1.


Required: Yes




**[x-amz-client-token](#API_RenameObject_RequestSyntax "#API_RenameObject_RequestSyntax")**


 A unique string with a max of 64 ASCII characters in the ASCII range of 33 - 126.


###### Note


`RenameObject` supports idempotency using a client token. To make an idempotent API request
 using `RenameObject`, specify a client token in the request. You should not reuse the same
 client token for other API requests. If you retry a request that completed successfully using the same
 client token and the same parameters, the retry succeeds without performing any further actions. If
 you retry a successful request using the same client token, but one or more of the parameters are
 different, the retry fails and an `IdempotentParameterMismatch` error is returned. 




**[x-amz-rename-source](#API_RenameObject_RequestSyntax "#API_RenameObject_RequestSyntax")**


Specifies the source for the rename operation. The value must be URL encoded.


Pattern: `\/?.+\/.+`



Required: Yes




**[x-amz-rename-source-if-match](#API_RenameObject_RequestSyntax "#API_RenameObject_RequestSyntax")**


Renames the object if the source exists and if its entity tag (ETag) matches the specified ETag.
 




**[x-amz-rename-source-if-modified-since](#API_RenameObject_RequestSyntax "#API_RenameObject_RequestSyntax")**


Renames the object if the source exists and if it has been modified since the specified time.




**[x-amz-rename-source-if-none-match](#API_RenameObject_RequestSyntax "#API_RenameObject_RequestSyntax")**


Renames the object if the source exists and if its entity tag (ETag) is different than the specified
 ETag. If an asterisk (`*`) character is provided, the operation will fail and return a
 `412 Precondition Failed` error. 




**[x-amz-rename-source-if-unmodified-since](#API_RenameObject_RequestSyntax "#API_RenameObject_RequestSyntax")**


Renames the object if the source exists and hasn't been modified since the specified time.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Errors





**IdempotencyParameterMismatch** 


Parameters on this idempotent request are inconsistent with parameters used in previous request(s). 


For a list of error codes and more information on Amazon S3 errors, see [Error codes](ErrorResponses.md#ErrorCodeList "ErrorResponses.md#ErrorCodeList").


###### Note

Idempotency ensures that an API request completes no more than one time. With an idempotent
 request, if the original request completes successfully, any subsequent retries complete successfully
 without performing any further actions.


HTTP Status Code: 400




## Examples


### Sample request: Renaming an object in a directory bucket


The following example request illustrates renaming the *srcfilename.txt*
 object in a directory bucket.



```
PUT */dstfilename.txt* HTTP/1.1
Host: *amzn-s3-demo-bucket*--*zone*-*id*--x-s3.s3express.amazonaws.com
If-Match: *9b2cf535f27731c974343645a3985328*
x-amz-rename-source: */srcfilename.txt*
            
```

### Sample request: Renaming an object in a directory bucket if the destination doesn't
 exist


The following example request illustrates renaming the *srcfilename.txt*
 object to *dstfilename.txt* if an object named
 *dstfilename.txt* doesn't already exist in the directory bucket.



```
PUT */dstfilename.txt* HTTP/1.1
Host: *amzn-s3-demo-bucket*--*zone*-*id*--x-s3.s3express.amazonaws.com
If-None-Match: *
x-amz-rename-source: */srcfilename.txt*
            
```

###  Sample request: Renaming an object in a directory bucket if the destination exists with a
 specific ETag


The following example request illustrates renaming the *srcfilename.txt*
 object only if the destination exists and has the ETag:
 *9b2cf535f27731c974343645a3985328*.



```
PUT */dstfilename.txt* HTTP/1.1
Host: *amzn-s3-demo-bucket*--*zone*-*id*--x-s3.s3express.amazonaws.com
If-Match: *9b2cf535f27731c974343645a3985328*
x-amz-rename-source: */srcfilename.txt*
            
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/RenameObject "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/RenameObject")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/RenameObject "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/RenameObject")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/RenameObject "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/RenameObject")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/RenameObject "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/RenameObject")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/RenameObject "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/RenameObject")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/RenameObject "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/RenameObject")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/RenameObject "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/RenameObject")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/RenameObject "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/RenameObject")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/RenameObject "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/RenameObject")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/RenameObject "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/RenameObject")
