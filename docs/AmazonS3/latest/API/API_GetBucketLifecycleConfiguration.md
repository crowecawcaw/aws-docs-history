# GetBucketLifecycleConfiguration

Returns the lifecycle configuration information set on the bucket. For information about lifecycle
 configuration, see [Object Lifecycle Management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html").

Bucket lifecycle configuration now supports specifying a lifecycle rule using an object key name
 prefix, one or more object tags, object size, or any combination of these. Accordingly, this section
 describes the latest API, which is compatible with the new functionality. The previous version of the
 API supported filtering based only on an object key name prefix, which is supported for general purpose
 buckets for backward compatibility. For the related API description, see [GetBucketLifecycle](API_GetBucketLifecycle.md "API_GetBucketLifecycle.md").

###### Note

Lifecyle configurations for directory buckets only support expiring objects and cancelling
 multipart uploads. Expiring of versioned objects, transitions and tag filters are not
 supported.



Permissions


* **General purpose bucket permissions** - By default, all Amazon S3
 resources are private, including buckets, objects, and related subresources (for example,
 lifecycle configuration and website configuration). Only the resource owner (that is, the
 AWS account that created it) can access the resource. The resource owner can optionally
 grant access permissions to others by writing an access policy. For this operation, a user
 must have the `s3:GetLifecycleConfiguration` permission.


For more information about permissions, see [Managing Access Permissions to Your
 Amazon S3 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md").


* **Directory bucket permissions** - You must have the
 `s3express:GetLifecycleConfiguration` permission in an IAM identity-based policy
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




`GetBucketLifecycleConfiguration` has the following special error:


* Error code: `NoSuchLifecycleConfiguration`





	+ Description: The lifecycle configuration does not exist.
	+ HTTP Status Code: 404 Not Found
	+ SOAP Fault Code Prefix: Client
The following operations are related to `GetBucketLifecycleConfiguration`:


* [GetBucketLifecycle](API_GetBucketLifecycle.md "API_GetBucketLifecycle.md")
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





**[Bucket](#API_GetBucketLifecycleConfiguration_RequestSyntax "#API_GetBucketLifecycleConfiguration_RequestSyntax")**


The name of the bucket for which to get the lifecycle information.


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetBucketLifecycleConfiguration_RequestSyntax "#API_GetBucketLifecycleConfiguration_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).


###### Note

This parameter applies to general purpose buckets only. It is not supported for directory bucket
 lifecycle configurations.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
x-amz-transition-default-minimum-object-size: `TransitionDefaultMinimumObjectSize`
<?xml version="1.0" encoding="UTF-8"?>
<[LifecycleConfiguration](#AmazonS3-GetBucketLifecycleConfiguration-response-GetBucketLifecycleConfigurationOutput "#AmazonS3-GetBucketLifecycleConfiguration-response-GetBucketLifecycleConfigurationOutput")>
   <[Rule](#AmazonS3-GetBucketLifecycleConfiguration-response-Rules "#AmazonS3-GetBucketLifecycleConfiguration-response-Rules")>
      <[AbortIncompleteMultipartUpload](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-AbortIncompleteMultipartUpload "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-AbortIncompleteMultipartUpload")>
         <[DaysAfterInitiation](API_AbortIncompleteMultipartUpload.md#AmazonS3-Type-AbortIncompleteMultipartUpload-DaysAfterInitiation "API_AbortIncompleteMultipartUpload.md#AmazonS3-Type-AbortIncompleteMultipartUpload-DaysAfterInitiation")>***integer***</[DaysAfterInitiation](API_AbortIncompleteMultipartUpload.md#AmazonS3-Type-AbortIncompleteMultipartUpload-DaysAfterInitiation "API_AbortIncompleteMultipartUpload.md#AmazonS3-Type-AbortIncompleteMultipartUpload-DaysAfterInitiation")>
      </[AbortIncompleteMultipartUpload](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-AbortIncompleteMultipartUpload "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-AbortIncompleteMultipartUpload")>
      <[Expiration](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Expiration "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Expiration")>
         <[Date](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Date "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Date")>***timestamp***</[Date](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Date "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Date")>
         <[Days](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Days "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Days")>***integer***</[Days](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Days "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Days")>
         <[ExpiredObjectDeleteMarker](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-ExpiredObjectDeleteMarker "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-ExpiredObjectDeleteMarker")>***boolean***</[ExpiredObjectDeleteMarker](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-ExpiredObjectDeleteMarker "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-ExpiredObjectDeleteMarker")>
      </[Expiration](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Expiration "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Expiration")>
      <[Filter](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Filter "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Filter")>
         <[And](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-And "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-And")>
            <[ObjectSizeGreaterThan](API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-ObjectSizeGreaterThan "API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-ObjectSizeGreaterThan")>***long***</[ObjectSizeGreaterThan](API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-ObjectSizeGreaterThan "API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-ObjectSizeGreaterThan")>
            <[ObjectSizeLessThan](API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-ObjectSizeLessThan "API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-ObjectSizeLessThan")>***long***</[ObjectSizeLessThan](API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-ObjectSizeLessThan "API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-ObjectSizeLessThan")>
            <[Prefix](API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-Prefix "API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-Prefix")>***string***</[Prefix](API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-Prefix "API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-Prefix")>
            <[Tag](API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-Tags "API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-Tags")>
               <[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>***string***</[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>
               <[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>***string***</[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>
            </[Tag](API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-Tags "API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-Tags")>
            ...
         </[And](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-And "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-And")>
         <[ObjectSizeGreaterThan](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-ObjectSizeGreaterThan "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-ObjectSizeGreaterThan")>***long***</[ObjectSizeGreaterThan](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-ObjectSizeGreaterThan "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-ObjectSizeGreaterThan")>
         <[ObjectSizeLessThan](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-ObjectSizeLessThan "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-ObjectSizeLessThan")>***long***</[ObjectSizeLessThan](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-ObjectSizeLessThan "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-ObjectSizeLessThan")>
         <[Prefix](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-Prefix "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-Prefix")>***string***</[Prefix](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-Prefix "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-Prefix")>
         <[Tag](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-Tag "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-Tag")>
            <[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>***string***</[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>
            <[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>***string***</[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>
         </[Tag](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-Tag "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-Tag")>
      </[Filter](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Filter "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Filter")>
      <[ID](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-ID "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-ID")>***string***</[ID](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-ID "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-ID")>
      <[NoncurrentVersionExpiration](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-NoncurrentVersionExpiration "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-NoncurrentVersionExpiration")>
         <[NewerNoncurrentVersions](API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NewerNoncurrentVersions "API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NewerNoncurrentVersions")>***integer***</[NewerNoncurrentVersions](API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NewerNoncurrentVersions "API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NewerNoncurrentVersions")>
         <[NoncurrentDays](API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NoncurrentDays "API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NoncurrentDays")>***integer***</[NoncurrentDays](API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NoncurrentDays "API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NoncurrentDays")>
      </[NoncurrentVersionExpiration](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-NoncurrentVersionExpiration "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-NoncurrentVersionExpiration")>
      <[NoncurrentVersionTransition](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-NoncurrentVersionTransitions "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-NoncurrentVersionTransitions")>
         <[NewerNoncurrentVersions](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NewerNoncurrentVersions "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NewerNoncurrentVersions")>***integer***</[NewerNoncurrentVersions](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NewerNoncurrentVersions "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NewerNoncurrentVersions")>
         <[NoncurrentDays](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NoncurrentDays "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NoncurrentDays")>***integer***</[NoncurrentDays](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NoncurrentDays "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NoncurrentDays")>
         <[StorageClass](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-StorageClass "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-StorageClass")>***string***</[StorageClass](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-StorageClass "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-StorageClass")>
      </[NoncurrentVersionTransition](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-NoncurrentVersionTransitions "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-NoncurrentVersionTransitions")>
      ...
      <[Prefix](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Prefix "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Prefix")>***string***</[Prefix](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Prefix "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Prefix")>
      <[Status](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Status "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Status")>***string***</[Status](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Status "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Status")>
      <[Transition](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Transitions "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Transitions")>
         <[Date](API_Transition.md#AmazonS3-Type-Transition-Date "API_Transition.md#AmazonS3-Type-Transition-Date")>***timestamp***</[Date](API_Transition.md#AmazonS3-Type-Transition-Date "API_Transition.md#AmazonS3-Type-Transition-Date")>
         <[Days](API_Transition.md#AmazonS3-Type-Transition-Days "API_Transition.md#AmazonS3-Type-Transition-Days")>***integer***</[Days](API_Transition.md#AmazonS3-Type-Transition-Days "API_Transition.md#AmazonS3-Type-Transition-Days")>
         <[StorageClass](API_Transition.md#AmazonS3-Type-Transition-StorageClass "API_Transition.md#AmazonS3-Type-Transition-StorageClass")>***string***</[StorageClass](API_Transition.md#AmazonS3-Type-Transition-StorageClass "API_Transition.md#AmazonS3-Type-Transition-StorageClass")>
      </[Transition](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Transitions "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Transitions")>
      ...
   </[Rule](#AmazonS3-GetBucketLifecycleConfiguration-response-Rules "#AmazonS3-GetBucketLifecycleConfiguration-response-Rules")>
   ...
</[LifecycleConfiguration](#AmazonS3-GetBucketLifecycleConfiguration-response-GetBucketLifecycleConfigurationOutput "#AmazonS3-GetBucketLifecycleConfiguration-response-GetBucketLifecycleConfigurationOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[x-amz-transition-default-minimum-object-size](#API_GetBucketLifecycleConfiguration_ResponseSyntax "#API_GetBucketLifecycleConfiguration_ResponseSyntax")**


Indicates which default minimum object size behavior is applied to the lifecycle
 configuration.


###### Note

This parameter applies to general purpose buckets only. It isn't supported for directory bucket
 lifecycle configurations.



* `all_storage_classes_128K` - Objects smaller than 128 KB will not transition to
 any storage class by default.
* `varies_by_storage_class` - Objects smaller than 128 KB will transition to Glacier
 Flexible Retrieval or Glacier Deep Archive storage classes. By default, all other storage classes
 will prevent transitions smaller than 128 KB.

To customize the minimum object size for any transition you can add a filter that specifies a custom
 `ObjectSizeGreaterThan` or `ObjectSizeLessThan` in the body of your transition
 rule. Custom filters always take precedence over the default transition behavior.


Valid Values: `varies_by_storage_class | all_storage_classes_128K`





The following data is returned in XML format by the service.





**[LifecycleConfiguration](#API_GetBucketLifecycleConfiguration_ResponseSyntax "#API_GetBucketLifecycleConfiguration_ResponseSyntax")**


Root level tag for the LifecycleConfiguration parameters.


Required: Yes




**[Rule](#API_GetBucketLifecycleConfiguration_ResponseSyntax "#API_GetBucketLifecycleConfiguration_ResponseSyntax")**


Container for a lifecycle rule.


Type: Array of [LifecycleRule](API_LifecycleRule.md "API_LifecycleRule.md") data types




## Examples


### Example 1: Get lifecycle configuration - general purpose bucket


This example illustrates how to use `GetBucketLifecycleConfiguration` to retrieve the
 lifecycle configuration for a general purpose bucket:



```
GET /?lifecycle HTTP/1.1
Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
x-amz-date: Thu, 15 Nov 2012 00:17:21 GMT
Authorization: signatureValue
         
```

### Sample Response


This example shows the response from the preceeding `GetBucketLifecycleConfiguration`
 request:



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

### Example 2: Get lifecycle configuration - directory bucket


This example illustrates how to use `GetBucketLifecycleConfiguration` to retrieve the
 lifecycle configuration for a directory bucket:



```
GET /?lifecycle HTTP/1.1
Host:s3express-control.us-west-2.amazonaws.com
           
```

### Sample Response


This example shows the response from the preceeding `GetBucketLifecycleConfiguration`
 request:



```

<?xml version="1.0" encoding="UTF-8"?>
<LifecycleConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <Rule>
      <ID>Lifecycle expiration rule</ID>
      <Filter>
         <And>
            <Prefix>myprefix/</Prefix>
            <ObjectSizeGreaterThan>500</ObjectSizeGreaterThan>
            <ObjectSizeLessThan>64000</ObjectSizeLessThan>
         </And>
      </Filter>
      <Status>Enabled</Status>
      <Expiration>
         <Days>7</Days>
      </Expiration>
   </Rule>
   <Rule>
      <ID>MPU Rule </ID>
      <Filter>
         <Prefix>another_prefix </Prefix>
      </Filter>
      <Status>Enabled</Status>
      <AbortIncompleteMultipartUpload>
         <DaysAfterInitiation>3</DaysAfterInitiation>
      </AbortIncompleteMultipartUpload>
   </Rule>
</LifecycleConfiguration>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketLifecycleConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketLifecycleConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketLifecycleConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketLifecycleConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketLifecycleConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketLifecycleConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketLifecycleConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketLifecycleConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketLifecycleConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketLifecycleConfiguration")
