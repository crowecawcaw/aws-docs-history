# GetBucketLifecycleConfiguration

###### Note

This action gets an Amazon S3 on Outposts bucket's lifecycle configuration. To get an S3
 bucket's lifecycle configuration, see [GetBucketLifecycleConfiguration](API_GetBucketLifecycleConfiguration.md "API_GetBucketLifecycleConfiguration.md") in the *Amazon S3 API Reference*.
 

Returns the lifecycle configuration information set on the Outposts bucket. For more
 information, see [Using Amazon S3 on Outposts](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") and for
 information about lifecycle configuration, see  [Object Lifecycle
 Management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html") in *Amazon S3 User Guide*.

To use this action, you must have permission to perform the
 `s3-outposts:GetLifecycleConfiguration` action. The Outposts bucket owner
 has this permission, by default. The bucket owner can grant this permission to others. For
 more information about permissions, see [Permissions Related to Bucket Subresource Operations](../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources "../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources") and [Managing
 Access Permissions to Your Amazon S3 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md").

All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](API_control_GetBucketLifecycleConfiguration.md#API_control_GetBucketLifecycleConfiguration_Examples "API_control_GetBucketLifecycleConfiguration.md#API_control_GetBucketLifecycleConfiguration_Examples") section.


`GetBucketLifecycleConfiguration` has the following special error:


* Error code: `NoSuchLifecycleConfiguration`





	+ Description: The lifecycle configuration does not exist.
	+ HTTP Status Code: 404 Not Found
	+ SOAP Fault Code Prefix: Client
The following actions are related to
 `GetBucketLifecycleConfiguration`:


* [PutBucketLifecycleConfiguration](API_control_PutBucketLifecycleConfiguration.md "API_control_PutBucketLifecycleConfiguration.md")
* [DeleteBucketLifecycleConfiguration](API_control_DeleteBucketLifecycleConfiguration.md "API_control_DeleteBucketLifecycleConfiguration.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/bucket/`name`/lifecycleconfiguration HTTP/1.1
Host: `Bucket`.s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_GetBucketLifecycleConfiguration_RequestSyntax "#API_control_GetBucketLifecycleConfiguration_RequestSyntax")**


The Amazon Resource Name (ARN) of the bucket.


For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.


For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the bucket accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name>`. For example, to access the bucket `reports` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports`. The value must be URL encoded. 


Length Constraints: Minimum length of 3. Maximum length of 255.


Required: Yes




**[x-amz-account-id](#API_control_GetBucketLifecycleConfiguration_RequestSyntax "#API_control_GetBucketLifecycleConfiguration_RequestSyntax")**


The AWS account ID of the Outposts bucket.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[GetBucketLifecycleConfigurationResult](#AmazonS3-control_GetBucketLifecycleConfiguration-response-GetBucketLifecycleConfigurationResult "#AmazonS3-control_GetBucketLifecycleConfiguration-response-GetBucketLifecycleConfigurationResult")>
   <[Rules](#AmazonS3-control_GetBucketLifecycleConfiguration-response-Rules "#AmazonS3-control_GetBucketLifecycleConfiguration-response-Rules")>
      <Rule>
         <[AbortIncompleteMultipartUpload](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-AbortIncompleteMultipartUpload "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-AbortIncompleteMultipartUpload")>
            <[DaysAfterInitiation](API_control_AbortIncompleteMultipartUpload.md#AmazonS3-Type-control_AbortIncompleteMultipartUpload-DaysAfterInitiation "API_control_AbortIncompleteMultipartUpload.md#AmazonS3-Type-control_AbortIncompleteMultipartUpload-DaysAfterInitiation")>***integer***</[DaysAfterInitiation](API_control_AbortIncompleteMultipartUpload.md#AmazonS3-Type-control_AbortIncompleteMultipartUpload-DaysAfterInitiation "API_control_AbortIncompleteMultipartUpload.md#AmazonS3-Type-control_AbortIncompleteMultipartUpload-DaysAfterInitiation")>
         </[AbortIncompleteMultipartUpload](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-AbortIncompleteMultipartUpload "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-AbortIncompleteMultipartUpload")>
         <[Expiration](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Expiration "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Expiration")>
            <[Date](API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-Date "API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-Date")>***timestamp***</[Date](API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-Date "API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-Date")>
            <[Days](API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-Days "API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-Days")>***integer***</[Days](API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-Days "API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-Days")>
            <[ExpiredObjectDeleteMarker](API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-ExpiredObjectDeleteMarker "API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-ExpiredObjectDeleteMarker")>***boolean***</[ExpiredObjectDeleteMarker](API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-ExpiredObjectDeleteMarker "API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-ExpiredObjectDeleteMarker")>
         </[Expiration](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Expiration "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Expiration")>
         <[Filter](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Filter "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Filter")>
            <[And](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-And "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-And")>
               <[ObjectSizeGreaterThan](API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-ObjectSizeGreaterThan "API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-ObjectSizeGreaterThan")>***long***</[ObjectSizeGreaterThan](API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-ObjectSizeGreaterThan "API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-ObjectSizeGreaterThan")>
               <[ObjectSizeLessThan](API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-ObjectSizeLessThan "API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-ObjectSizeLessThan")>***long***</[ObjectSizeLessThan](API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-ObjectSizeLessThan "API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-ObjectSizeLessThan")>
               <[Prefix](API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-Prefix "API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-Prefix")>***string***</[Prefix](API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-Prefix "API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-Prefix")>
               <[Tags](API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-Tags "API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-Tags")>
                  <S3Tag>
                     <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>***string***</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
                     <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>***string***</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
                  </S3Tag>
               </[Tags](API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-Tags "API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-Tags")>
            </[And](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-And "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-And")>
            <[ObjectSizeGreaterThan](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-ObjectSizeGreaterThan "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-ObjectSizeGreaterThan")>***long***</[ObjectSizeGreaterThan](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-ObjectSizeGreaterThan "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-ObjectSizeGreaterThan")>
            <[ObjectSizeLessThan](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-ObjectSizeLessThan "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-ObjectSizeLessThan")>***long***</[ObjectSizeLessThan](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-ObjectSizeLessThan "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-ObjectSizeLessThan")>
            <[Prefix](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-Prefix "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-Prefix")>***string***</[Prefix](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-Prefix "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-Prefix")>
            <[Tag](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-Tag "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-Tag")>
               <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>***string***</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
               <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>***string***</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
            </[Tag](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-Tag "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-Tag")>
         </[Filter](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Filter "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Filter")>
         <[ID](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-ID "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-ID")>***string***</[ID](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-ID "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-ID")>
         <[NoncurrentVersionExpiration](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-NoncurrentVersionExpiration "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-NoncurrentVersionExpiration")>
            <[NewerNoncurrentVersions](API_control_NoncurrentVersionExpiration.md#AmazonS3-Type-control_NoncurrentVersionExpiration-NewerNoncurrentVersions "API_control_NoncurrentVersionExpiration.md#AmazonS3-Type-control_NoncurrentVersionExpiration-NewerNoncurrentVersions")>***integer***</[NewerNoncurrentVersions](API_control_NoncurrentVersionExpiration.md#AmazonS3-Type-control_NoncurrentVersionExpiration-NewerNoncurrentVersions "API_control_NoncurrentVersionExpiration.md#AmazonS3-Type-control_NoncurrentVersionExpiration-NewerNoncurrentVersions")>
            <[NoncurrentDays](API_control_NoncurrentVersionExpiration.md#AmazonS3-Type-control_NoncurrentVersionExpiration-NoncurrentDays "API_control_NoncurrentVersionExpiration.md#AmazonS3-Type-control_NoncurrentVersionExpiration-NoncurrentDays")>***integer***</[NoncurrentDays](API_control_NoncurrentVersionExpiration.md#AmazonS3-Type-control_NoncurrentVersionExpiration-NoncurrentDays "API_control_NoncurrentVersionExpiration.md#AmazonS3-Type-control_NoncurrentVersionExpiration-NoncurrentDays")>
         </[NoncurrentVersionExpiration](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-NoncurrentVersionExpiration "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-NoncurrentVersionExpiration")>
         <[NoncurrentVersionTransitions](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-NoncurrentVersionTransitions "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-NoncurrentVersionTransitions")>
            <NoncurrentVersionTransition>
               <[NoncurrentDays](API_control_NoncurrentVersionTransition.md#AmazonS3-Type-control_NoncurrentVersionTransition-NoncurrentDays "API_control_NoncurrentVersionTransition.md#AmazonS3-Type-control_NoncurrentVersionTransition-NoncurrentDays")>***integer***</[NoncurrentDays](API_control_NoncurrentVersionTransition.md#AmazonS3-Type-control_NoncurrentVersionTransition-NoncurrentDays "API_control_NoncurrentVersionTransition.md#AmazonS3-Type-control_NoncurrentVersionTransition-NoncurrentDays")>
               <[StorageClass](API_control_NoncurrentVersionTransition.md#AmazonS3-Type-control_NoncurrentVersionTransition-StorageClass "API_control_NoncurrentVersionTransition.md#AmazonS3-Type-control_NoncurrentVersionTransition-StorageClass")>***string***</[StorageClass](API_control_NoncurrentVersionTransition.md#AmazonS3-Type-control_NoncurrentVersionTransition-StorageClass "API_control_NoncurrentVersionTransition.md#AmazonS3-Type-control_NoncurrentVersionTransition-StorageClass")>
            </NoncurrentVersionTransition>
         </[NoncurrentVersionTransitions](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-NoncurrentVersionTransitions "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-NoncurrentVersionTransitions")>
         <[Status](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Status "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Status")>***string***</[Status](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Status "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Status")>
         <[Transitions](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Transitions "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Transitions")>
            <Transition>
               <[Date](API_control_Transition.md#AmazonS3-Type-control_Transition-Date "API_control_Transition.md#AmazonS3-Type-control_Transition-Date")>***timestamp***</[Date](API_control_Transition.md#AmazonS3-Type-control_Transition-Date "API_control_Transition.md#AmazonS3-Type-control_Transition-Date")>
               <[Days](API_control_Transition.md#AmazonS3-Type-control_Transition-Days "API_control_Transition.md#AmazonS3-Type-control_Transition-Days")>***integer***</[Days](API_control_Transition.md#AmazonS3-Type-control_Transition-Days "API_control_Transition.md#AmazonS3-Type-control_Transition-Days")>
               <[StorageClass](API_control_Transition.md#AmazonS3-Type-control_Transition-StorageClass "API_control_Transition.md#AmazonS3-Type-control_Transition-StorageClass")>***string***</[StorageClass](API_control_Transition.md#AmazonS3-Type-control_Transition-StorageClass "API_control_Transition.md#AmazonS3-Type-control_Transition-StorageClass")>
            </Transition>
         </[Transitions](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Transitions "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Transitions")>
      </Rule>
   </[Rules](#AmazonS3-control_GetBucketLifecycleConfiguration-response-Rules "#AmazonS3-control_GetBucketLifecycleConfiguration-response-Rules")>
</[GetBucketLifecycleConfigurationResult](#AmazonS3-control_GetBucketLifecycleConfiguration-response-GetBucketLifecycleConfigurationResult "#AmazonS3-control_GetBucketLifecycleConfiguration-response-GetBucketLifecycleConfigurationResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetBucketLifecycleConfigurationResult](#API_control_GetBucketLifecycleConfiguration_ResponseSyntax "#API_control_GetBucketLifecycleConfiguration_ResponseSyntax")**


Root level tag for the GetBucketLifecycleConfigurationResult parameters.


Required: Yes




**[Rules](#API_control_GetBucketLifecycleConfiguration_ResponseSyntax "#API_control_GetBucketLifecycleConfiguration_ResponseSyntax")**


Container for the lifecycle rule of the Outposts bucket.


Type: Array of [LifecycleRule](API_control_LifecycleRule.md "API_control_LifecycleRule.md") data types




## Examples


### Sample request to get the lifecycle configuration of the Amazon S3 on Outposts bucket


The following example shows how to get the lifecycle configuration of the
 Outposts bucket.



```

            GET /v20180820/bucket/example-outpost-bucket/lifecycleconfiguration HTTP/1.1
            Host: s3-outposts.<Region>.amazonaws.com 
            x-amz-account-id: example-account-id
            x-amz-outpost-id: op-01ac5d28a6a232904
            x-amz-date: Thu, 15 Nov 2012 00:17:21 GMT
            Authorization: signatureValue
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetBucketLifecycleConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetBucketLifecycleConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetBucketLifecycleConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetBucketLifecycleConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetBucketLifecycleConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetBucketLifecycleConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetBucketLifecycleConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetBucketLifecycleConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetBucketLifecycleConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetBucketLifecycleConfiguration")
