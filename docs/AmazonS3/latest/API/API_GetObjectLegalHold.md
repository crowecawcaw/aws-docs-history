# GetObjectLegalHold

###### Note

This operation is not supported for directory buckets.

Gets an object's current legal hold status. For more information, see [Locking Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html").

This functionality is not supported for Amazon S3 on Outposts.

The following action is related to `GetObjectLegalHold`:


* [GetObjectAttributes](API_GetObjectAttributes.md "API_GetObjectAttributes.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /{Key+}?legal-hold&versionId=`VersionId` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-request-payer: `RequestPayer`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetObjectLegalHold_RequestSyntax "#API_GetObjectLegalHold_RequestSyntax")**


The bucket name containing the object whose legal hold status you want to retrieve. 



**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](../userguide/using-access-points.md "../userguide/using-access-points.md") in the *Amazon S3 User Guide*.


Required: Yes




**[Key](#API_GetObjectLegalHold_RequestSyntax "#API_GetObjectLegalHold_RequestSyntax")**


The key name for the object whose legal hold status you want to retrieve.


Length Constraints: Minimum length of 1.


Required: Yes




**[versionId](#API_GetObjectLegalHold_RequestSyntax "#API_GetObjectLegalHold_RequestSyntax")**


The version ID of the object whose legal hold status you want to retrieve.




**[x-amz-expected-bucket-owner](#API_GetObjectLegalHold_RequestSyntax "#API_GetObjectLegalHold_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-request-payer](#API_GetObjectLegalHold_RequestSyntax "#API_GetObjectLegalHold_RequestSyntax")**


Confirms that the requester knows that they will be charged for the request. Bucket owners need not
 specify this parameter in their requests. If either the source or destination S3 bucket has Requester
 Pays enabled, the requester will pay for corresponding charges to copy the object. For information about
 downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html") in the *Amazon S3 User Guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[LegalHold](#AmazonS3-GetObjectLegalHold-response-LegalHold "#AmazonS3-GetObjectLegalHold-response-LegalHold")>
   <[Status](#AmazonS3-GetObjectLegalHold-response-Status "#AmazonS3-GetObjectLegalHold-response-Status")>***string***</[Status](#AmazonS3-GetObjectLegalHold-response-Status "#AmazonS3-GetObjectLegalHold-response-Status")>
</[LegalHold](#AmazonS3-GetObjectLegalHold-response-LegalHold "#AmazonS3-GetObjectLegalHold-response-LegalHold")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[LegalHold](#API_GetObjectLegalHold_ResponseSyntax "#API_GetObjectLegalHold_ResponseSyntax")**


Root level tag for the LegalHold parameters.


Required: Yes




**[Status](#API_GetObjectLegalHold_ResponseSyntax "#API_GetObjectLegalHold_ResponseSyntax")**


Indicates whether the specified object has a legal hold in place.


Type: String


Valid Values: `ON | OFF`





## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetObjectLegalHold "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetObjectLegalHold")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetObjectLegalHold "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetObjectLegalHold")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetObjectLegalHold "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetObjectLegalHold")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetObjectLegalHold "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetObjectLegalHold")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectLegalHold "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectLegalHold")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetObjectLegalHold "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetObjectLegalHold")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetObjectLegalHold "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetObjectLegalHold")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetObjectLegalHold "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetObjectLegalHold")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetObjectLegalHold "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetObjectLegalHold")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetObjectLegalHold "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetObjectLegalHold")
