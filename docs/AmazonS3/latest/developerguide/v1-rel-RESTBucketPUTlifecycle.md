

# PUT Bucket lifecycle (Deprecated)
<a name="v1-rel-RESTBucketPUTlifecycle"></a>

## Description
<a name="v1-rel-RESTBucketPUTlifecycle-description"></a>

 

**Important**  
For an updated version of this API, see [PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html). This version has been deprecated. Existing lifecycle configurations will work. For new lifecycle configurations, use the updated API.

Creates a new lifecycle configuration for the bucket or replaces an existing lifecycle configuration. For information about lifecycle configuration, see [Object Lifecycle Management](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) in the *Amazon Simple Storage Service User Guide*.

### Permissions
<a name="v1-rel-put-object-lifecycle-permissions"></a>

By default, all Amazon S3 resources, including buckets, objects, and related subresources (for example, lifecycle configuration and website configuration) are private. Only the resource owner, the AWS account that created the resource, can access it. The resource owner can optionally grant access permissions to others by writing an access policy. For this operation, users must get the `s3:PutLifecycleConfiguration` permission. 

You can also explicitly deny permissions. Explicit denial also supersedes any other permissions. If you want to prevent users or accounts from removing or deleting objects from your bucket, you must deny them permissions for the following actions: 
+ `s3:DeleteObject`
+ `s3:DeleteObjectVersion`
+ `s3:PutLifecycleConfiguration`

For more information about permissions, see [Managing Access Permissions to Your Amazon S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html) in the *Amazon Simple Storage Service User Guide*. 

## Requests
<a name="v1-rel-RESTBucketPUTlifecycle-requests"></a>

### Syntax
<a name="v1-rel-RESTBucketPUTlifecycle-requests-syntax"></a>

```
1. PUT /?lifecycle HTTP/1.1
2. Host: {{bucketname}}.s3.amazonaws.com
3. Content-Length: {{length}}
4. Date: {{date}}
5. Authorization: {{authorization string}} 
6. Content-MD5: {{MD5}}
7. 
8. {{Lifecycle configuration in the request body}}
```

For details about authorization strings, see [Authenticating Requests (AWS Signature Version 4)](sig-v4-authenticating-requests.md).

### Request Parameters
<a name="v1-rel-RESTBucketPUTlifecycle-requests-request-parameters"></a>

This implementation of the operation does not use request parameters.

### Request Headers
<a name="v1-rel-RESTBucketPUTlifecycle-requests-request-headers"></a>


