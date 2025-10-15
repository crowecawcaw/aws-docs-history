# DeleteBucketLifecycle

Deletes the lifecycle configuration from the specified bucket. Amazon S3 removes all the lifecycle
 configuration rules in the lifecycle subresource associated with the bucket. Your objects never expire,
 and Amazon S3 no longer automatically deletes any objects on the basis of rules contained in the deleted
 lifecycle configuration.



Permissions


* **General purpose bucket permissions** - By default, all Amazon S3
 resources are private, including buckets, objects, and related subresources (for example,
 lifecycle configuration and website configuration). Only the resource owner (that is, the
 AWS account that created it) can access the resource. The resource owner can optionally
 grant access permissions to others by writing an access policy. For this operation, a user
 must have the `s3:PutLifecycleConfiguration` permission.


For more information about permissions, see [Managing Access Permissions to Your
 Amazon S3 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md").


* **Directory bucket permissions** - You must have the
 `s3express:PutLifecycleConfiguration` permission in an IAM identity-based policy
 to use this operation. Cross-account access to this API operation isn't supported. The
 resource owner can optionally grant access permissions to others by creating a role or user
 for them as long as they are within the same account as the owner and resource.


For more information about directory bucket policies and permissions, see [Authorizing Regional endpoint APIs with IAM](../userguide/s3-express-security-iam.md "../userguide/s3-express-security-iam.md") in the *Amazon S3 User
 Guide*.


###### Note


**Directory buckets**  - For directory buckets, you must make requests for this API operation to the Regional endpoint. These endpoints support path-style requests in the format `https://s3express-control.*region-code*.amazonaws.com/*bucket-name*`. Virtual-hosted-style requests aren't supported. 
For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](../userguide/endpoint-directory-buckets-AZ.md "../userguide/endpoint-directory-buckets-AZ.md") in the
 *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](../userguide/s3-lzs-for-directory-buckets.md "../userguide/s3-lzs-for-directory-buckets.md") in the
 *Amazon S3 User Guide*.




HTTP Host header syntax


**Directory buckets**  - The HTTP Host header syntax is
 `s3express-control.*region*.amazonaws.com`.



For more information about the object expiration, see [Elements to
 Describe Lifecycle Actions](https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#intro-lifecycle-rules-actions "https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#intro-lifecycle-rules-actions").

Related actions include:


* [PutBucketLifecycleConfiguration](API_PutBucketLifecycleConfiguration.md "API_PutBucketLifecycleConfiguration.md")
* [GetBucketLifecycleConfiguration](API_GetBucketLifecycleConfiguration.md "API_GetBucketLifecycleConfiguration.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
DELETE /?lifecycle HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_DeleteBucketLifecycle_RequestSyntax "#API_DeleteBucketLifecycle_RequestSyntax")**


The bucket name of the lifecycle to delete.


Required: Yes




**[x-amz-expected-bucket-owner](#API_DeleteBucketLifecycle_RequestSyntax "#API_DeleteBucketLifecycle_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).


###### Note

This parameter applies to general purpose buckets only. It is not supported for directory bucket
 lifecycle configurations.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 204

```

## Response Elements


If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.


## Examples


### Sample Request


The following DELETE request deletes the lifecycle subresource from the specified general
 purpose bucket. This removes lifecycle configuration stored in the subresource.



```

            DELETE /?lifecycle HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com  
            Date: Wed, 14 Dec 2011 05:37:16 GMT
            Authorization: signatureValue 

```

### Sample Response


The following successful response shows Amazon S3 returning a 204 No Content response. Objects in
 your general purpose bucket no longer expire.



```

            HTTP/1.1 204 No Content 
            x-amz-id-2: Uuag1LuByRx9e6j5OnimrSAMPLEtRPfTaOAa==  
            x-amz-request-id: 656c76696e672SAMPLE5657374  
            Date: Wed, 14 Dec 2011 05:37:16 GMT
            Connection: keep-alive  
            Server: AmazonS3 

```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteBucketLifecycle "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteBucketLifecycle")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteBucketLifecycle "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteBucketLifecycle")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteBucketLifecycle")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteBucketLifecycle")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteBucketLifecycle")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteBucketLifecycle")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteBucketLifecycle")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteBucketLifecycle")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteBucketLifecycle "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteBucketLifecycle")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteBucketLifecycle")
