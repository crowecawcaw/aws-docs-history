# ListDirectoryBuckets

Returns a list of all Amazon S3 directory buckets owned by the authenticated sender of the request. For
 more information about directory buckets, see [Directory buckets](../userguide/directory-buckets-overview.md "../userguide/directory-buckets-overview.md") in the
 *Amazon S3 User Guide*.

###### Note


**Directory buckets**  - For directory buckets, you must make requests for this API operation to the Regional endpoint. These endpoints support path-style requests in the format `https://s3express-control.*region-code*.amazonaws.com/*bucket-name*`. Virtual-hosted-style requests aren't supported. 
For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](../userguide/endpoint-directory-buckets-AZ.md "../userguide/endpoint-directory-buckets-AZ.md") in the
 *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](../userguide/s3-lzs-for-directory-buckets.md "../userguide/s3-lzs-for-directory-buckets.md") in the
 *Amazon S3 User Guide*.



Permissions

You must have the `s3express:ListAllMyDirectoryBuckets` permission in
 an IAM identity-based policy instead of a bucket policy. Cross-account access to this API operation isn't supported. This operation can only be performed by the AWS account that owns the resource.
 For more information about directory bucket policies and permissions, see [AWS Identity and Access Management (IAM) for S3 Express One Zone](../userguide/s3-express-security-iam.md "../userguide/s3-express-security-iam.md") in the *Amazon S3 User Guide*.



HTTP Host header syntax


**Directory buckets**  - The HTTP Host header syntax is
 `s3express-control.*region*.amazonaws.com`.



###### Note

 The `BucketRegion` response element is not part of the
 `ListDirectoryBuckets` Response Syntax.

###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?continuation-token=`ContinuationToken`&max-directory-buckets=`MaxDirectoryBuckets` HTTP/1.1
Host: s3.amazonaws.com

```

## URI Request Parameters


The request uses the following URI parameters.





**[continuation-token](#API_ListDirectoryBuckets_RequestSyntax "#API_ListDirectoryBuckets_RequestSyntax")**



`ContinuationToken` indicates to Amazon S3 that the list is being continued on buckets in this
 account with a token. `ContinuationToken` is obfuscated and is not a real bucket name. You
 can use this `ContinuationToken` for the pagination of the list results. 


Length Constraints: Minimum length of 0. Maximum length of 1024.




**[max-directory-buckets](#API_ListDirectoryBuckets_RequestSyntax "#API_ListDirectoryBuckets_RequestSyntax")**


Maximum number of buckets to be returned in response. When the number is more than the count of
 buckets that are owned by an AWS account, return all the buckets in response.


Valid Range: Minimum value of 0. Maximum value of 1000.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[ListAllMyDirectoryBucketsResult](#AmazonS3-ListDirectoryBuckets-response-ListDirectoryBucketsOutput "#AmazonS3-ListDirectoryBuckets-response-ListDirectoryBucketsOutput")>
   <[Buckets](#AmazonS3-ListDirectoryBuckets-response-Buckets "#AmazonS3-ListDirectoryBuckets-response-Buckets")>
      <Bucket>
         <[BucketArn](API_Bucket.md#AmazonS3-Type-Bucket-BucketArn "API_Bucket.md#AmazonS3-Type-Bucket-BucketArn")>***string***</[BucketArn](API_Bucket.md#AmazonS3-Type-Bucket-BucketArn "API_Bucket.md#AmazonS3-Type-Bucket-BucketArn")>
         <[BucketRegion](API_Bucket.md#AmazonS3-Type-Bucket-BucketRegion "API_Bucket.md#AmazonS3-Type-Bucket-BucketRegion")>***string***</[BucketRegion](API_Bucket.md#AmazonS3-Type-Bucket-BucketRegion "API_Bucket.md#AmazonS3-Type-Bucket-BucketRegion")>
         <[CreationDate](API_Bucket.md#AmazonS3-Type-Bucket-CreationDate "API_Bucket.md#AmazonS3-Type-Bucket-CreationDate")>***timestamp***</[CreationDate](API_Bucket.md#AmazonS3-Type-Bucket-CreationDate "API_Bucket.md#AmazonS3-Type-Bucket-CreationDate")>
         <[Name](API_Bucket.md#AmazonS3-Type-Bucket-Name "API_Bucket.md#AmazonS3-Type-Bucket-Name")>***string***</[Name](API_Bucket.md#AmazonS3-Type-Bucket-Name "API_Bucket.md#AmazonS3-Type-Bucket-Name")>
      </Bucket>
   </[Buckets](#AmazonS3-ListDirectoryBuckets-response-Buckets "#AmazonS3-ListDirectoryBuckets-response-Buckets")>
   <[ContinuationToken](#AmazonS3-ListDirectoryBuckets-response-ContinuationToken "#AmazonS3-ListDirectoryBuckets-response-ContinuationToken")>***string***</[ContinuationToken](#AmazonS3-ListDirectoryBuckets-response-ContinuationToken "#AmazonS3-ListDirectoryBuckets-response-ContinuationToken")>
</[ListAllMyDirectoryBucketsResult](#AmazonS3-ListDirectoryBuckets-response-ListDirectoryBucketsOutput "#AmazonS3-ListDirectoryBuckets-response-ListDirectoryBucketsOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[ListAllMyDirectoryBucketsResult](#API_ListDirectoryBuckets_ResponseSyntax "#API_ListDirectoryBuckets_ResponseSyntax")**


Root level tag for the ListAllMyDirectoryBucketsResult parameters.


Required: Yes




**[Buckets](#API_ListDirectoryBuckets_ResponseSyntax "#API_ListDirectoryBuckets_ResponseSyntax")**


The list of buckets owned by the requester. 


Type: Array of [Bucket](API_Bucket.md "API_Bucket.md") data types




**[ContinuationToken](#API_ListDirectoryBuckets_ResponseSyntax "#API_ListDirectoryBuckets_ResponseSyntax")**


If `ContinuationToken` was sent with the request, it is included in the response. You can
 use the returned `ContinuationToken` for pagination of the list response.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1024.




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/ListDirectoryBuckets "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/ListDirectoryBuckets")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/ListDirectoryBuckets "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/ListDirectoryBuckets")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ListDirectoryBuckets "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ListDirectoryBuckets")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/ListDirectoryBuckets "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/ListDirectoryBuckets")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ListDirectoryBuckets "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ListDirectoryBuckets")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/ListDirectoryBuckets "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/ListDirectoryBuckets")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/ListDirectoryBuckets "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/ListDirectoryBuckets")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/ListDirectoryBuckets "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/ListDirectoryBuckets")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/ListDirectoryBuckets "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/ListDirectoryBuckets")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ListDirectoryBuckets "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ListDirectoryBuckets")