|  Name  |  Description  |  Required  | 
| --- | --- | --- | 
| Content-MD5 | The base64-encoded 128-bit MD5 digest of the data. You must use this header as a message integrity check to verify that the request body was not corrupted in transit. For more information, see [RFC 1864](http://www.ietf.org/rfc/rfc1864.txt).<br />Type: String <br />Default: None |  Yes  | 

### Request Body
<a name="v1-rel-RESTBucketPUTlifecycle-requests-request-elements"></a>

In the request, you specify the lifecycle configuration in the request body. The lifecycle configuration is specified as XML. The following is an example of a basic lifecycle configuration. It specifies one rule. The `Prefix` in the rule identifies objects to which the rule applies. The rule also specifies two actions (`Transition`and `Expiration`). Each action specifies a timeline when Amazon S3 should perform the action. The `Status` indicates whether the rule is enabled or disabled.

```
<LifecycleConfiguration>
    <Rule>
        <ID>sample-rule</ID>
        <Prefix>{{key-prefix}}</Prefix>
        <Status>{{rule-status}}</Status>
        <Transition>        
           <Date>{{value}}</Date>        
           <StorageClass>{{storage class}}</StorageClass>       
        </Transition>    
        <Expiration>
           <Days>{{value}}</Days>
        </Expiration>
    </Rule>
</LifecycleConfiguration>
```

If the state of your bucket is versioning-enabled or versioning-suspended, you can have many versions of the same object: one current version and zero or more noncurrent versions. The following lifecycle configuration specifies the actions (`NoncurrentVersionTransition`, `NoncurrentVersionExpiration`) that are specific to noncurrent object versions.

```
<LifecycleConfiguration>
    <Rule>
        <ID>sample-rule</ID>
        <Prefix>{{key-prefix}}</Prefix>
        <Status>{{rule-status}}</Status>
        <NoncurrentVersionTransition>      
           <NoncurrentDays>{{value}}</NoncurrentDays>      
           <StorageClass>{{storage class}}</StorageClass>   
        </NoncurrentVersionTransition>    
        <NoncurrentVersionExpiration>     
           <NoncurrentDays>{{value}}</NoncurrentDays>    
        </NoncurrentVersionExpiration> 
    </Rule>
</LifecycleConfiguration>
```

You can use the multipart upload API to upload large objects in parts. For more information about multipart uploads, see [Multipart Upload Overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html) in the *Amazon Simple Storage Service User Guide*. With lifecycle configuration, you can tell Amazon S3 to cancel incomplete multipart uploads, which are identified by the key name prefix specified in the rule, if they don't complete within a specified number of days. When Amazon S3 cancels a multipart upload, it deletes all parts associated with the upload. This ensures that you don't have incomplete multipart uploads that have left parts stored in Amazon S3, so you don't have to pay storage costs for them. The following is an example lifecycle configuration that specifies a rule with the `AbortIncompleteMultipartUpload` action. This action tells Amazon S3 to cancel incomplete multipart uploads seven days after initiation.

 

```
<LifecycleConfiguration>
    <Rule>
        <ID>sample-rule</ID>
        <Prefix>{{SomeKeyPrefix}}/</Prefix>
        <Status>{{rule-status}}</Status>
        <AbortIncompleteMultipartUpload>
          <DaysAfterInitiation>7</DaysAfterInitiation>
        </AbortIncompleteMultipartUpload>
    </Rule>
</LifecycleConfiguration>
```

The following table describes the XML elements in the lifecycle configuration.


|  Name  |  Description  | Required | 
| --- | --- | --- | 
|  AbortIncompleteMultipartUpload  | Container for specifying when an incomplete multipart upload becomes eligible for an abort operation. <br />Child: `DaysAfterInitiation`<br />Type: Container<br />Ancestor: `Rule` | Yes, if no other action is specified for the rule | 
|  Date  | Date when you want Amazon S3 to take the action. For more information, see [Lifecycle Rules: Based on a Specific Date](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-rules.html#intro-lifecycle-rules-date) in the *Amazon Simple Storage Service User Guide*.<br />The date value must conform to ISO 8601 format. The time is always midnight UTC. <br />Type: String<br />Ancestor: `Expiration` or `Transition` | Yes, if Days and ExpiredObjectDeleteMarker are absent | 
|  Days  | Specifies the number of days after object creation when the specific rule action takes effect. <br />Type: Nonnegative Integer when used with `Transition`, Positive Integer when used with `Expiration`<br />Ancestor: `Expiration`, `Transition` | Yes, if Date and ExpiredObjectDeleteMarker are absent | 
|  DaysAfterInitiation  | Specifies the number of days after initiating a multipart upload when the multipart upload must be completed. If it does not complete by the specified number of days, it becomes eligible for an abort operation and Amazon S3 cancels the incomplete multipart upload.<br />Type: Positive Integer<br />Ancestor: `AbortIncompleteMultipartUpload` | Yes, if a parent tag is specified | 
|  Expiration  | This action specifies a period in an object's lifetime when Amazon S3 should take the appropriate expiration action. The action Amazon S3 takes depends on whether the bucket is versioning-enabled. +  If versioning has never been enabled on the bucket, Amazon S3 deletes the only copy of the object permanently.  <br />+  If the bucket is versioning-enabled (or versioning is suspended), the action applies only to the current version of the object. A versioning-enabled bucket can have many versions of the same object: one current version and zero or more noncurrent versions. <br />Instead of deleting the current version, Amazon S3 makes it a noncurrent version by adding a delete marker as the new current version.  <br />  If a bucket's state is versioning-suspended, Amazon S3 creates a delete marker with version ID `null`. If you have a version with version ID `null`, Amazon S3 overwrites that version.    To set the expiration for noncurrent objects, use the `NoncurrentVersionExpiration` action.  <br />Type: Container<br />Children: Days or Date<br />Ancestor: Rule | Yes, if no other action is present in the Rule. | 
|  ID  | Unique identifier for the rule. The value cannot be longer than 255 characters.<br />Type: String<br />Ancestor: Rule | No | 
| LifecycleConfiguration | Container for lifecycle rules. You can add as many as 1000 rules.<br />Type: Container<br />Children: Rule<br />Ancestor: None | Yes | 
| ExpiredObjectDeleteMarker | On a versioned bucket (a versioning-enabled or versioning-suspended bucket), you can add this element in the lifecycle configuration to tell Amazon S3 to delete expired object delete markers. For an example, see [Example 8: Removing Expired Object Delete Markers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-rules.html#lifecycle-config-conceptual-ex8) in the *Amazon Simple Storage Service User Guide*. Don't add it to a non-versioned bucket, because that type of bucket cannot include delete markers. <br />Type: String <br />Valid values: true \| false (the value `false` is allowed, but it is no-op, which means that Amazon S3 will not take action)<br />Ancestor: `Expiration` | Yes, if Date and Days are absent | 
| NoncurrentDays | Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see [How Amazon S3 Calculates When an Object Became Noncurrent](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html) in the *Amazon Simple Storage Service User Guide*.<br />Type: Nonnegative Integer when used with `NoncurrentVersionTransition`, Positive Integer when used with `NoncurrentVersionExpiration`<br />Ancestor: `NoncurrentVersionExpiration` or `NoncurrentVersionTransition` | Yes | 
| NoncurrentVersionExpiration | Specifies when noncurrent object versions expire. Upon expiration, Amazon S3 permanently deletes the noncurrent object versions. <br />Set this lifecycle configuration action on a bucket that has versioning enabled (or suspended) to tell Amazon S3 to delete noncurrent object versions at a specific period in the object's lifetime.<br />Type: Container<br />Children: NoncurrentDays <br />Ancestor: Rule | Yes, if no other action is present in the Rule | 
| NoncurrentVersionTransition | Container for the transition rule that describes when noncurrent objects transition to the `STANDARD_IA`, `ONEZONE_IA`, or storage class. <br />If your bucket is versioning-enabled (or if versioning is suspended), you can set this action to tell Amazon S3 to transition noncurrent object versions at a specific period in the object's lifetime.<br />Type: Container<br />Children: NoncurrentDays and StorageClass<br />Ancestor: Rule | Yes, if no other action is present in the Rule | 
|  Prefix  | Object key prefix that identifies one or more objects to which the rule applies.<br />Type: String<br />Ancestor: Rule | Yes | 
| Rule  | Container for a lifecycle rule. A lifecycle configuration can contain as many as 1000 rules. <br />Type: Container<br />Ancestor:LifecycleConfiguration | Yes | 
|  Status  | If enabled, Amazon S3 executes the rule as scheduled. If it is disabled, Amazon S3 ignores the rule.<br />Type: String<br />Ancestor: Rule<br />Valid values: Enabled, Disabled | Yes | 
|  StorageClass  | Specifies the Amazon S3 storage class to which you want the object to transition. <br />Type: String<br />Ancestor: Transition and NoncurrentVersionTransition<br />Valid values: STANDARD\_IA \| ONEZONE\_IA \| GLACIER  | Yes<br />This element is required only if you specify one or both its ancestors. | 
|  Transition  | This action specifies a period in the objects' lifetime when Amazon S3 should transition them to the `STANDARD_IA`, `ONEZONE_IA`, or storage class. When this action is in effect, what Amazon S3 does depends on whether the bucket is versioning-enabled.+  If versioning has never been enabled on the bucket, Amazon S3 transitions the only copy of the object to the specified storage class.  <br />+  If your bucket is versioning-enabled (or versioning is suspended), Amazon S3 transitions only the current versions of objects identified in the rule. <br />  A versioning-enabled bucket can have many versions of an object. This action has no effect on noncurrent object versions. To transition noncurrent objects, you must use the `NoncurrentVersionTransition` action.  <br />Type: Container<br />Children: Days or Date, and StorageClass<br />Ancestor: Rule | Yes, if no other action is present in the Rule | 

## Responses
<a name="v1-rel-RESTBucketPUTlifecycle-responses"></a>

### Response Headers
<a name="v1-rel-RESTBucketPUTlifecycle-responses-response-headers"></a>

This implementation of the operation uses only response headers that are common to most responses. For more information, see [Common Response Headers](RESTCommonResponseHeaders.md).

### Response Elements
<a name="v1-rel-RESTBucketPUTlifecycle-responses-response-elements"></a>

This implementation of the operation does not return response elements.

### Special Errors
<a name="v1-rel-RESTBucketPUTlifecycle-responses-special-errors"></a>

This implementation of the operation does not return special errors. For general information about Amazon S3 errors and a list of error codes, see [Error Responses](ErrorResponses.md).

## Examples
<a name="v1-rel-RESTBucketPUTlifecycle-examples"></a>

### Example 1: Add Lifecycle Configuration to a Bucket That Is Not Versioning-enabled
<a name="v1-rel-put-bucket-lifecycle-ex1"></a>

The following lifecycle configuration specifies two rules, each with one action. 
+ The Transition action tells Amazon S3 to transition objects with the "documents/" prefix to the storage class 30 days after creation.
+ The Expiration action tells Amazon S3 to delete objects with the "logs/" prefix 365 days after creation.

```
 1. <LifecycleConfiguration>
 2.   <Rule>
 3.     <ID>id1</ID>
 4.     <Prefix>documents/</Prefix>
 5.     <Status>Enabled</Status>
 6.     <Transition>
 7.       <Days>30</Days>
 8.       <StorageClass>GLACIER</StorageClass>
 9.     </Transition>
10.   </Rule>
11.   <Rule>
12.     <ID>id2</ID>
13.     <Prefix>logs/</Prefix>
14.     <Status>Enabled</Status>
15.     <Expiration>
16.       <Days>365</Days>
17.     </Expiration>
18.   </Rule>
19. </LifecycleConfiguration>
```

The following is a sample `PUT /?lifecycle` request that adds the preceding lifecycle configuration to the `examplebucket` bucket.

```
 1. PUT /?lifecycle HTTP/1.1
 2. Host: examplebucket.s3.amazonaws.com 
 3. x-amz-date: Wed, 14 May 2014 02:11:21 GMT
 4. Content-MD5: q6yJDlIkcBaGGfb3QLY69A==
 5. Authorization: {{authorization string}}
 6. Content-Length: 415
 7. 
 8. <LifecycleConfiguration>
 9.   <Rule>
10.     <ID>id1</ID>
11.     <Prefix>documents/</Prefix>
12.     <Status>Enabled</Status>
13.     <Transition>
14.       <Days>30</Days>
15.       <StorageClass>GLACIER</StorageClass>
16.     </Transition>
17.   </Rule>
18.   <Rule>
19.     <ID>id2</ID>
20.     <Prefix>logs/</Prefix>
21.     <Status>Enabled</Status>
22.     <Expiration>
23.       <Days>365</Days>
24.     </Expiration>
25.   </Rule>
26. </LifecycleConfiguration>
```

The following is a sample response.

 

```
1. HTTP/1.1 200 OK
2. x-amz-id-2: r+qR7+nhXtJDDIJ0JJYcd+1j5nM/rUFiiiZ/fNbDOsd3JUE8NWMLNHXmvPfwMpdc
3. x-amz-request-id: 9E26D08072A8EF9E
4. Date: Wed, 14 May 2014 02:11:22 GMT
5. Content-Length: 0
6. Server: AmazonS3
```

### Example 2: Add Lifecycle Configuration to a Versioning-enabled Bucket
<a name="v1-rel-put-bucket-lifecycle-ex2"></a>

The following lifecycle configuration specifies two rules, each with one action for Amazon S3 to perform. You specify these actions when your bucket is versioning-enabled or versioning is suspended:
+ The `NoncurrentVersionExpiration` action tells Amazon S3 to expire noncurrent versions of objects with the "logs/" prefix 100 days after the objects become noncurrent. 
+ The `NoncurrentVersionTransition` action tells Amazon S3 to transition noncurrent versions of objects with the "documents/" prefix to the storage class 30 days after they become noncurrent.

```
 1. <LifeCycleConfiguration>
 2.   <Rule>
 3.     <ID>DeleteAfterBecomingNonCurrent</ID>
 4.     <Prefix>logs/</Prefix>
 5.     <Status>Enabled</Status>
 6.     <NoncurrentVersionExpiration>
 7.       <NoncurrentDays>100</NoncurrentDays>
 8.     </NoncurrentVersionExpiration>
 9.   </Rule>
10.   <Rule>
11.     <ID>TransitionAfterBecomingNonCurrent</ID>
12.     <Prefix>documents/</Prefix>
13.     <Status>Enabled</Status>
14.     <NoncurrentVersionTransition>
15.       <NoncurrentDays>30</NoncurrentDays>
16.       <StorageClass>GLACIER</StorageClass>
17.     </NoncurrentVersionTransition>
18.   </Rule>
19. </LifeCycleConfiguration>
```

The following is a sample `PUT /?lifecycle` request that adds the preceding lifecycle configuration to the `examplebucket` bucket.

```
 1. PUT /?lifecycle HTTP/1.1
 2. Host: examplebucket.s3.amazonaws.com 
 3. x-amz-date: Wed, 14 May 2014 02:21:48 GMT
 4. Content-MD5: 96rxH9mDqVNKkaZDddgnw==
 5. Authorization: {{authorization string}}
 6. Content-Length: 598
 7. 
 8. <LifeCycleConfiguration>
 9.   <Rule>
10.     <ID>DeleteAfterBecomingNonCurrent</ID>
11.     <Prefix>logs/</Prefix>
12.     <Status>Enabled</Status>
13.     <NoncurrentVersionExpiration>
14.       <NoncurrentDays>1</NoncurrentDays>
15.     </NoncurrentVersionExpiration>
16.   </Rule>
17.   <Rule>
18.     <ID>TransitionSoonAfterBecomingNonCurrent</ID>
19.     <Prefix>documents/</Prefix>
20.     <Status>Enabled</Status>
21.     <NoncurrentVersionTransition>
22.       <NoncurrentDays>0</NoncurrentDays>
23.       <StorageClass>GLACIER</StorageClass>
24.     </NoncurrentVersionTransition>
25.   </Rule>
26. </LifeCycleConfiguration>
```

The following is a sample response.

```
1. HTTP/1.1 200 OK
2. x-amz-id-2: aXQ+KbIrmMmoO//3bMdDTw/CnjArwje+J49Hf+j44yRb/VmbIkgIO5A+PT98Cp/6k07hf+LD2mY=
3. x-amz-request-id: 02D7EC4C10381EB1
4. Date: Wed, 14 May 2014 02:21:50 GMT
5. Content-Length: 0
6. Server: AmazonS3
```

### Additional Examples
<a name="v1-rel-put-bucket-lifecycle-ex3"></a>

For more examples of transitioning objects to storage classes such as STANDARD\_IA or ONEZONE\_IA, see [Examples of Lifecycle Configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-rules.html#lifecycle-configuration-examples).

## Related Resources
<a name="v1-rel-RESTObjectPOSTrestore-responses-related-resources"></a>
+ [GetBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html)
+ [POST Object restore](RESTObjectPOSTrestore.md)
+  By default, a resource owner—in this case, a bucket owner, which is the AWS account that created the bucket—can perform any of the operations. A resource owner can also grant others permission to perform the operation. For more information, see the following topics in the *Amazon Simple Storage Service User Guide*:
  +  [Specifying Permissions in a Policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html)
  + [Managing Access Permissions to Your Amazon S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html)