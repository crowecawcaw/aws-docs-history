# GetBucketLifecycle

###### Important

For an updated version of this API, see [GetBucketLifecycleConfiguration](API_GetBucketLifecycleConfiguration.md "API_GetBucketLifecycleConfiguration.md"). If you configured a bucket lifecycle using the
 `filter` element, you should see the updated version of this topic. This topic is
 provided for backward compatibility.

###### Note

This operation is not supported for directory buckets.

Returns the lifecycle configuration information set on the bucket. For information about lifecycle
 configuration, see [Object Lifecycle Management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html").

 To use this operation, you must have permission to perform the
 `s3:GetLifecycleConfiguration` action. The bucket owner has this permission by default. The
 bucket owner can grant this permission to others. For more information about permissions, see [Permissions Related to Bucket Subresource Operations](../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources "../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources") and [Managing Access Permissions to Your Amazon S3
 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md").


`GetBucketLifecycle` has the following special error:


* Error code: `NoSuchLifecycleConfiguration`





	+ Description: The lifecycle configuration does not exist.
	+ HTTP Status Code: 404 Not Found
	+ SOAP Fault Code Prefix: Client
The following operations are related to `GetBucketLifecycle`:


* [GetBucketLifecycleConfiguration](API_GetBucketLifecycleConfiguration.md "API_GetBucketLifecycleConfiguration.md")
* [PutBucketLifecycle](API_PutBucketLifecycle.md "API_PutBucketLifecycle.md")
* [DeleteBucketLifecycle](API_DeleteBucketLifecycle.md "API_DeleteBucketLifecycle.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?lifecycle HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetBucketLifecycle_RequestSyntax "#API_GetBucketLifecycle_RequestSyntax")**


The name of the bucket for which to get the lifecycle information.


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetBucketLifecycle_RequestSyntax "#API_GetBucketLifecycle_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[LifecycleConfiguration](#AmazonS3-GetBucketLifecycle-response-GetBucketLifecycleOutput "#AmazonS3-GetBucketLifecycle-response-GetBucketLifecycleOutput")>
   <[Rule](#AmazonS3-GetBucketLifecycle-response-Rules "#AmazonS3-GetBucketLifecycle-response-Rules")>
      <[AbortIncompleteMultipartUpload](API_Rule.md#AmazonS3-Type-Rule-AbortIncompleteMultipartUpload "API_Rule.md#AmazonS3-Type-Rule-AbortIncompleteMultipartUpload")>
         <[DaysAfterInitiation](API_AbortIncompleteMultipartUpload.md#AmazonS3-Type-AbortIncompleteMultipartUpload-DaysAfterInitiation "API_AbortIncompleteMultipartUpload.md#AmazonS3-Type-AbortIncompleteMultipartUpload-DaysAfterInitiation")>***integer***</[DaysAfterInitiation](API_AbortIncompleteMultipartUpload.md#AmazonS3-Type-AbortIncompleteMultipartUpload-DaysAfterInitiation "API_AbortIncompleteMultipartUpload.md#AmazonS3-Type-AbortIncompleteMultipartUpload-DaysAfterInitiation")>
      </[AbortIncompleteMultipartUpload](API_Rule.md#AmazonS3-Type-Rule-AbortIncompleteMultipartUpload "API_Rule.md#AmazonS3-Type-Rule-AbortIncompleteMultipartUpload")>
      <[Expiration](API_Rule.md#AmazonS3-Type-Rule-Expiration "API_Rule.md#AmazonS3-Type-Rule-Expiration")>
         <[Date](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Date "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Date")>***timestamp***</[Date](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Date "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Date")>
         <[Days](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Days "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Days")>***integer***</[Days](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Days "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Days")>
         <[ExpiredObjectDeleteMarker](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-ExpiredObjectDeleteMarker "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-ExpiredObjectDeleteMarker")>***boolean***</[ExpiredObjectDeleteMarker](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-ExpiredObjectDeleteMarker "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-ExpiredObjectDeleteMarker")>
      </[Expiration](API_Rule.md#AmazonS3-Type-Rule-Expiration "API_Rule.md#AmazonS3-Type-Rule-Expiration")>
      <[ID](API_Rule.md#AmazonS3-Type-Rule-ID "API_Rule.md#AmazonS3-Type-Rule-ID")>***string***</[ID](API_Rule.md#AmazonS3-Type-Rule-ID "API_Rule.md#AmazonS3-Type-Rule-ID")>
      <[NoncurrentVersionExpiration](API_Rule.md#AmazonS3-Type-Rule-NoncurrentVersionExpiration "API_Rule.md#AmazonS3-Type-Rule-NoncurrentVersionExpiration")>
         <[NewerNoncurrentVersions](API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NewerNoncurrentVersions "API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NewerNoncurrentVersions")>***integer***</[NewerNoncurrentVersions](API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NewerNoncurrentVersions "API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NewerNoncurrentVersions")>
         <[NoncurrentDays](API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NoncurrentDays "API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NoncurrentDays")>***integer***</[NoncurrentDays](API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NoncurrentDays "API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NoncurrentDays")>
      </[NoncurrentVersionExpiration](API_Rule.md#AmazonS3-Type-Rule-NoncurrentVersionExpiration "API_Rule.md#AmazonS3-Type-Rule-NoncurrentVersionExpiration")>
      <[NoncurrentVersionTransition](API_Rule.md#AmazonS3-Type-Rule-NoncurrentVersionTransition "API_Rule.md#AmazonS3-Type-Rule-NoncurrentVersionTransition")>
         <[NewerNoncurrentVersions](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NewerNoncurrentVersions "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NewerNoncurrentVersions")>***integer***</[NewerNoncurrentVersions](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NewerNoncurrentVersions "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NewerNoncurrentVersions")>
         <[NoncurrentDays](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NoncurrentDays "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NoncurrentDays")>***integer***</[NoncurrentDays](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NoncurrentDays "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NoncurrentDays")>
         <[StorageClass](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-StorageClass "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-StorageClass")>***string***</[StorageClass](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-StorageClass "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-StorageClass")>
      </[NoncurrentVersionTransition](API_Rule.md#AmazonS3-Type-Rule-NoncurrentVersionTransition "API_Rule.md#AmazonS3-Type-Rule-NoncurrentVersionTransition")>
      <[Prefix](API_Rule.md#AmazonS3-Type-Rule-Prefix "API_Rule.md#AmazonS3-Type-Rule-Prefix")>***string***</[Prefix](API_Rule.md#AmazonS3-Type-Rule-Prefix "API_Rule.md#AmazonS3-Type-Rule-Prefix")>
      <[Status](API_Rule.md#AmazonS3-Type-Rule-Status "API_Rule.md#AmazonS3-Type-Rule-Status")>***string***</[Status](API_Rule.md#AmazonS3-Type-Rule-Status "API_Rule.md#AmazonS3-Type-Rule-Status")>
      <[Transition](API_Rule.md#AmazonS3-Type-Rule-Transition "API_Rule.md#AmazonS3-Type-Rule-Transition")>
         <[Date](API_Transition.md#AmazonS3-Type-Transition-Date "API_Transition.md#AmazonS3-Type-Transition-Date")>***timestamp***</[Date](API_Transition.md#AmazonS3-Type-Transition-Date "API_Transition.md#AmazonS3-Type-Transition-Date")>
         <[Days](API_Transition.md#AmazonS3-Type-Transition-Days "API_Transition.md#AmazonS3-Type-Transition-Days")>***integer***</[Days](API_Transition.md#AmazonS3-Type-Transition-Days "API_Transition.md#AmazonS3-Type-Transition-Days")>
         <[StorageClass](API_Transition.md#AmazonS3-Type-Transition-StorageClass "API_Transition.md#AmazonS3-Type-Transition-StorageClass")>***string***</[StorageClass](API_Transition.md#AmazonS3-Type-Transition-StorageClass "API_Transition.md#AmazonS3-Type-Transition-StorageClass")>
      </[Transition](API_Rule.md#AmazonS3-Type-Rule-Transition "API_Rule.md#AmazonS3-Type-Rule-Transition")>
   </[Rule](#AmazonS3-GetBucketLifecycle-response-Rules "#AmazonS3-GetBucketLifecycle-response-Rules")>
   ...
</[LifecycleConfiguration](#AmazonS3-GetBucketLifecycle-response-GetBucketLifecycleOutput "#AmazonS3-GetBucketLifecycle-response-GetBucketLifecycleOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[LifecycleConfiguration](#API_GetBucketLifecycle_ResponseSyntax "#API_GetBucketLifecycle_ResponseSyntax")**


Root level tag for the LifecycleConfiguration parameters.


Required: Yes




**[Rule](#API_GetBucketLifecycle_ResponseSyntax "#API_GetBucketLifecycle_ResponseSyntax")**


Container for a lifecycle rule.


Type: Array of [Rule](API_Rule.md "API_Rule.md") data types




## Examples


### Sample Request: Retrieve a lifecycle subresource


This example is a GET request to retrieve the lifecycle subresource from the specified bucket,
 and an example response with the returned lifecycle configuration. 



```

            GET /?lifecycle HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            x-amz-date: Thu, 15 Nov 2012 00:17:21 GMT
            Authorization: signatureValue
         
```

### Sample Response


This example illustrates one usage of GetBucketLifecycle.



```

            HTTP/1.1 200 OK
            x-amz-id-2: ITnGT1y4RyTmXa3rPi4hklTXouTf0hccUjo0iCPjz6FnfIutBj3M7fPGlWO2SEWp
            x-amz-request-id: 51991C342C575321
            Date: Thu, 15 Nov 2012 00:17:23 GMT
            Server: AmazonS3
            Content-Length: 358

            <?xml version="1.0" encoding="UTF-8"?>
            <LifecycleConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
               <Rule>
                    <ID>Archive and then delete rule</ID>
                    <Prefix>projectdocs/</Prefix>
                   <Status>Enabled</Status>
                  <Transition>
                       <Days>30</Days>
                       <StorageClass>STANDARD_IA</StorageClass>
                  </Transition>
                  <Transition>
                     <Days>365</Days>
                      <StorageClass>GLACIER</StorageClass>
                   </Transition>
                   <Expiration>
                      <Days>3650</Days>
                   </Expiration>
               </Rule>
            </LifecycleConfiguration>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketLifecycle "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketLifecycle")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketLifecycle "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketLifecycle")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketLifecycle")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketLifecycle")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketLifecycle")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketLifecycle")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketLifecycle")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketLifecycle")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketLifecycle "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketLifecycle")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketLifecycle")
