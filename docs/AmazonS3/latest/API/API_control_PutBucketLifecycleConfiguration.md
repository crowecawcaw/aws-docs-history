# PutBucketLifecycleConfiguration

###### Note

This action puts a lifecycle configuration to an Amazon S3 on Outposts bucket. To put a
 lifecycle configuration to an S3 bucket, see [PutBucketLifecycleConfiguration](API_PutBucketLifecycleConfiguration.md "API_PutBucketLifecycleConfiguration.md") in the *Amazon S3 API Reference*.
 

Creates a new lifecycle configuration for the S3 on Outposts bucket or replaces an
 existing lifecycle configuration. Outposts buckets only support lifecycle configurations
 that delete/expire objects after a certain period of time and abort incomplete multipart
 uploads.

All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](API_control_PutBucketLifecycleConfiguration.md#API_control_PutBucketLifecycleConfiguration_Examples "API_control_PutBucketLifecycleConfiguration.md#API_control_PutBucketLifecycleConfiguration_Examples") section.

The following actions are related to
 `PutBucketLifecycleConfiguration`:


* [GetBucketLifecycleConfiguration](API_control_GetBucketLifecycleConfiguration.md "API_control_GetBucketLifecycleConfiguration.md")
* [DeleteBucketLifecycleConfiguration](API_control_DeleteBucketLifecycleConfiguration.md "API_control_DeleteBucketLifecycleConfiguration.md")

## Request Syntax



```
PUT /v20180820/bucket/`name`/lifecycleconfiguration HTTP/1.1
Host: `Bucket`.s3-control.amazonaws.com
x-amz-account-id: `AccountId`
<?xml version="1.0" encoding="UTF-8"?>
<[LifecycleConfiguration](#AmazonS3-control_PutBucketLifecycleConfiguration-request-LifecycleConfiguration "#AmazonS3-control_PutBucketLifecycleConfiguration-request-LifecycleConfiguration") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[Rules](#AmazonS3-control_PutBucketLifecycleConfiguration-request-Rules "#AmazonS3-control_PutBucketLifecycleConfiguration-request-Rules")>
      <Rule>
         <[AbortIncompleteMultipartUpload](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-AbortIncompleteMultipartUpload "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-AbortIncompleteMultipartUpload")>
            <[DaysAfterInitiation](API_control_AbortIncompleteMultipartUpload.md#AmazonS3-Type-control_AbortIncompleteMultipartUpload-DaysAfterInitiation "API_control_AbortIncompleteMultipartUpload.md#AmazonS3-Type-control_AbortIncompleteMultipartUpload-DaysAfterInitiation")>`integer`</[DaysAfterInitiation](API_control_AbortIncompleteMultipartUpload.md#AmazonS3-Type-control_AbortIncompleteMultipartUpload-DaysAfterInitiation "API_control_AbortIncompleteMultipartUpload.md#AmazonS3-Type-control_AbortIncompleteMultipartUpload-DaysAfterInitiation")>
         </[AbortIncompleteMultipartUpload](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-AbortIncompleteMultipartUpload "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-AbortIncompleteMultipartUpload")>
         <[Expiration](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Expiration "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Expiration")>
            <[Date](API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-Date "API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-Date")>`timestamp`</[Date](API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-Date "API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-Date")>
            <[Days](API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-Days "API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-Days")>`integer`</[Days](API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-Days "API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-Days")>
            <[ExpiredObjectDeleteMarker](API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-ExpiredObjectDeleteMarker "API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-ExpiredObjectDeleteMarker")>`boolean`</[ExpiredObjectDeleteMarker](API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-ExpiredObjectDeleteMarker "API_control_LifecycleExpiration.md#AmazonS3-Type-control_LifecycleExpiration-ExpiredObjectDeleteMarker")>
         </[Expiration](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Expiration "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Expiration")>
         <[Filter](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Filter "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Filter")>
            <[And](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-And "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-And")>
               <[ObjectSizeGreaterThan](API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-ObjectSizeGreaterThan "API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-ObjectSizeGreaterThan")>`long`</[ObjectSizeGreaterThan](API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-ObjectSizeGreaterThan "API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-ObjectSizeGreaterThan")>
               <[ObjectSizeLessThan](API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-ObjectSizeLessThan "API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-ObjectSizeLessThan")>`long`</[ObjectSizeLessThan](API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-ObjectSizeLessThan "API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-ObjectSizeLessThan")>
               <[Prefix](API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-Prefix "API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-Prefix")>`string`</[Prefix](API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-Prefix "API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-Prefix")>
               <[Tags](API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-Tags "API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-Tags")>
                  <S3Tag>
                     <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>`string`</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
                     <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>`string`</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
                  </S3Tag>
               </[Tags](API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-Tags "API_control_LifecycleRuleAndOperator.md#AmazonS3-Type-control_LifecycleRuleAndOperator-Tags")>
            </[And](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-And "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-And")>
            <[ObjectSizeGreaterThan](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-ObjectSizeGreaterThan "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-ObjectSizeGreaterThan")>`long`</[ObjectSizeGreaterThan](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-ObjectSizeGreaterThan "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-ObjectSizeGreaterThan")>
            <[ObjectSizeLessThan](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-ObjectSizeLessThan "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-ObjectSizeLessThan")>`long`</[ObjectSizeLessThan](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-ObjectSizeLessThan "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-ObjectSizeLessThan")>
            <[Prefix](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-Prefix "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-Prefix")>`string`</[Prefix](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-Prefix "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-Prefix")>
            <[Tag](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-Tag "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-Tag")>
               <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>`string`</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
               <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>`string`</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
            </[Tag](API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-Tag "API_control_LifecycleRuleFilter.md#AmazonS3-Type-control_LifecycleRuleFilter-Tag")>
         </[Filter](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Filter "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Filter")>
         <[ID](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-ID "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-ID")>`string`</[ID](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-ID "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-ID")>
         <[NoncurrentVersionExpiration](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-NoncurrentVersionExpiration "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-NoncurrentVersionExpiration")>
            <[NewerNoncurrentVersions](API_control_NoncurrentVersionExpiration.md#AmazonS3-Type-control_NoncurrentVersionExpiration-NewerNoncurrentVersions "API_control_NoncurrentVersionExpiration.md#AmazonS3-Type-control_NoncurrentVersionExpiration-NewerNoncurrentVersions")>`integer`</[NewerNoncurrentVersions](API_control_NoncurrentVersionExpiration.md#AmazonS3-Type-control_NoncurrentVersionExpiration-NewerNoncurrentVersions "API_control_NoncurrentVersionExpiration.md#AmazonS3-Type-control_NoncurrentVersionExpiration-NewerNoncurrentVersions")>
            <[NoncurrentDays](API_control_NoncurrentVersionExpiration.md#AmazonS3-Type-control_NoncurrentVersionExpiration-NoncurrentDays "API_control_NoncurrentVersionExpiration.md#AmazonS3-Type-control_NoncurrentVersionExpiration-NoncurrentDays")>`integer`</[NoncurrentDays](API_control_NoncurrentVersionExpiration.md#AmazonS3-Type-control_NoncurrentVersionExpiration-NoncurrentDays "API_control_NoncurrentVersionExpiration.md#AmazonS3-Type-control_NoncurrentVersionExpiration-NoncurrentDays")>
         </[NoncurrentVersionExpiration](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-NoncurrentVersionExpiration "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-NoncurrentVersionExpiration")>
         <[NoncurrentVersionTransitions](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-NoncurrentVersionTransitions "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-NoncurrentVersionTransitions")>
            <NoncurrentVersionTransition>
               <[NoncurrentDays](API_control_NoncurrentVersionTransition.md#AmazonS3-Type-control_NoncurrentVersionTransition-NoncurrentDays "API_control_NoncurrentVersionTransition.md#AmazonS3-Type-control_NoncurrentVersionTransition-NoncurrentDays")>`integer`</[NoncurrentDays](API_control_NoncurrentVersionTransition.md#AmazonS3-Type-control_NoncurrentVersionTransition-NoncurrentDays "API_control_NoncurrentVersionTransition.md#AmazonS3-Type-control_NoncurrentVersionTransition-NoncurrentDays")>
               <[StorageClass](API_control_NoncurrentVersionTransition.md#AmazonS3-Type-control_NoncurrentVersionTransition-StorageClass "API_control_NoncurrentVersionTransition.md#AmazonS3-Type-control_NoncurrentVersionTransition-StorageClass")>`string`</[StorageClass](API_control_NoncurrentVersionTransition.md#AmazonS3-Type-control_NoncurrentVersionTransition-StorageClass "API_control_NoncurrentVersionTransition.md#AmazonS3-Type-control_NoncurrentVersionTransition-StorageClass")>
            </NoncurrentVersionTransition>
         </[NoncurrentVersionTransitions](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-NoncurrentVersionTransitions "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-NoncurrentVersionTransitions")>
         <[Status](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Status "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Status")>`string`</[Status](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Status "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Status")>
         <[Transitions](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Transitions "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Transitions")>
            <Transition>
               <[Date](API_control_Transition.md#AmazonS3-Type-control_Transition-Date "API_control_Transition.md#AmazonS3-Type-control_Transition-Date")>`timestamp`</[Date](API_control_Transition.md#AmazonS3-Type-control_Transition-Date "API_control_Transition.md#AmazonS3-Type-control_Transition-Date")>
               <[Days](API_control_Transition.md#AmazonS3-Type-control_Transition-Days "API_control_Transition.md#AmazonS3-Type-control_Transition-Days")>`integer`</[Days](API_control_Transition.md#AmazonS3-Type-control_Transition-Days "API_control_Transition.md#AmazonS3-Type-control_Transition-Days")>
               <[StorageClass](API_control_Transition.md#AmazonS3-Type-control_Transition-StorageClass "API_control_Transition.md#AmazonS3-Type-control_Transition-StorageClass")>`string`</[StorageClass](API_control_Transition.md#AmazonS3-Type-control_Transition-StorageClass "API_control_Transition.md#AmazonS3-Type-control_Transition-StorageClass")>
            </Transition>
         </[Transitions](API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Transitions "API_control_LifecycleRule.md#AmazonS3-Type-control_LifecycleRule-Transitions")>
      </Rule>
   </[Rules](#AmazonS3-control_PutBucketLifecycleConfiguration-request-Rules "#AmazonS3-control_PutBucketLifecycleConfiguration-request-Rules")>
</[LifecycleConfiguration](#AmazonS3-control_PutBucketLifecycleConfiguration-request-LifecycleConfiguration "#AmazonS3-control_PutBucketLifecycleConfiguration-request-LifecycleConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_PutBucketLifecycleConfiguration_RequestSyntax "#API_control_PutBucketLifecycleConfiguration_RequestSyntax")**


The name of the bucket for which to set the configuration.


Length Constraints: Minimum length of 3. Maximum length of 255.


Required: Yes




**[x-amz-account-id](#API_control_PutBucketLifecycleConfiguration_RequestSyntax "#API_control_PutBucketLifecycleConfiguration_RequestSyntax")**


The AWS account ID of the Outposts bucket.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[LifecycleConfiguration](#API_control_PutBucketLifecycleConfiguration_RequestSyntax "#API_control_PutBucketLifecycleConfiguration_RequestSyntax")**


Root level tag for the LifecycleConfiguration parameters.


Required: Yes




**[Rules](#API_control_PutBucketLifecycleConfiguration_RequestSyntax "#API_control_PutBucketLifecycleConfiguration_RequestSyntax")**


A lifecycle rule for individual objects in an Outposts bucket. 


Type: Array of [LifecycleRule](API_control_LifecycleRule.md "API_control_LifecycleRule.md") data types


Required: No




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Sample PutBucketLifecycleConfiguration request on an Amazon S3 on Outposts
 bucket


This request puts a lifecycle configuration on an Outposts bucket named
 `example-outpost-bucket`.



```

            PUT /v20180820/bucket/example-outpost-bucket/lifecycleconfiguration HTTP/1.1
            Host:s3-outposts.<Region>.amazonaws.com
            x-amz-account-id: example-account-id
            x-amz-outpost-id: op-01ac5d28a6a232904
            Content-Length: 0
            Date: Wed, 01 Mar  2006 12:00:00 GMT
            Content-MD5: q6yJDlIkcBaGGfb3QLY69A==
            Authorization: authorization string
            Content-Length: 214
            
            <LifecycleConfiguration>
              <Rule>
                <ID>id2</ID>
                <Filter>
                   <Prefix>logs/</Prefix>
                </Filter>
                <Status>Enabled</Status>
                <Expiration>
                  <Days>365</Days>
                </Expiration>
              </Rule>
            </LifecycleConfiguration>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutBucketLifecycleConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/PutBucketLifecycleConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutBucketLifecycleConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutBucketLifecycleConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutBucketLifecycleConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutBucketLifecycleConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutBucketLifecycleConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutBucketLifecycleConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutBucketLifecycleConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutBucketLifecycleConfiguration")
