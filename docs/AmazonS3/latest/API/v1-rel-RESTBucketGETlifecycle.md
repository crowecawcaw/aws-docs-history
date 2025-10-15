# GET Bucket lifecycle (Deprecated)

## Description






###### Important

For an updated version of this API, see [GetBucketLifecycleConfiguration](API_GetBucketLifecycleConfiguration.md "API_GetBucketLifecycleConfiguration.md"). If you configured a bucket lifecycle
 using the <filter> element, you should see an updated version of this topic.
 This topic is provided for backward compatibility. 


Returns the `lifecycle` configuration information set on the
 bucket. For information about lifecycle configuration, go to 
 [Object Lifecycle Management](../userguide/object-lifecycle-mgmt.md "../userguide/object-lifecycle-mgmt.md") in the *Amazon Simple Storage Service User Guide*.
 


To use this operation, you must have permission to perform the
 `s3:GetLifecycleConfiguration` action. The bucket owner has this
 permission by default. The bucket owner can grant this permission to others. For more
 information about permissions, see [Managing Access Permissions to Your Amazon S3 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md") in the
 *Amazon Simple Storage Service User Guide*.


## Requests


### Syntax



```
GET /?lifecycle HTTP/1.1
Host: `bucketname`.s3.amazonaws.com
Date: `date`
Authorization: `authorization string` (see [Authenticating Requests (AWS Signature Version
 4)](sig-v4-authenticating-requests.md "sig-v4-authenticating-requests.md"))
```

### Request Parameters


This implementation of the operation does not use request parameters.


### Request Headers


This implementation of the operation uses only request headers that are common to all operations. For more information, see [Common Request Headers](RESTCommonRequestHeaders.md "RESTCommonRequestHeaders.md").


### Request Elements


This implementation of the operation does not use request elements.


## Responses


### Response Headers


This implementation of the operation uses only response headers that are common to most responses. For more information, see [Common Response Headers](RESTCommonResponseHeaders.md "RESTCommonResponseHeaders.md").


### Response Elements


This implementation of `GET` returns the following response
 elements.




|  Name  |  Description  | Required |
| --- | --- | --- |
| `AbortIncompleteMultipartUpload` | Container for specifying when an incomplete multipart upload becomes eligible for an
 abort operation.Child:
 `DaysAfterInitiation`Type:
 ContainerAncestor: `Rule` | Yes, if no other action is specified for the rule |
| `Date` | Date when you want Amazon S3 to take the action. For more information, see [Lifecycle Rules: Based on a Specific Date](../userguide/intro-lifecycle-rules.md#intro-lifecycle-rules-date "../userguide/intro-lifecycle-rules.md#intro-lifecycle-rules-date") in the
 *Amazon Simple Storage Service User Guide*.
The date value must conform to the ISO 8601 format. The time is always 
 midnight UTC. 
Type: String
Ancestor: `Expiration` or `Transition` | Yes, if `Days` and `ExpiredObjectDeleteMarker` are
 absent |
| `Days` | Specifies the number of days after object creation when the specific rule action takes
 effect. The object's eligibility time is calculated as creation
 time + the number of days with the resulting time rounded to
 midnight UTC of the next day.
Type: Non-negative Integer when used with `Transition`, Positive Integer
 when used with `Expiration`.
Ancestor: `Transition` or `Expiration` | Yes, if `Date` and `ExpiredObjectDeleteMarker` are
 absent |
| `DaysAfterInitiation` | Specifies the number of days after initiating a multipart
 upload when the multipart upload must be completed. If it does
 not complete by the specified number of days, it becomes
 eligible for an abort operation and Amazon S3 cancels the incomplete
 multipart upload.
Type: Positive Integer
Ancestor: `AbortIncompleteMultipartUpload` | Yes, if `Date` is absent |
| `Expiration` | This action specifies a period in the object's lifetime when Amazon S3 should take the
 appropriate expiration action. The expiration action occurs only on objects 
 that are eligible according to the period specified in the child `Date` or `Days` element. 
 The action Amazon S3 takes
 depends on whether the bucket is versioning enabled. 


* If versioning has never been enabled on the
 bucket, Amazon S3 deletes the only copy of the
 object permanently.
* Otherwise, if your bucket is versioning-enabled (or versioning is suspended), the
 action applies only to the current version of the
 object. Buckets that are versioning-enabled or
 versioning-suspended can have many versions of the same
 object: one current version, and zero or more noncurrent
 versions.
Instead of deleting the current version, Amazon S3
 makes it a noncurrent version by adding a delete
 marker as the new current version. 

ImportantIf the state of a bucket is versioning-suspended, Amazon S3 creates a delete marker
 with version ID `null`. If you have a
 version with version ID `null`, then Amazon S3
 overwrites that version. 

NoteTo set the expiration for noncurrent objects, you must use the
 `NoncurrentVersionExpiration`
 action.

Type: Container
Children: Days or Date
Ancestor: Rule | Yes, if the parent tag is specified |
| `ID` | Unique identifier for the rule. The value cannot be longer than 255
 characters.
Type: String
Ancestor: Rule | No |
| `LifecycleConfiguration` | Container for lifecycle rules. You can add as many as 1000 rules.
Type: Container
Children: Rule
Ancestor: None | Yes |
| `ExpiredObjectDeleteMarker` | On a versioned bucket (versioning-enabled or versioning-suspended bucket), this
 element indicates whether Amazon S3 will delete any expired
 object delete markers in the bucket. For an example, go to
 [Example 8: Specify Expiration Action to Remove Expired
 Object Delete Markers](../userguide/intro-lifecycle-rules.md#lifecycle-config-conceptual-ex8 "../userguide/intro-lifecycle-rules.md#lifecycle-config-conceptual-ex8") in the*Amazon Simple Storage Service User Guide*.
Type: String 
Valid values: true | false (the value false is allowed but it is no-op, Amazon S3
 doesn't take action if the value is false)
Ancestor: `Expiration` | Yes, if `Date` and `Days` are absent |
| `NoncurrentDays` | Specifies the number of days that an object is noncurrent before Amazon S3 can perform the
 associated action. For information about calculating noncurrent
 days, see [Lifecycle Rules Based on the Number of Days](../userguide/object-lifecycle-mgmt.md#intro-lifecycle-actions-number-of-days "../userguide/object-lifecycle-mgmt.md#intro-lifecycle-actions-number-of-days") in the
 *Amazon Simple Storage Service User Guide*.
Type: Nonnegative Integer when used with `NoncurrentVersionTransition`,
 Positive Integer when used with
 `NoncurrentVersionExpiration`
Ancestor: `NoncurrentVersionExpiration` or
 `NoncurrentVersionTransition` | Yes, only if the ancestor is present |
| `NoncurrentVersionExpiration` | Specifies when noncurrent object versions expire. Upon expiration, Amazon S3
 permanently deletes the noncurrent object versions. 
Set this lifecycle configuration action on a bucket that has versioning enabled (or
 suspended) to request that Amazon S3 delete noncurrent object
 versions at a specific period in the object's lifetime.
Type: Container
Children: NoncurrentDays 
Ancestor: Rule | Yes, if no other action is present in the `Rule` |
| `NoncurrentVersionTransition` | Container for the transition rule that describes when noncurrent objects transition to
 the `STANDARD_IA`, `ONEZONE_IA`, or the
 GLACIER storage class. 
If your bucket is versioning-enabled (or versioning is suspended), you can set this
 action to request Amazon S3 to transition noncurrent object
 versions to the GLACIER storage class at a specific period in
 the object's lifetime.
Type: Container
Children: NoncurrentDays and StorageClass
Ancestor: Rule | Yes, if no other action is present in the `Rule` |
| `Prefix` | Object key prefix identifying one or more objects to which the rule applies.
Type: String
Ancestor: Rule | Yes |
| `Rule` | Container for a lifecycle rule.
Type: Container
Ancestor: LifecycleConfiguration | Yes |
| `Status` | If Enabled, Amazon S3 executes the rule as scheduled. If Disabled, Amazon S3 ignores the rule.
Type: String
Ancestor: Rule
Valid values: Enabled or Disabled | Yes |
| `StorageClass` | Specifies the Amazon S3 storage class to which you want to transition the
 object.
Type: String
Ancestor: Transition and
 NoncurrentVersionTransition
Valid values: `STANDARD_IA` | `ONEZONE_IA` |
 GLACIER | Yes |
| `Transition` | This action specifies a period in the objects' lifetime when Amazon S3 should transition
 them to the `STANDARD_IA`, `ONEZONE_IA`,
 or GLACIER storage class. When this action
 is in effect, what Amazon S3 does depends on whether the bucket is
 versioning-enabled.


* If versioning has never been enabled on the bucket, Amazon S3 transitions the only copy
 of the object to the specified storage class.
* When your bucket is versioning-enabled (or versioning is suspended), Amazon S3
 transitions only the current versions of the objects
 identified in the rule.

NoteA versioning-enabled or versioning-suspended bucket can contain many versions of
 an object. This action has no effect on the
 noncurrent object versions. To transition noncurrent
 objects, you must use the
 `NoncurrentVersionTransition`
 action.

Type: Container
Children: Days or Date, and StorageClass
Ancestor: Rule | Yes, if no other action is present in the `Rule` |


## Special Errors




| Error Code | Description | HTTP Status Code | SOAP Fault Code Prefix |
| --- | --- | --- | --- |
| `NoSuchLifecycleConfiguration` | The lifecycle configuration does not exist.  | 404 Not Found | Client |


For general information about Amazon S3 errors and a list of error codes, see [Error responses](ErrorResponses.md "ErrorResponses.md").


## Examples


### Example 1: Retrieve a Lifecycle Subresource


This example is a GET request to retrieve the `lifecycle` subresource from the
 specified bucket, and an example response with the returned lifecycle configuration. 


#### Sample Request



```
GET /?lifecycle HTTP/1.1
Host: examplebucket.s3.amazonaws.com
x-amz-date: Thu, 15 Nov 2012 00:17:21 GMT
Authorization: `signatureValue`
```

#### Sample Response



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

## Related Resources



* [PutBucketLifecycleConfiguration](API_PutBucketLifecycleConfiguration.md "API_PutBucketLifecycleConfiguration.md")
* [DeleteBucketLifecycle](API_DeleteBucketLifecycle.md "API_DeleteBucketLifecycle.md")
