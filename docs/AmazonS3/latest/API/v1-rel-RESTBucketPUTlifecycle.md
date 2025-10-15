# PUT Bucket lifecycle (Deprecated)

## Description





###### Important

For an updated version of this API, see [PutBucketLifecycleConfiguration](API_PutBucketLifecycleConfiguration.md "API_PutBucketLifecycleConfiguration.md"). This version has been deprecated.
 Existing lifecycle configurations will work. For new lifecycle configurations, use
 the updated API.


Creates a new lifecycle configuration for the bucket or replaces an existing lifecycle
 configuration. For information about lifecycle configuration, see [Object Lifecycle Management](../userguide/object-lifecycle-mgmt.md "../userguide/object-lifecycle-mgmt.md") in
 the *Amazon Simple Storage Service User Guide*.


### Permissions


By default, all Amazon S3 resources, including buckets, objects, and related subresources (for
 example, lifecycle configuration and website configuration) are private. Only the
 resource owner, the AWS account that created the resource, can access it. The
 resource owner can optionally grant access permissions to others by writing an
 access policy. For this operation, users must get the
 `s3:PutLifecycleConfiguration` permission. 


You can also explicitly deny permissions. Explicit denial also supersedes any other
 permissions. If you want to prevent users or accounts from removing or deleting
 objects from your bucket, you must deny them permissions for the following actions: 



* `s3:DeleteObject`
* `s3:DeleteObjectVersion`
* `s3:PutLifecycleConfiguration`

For more information about permissions, see [Managing Access Permissions to Your Amazon S3 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md") in the
 *Amazon Simple Storage Service User Guide*. 


## Requests


### Syntax



```
PUT /?lifecycle HTTP/1.1
Host: `bucketname`.s3.amazonaws.com
Content-Length: `length`
Date: `date`
Authorization: `authorization string` 
Content-MD5: `MD5`

`Lifecycle configuration in the request body`
```

For details about authorization strings, 
 see [Authenticating Requests (AWS Signature Version
 4)](sig-v4-authenticating-requests.md "sig-v4-authenticating-requests.md").


### Request Parameters


This implementation of the operation does not use request parameters.


### Request Headers




|  Name  |  Description  |  Required  |
| --- | --- | --- |
| `Content-MD5` | The base64-encoded 128-bit MD5 digest of the data. You must use this header as a
 message integrity check to verify that the request body was not
 corrupted in transit. For more information, see [RFC
 1864](http://www.ietf.org/rfc/rfc1864.txt "http://www.ietf.org/rfc/rfc1864.txt").
Type: String 
Default: None |  Yes  |


### Request Body


In the request, you specify the lifecycle configuration in the request body. The lifecycle
 configuration is specified as XML. The following is an example of a basic lifecycle
 configuration. It specifies one rule. The `Prefix` in the rule identifies
 objects to which the rule applies. The rule also specifies two actions
 (`Transition`and `Expiration`). Each action specifies a
 timeline when Amazon S3 should perform the action. The `Status` indicates
 whether the rule is enabled or disabled.



```
<LifecycleConfiguration>
    <Rule>
        <ID>sample-rule</ID>
        <Prefix>`key-prefix`</Prefix>
        <Status>`rule-status`</Status>
        <Transition>        
           <Date>`value`</Date>        
           <StorageClass>`storage class`</StorageClass>       
        </Transition>    
        <Expiration>
           <Days>`value`</Days>
        </Expiration>
    </Rule>
</LifecycleConfiguration>
```

If the state of your bucket is versioning-enabled or versioning-suspended, you can have
 many versions of the same object: one current version and zero or more noncurrent
 versions. The following lifecycle configuration specifies the actions
 (`NoncurrentVersionTransition`,
 `NoncurrentVersionExpiration`) that are specific to noncurrent object
 versions.



```
<LifecycleConfiguration>
    <Rule>
        <ID>sample-rule</ID>
        <Prefix>`key-prefix`</Prefix>
        <Status>`rule-status`</Status>
        <NoncurrentVersionTransition>      
           <NoncurrentDays>`value`</NoncurrentDays>      
           <StorageClass>`storage class`</StorageClass>   
        </NoncurrentVersionTransition>    
        <NoncurrentVersionExpiration>     
           <NoncurrentDays>`value`</NoncurrentDays>    
        </NoncurrentVersionExpiration> 
    </Rule>
</LifecycleConfiguration>
```

You can use the multipart upload API to upload large objects in parts. For more information
 about multipart uploads, see [Multipart
 Upload Overview](../userguide/mpuoverview.md "../userguide/mpuoverview.md") in the *Amazon Simple Storage Service User Guide*. With
 lifecycle configuration, you can tell Amazon S3 to cancel incomplete multipart uploads,
 which are identified by the key name prefix specified in the rule, if they don't
 complete within a specified number of days. When Amazon S3 cancels a multipart upload, it
 deletes all parts associated with the upload. This ensures that you don't have
 incomplete multipart uploads that have left parts stored in Amazon S3, so you don't have
 to pay storage costs for them. The following is an example lifecycle configuration
 that specifies a rule with the `AbortIncompleteMultipartUpload` action.
 This action tells Amazon S3 to cancel incomplete multipart uploads seven days after
 initiation.






```
<LifecycleConfiguration>
    <Rule>
        <ID>sample-rule</ID>
        <Prefix>`SomeKeyPrefix`/</Prefix>
        <Status>`rule-status`</Status>
        <AbortIncompleteMultipartUpload>
          <DaysAfterInitiation>7</DaysAfterInitiation>
        </AbortIncompleteMultipartUpload>
    </Rule>
</LifecycleConfiguration>
```

The following table describes the XML elements in the lifecycle configuration.




|  Name  |  Description  | Required |
| --- | --- | --- |
| `AbortIncompleteMultipartUpload` | Container for specifying when an incomplete multipart upload becomes eligible for an 
 abort operation. 
Child: `DaysAfterInitiation`
Type: Container
Ancestor: `Rule` | Yes, if no other action is specified for the rule |
| `Date` | Date when you want Amazon S3 to take the action. For more information, see [Lifecycle Rules: Based on a Specific Date](../userguide/intro-lifecycle-rules.md#intro-lifecycle-rules-date "../userguide/intro-lifecycle-rules.md#intro-lifecycle-rules-date") in the
 *Amazon Simple Storage Service User Guide*.
The date value must conform to ISO 8601 format. The time is always midnight UTC. 
Type: String
Ancestor: `Expiration` or `Transition` | Yes, if `Days` and `ExpiredObjectDeleteMarker` are
 absent |
| `Days` | Specifies the number of days after object creation when the specific rule action
 takes effect. 
Type: Nonnegative Integer when used with `Transition`, Positive Integer
 when used with `Expiration`
Ancestor: `Expiration`, `Transition` | Yes, if `Date` and `ExpiredObjectDeleteMarker` are
 absent |
| `DaysAfterInitiation` | Specifies the number of days after initiating a multipart upload when the multipart
 upload must be completed. If it does not complete by the specified number of days, 
 it becomes eligible for an abort operation and Amazon S3 cancels the incomplete multipart
 upload.
Type: Positive Integer
Ancestor: `AbortIncompleteMultipartUpload` | Yes, if a parent tag is specified |
| `Expiration` | This action specifies a period in an object's lifetime when Amazon S3 should take the
 appropriate expiration action. The action Amazon S3 takes
 depends on whether the bucket is versioning-enabled. 

* If versioning has never been enabled on the
 bucket, Amazon S3 deletes the only copy of the
 object permanently.
* If the bucket is versioning-enabled (or versioning is suspended), the action
 applies only to the current version of the object. A
 versioning-enabled bucket can have many versions of the
 same object: one current version and zero or more
 noncurrent versions.
Instead of deleting the current version, Amazon S3
 makes it a noncurrent version by adding a delete
 marker as the new current version. 

ImportantIf a bucket's state is versioning-suspended, Amazon S3 creates a delete marker with
 version ID `null`. If you have a version
 with version ID `null`, Amazon S3 overwrites
 that version. 
NoteTo set the expiration for noncurrent objects, use the
 `NoncurrentVersionExpiration`
 action.

Type: Container
Children: Days or Date
Ancestor: Rule | Yes, if no other action is present in the `Rule`. |
| `ID` | Unique identifier for the rule. The value cannot be longer than 255
 characters.
Type: String
Ancestor: Rule | No |
| `LifecycleConfiguration` | Container for lifecycle rules. You can add as many as 1000 rules.
Type: Container
Children: Rule
Ancestor: None | Yes |
| `ExpiredObjectDeleteMarker` | On a versioned bucket (a versioning-enabled or versioning-suspended bucket), you can
 add this element in the lifecycle configuration to tell Amazon S3 to
 delete expired object delete markers. For an example, see [Example 8: Removing Expired Object Delete Markers](../userguide/intro-lifecycle-rules.md#lifecycle-config-conceptual-ex8 "../userguide/intro-lifecycle-rules.md#lifecycle-config-conceptual-ex8")
 in the *Amazon Simple Storage Service User Guide*. Don't add it to a
 non-versioned bucket, because that type of bucket cannot include
 delete markers. 
Type: String 
Valid values: true | false (the value `false` is allowed, but it is no-op,
 which means that Amazon S3 will not take action)
Ancestor: `Expiration` | Yes, if `Date` and `Days` are absent |
| `NoncurrentDays` | Specifies the number of days an object is noncurrent before Amazon S3 can perform
 the associated action. For information about the noncurrent days
 calculations, see [How Amazon S3 Calculates When an Object Became Noncurrent](../userguide/s3-access-control.md "../userguide/s3-access-control.md")
 in the *Amazon Simple Storage Service User Guide*.
Type: Nonnegative Integer when used with `NoncurrentVersionTransition`,
 Positive Integer when used with
 `NoncurrentVersionExpiration`
Ancestor: `NoncurrentVersionExpiration` or
 `NoncurrentVersionTransition` | Yes |
| `NoncurrentVersionExpiration` | Specifies when noncurrent object versions expire. Upon expiration, Amazon S3
 permanently deletes the noncurrent object versions. 
Set this lifecycle configuration action on a bucket that has versioning enabled (or
 suspended) to tell Amazon S3 to delete noncurrent object versions at
 a specific period in the object's lifetime.
Type: Container
Children: NoncurrentDays 
Ancestor: Rule | Yes, if no other action is present in the `Rule` |
| `NoncurrentVersionTransition` | Container for the transition rule that describes when noncurrent objects transition to
 the `STANDARD_IA`, `ONEZONE_IA`, or
 GLACIER storage class. 
If your bucket is versioning-enabled (or if versioning is suspended), you can set this
 action to tell Amazon S3 to transition noncurrent object versions at
 a specific period in the object's lifetime.
Type: Container
Children: NoncurrentDays and StorageClass
Ancestor: Rule | Yes, if no other action is present in the `Rule` |
| `Prefix` | Object key prefix that identifies one or more objects to which the rule
 applies.
Type: String
Ancestor: Rule | Yes |
| `Rule` | Container for a lifecycle rule. A lifecycle configuration can contain as many as
 1000 rules. 
Type: Container
Ancestor:LifecycleConfiguration | Yes |
| `Status` | If enabled, Amazon S3 executes the rule as scheduled. If it is disabled, Amazon S3 ignores the
 rule.
Type: String
Ancestor: Rule
Valid values: Enabled, Disabled | Yes |
| `StorageClass` | Specifies the Amazon S3 storage class to which you want the object to transition. 
Type: String
Ancestor: Transition and NoncurrentVersionTransition
Valid values: STANDARD\_IA | ONEZONE\_IA | GLACIER  | Yes
This element is required only if you specify one or both its
 ancestors. |
| `Transition` | This action specifies a period in the objects' lifetime when Amazon S3 should transition
 them to the `STANDARD_IA`, `ONEZONE_IA`,
 or GLACIER storage class. When this action
 is in effect, what Amazon S3 does depends on whether the bucket is
 versioning-enabled.

* If versioning has never been enabled on the bucket, Amazon S3 transitions the only copy
 of the object to the specified storage class.
* If your bucket is versioning-enabled (or versioning is suspended), Amazon S3 transitions
 only the current versions of objects identified in the
 rule.

NoteA versioning-enabled bucket can have many versions of an object. This action has
 no effect on noncurrent object versions. To
 transition noncurrent objects, you must use the
 `NoncurrentVersionTransition`
 action.

Type: Container
Children: Days or Date, and StorageClass
Ancestor: Rule | Yes, if no other action is present in the `Rule` |


## Responses


### Response Headers


This implementation of the operation uses only response headers that are common to most responses. For more information, see [Common Response Headers](RESTCommonResponseHeaders.md "RESTCommonResponseHeaders.md").


### Response Elements


This implementation of the operation does not return response elements.


### Special Errors


This implementation of the operation does not return special errors. For general information about Amazon S3 errors and a list of error codes, see [Error Responses](ErrorResponses.md "ErrorResponses.md").


## Examples


### Example 1: Add Lifecycle Configuration to a Bucket
 That Is Not Versioning-enabled


The following lifecycle configuration specifies two rules, each with one action. 



* The Transition action tells Amazon S3 to transition objects with the "documents/" prefix to
 the GLACIER storage class 30 days after
 creation.
* The Expiration action tells Amazon S3 to delete objects with the "logs/" prefix 365 days
 after creation.


```

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

The following is a sample `PUT /?lifecycle` request that adds the
 preceding lifecycle configuration to the `examplebucket` bucket.



```
PUT /?lifecycle HTTP/1.1
Host: examplebucket.s3.amazonaws.com 
x-amz-date: Wed, 14 May 2014 02:11:21 GMT
Content-MD5: q6yJDlIkcBaGGfb3QLY69A==
Authorization: `authorization string`
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

The following is a sample response.






```
HTTP/1.1 200 OK
x-amz-id-2: r+qR7+nhXtJDDIJ0JJYcd+1j5nM/rUFiiiZ/fNbDOsd3JUE8NWMLNHXmvPfwMpdc
x-amz-request-id: 9E26D08072A8EF9E
Date: Wed, 14 May 2014 02:11:22 GMT
Content-Length: 0
Server: AmazonS3
```

### Example 2: Add Lifecycle Configuration to a
 Versioning-enabled Bucket


The following lifecycle configuration specifies two rules, each with one action
 for Amazon S3 to perform. You specify these actions when your bucket is
 versioning-enabled or versioning is suspended:



* The `NoncurrentVersionExpiration` action tells Amazon S3 to expire noncurrent
 versions of objects with the "logs/" prefix 100 days after the objects
 become noncurrent.
* The `NoncurrentVersionTransition` action tells Amazon S3 to transition noncurrent
 versions of objects with the "documents/" prefix to the
 GLACIER storage class 30 days after they become
 noncurrent.


```
<LifeCycleConfiguration>
  <Rule>
    <ID>DeleteAfterBecomingNonCurrent</ID>
    <Prefix>logs/</Prefix>
    <Status>Enabled</Status>
    <NoncurrentVersionExpiration>
      <NoncurrentDays>100</NoncurrentDays>
    </NoncurrentVersionExpiration>
  </Rule>
  <Rule>
    <ID>TransitionAfterBecomingNonCurrent</ID>
    <Prefix>documents/</Prefix>
    <Status>Enabled</Status>
    <NoncurrentVersionTransition>
      <NoncurrentDays>30</NoncurrentDays>
      <StorageClass>GLACIER</StorageClass>
    </NoncurrentVersionTransition>
  </Rule>
</LifeCycleConfiguration>
```

The following is a sample `PUT /?lifecycle` request that adds the
 preceding lifecycle configuration to the `examplebucket` bucket.



```
PUT /?lifecycle HTTP/1.1
Host: examplebucket.s3.amazonaws.com 
x-amz-date: Wed, 14 May 2014 02:21:48 GMT
Content-MD5: 96rxH9mDqVNKkaZDddgnw==
Authorization: `authorization string`
Content-Length: 598

<LifeCycleConfiguration>
  <Rule>
    <ID>DeleteAfterBecomingNonCurrent</ID>
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
</LifeCycleConfiguration>
```

The following is a sample response.



```
HTTP/1.1 200 OK
x-amz-id-2: aXQ+KbIrmMmoO//3bMdDTw/CnjArwje+J49Hf+j44yRb/VmbIkgIO5A+PT98Cp/6k07hf+LD2mY=
x-amz-request-id: 02D7EC4C10381EB1
Date: Wed, 14 May 2014 02:21:50 GMT
Content-Length: 0
Server: AmazonS3
```

### Additional Examples


For more examples of transitioning objects to storage classes such as STANDARD\_IA or
 ONEZONE\_IA, see [Examples of Lifecycle Configuration](../userguide/intro-lifecycle-rules.md#lifecycle-configuration-examples "../userguide/intro-lifecycle-rules.md#lifecycle-configuration-examples").


## Related Resources



* [GetBucketLifecycleConfiguration](API_GetBucketLifecycleConfiguration.md "API_GetBucketLifecycleConfiguration.md")
* [POST Object restore](RESTObjectPOSTrestore.md "RESTObjectPOSTrestore.md")
* By default, a resource owner—in this case, a bucket owner, which is the AWS account that created the bucket—can perform any of the operations. A
 resource owner can also grant others permission to perform the operation. For
 more information, see the following topics in the
 *Amazon Simple Storage Service User Guide*:




	+ [Specifying Permissions in a Policy](../userguide/using-with-s3-actions.md "../userguide/using-with-s3-actions.md")
	+ [Managing Access Permissions to Your Amazon S3 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md")
