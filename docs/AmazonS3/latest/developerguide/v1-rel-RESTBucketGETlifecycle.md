

# GET Bucket lifecycle (Deprecated)
<a name="v1-rel-RESTBucketGETlifecycle"></a>

## Description
<a name="v1-rel-RESTBucketGETlifecycle_Description"></a>



 

**Important**  
For an updated version of this API, see [GetBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html). If you configured a bucket lifecycle using the <filter> element, you should see an updated version of this topic. This topic is provided for backward compatibility. 

Returns the `lifecycle` configuration information set on the bucket. For information about lifecycle configuration, go to [Object Lifecycle Management](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) in the *Amazon Simple Storage Service User Guide*. 

To use this operation, you must have permission to perform the `s3:GetLifecycleConfiguration` action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see [Managing Access Permissions to Your Amazon S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html) in the *Amazon Simple Storage Service User Guide*.

## Requests
<a name="v1-rel-RESTBucketGETlifecycle-requests"></a>

### Syntax
<a name="v1-rel-RESTBucketGETlifecycle-requests-syntax"></a>

```
1. GET /?lifecycle HTTP/1.1
2. Host: {{bucketname}}.s3.amazonaws.com
3. Date: {{date}}
4. Authorization: {{authorization string}} (see Authenticating Requests (AWS Signature Version 4))
```

### Request Parameters
<a name="v1-rel-RESTBucketGETlifecycle-requests-request-parameters"></a>

This implementation of the operation does not use request parameters.

### Request Headers
<a name="v1-rel-RESTBucketGETlifecycle-requests-request-headers"></a>

This implementation of the operation uses only request headers that are common to all operations. For more information, see [Common Request Headers](RESTCommonRequestHeaders.md).

### Request Elements
<a name="v1-rel-RESTBucketGETlifecycle-requests-request-elements"></a>

This implementation of the operation does not use request elements.

## Responses
<a name="v1-rel-RESTBucketGETlifecycle-responses"></a>

### Response Headers
<a name="v1-rel-RESTBucketGETlifecycle-responses-response-headers"></a>

This implementation of the operation uses only response headers that are common to most responses. For more information, see [Common Response Headers](RESTCommonResponseHeaders.md).

### Response Elements
<a name="v1-rel-RESTBucketGETlifecycle-responses-response-elements"></a>

This implementation of `GET` returns the following response elements.


|  Name  |  Description  | Required | 
| --- | --- | --- | 
|  AbortIncompleteMultipartUpload  | Container for specifying when an incomplete multipart upload becomes eligible for an abort operation.Child: `DaysAfterInitiation`<br />Type: Container<br />Ancestor: `Rule` | Yes, if no other action is specified for the rule | 
|  Date  | Date when you want Amazon S3 to take the action. For more information, see [Lifecycle Rules: Based on a Specific Date](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-rules.html#intro-lifecycle-rules-date) in the *Amazon Simple Storage Service User Guide*.<br />The date value must conform to the ISO 8601 format. The time is always midnight UTC. <br />Type: String<br />Ancestor: `Expiration` or `Transition` | Yes, if Days and ExpiredObjectDeleteMarker are absent | 
|  Days  | Specifies the number of days after object creation when the specific rule action takes effect. The object's eligibility time is calculated as creation time \+ the number of days with the resulting time rounded to midnight UTC of the next day.<br />Type: Non-negative Integer when used with `Transition`, Positive Integer when used with `Expiration`.<br />Ancestor: `Transition` or `Expiration` | Yes, if Date and ExpiredObjectDeleteMarker are absent | 
|  DaysAfterInitiation  | Specifies the number of days after initiating a multipart upload when the multipart upload must be completed. If it does not complete by the specified number of days, it becomes eligible for an abort operation and Amazon S3 cancels the incomplete multipart upload.<br />Type: Positive Integer<br />Ancestor: `AbortIncompleteMultipartUpload` | Yes, if Date is absent | 
|  Expiration  | This action specifies a period in the object's lifetime when Amazon S3 should take the appropriate expiration action. The expiration action occurs only on objects that are eligible according to the period specified in the child `Date` or `Days` element. The action Amazon S3 takes depends on whether the bucket is versioning enabled. <br /> +  If versioning has never been enabled on the bucket, Amazon S3 deletes the only copy of the object permanently.  <br />+  Otherwise, if your bucket is versioning-enabled (or versioning is suspended), the action applies only to the current version of the object. Buckets that are versioning-enabled or versioning-suspended can have many versions of the same object: one current version, and zero or more noncurrent versions. <br />Instead of deleting the current version, Amazon S3 makes it a noncurrent version by adding a delete marker as the new current version.  <br />  If the state of a bucket is versioning-suspended, Amazon S3 creates a delete marker with version ID `null`. If you have a version with version ID `null`, then Amazon S3 overwrites that version.   <br />  To set the expiration for noncurrent objects, you must use the `NoncurrentVersionExpiration` action.  <br />Type: Container<br />Children: Days or Date<br />Ancestor: Rule | Yes, if the parent tag is specified | 
|  ID  | Unique identifier for the rule. The value cannot be longer than 255 characters.<br />Type: String<br />Ancestor: Rule | No | 
| LifecycleConfiguration  | Container for lifecycle rules. You can add as many as 1000 rules.<br />Type: Container<br />Children: Rule<br />Ancestor: None | Yes | 
| ExpiredObjectDeleteMarker | On a versioned bucket (versioning-enabled or versioning-suspended bucket), this element indicates whether Amazon S3 will delete any expired object delete markers in the bucket. For an example, go to [Example 8: Specify Expiration Action to Remove Expired Object Delete Markers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-rules.html#lifecycle-config-conceptual-ex8) in the* Amazon Simple Storage Service User Guide*.<br />Type: String <br />Valid values: true \| false (the value false is allowed but it is no-op, Amazon S3 doesn't take action if the value is false)<br />Ancestor: `Expiration` | Yes, if Date and Days are absent | 
| NoncurrentDays  | Specifies the number of days that an object is noncurrent before Amazon S3 can perform the associated action. For information about calculating noncurrent days, see [Lifecycle Rules Based on the Number of Days](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html#intro-lifecycle-actions-number-of-days) in the *Amazon Simple Storage Service User Guide*.<br />Type: Nonnegative Integer when used with `NoncurrentVersionTransition`, Positive Integer when used with `NoncurrentVersionExpiration`<br />Ancestor: `NoncurrentVersionExpiration` or `NoncurrentVersionTransition` | Yes, only if the ancestor is present | 
| NoncurrentVersionExpiration  | Specifies when noncurrent object versions expire. Upon expiration, Amazon S3 permanently deletes the noncurrent object versions. <br />Set this lifecycle configuration action on a bucket that has versioning enabled (or suspended) to request that Amazon S3 delete noncurrent object versions at a specific period in the object's lifetime.<br />Type: Container<br />Children: NoncurrentDays <br />Ancestor: Rule | Yes, if no other action is present in the Rule | 
| NoncurrentVersionTransition | Container for the transition rule that describes when noncurrent objects transition to the `STANDARD_IA`, `ONEZONE_IA`, or the storage class. <br />If your bucket is versioning-enabled (or versioning is suspended), you can set this action to request Amazon S3 to transition noncurrent object versions to the storage class at a specific period in the object's lifetime.<br />Type: Container<br />Children: NoncurrentDays and StorageClass<br />Ancestor: Rule | Yes, if no other action is present in the Rule | 
|  Prefix  | Object key prefix identifying one or more objects to which the rule applies.<br />Type: String<br />Ancestor: Rule | Yes | 
| Rule  | Container for a lifecycle rule.<br />Type: Container<br />Ancestor: LifecycleConfiguration | Yes | 
|  Status  | If Enabled, Amazon S3 executes the rule as scheduled. If Disabled, Amazon S3 ignores the rule.<br />Type: String<br />Ancestor: Rule<br />Valid values: Enabled or Disabled | Yes | 
|  StorageClass  | Specifies the Amazon S3 storage class to which you want to transition the object.<br />Type: String<br />Ancestor: Transition and NoncurrentVersionTransition<br />Valid values: `STANDARD_IA` \| `ONEZONE_IA` \|  | Yes | 
|  Transition  | This action specifies a period in the objects' lifetime when Amazon S3 should transition them to the `STANDARD_IA`, `ONEZONE_IA`, or storage class. When this action is in effect, what Amazon S3 does depends on whether the bucket is versioning-enabled.<br /> +  If versioning has never been enabled on the bucket, Amazon S3 transitions the only copy of the object to the specified storage class.  <br />+  When your bucket is versioning-enabled (or versioning is suspended), Amazon S3 transitions only the current versions of the objects identified in the rule. <br />  A versioning-enabled or versioning-suspended bucket can contain many versions of an object. This action has no effect on the noncurrent object versions. To transition noncurrent objects, you must use the `NoncurrentVersionTransition` action.  <br />Type: Container<br />Children: Days or Date, and StorageClass<br />Ancestor: Rule | Yes, if no other action is present in the Rule | 

## Special Errors
<a name="v1-rel-RESTBucketGETlifecycle-special-errors"></a>


| Error Code | Description | HTTP Status Code | SOAP Fault Code Prefix | 
| --- | --- | --- | --- | 
| NoSuchLifecycleConfiguration | The lifecycle configuration does not exist.  | 404 Not Found | Client | 

For general information about Amazon S3 errors and a list of error codes, see [Error responses](ErrorResponses.md).

## Examples
<a name="v1-rel-RESTBucketGETlifecycle-examples"></a>

### Example 1: Retrieve a Lifecycle Subresource
<a name="v1-rel-RESTBucketGETlifecycle-examples-example-1-retrieve-lifecycle-subresource-"></a>

This example is a GET request to retrieve the `lifecycle` subresource from the specified bucket, and an example response with the returned lifecycle configuration. 

#### Sample Request
<a name="v1-rel-RESTBucketGETlifecycle-examples-example-1-retrieve-lifecycle-subresource--sample-request"></a>

```
1. GET /?lifecycle HTTP/1.1
2. Host: examplebucket.s3.amazonaws.com
3. x-amz-date: Thu, 15 Nov 2012 00:17:21 GMT
4. Authorization: {{signatureValue}}
```

#### Sample Response
<a name="v1-rel-RESTBucketGETlifecycle-examples-example-1-retrieve-lifecycle-subresource--sample-response"></a>

```
 1. HTTP/1.1 200 OK
 2. x-amz-id-2: ITnGT1y4RyTmXa3rPi4hklTXouTf0hccUjo0iCPjz6FnfIutBj3M7fPGlWO2SEWp
 3. x-amz-request-id: 51991C342C575321
 4. Date: Thu, 15 Nov 2012 00:17:23 GMT
 5. Server: AmazonS3
 6. Content-Length: 358
 7. 
 8. <?xml version="1.0" encoding="UTF-8"?>
 9. <LifecycleConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
10.     <Rule>
11.         <ID>Archive and then delete rule</ID>
12.         <Prefix>projectdocs/</Prefix>
13.         <Status>Enabled</Status>
14.        <Transition>
15.            <Days>30</Days>
16.            <StorageClass>STANDARD_IA</StorageClass>
17.         </Transition>
18.         <Transition>
19.            <Days>365</Days>
20.            <StorageClass>GLACIER</StorageClass>
21.         </Transition>
22.         <Expiration>
23.            <Days>3650</Days>
24.         </Expiration>
25.     </Rule>
26. </LifecycleConfiguration>
```

## Related Resources
<a name="v1-rel-RESTBucketGETlifecycle-related-resources"></a>
+ [PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html)
+ [DeleteBucketLifecycle](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketLifecycle.html)