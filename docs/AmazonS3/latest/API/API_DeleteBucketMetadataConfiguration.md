# DeleteBucketMetadataConfiguration

 Deletes an S3 Metadata configuration from a general purpose bucket. For more information, see
 [Accelerating
 data discovery with S3 Metadata](../userguide/metadata-tables-overview.md "../userguide/metadata-tables-overview.md") in the *Amazon S3 User Guide*. 

###### Note

You can use the V2 `DeleteBucketMetadataConfiguration` API operation with V1 or V2 
 metadata configurations. However, if you try to use the V1 
 `DeleteBucketMetadataTableConfiguration` API operation with V2 configurations, you
 will receive an HTTP `405 Method Not Allowed` error.



Permissions

To use this operation, you must have the
 `s3:DeleteBucketMetadataTableConfiguration` permission. For more information, see
 [Setting up permissions for configuring metadata tables](../userguide/metadata-tables-permissions.md "../userguide/metadata-tables-permissions.md") in the
 *Amazon S3 User Guide*. 


###### Note

The IAM policy action name is the same for the V1 and V2 API operations.



The following operations are related to `DeleteBucketMetadataConfiguration`:


* [CreateBucketMetadataConfiguration](API_CreateBucketMetadataConfiguration.md "API_CreateBucketMetadataConfiguration.md")
* [GetBucketMetadataConfiguration](API_GetBucketMetadataConfiguration.md "API_GetBucketMetadataConfiguration.md")
* [UpdateBucketMetadataInventoryTableConfiguration](API_UpdateBucketMetadataInventoryTableConfiguration.md "API_UpdateBucketMetadataInventoryTableConfiguration.md")
* [UpdateBucketMetadataJournalTableConfiguration](API_UpdateBucketMetadataJournalTableConfiguration.md "API_UpdateBucketMetadataJournalTableConfiguration.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
DELETE /?metadataConfiguration HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_DeleteBucketMetadataConfiguration_RequestSyntax "#API_DeleteBucketMetadataConfiguration_RequestSyntax")**



 The general purpose bucket that you want to remove the metadata configuration from.
 


Required: Yes




**[x-amz-expected-bucket-owner](#API_DeleteBucketMetadataConfiguration_RequestSyntax "#API_DeleteBucketMetadataConfiguration_RequestSyntax")**



 The expected bucket owner of the general purpose bucket that you want to remove the metadata table
 configuration from.
 




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 204

```

## Response Elements


If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.


## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteBucketMetadataConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteBucketMetadataConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteBucketMetadataConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteBucketMetadataConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteBucketMetadataConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteBucketMetadataConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteBucketMetadataConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteBucketMetadataConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteBucketMetadataConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteBucketMetadataConfiguration")
