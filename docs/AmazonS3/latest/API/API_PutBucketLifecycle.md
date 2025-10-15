# PutBucketLifecycle

###### Note

This operation is not supported for directory buckets.

###### Important

For an updated version of this API, see [PutBucketLifecycleConfiguration](API_PutBucketLifecycleConfiguration.md "API_PutBucketLifecycleConfiguration.md"). This version has been deprecated. Existing lifecycle
 configurations will work. For new lifecycle configurations, use the updated API. 

###### Note

This operation is not supported for directory buckets.

Creates a new lifecycle configuration for the bucket or replaces an existing lifecycle
 configuration. For information about lifecycle configuration, see [Object Lifecycle Management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html") in the
 *Amazon S3 User Guide*. 

By default, all Amazon S3 resources, including buckets, objects, and related subresources (for example,
 lifecycle configuration and website configuration) are private. Only the resource owner, the
 AWS account that created the resource, can access it. The resource owner can optionally grant access
 permissions to others by writing an access policy. For this operation, users must get the
 `s3:PutLifecycleConfiguration` permission.

You can also explicitly deny permissions. Explicit denial also supersedes any other permissions. If
 you want to prevent users or accounts from removing or deleting objects from your bucket, you must deny
 them permissions for the following actions: 


* `s3:DeleteObject`
* `s3:DeleteObjectVersion`
* `s3:PutLifecycleConfiguration`
For more information about permissions, see [Managing Access Permissions to your Amazon S3
 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md") in the *Amazon S3 User Guide*.

For more examples of transitioning objects to storage classes such as STANDARD\_IA or ONEZONE\_IA, see
 [Examples of
 Lifecycle Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#lifecycle-configuration-examples "https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#lifecycle-configuration-examples").

The following operations are related to `PutBucketLifecycle`:


* [GetBucketLifecycle](API_GetBucketLifecycle.md "API_GetBucketLifecycle.md")(Deprecated)
* [GetBucketLifecycleConfiguration](API_GetBucketLifecycleConfiguration.md "API_GetBucketLifecycleConfiguration.md")
* [RestoreObject](API_RestoreObject.md "API_RestoreObject.md")
* By default, a resource owner—in this case, a bucket owner, which is the AWS account that
 created the bucket—can perform any of the operations. A resource owner can also grant others
 permission to perform the operation. For more information, see the following topics in the
 Amazon S3 User Guide: 




	+ [Specifying
	 Permissions in a Policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html")
	+ [Managing
	 Access Permissions to your Amazon S3 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /?lifecycle HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
Content-MD5: `ContentMD5`
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[LifecycleConfiguration](#AmazonS3-PutBucketLifecycle-request-LifecycleConfiguration "#AmazonS3-PutBucketLifecycle-request-LifecycleConfiguration") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[Rule](#AmazonS3-PutBucketLifecycle-request-Rules "#AmazonS3-PutBucketLifecycle-request-Rules")>
      <[AbortIncompleteMultipartUpload](API_Rule.md#AmazonS3-Type-Rule-AbortIncompleteMultipartUpload "API_Rule.md#AmazonS3-Type-Rule-AbortIncompleteMultipartUpload")>
         <[DaysAfterInitiation](API_AbortIncompleteMultipartUpload.md#AmazonS3-Type-AbortIncompleteMultipartUpload-DaysAfterInitiation "API_AbortIncompleteMultipartUpload.md#AmazonS3-Type-AbortIncompleteMultipartUpload-DaysAfterInitiation")>`integer`</[DaysAfterInitiation](API_AbortIncompleteMultipartUpload.md#AmazonS3-Type-AbortIncompleteMultipartUpload-DaysAfterInitiation "API_AbortIncompleteMultipartUpload.md#AmazonS3-Type-AbortIncompleteMultipartUpload-DaysAfterInitiation")>
      </[AbortIncompleteMultipartUpload](API_Rule.md#AmazonS3-Type-Rule-AbortIncompleteMultipartUpload "API_Rule.md#AmazonS3-Type-Rule-AbortIncompleteMultipartUpload")>
      <[Expiration](API_Rule.md#AmazonS3-Type-Rule-Expiration "API_Rule.md#AmazonS3-Type-Rule-Expiration")>
         <[Date](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Date "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Date")>`timestamp`</[Date](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Date "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Date")>
         <[Days](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Days "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Days")>`integer`</[Days](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Days "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Days")>
         <[ExpiredObjectDeleteMarker](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-ExpiredObjectDeleteMarker "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-ExpiredObjectDeleteMarker")>`boolean`</[ExpiredObjectDeleteMarker](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-ExpiredObjectDeleteMarker "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-ExpiredObjectDeleteMarker")>
      </[Expiration](API_Rule.md#AmazonS3-Type-Rule-Expiration "API_Rule.md#AmazonS3-Type-Rule-Expiration")>
      <[ID](API_Rule.md#AmazonS3-Type-Rule-ID "API_Rule.md#AmazonS3-Type-Rule-ID")>`string`</[ID](API_Rule.md#AmazonS3-Type-Rule-ID "API_Rule.md#AmazonS3-Type-Rule-ID")>
      <[NoncurrentVersionExpiration](API_Rule.md#AmazonS3-Type-Rule-NoncurrentVersionExpiration "API_Rule.md#AmazonS3-Type-Rule-NoncurrentVersionExpiration")>
         <[NewerNoncurrentVersions](API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NewerNoncurrentVersions "API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NewerNoncurrentVersions")>`integer`</[NewerNoncurrentVersions](API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NewerNoncurrentVersions "API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NewerNoncurrentVersions")>
         <[NoncurrentDays](API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NoncurrentDays "API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NoncurrentDays")>`integer`</[NoncurrentDays](API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NoncurrentDays "API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NoncurrentDays")>
      </[NoncurrentVersionExpiration](API_Rule.md#AmazonS3-Type-Rule-NoncurrentVersionExpiration "API_Rule.md#AmazonS3-Type-Rule-NoncurrentVersionExpiration")>
      <[NoncurrentVersionTransition](API_Rule.md#AmazonS3-Type-Rule-NoncurrentVersionTransition "API_Rule.md#AmazonS3-Type-Rule-NoncurrentVersionTransition")>
         <[NewerNoncurrentVersions](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NewerNoncurrentVersions "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NewerNoncurrentVersions")>`integer`</[NewerNoncurrentVersions](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NewerNoncurrentVersions "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NewerNoncurrentVersions")>
         <[NoncurrentDays](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NoncurrentDays "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NoncurrentDays")>`integer`</[NoncurrentDays](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NoncurrentDays "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NoncurrentDays")>
         <[StorageClass](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-StorageClass "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-StorageClass")>`string`</[StorageClass](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-StorageClass "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-StorageClass")>
      </[NoncurrentVersionTransition](API_Rule.md#AmazonS3-Type-Rule-NoncurrentVersionTransition "API_Rule.md#AmazonS3-Type-Rule-NoncurrentVersionTransition")>
      <[Prefix](API_Rule.md#AmazonS3-Type-Rule-Prefix "API_Rule.md#AmazonS3-Type-Rule-Prefix")>`string`</[Prefix](API_Rule.md#AmazonS3-Type-Rule-Prefix "API_Rule.md#AmazonS3-Type-Rule-Prefix")>
      <[Status](API_Rule.md#AmazonS3-Type-Rule-Status "API_Rule.md#AmazonS3-Type-Rule-Status")>`string`</[Status](API_Rule.md#AmazonS3-Type-Rule-Status "API_Rule.md#AmazonS3-Type-Rule-Status")>
      <[Transition](API_Rule.md#AmazonS3-Type-Rule-Transition "API_Rule.md#AmazonS3-Type-Rule-Transition")>
         <[Date](API_Transition.md#AmazonS3-Type-Transition-Date "API_Transition.md#AmazonS3-Type-Transition-Date")>`timestamp`</[Date](API_Transition.md#AmazonS3-Type-Transition-Date "API_Transition.md#AmazonS3-Type-Transition-Date")>
         <[Days](API_Transition.md#AmazonS3-Type-Transition-Days "API_Transition.md#AmazonS3-Type-Transition-Days")>`integer`</[Days](API_Transition.md#AmazonS3-Type-Transition-Days "API_Transition.md#AmazonS3-Type-Transition-Days")>
         <[StorageClass](API_Transition.md#AmazonS3-Type-Transition-StorageClass "API_Transition.md#AmazonS3-Type-Transition-StorageClass")>`string`</[StorageClass](API_Transition.md#AmazonS3-Type-Transition-StorageClass "API_Transition.md#AmazonS3-Type-Transition-StorageClass")>
      </[Transition](API_Rule.md#AmazonS3-Type-Rule-Transition "API_Rule.md#AmazonS3-Type-Rule-Transition")>
   </[Rule](#AmazonS3-PutBucketLifecycle-request-Rules "#AmazonS3-PutBucketLifecycle-request-Rules")>
   ...
</[LifecycleConfiguration](#AmazonS3-PutBucketLifecycle-request-LifecycleConfiguration "#AmazonS3-PutBucketLifecycle-request-LifecycleConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_PutBucketLifecycle_RequestSyntax "#API_PutBucketLifecycle_RequestSyntax")**



Required: Yes




**[Content-MD5](#API_PutBucketLifecycle_RequestSyntax "#API_PutBucketLifecycle_RequestSyntax")**



For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.




**[x-amz-expected-bucket-owner](#API_PutBucketLifecycle_RequestSyntax "#API_PutBucketLifecycle_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-sdk-checksum-algorithm](#API_PutBucketLifecycle_RequestSyntax "#API_PutBucketLifecycle_RequestSyntax")**


Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any
 additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or
 `x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
 information, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
 parameter.


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`





## Request Body


The request accepts the following data in XML format.





**[LifecycleConfiguration](#API_PutBucketLifecycle_RequestSyntax "#API_PutBucketLifecycle_RequestSyntax")**


Root level tag for the LifecycleConfiguration parameters.


Required: Yes




**[Rule](#API_PutBucketLifecycle_RequestSyntax "#API_PutBucketLifecycle_RequestSyntax")**


Specifies lifecycle configuration rules for an Amazon S3 bucket. 


Type: Array of [Rule](API_Rule.md "API_Rule.md") data types


Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Sample Request: Body of a basic lifecycle configuration


In the request, you specify the lifecycle configuration in the request body. The lifecycle
 configuration is specified as XML. The following is an example of a basic lifecycle configuration.
 It specifies one rule. The `Prefix` in the rule identifies objects to which the rule
 applies. The rule also specifies two actions (`Transition` and `Expiration`).
 Each action specifies a time line when Amazon S3 should perform the action. The Status indicates whether
 the rule is enabled or disabled. 



```

<LifecycleConfiguration>
    <Rule>
        <ID>sample-rule</ID>
        <Prefix>key-prefix</Prefix>
        <Status>rule-status</Status>
        <Transition>        
           <Date>value</Date>        
           <StorageClass>storage class</StorageClass>       
        </Transition>    
        <Expiration>
           <Days>value</Days>
        </Expiration>
    </Rule>
</LifecycleConfiguration>               
           
```

### Sample Request: Body of a lifecycle configuration specifying noncurrent versions


If the state of your bucket is versioning-enabled or versioning-suspended, you can have many
 versions of the same object: one current version and zero or more noncurrent versions. The following
 lifecycle configuration specifies the actions (`NoncurrentVersionTransition`,
 `NoncurrentVersionExpiration`) that are specific to noncurrent object versions. 



```

<LifecycleConfiguration>
    <Rule>
        <ID>sample-rule</ID>
        <Prefix>key-prefix</Prefix>
        <Status>rule-status</Status>
        <NoncurrentVersionTransition>        
           <NoncurrentDays>value</NoncurrentDays>        
           <StorageClass>storage class</StorageClass>       
        </NoncurrentVersionTransition>    
        <NoncurrentVersionExpiration>
           <NoncurrentDays>value</NoncurrentDays>
        </NoncurrentVersionExpiration>
    </Rule>
</LifecycleConfiguration>               
           
```

### Sample Request: Body of a lifecycle configuration that specifies a rule with
 AbortIncompleteMultipartUpload


You can use the multipart upload to upload large objects in parts. For more information about
 multipart uploads, see [Multipart Upload Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html") in the *Amazon S3 User Guide*. With lifecycle
 configuration, you can tell Amazon S3 to abort incomplete multipart uploads, which are identified by the
 key name prefix specified in the rule, if they don't complete within a specified number of days.
 When Amazon S3 aborts a multipart upload, it deletes all parts associated with the upload. This ensures
 that you don't have incomplete multipart uploads that have left parts stored in Amazon S3, so you don't
 have to pay storage costs for them. The following is an example lifecycle configuration that
 specifies a rule with the `AbortIncompleteMultipartUpload` action. This action tells Amazon S3
 to abort incomplete multipart uploads seven days after initiation. 



```

<LifecycleConfiguration>
    <Rule>
        <ID>sample-rule</ID>
        <Prefix>SomeKeyPrefix</Prefix>
        <Status>rule-status</Status>
        <AbortIncompleteMultipartUpload>        
           <DaysAfterInitiation>7</DaysAfterInitiation>        
        </AbortIncompleteMultipartUpload>    
    </Rule>
</LifecycleConfiguration>               
           
```

### Add lifecycle configuration to a bucket that is not versioning-enabled


The following is a sample `PUT /?lifecycle` request that adds the lifecycle
 configuration to the `examplebucket` bucket. The lifecycle configuration specifies two
 rules, each with one action:



* The `Transition` action tells Amazon S3 to transition objects with the "documents/"
 prefix to the GLACIER storage class 30 days after creation.
* The `Expiration` action tells Amazon S3 to delete objects with the "logs/" prefix 365
 days after creation.

The sample response follows the sample request.



```
PUT /?lifecycle HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com 
x-amz-date: Wed, 14 May 2014 02:11:21 GMT
Content-MD5: q6yJDlIkcBaGGfb3QLY69A==
Authorization: authorization string
Content-Length: 415
<LifecycleConfiguration>
  <Rule>
    <ID>id1</ID>
    <Prefix>documents/</Prefix>
    <Status>Enabled</Status>
    <Transition>
      <Days>30</Days>
      <StorageClass>GLACIER</StorageClass>
    </Transition>
  </Rule>
  <Rule>
    <ID>id2</ID>
    <Prefix>logs/</Prefix>
    <Status>Enabled</Status>
    <Expiration>
      <Days>365</Days>
    </Expiration>
  </Rule>
</LifecycleConfiguration>
            
```


```
HTTP/1.1 200 OK
x-amz-id-2: r+qR7+nhXtJDDIJ0JJYcd+1j5nM/rUFiiiZ/fNbDOsd3JUE8NWMLNHXmvPfwMpdc
x-amz-request-id: 9E26D08072A8EF9E
Date: Wed, 14 May 2014 02:11:22 GMT
Content-Length: 0
Server: AmazonS3               
            
```

### Add lifecycle configuration to a bucket that is versioning-enabled


The following is a sample PUT /?lifecycle request that adds the lifecycle configuration to the
 `examplebucket` bucket. The lifecycle configuration specifies two rules, each with one
 action. You specify these actions when your bucket is versioning-enabled or versioning is suspended: 



* The `NoncurrentVersionExpiration` action tells Amazon S3 to expire noncurrent versions
 of objects with the "logs/" prefix 100 days after the objects become noncurrent.
* The `NoncurrentVersionTransition` action tells Amazon S3 to transition noncurrent
 versions of objects with the "documents/" prefix to the GLACIER storage class 30 days after they
 become noncurrent.

The sample response follows the sample request.



```
PUT /?lifecycle HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com 
x-amz-date: Wed, 14 May 2014 02:21:48 GMT
Content-MD5: 96rxH9mDqVNKkaZDddgnw==
Authorization: authorization string
Content-Length: 598
<LifecycleConfiguration>
  <Rule>
    <ID>id1</ID>
    <Prefix>logs/</Prefix>
    <Status>Enabled</Status>
    <NoncurrentVersionExpiration>
      <NoncurrentDays>1</NoncurrentDays>
    </NoncurrentVersionExpiration>
  </Rule>
  <Rule>
    <ID>TransitionSoonAfterBecomingNonCurrent</ID>
    <Prefix>documents/</Prefix>
    <Status>Enabled</Status>
    <NoncurrentVersionTransition>
      <NoncurrentDays>0</NoncurrentDays>
      <StorageClass>GLACIER</StorageClass>
    </NoncurrentVersionTransition>
  </Rule>
</LifecycleConfiguration>
            
```


```
HTTP/1.1 200 OK
x-amz-id-2: aXQ+KbIrmMmoO//3bMdDTw/CnjArwje+J49Hf+j44yRb/VmbIkgIO5A+PT98Cp/6k07hf+LD2mY=
x-amz-request-id: 02D7EC4C10381EB1
Date: Wed, 14 May 2014 02:21:50 GMT
Content-Length: 0
Server: AmazonS3
            
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketLifecycle "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketLifecycle")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketLifecycle "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketLifecycle")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketLifecycle")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketLifecycle")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketLifecycle")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketLifecycle")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketLifecycle")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketLifecycle")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketLifecycle "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketLifecycle")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketLifecycle "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketLifecycle")
